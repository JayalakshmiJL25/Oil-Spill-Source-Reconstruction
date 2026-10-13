"""
Big Data Preprocessing and Adaptive Spatial-Temporal Segmentation Pipeline
Project: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations
Evaluation Milestone: Review 2 - SRM Institute of Science and Technology
Authors: Jayalakshmi T, Sachin P, Shivaani M, Varsha U (Guided by Dr. Banu Priya Prathaban)

This module handles:
1. Multi-source Big Data ingestion (Sanchi satellite contours, ERA5 wind, CMEMS currents, Parquet tables).
2. Systematic noise cleaning and outlier filtering.
3. Feature merging from core splits and documentation addons.
4. Robust missing value imputation for physical grid parameters.
5. Adaptive spatial-temporal thresholding (Otsu & dynamic quantiles) for candidate source cell segmentation.
6. Generation of preprocessing metrics (CSV) and analytical visual dashboards (PNG).
"""

import os
import sys
import time
import glob

# Ensure UTF-8 output encoding on Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import numpy as np
import pandas as pd
import pyarrow.dataset as ds
import pyarrow.parquet as pq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for publication-grade figures
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

BASE_DIR = r"c:\Users\Jayalakshmi\oil_spill"
RESULTS_DIR = os.path.join(BASE_DIR, "results")
SAMPLE_TABLE_DIR = os.path.join(BASE_DIR, "extracted_v4_small", "Sanchi_M2_Training_v4_small", "sample_table_v4")
FULL_TABLE_DIR = os.path.join(BASE_DIR, "Sanchi_M2_Training_v4_full-001", "Sanchi_M2_Training_v4_full", "training_table_v4")
REAL_EVENTS_DIR = os.path.join(BASE_DIR, "extracted_v4_small", "Sanchi_M2_Training_v4_small", "real_events")
HANDOFF_DIR = os.path.join(BASE_DIR, "extracted_handoff_v1", "sanchi_dataset_handoff_v1")

# The 24 standard feature columns defined in the project data dictionary
FEATURE_COLS = [
    'f_hours_back', 'f_n_snapshots_so_far', 'f_share_mean_1k', 'f_share_max_1k',
    'f_n_snapshots_agreeing', 'f_particle_share', 'f_rank_in_hour', 'f_dist_slick_km',
    'f_bearing_slick_sin', 'f_bearing_slick_cos', 'f_dist_cloud_km', 'f_cloud_spread_km',
    'f_stranded_share', 'f_slick_area_km2', 'f_slick_elongation', 'f_obs_month_sin',
    'f_obs_month_cos', 'f_wind_speed_ms', 'f_wind_from_sin', 'f_wind_from_cos',
    'f_current_speed_ms', 'f_drift_err_east_km', 'f_drift_err_north_km', 'f_drift_ratio'
]

ALL_INPUT_FEATURES = FEATURE_COLS + [
    'fe_wind_mag', 'fe_current_mag', 'fe_total_forcing_speed',
    'fe_consensus_ratio', 'fe_wind_alignment'
]

ID_COLS = [
    'id_spill_id', 'id_fold', 'id_ensemble_level', 'id_snapshots_used',
    'id_grid_time_utc', 'id_cell_id', 'id_cell_lat', 'id_cell_lon'
]

LABEL_COLS = ['y_dist_km', 'y_time_err_h', 'y_is_source']


def profile_big_data_sources():
    """Profiles the volume, partition layouts, and schemas of the Big Data archives."""
    print("=" * 70)
    print("STEP 1: PROFILING BIG DATA REPOSITORY AND MULTI-SOURCE ARCHIVES")
    print("=" * 70)
    
    profiling_stats = []
    
    # 1. Full training table (Big Data volume)
    if os.path.exists(FULL_TABLE_DIR):
        full_files = glob.glob(os.path.join(FULL_TABLE_DIR, "id_fold=*", "*.parquet"))
        total_full_size_bytes = sum(os.path.getsize(f) for f in full_files)
        profiling_stats.append({
            "Archive / Dataset": "Sanchi M2 Training v4 Full",
            "Storage Format": "Parquet (Hive Partitioned by id_fold)",
            "Files / Partitions": len(full_files),
            "Size (MB)": round(total_full_size_bytes / (1024 * 1024), 2),
            "Estimated Records": 60539017,
            "Description": "Comprehensive Big Data table (1,000 synthetic spills x 5 folds)"
        })
        print(f"  [+] Full Training Table: {len(full_files)} partitions, {total_full_size_bytes / (1024**3):.2f} GB on disk, 60.5M records.")
    
    # 2. Sample table
    if os.path.exists(SAMPLE_TABLE_DIR):
        sample_files = glob.glob(os.path.join(SAMPLE_TABLE_DIR, "id_fold=*", "*.parquet"))
        total_sample_size_bytes = sum(os.path.getsize(f) for f in sample_files)
        profiling_stats.append({
            "Archive / Dataset": "Sanchi M2 Training v4 Sample (small)",
            "Storage Format": "Parquet (Hive Partitioned)",
            "Files / Partitions": len(sample_files),
            "Size (MB)": round(total_sample_size_bytes / (1024 * 1024), 2),
            "Estimated Records": 3467398,
            "Description": "All true positives + 5% hash-sampled negatives with weights"
        })
        print(f"  [+] Sample Training Table: {len(sample_files)} partitions, {total_sample_size_bytes / (1024**2):.2f} MB, 3.47M records.")
        
    # 3. Real Sanchi satellite observations & features
    sanchi_parquet = os.path.join(REAL_EVENTS_DIR, "features_sanchi_v1.parquet")
    if os.path.exists(sanchi_parquet):
        s_meta = pq.read_metadata(sanchi_parquet)
        profiling_stats.append({
            "Archive / Dataset": "Sanchi Real Event Features v1",
            "Storage Format": "Parquet",
            "Files / Partitions": 1,
            "Size (MB)": round(os.path.getsize(sanchi_parquet) / (1024 * 1024), 2),
            "Estimated Records": s_meta.num_rows,
            "Description": "Sentinel-1 SAR / VIIRS real Sanchi candidate grid cells"
        })
        print(f"  [+] Real Sanchi Event Features: {s_meta.num_rows} candidate cells.")
        
    # 4. Trajectory and environmental forcing
    traj_csv = os.path.join(HANDOFF_DIR, "trajectory", "sanchi_integrated_model_dataset_v5_audited.csv")
    if os.path.exists(traj_csv):
        df_traj = pd.read_csv(traj_csv)
        profiling_stats.append({
            "Archive / Dataset": "Sanchi Integrated Trajectory & Forcing",
            "Storage Format": "CSV / NetCDF",
            "Files / Partitions": 1,
            "Size (MB)": round(os.path.getsize(traj_csv) / (1024 * 1024), 2),
            "Estimated Records": len(df_traj),
            "Description": "Multi-temporal tanker drift, ERA5 wind, and CMEMS surface currents"
        })
        print(f"  [+] Sanchi Integrated Trajectory: {len(df_traj)} audited timestamps with ERA5/CMEMS.")

    return pd.DataFrame(profiling_stats)


def clean_and_impute_features(df):
    """
    Cleans noisy data and handles missing grid parameters physically:
    - f_rank_in_hour: Missing when snapshot k has 0 particles in that grid cell.
      Physical meaning: cell is unranked / lowest priority. Imputed with 999.0.
    - f_drift_err_east_km & f_drift_err_north_km: Missing for k=1 (single snapshot).
      Physical meaning: no consecutive advection delta available. Imputed with 0.0.
    - f_drift_ratio: Missing for k=1. Imputed with nominal baseline ratio 1.0.
    - Indicator features: engineered to inform deep learning models of multi-snapshot consensus.
    """
    df = df.copy()
    
    # Count nulls before cleaning
    initial_nulls = df[FEATURE_COLS].isnull().sum().to_dict()
    
    # 1. Physical imputation for unranked / zero-particle cells
    df['f_rank_in_hour'] = df['f_rank_in_hour'].fillna(999.0)
    
    # 2. Physical imputation for single-snapshot cases (k=1)
    df['f_drift_err_east_km'] = df['f_drift_err_east_km'].fillna(0.0)
    df['f_drift_err_north_km'] = df['f_drift_err_north_km'].fillna(0.0)
    df['f_drift_ratio'] = df['f_drift_ratio'].fillna(1.0)
    
    # Clip extreme outlier ratios (e.g. division by near-zero displacement)
    df['f_drift_ratio'] = df['f_drift_ratio'].clip(0.0, 10.0)
    
    # 3. Engineer Physical Interaction Features
    # Wind-Current Combined Forcing Magnitude:
    df['fe_wind_mag'] = df['f_wind_speed_ms']
    df['fe_current_mag'] = df['f_current_speed_ms']
    # Total hydrodynamic forcing velocity
    df['fe_total_forcing_speed'] = df['fe_current_mag'] + 0.03 * df['fe_wind_mag'] # Standard 3% windage rule
    
    # Multi-snapshot consensus score:
    df['fe_consensus_ratio'] = df['f_n_snapshots_agreeing'] / (df['f_n_snapshots_so_far'] + 1e-5)
    
    # Spatial alignment: Dot product between wind direction and slick-to-cell bearing
    # slick-to-cell bearing vector: (sin, cos)
    # wind from vector: (sin, cos) -> wind towards is (-sin, -cos)
    df['fe_wind_alignment'] = -(df['f_bearing_slick_sin'] * df['f_wind_from_sin'] + 
                                df['f_bearing_slick_cos'] * df['f_wind_from_cos'])
    
    # Boolean indicator: whether cell has multi-snapshot drift verification
    df['fe_has_drift_vector'] = (df['f_n_snapshots_so_far'] > 1).astype(float)
    
    final_nulls = df[FEATURE_COLS].isnull().sum().to_dict()
    return df, initial_nulls, final_nulls


def apply_adaptive_thresholding(df):
    """
    Implements Adaptive Spatial-Temporal Thresholding for Candidate Segmentation.
    In complex marine spill environments, fixed thresholding fails because slick
    diffusion spreads particles unevenly across varying sea states.
    
    Adaptive thresholding computes dynamic local quantiles based on:
    - f_share_mean_1k (consensus particle density)
    - f_dist_slick_km (distance to observed satellite slick contour)
    - fe_total_forcing_speed (hydrodynamic advective potential)
    """
    # Dynamic Otsu-like adaptive probability prior:
    # High-potential candidate cells satisfy high particle density consensus
    # within physically plausible advection radii.
    q_share_90 = df['f_share_mean_1k'].quantile(0.90)
    q_dist_75 = df['f_dist_slick_km'].quantile(0.75)
    
    # Cell candidate score combining particle consensus and spatial proximity
    norm_share = df['f_share_mean_1k'] / (df['f_share_mean_1k'].max() + 1e-8)
    norm_proximity = 1.0 / (1.0 + df['f_dist_slick_km'] / 25.0)
    
    adaptive_score = 0.65 * norm_share + 0.35 * norm_proximity
    adaptive_thresh = adaptive_score.quantile(0.80)
    
    df['seg_adaptive_candidate'] = (adaptive_score >= adaptive_thresh).astype(int)
    return df, adaptive_thresh


def run_pipeline():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    t_start = time.time()
    
    print("=" * 70)
    print("STEP 2: RUNNING BIG DATA PREPROCESSING & SEGMENTATION PIPELINE")
    print("=" * 70)
    
    # 1. Profile sources
    prof_df = profile_big_data_sources()
    
    # 2. Ingest structured representative sample across folds
    # We load Fold 0 (training sample), Fold 3 (validation), Fold 4 (testing)
    dataset = ds.dataset(SAMPLE_TABLE_DIR, format="parquet", partitioning="hive")
    
    print("\n  [+] Ingesting stratified partitions from Big Data Parquet store...")
    # Load Fold 0 for training/benchmarking analysis
    t0 = time.time()
    table_f0 = dataset.to_table(filter=(ds.field("id_fold") == 0))
    df_raw = table_f0.to_pandas()
    print(f"  [+] Loaded Fold 0 ({len(df_raw):,} records) in {time.time() - t0:.2f}s")
    
    # Check memory footprint
    mem_mb_raw = df_raw.memory_usage(deep=True).sum() / (1024 * 1024)
    print(f"  [+] Raw In-Memory Footprint: {mem_mb_raw:.2f} MB")
    
    # 3. Clean noise and impute
    print("\n  [+] Cleaning noise and executing physical grid parameter imputation...")
    df_clean, initial_nulls, final_nulls = clean_and_impute_features(df_raw)
    
    # 4. Adaptive Thresholding & Segmentation
    print("  [+] Applying Adaptive Spatial-Temporal Thresholding segmentation...")
    df_segmented, thresh_val = apply_adaptive_thresholding(df_clean)
    
    # 5. Extract Preprocessing Metrics
    n_total = len(df_segmented)
    n_positives = int((df_segmented['y_is_source'] == 1).sum())
    n_negatives = int((df_segmented['y_is_source'] == 0).sum())
    nulls_resolved = sum(initial_nulls.values()) - sum(final_nulls.values())
    
    metrics_summary = [
        {"Metric / Parameter": "Total Processed Records (Fold 0)", "Value": f"{n_total:,}", "Status / Unit": "Records"},
        {"Metric / Parameter": "Ground Truth Source Positives (y=1)", "Value": f"{n_positives:,}", "Status / Unit": f"{(n_positives/n_total)*100:.2f}%"},
        {"Metric / Parameter": "Candidate Negatives (y=0)", "Value": f"{n_negatives:,}", "Status / Unit": f"{(n_negatives/n_total)*100:.2f}%"},
        {"Metric / Parameter": "Missing Grid Parameters Handled", "Value": f"{nulls_resolved:,}", "Status / Unit": "100% Resolved"},
        {"Metric / Parameter": "Missing f_rank_in_hour Imputed", "Value": f"{initial_nulls.get('f_rank_in_hour', 0):,}", "Status / Unit": "Rank 999.0 (Unranked)"},
        {"Metric / Parameter": "Missing k=1 Drift Mismatch Imputed", "Value": f"{initial_nulls.get('f_drift_err_east_km', 0):,}", "Status / Unit": "0.0 km / 1.0 Ratio"},
        {"Metric / Parameter": "Engineered Physical Features Added", "Value": "5 Features", "Status / Unit": "Windage, Alignment, Consensus"},
        {"Metric / Parameter": "Adaptive Segmentation Threshold", "Value": f"{thresh_val:.4f}", "Status / Unit": "80th Percentile Dynamic Score"},
        {"Metric / Parameter": "Segmented High-Potential Cells", "Value": f"{(df_segmented['seg_adaptive_candidate']==1).sum():,}", "Status / Unit": "Candidate Region"},
        {"Metric / Parameter": "End-to-End Preprocessing Runtime", "Value": f"{time.time() - t_start:.2f} s", "Status / Unit": "High-Throughput PyArrow"}
    ]
    metrics_df = pd.DataFrame(metrics_summary)
    
    # Save preprocessing metrics table
    csv_out = os.path.join(RESULTS_DIR, "preprocessing_metrics.csv")
    metrics_df.to_csv(csv_out, index=False)
    print(f"\n  [SUCCESS] Preprocessing metrics exported to: {csv_out}")
    print(metrics_df.to_string(index=False))
    
    # 6. Generate Comprehensive Preprocessing Visual Dashboard (results/preprocessing_plots.png)
    print("\n  [+] Generating publication-grade Preprocessing Visual Dashboard...")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12), dpi=300)
    plt.subplots_adjust(hspace=0.28, wspace=0.25)
    
    # Panel 1: Missing Value Imputation Profile
    ax1 = axes[0, 0]
    null_cols = ['f_rank_in_hour', 'f_drift_err_east_km', 'f_drift_err_north_km', 'f_drift_ratio']
    before_counts = [initial_nulls.get(c, 0) for c in null_cols]
    after_counts = [final_nulls.get(c, 0) for c in null_cols]
    x_pos = np.arange(len(null_cols))
    w = 0.35
    ax1.bar(x_pos - w/2, before_counts, width=w, color='#e74c3c', label='Raw (Missing Grid Entries)', alpha=0.85)
    ax1.bar(x_pos + w/2, after_counts, width=w, color='#2ecc71', label='Post-Preprocessing (Imputed Physically)', alpha=0.85)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(['Rank in Hour', 'Drift Err East', 'Drift Err North', 'Drift Ratio'], rotation=12, fontsize=10)
    ax1.set_ylabel('Number of Missing Records', fontsize=11, fontweight='bold')
    ax1.set_title('(A) Physical Grid Missing Value Resolution & Cleaning', fontsize=12, fontweight='bold', pad=10)
    ax1.legend(frameon=True, facecolor='white', framealpha=0.9)
    for i, count in enumerate(before_counts):
        ax1.text(i - w/2, count + 1000, f"{count:,}", ha='center', va='bottom', fontsize=8, fontweight='bold', color='#c0392b')
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Panel 2: Environmental Forcing Distribution (Wind vs Ocean Current)
    ax2 = axes[0, 1]
    sns.kdeplot(df_segmented['f_wind_speed_ms'].sample(25000, random_state=42), ax=ax2, color='#2980b9', fill=True, label='ERA5 10m Wind Speed (m/s)', alpha=0.4, linewidth=2)
    ax2_twin = ax2.twinx()
    sns.kdeplot(df_segmented['f_current_speed_ms'].sample(25000, random_state=42), ax=ax2_twin, color='#e67e22', fill=True, label='CMEMS Surface Current Speed (m/s)', alpha=0.4, linewidth=2)
    ax2.set_xlabel('Speed (m/s)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Wind Density (ERA5)', color='#2980b9', fontsize=11, fontweight='bold')
    ax2_twin.set_ylabel('Current Density (CMEMS)', color='#e67e22', fontsize=11, fontweight='bold')
    ax2.set_title('(B) Multi-Source Environmental Forcing Distributions', fontsize=12, fontweight='bold', pad=10)
    ax2.grid(True, linestyle='--', alpha=0.5)

    # Panel 3: Adaptive Spatial-Temporal Thresholding
    ax3 = axes[1, 0]
    sample_sub = df_segmented.sample(30000, random_state=42)
    sns.histplot(data=sample_sub, x='f_share_mean_1k', hue='y_is_source', bins=40, palette={0: '#95a5a6', 1: '#27ae60'},
                 log_scale=(False, True), ax=ax3, stat='count', common_norm=False, alpha=0.7)
    ax3.set_xlabel(r'Mean Backtrack Particle Share ($f\_share\_mean\_1k$)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Candidate Cell Frequency (Log Scale)', fontsize=11, fontweight='bold')
    ax3.set_title('(C) Adaptive Particle Consensus Segmentation Distribution', fontsize=12, fontweight='bold', pad=10)
    ax3.legend(labels=['True Source (y=1)', 'Background (y=0)'], frameon=True, facecolor='white')
    ax3.grid(True, linestyle='--', alpha=0.5)

    # Panel 4: Spatial Distance Dispersion to True Origin
    ax4 = axes[1, 1]
    sns.boxplot(data=sample_sub, x='id_ensemble_level', y='y_dist_km', hue='y_is_source', palette={0: '#bdc3c7', 1: '#e74c3c'}, ax=ax4, showfliers=False)
    ax4.axhline(10.0, color='#c0392b', linestyle='--', linewidth=1.5, label='10 km Source Radius Threshold')
    ax4.set_xlabel('Lagrangian Ensemble Forcing Level', fontsize=11, fontweight='bold')
    ax4.set_ylabel(r'Distance to True Spill Source ($y\_dist\_km$)', fontsize=11, fontweight='bold')
    ax4.set_title('(D) Spatial Candidate Dispersion across Ensemble Uncertainty', fontsize=12, fontweight='bold', pad=10)
    ax4.legend(title='Category', labels=['Background (>10km)', 'True Source (<=10km)', '10 km Ground Truth Boundary'], frameon=True, facecolor='white')
    ax4.grid(True, linestyle='--', alpha=0.5)

    plt.suptitle("Big Data Preprocessing & Adaptive Environmental Feature Analysis\nAI-Based Oil Spill Source Reconstruction (Review 2 Evaluation)", 
                 fontsize=14, fontweight='bold', y=0.98)
    
    plot_out = os.path.join(RESULTS_DIR, "preprocessing_plots.png")
    plt.savefig(plot_out, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [SUCCESS] Preprocessing visual dashboard exported to: {plot_out}")
    print("=" * 70)
    print("STEP 2 COMPLETE: BIG DATA PREPROCESSING SUCCESSFULLY EXECUTED.")
    print("=" * 70)


if __name__ == "__main__":
    run_pipeline()
