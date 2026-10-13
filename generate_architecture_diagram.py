"""
Publication-Grade System Architecture & Data Pipeline Diagram Generator
Project: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations
Theme: Top-Tier AI Research Architecture Pipeline for Review 2 (Slide 5)
Outputs: results/system_architecture_diagram.png (High-DPI 16:9 Widescreen Image)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Rectangle
import numpy as np

def generate_pipeline_diagram(output_path):
    # Dimensions: 24 x 11.8 inches at 300 DPI (7200 x 3540 px)
    fig = plt.figure(figsize=(24, 11.8), dpi=300, facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 11.8)
    ax.axis('off')

    FONT_FAMILY = 'Arial'

    # =========================================================================
    # 1. TOP HEADER BANNER
    # =========================================================================
    # Header bar
    header_box = FancyBboxPatch((0.5, 10.45), 23.0, 1.05,
                                boxstyle="round,pad=0.06,rounding_size=0.18",
                                facecolor='#002B49', edgecolor='#001A2C', linewidth=1.5, zorder=2)
    ax.add_patch(header_box)

    # Main Title & Subtitle
    ax.text(0.85, 11.12, "OVERALL SYSTEM ARCHITECTURE & DATA PIPELINE",
            fontfamily=FONT_FAMILY, fontsize=19, fontweight='bold', color='#FFFFFF', va='center', zorder=3)
    ax.text(0.85, 10.72, "AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations & Environmental Uncertainty (AST-CLAM)",
            fontfamily=FONT_FAMILY, fontsize=11, fontweight='normal', color='#93C5FD', va='center', zorder=3)

    # Badges
    badges = [
        ("SRM BATCH 10", "#1D4ED8"),
        ("21CSC314P BIG DATA ESSENTIALS", "#059669"),
        ("END-TO-END PIPELINE", "#D97706")
    ]
    bx = 23.1
    for b_text, b_color in reversed(badges):
        bw = len(b_text) * 0.105 + 0.38
        bx -= bw
        bp = FancyBboxPatch((bx, 10.73), bw - 0.12, 0.45,
                            boxstyle="round,pad=0.04,rounding_size=0.09",
                            facecolor=b_color, edgecolor='none', zorder=3)
        ax.add_patch(bp)
        ax.text(bx + (bw - 0.12)/2, 10.95, b_text,
                fontfamily=FONT_FAMILY, fontsize=8.5, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)
        bx -= 0.1

    # =========================================================================
    # 2. FIVE COGNITIVE PIPELINE STAGES
    # =========================================================================
    stages = [
        {
            "id": "STAGE 1",
            "title": "MULTI-SOURCE INGESTION",
            "sub": "Remote Sensing & Metocean",
            "theme": "#1E3A8A", "light": "#EFF6FF", "border": "#3B82F6", "badge": "#2563EB",
            "x": 0.5, "w": 4.15,
            "cards": [
                {
                    "tag": "SATELLITE REMOTE SENSING",
                    "title": "Sentinel-1 SAR Slick Delineation",
                    "points": ["Multi-temporal radar slicks (C-band)", "20,951 spatial candidate grid cells", "Observed slick area & diffusion axes"],
                    "pill": "Multi-Temporal SAR Observations",
                    "icon": "sar"
                },
                {
                    "tag": "ATMOSPHERIC REANALYSIS",
                    "title": "ECMWF ERA5 Wind Vectors",
                    "points": ["Hourly 10m wind fields (u10, v10)", "0.25° x 0.25° spatial reanalysis grid", "Wind direction & dynamic gust variance"],
                    "pill": "ERA5 Boundary Layer Wind",
                    "icon": "wind"
                },
                {
                    "tag": "OCEAN HYDRODYNAMICS",
                    "title": "CMEMS Ocean Current Fields",
                    "points": ["Hourly surface currents (u, v)", "0.083° Copernicus hydrodynamic mesh", "Wave Stokes drift & 3% windage coupling"],
                    "pill": "CMEMS Marine Reanalysis",
                    "icon": "current"
                },
                {
                    "tag": "AUDITED DISASTER BENCHMARK",
                    "title": "Sanchi Tanker Disaster Track",
                    "points": ["Audited AIS coordinates prior to sinking", "Verified sinking wreck: 28.375°N, 125.942°E", "115m sea-depth ground truth anchor"],
                    "pill": "Disaster Ground Truth (2018)",
                    "icon": "tanker"
                }
            ]
        },
        {
            "id": "STAGE 2",
            "title": "BIG DATA PREPROCESSING",
            "sub": "Distributed PyArrow Pipeline",
            "theme": "#065F46", "light": "#F0FDF4", "border": "#10B981", "badge": "#059669",
            "x": 5.18, "w": 4.15,
            "cards": [
                {
                    "tag": "DISTRIBUTED I/O ENGINE",
                    "title": "Apache PyArrow Hive Reader",
                    "points": ["Distributed reading across 5 folds", "60.5M records processed without memory bottleneck", "Whole-spill splits prevent data leakage"],
                    "pill": "PyArrow Distributed Dataset",
                    "icon": "pyarrow"
                },
                {
                    "tag": "SCHEMA & SINGULARITY CLEANSE",
                    "title": "Range & Outlier Normalization",
                    "points": ["Synchronized UTC timestamp intervals", "Clipping f_drift_ratio to [0.0, 10.0]", "Eliminates division-by-zero singularities"],
                    "pill": "Mathematical Safeguards",
                    "icon": "cleanse"
                },
                {
                    "tag": "DOMAIN PHYSICS IMPUTATION",
                    "title": "Physical Grid Null Imputation",
                    "points": ["f_rank_in_hour -> 999.0 for empty cells", "k=1 single-snapshot drift error -> 0.0", "Preserves ocean dynamics fidelity"],
                    "pill": "Physics-Informed Null Fill",
                    "icon": "impute"
                },
                {
                    "tag": "SPATIAL CANDIDATE FILTER",
                    "title": "Adaptive Energy Thresholding",
                    "points": ["80th-percentile energy contour masking", "Filters 82.3% non-source background cells", "Sharpens gradient backward propagation"],
                    "pill": "Adaptive Energy Masking",
                    "icon": "threshold"
                }
            ]
        },
        {
            "id": "STAGE 3",
            "title": "TRI-BRANCH EMBEDDING",
            "sub": "Physics-Informed Decoupling",
            "theme": "#9A3412", "light": "#FFF7ED", "border": "#F97316", "badge": "#EA580C",
            "x": 9.86, "w": 4.15,
            "cards": [
                {
                    "tag": "BRANCH 1: SPATIAL GEOMETRY",
                    "title": "Spatial Geometry Branch (14-D)",
                    "points": ["Distance to slick centroid d_slick (km)", "Particle cloud dispersion radius & spread", "Polygon major/minor axes & bearing"],
                    "pill": "14 Geometric Dimensions",
                    "icon": "branch1"
                },
                {
                    "tag": "BRANCH 2: HYDRODYNAMICS",
                    "title": "Dynamic Forcing Branch (10-D)",
                    "points": ["Wind velocity magnitude W_mag (m/s)", "CMEMS ocean current speed C_mag", "Combined 3% windage advection vectors"],
                    "pill": "10 Hydrodynamic Dimensions",
                    "icon": "branch2"
                },
                {
                    "tag": "BRANCH 3: DRIFT RESIDUALS",
                    "title": "Drift Mismatch Branch (5-D)",
                    "points": ["East/North drift mismatch (f_drift_err)", "Advective divergence velocity delta-u, delta-v", "Lagrangian particle drift ratio"],
                    "pill": "5 Residual Dimensions",
                    "icon": "branch3"
                },
                {
                    "tag": "LATENT TENSOR CONCATENATION",
                    "title": "Fused 29-D Feature Tensor",
                    "points": ["Standardized multi-modal projection", "Tensor representation: X in R^{B x T x 29}", "Retrograde time window: t=0 -> -120h"],
                    "pill": "Unified 29-D Input Tensor",
                    "icon": "fusion"
                }
            ]
        },
        {
            "id": "STAGE 4",
            "title": "NOVEL AST-CLAM CORE",
            "sub": "Adaptive Neural Architecture",
            "theme": "#581C87", "light": "#FAF5FF", "border": "#8B5CF6", "badge": "#7C3AED",
            "x": 14.54, "w": 4.4,
            "cards": [
                {
                    "tag": "LOCAL RECEPTIVE FIELD",
                    "title": "Spatio-Temporal Conv1D",
                    "points": ["Multi-scale 1D spatial convolutions", "Kernel size = 3, Hidden channels = 64", "Extracts candidate marine neighborhood"],
                    "pill": "Dilated Spatial Convolutions",
                    "icon": "conv1d"
                },
                {
                    "tag": "RETROGRADE DYNAMICS",
                    "title": "Bidirectional ConvLSTM",
                    "points": ["Dual forward/backward temporal recurrence", "Models backward-in-time drift trajectory", "Dual cell state memory gating (64-D)"],
                    "pill": "Bidirectional Temporal Recurrence",
                    "icon": "bilstm"
                },
                {
                    "tag": "NOVEL UNCERTAINTY GATING",
                    "title": "AEU-Attention Mechanism",
                    "points": ["Query: Spatial state | Key/Val: Drift error", "Downweights noisy vectors in turbulent seas", "Preserves multi-snapshot consensus"],
                    "pill": "Adaptive Uncertainty Attention",
                    "icon": "attn"
                },
                {
                    "tag": "MULTI-OBJECTIVE PROJECTION",
                    "title": "Decoupled Latent Heads",
                    "points": ["Classification Head: Source probability P(y)", "Continuous Regression Head: Origin offset", "Preserves physical spatial topology"],
                    "pill": "Dual Output Decoupling",
                    "icon": "heads"
                }
            ]
        },
        {
            "id": "STAGE 5",
            "title": "LOCALIZATION & HIT",
            "sub": "Decision Support & Ground Truth",
            "theme": "#065F46", "light": "#F0FDF4", "border": "#10B981", "badge": "#059669",
            "x": 19.46, "w": 4.04,
            "cards": [
                {
                    "tag": "DUAL LOSS CONVERGENCE",
                    "title": "Focal + Smooth L1 Huber",
                    "points": ["Focal Loss (alpha=0.75, gamma=2.0)", "Solves 1:5 background class imbalance", "Euclidean distance Huber regression"],
                    "pill": "Dual-Task Joint Optimization",
                    "icon": "loss"
                },
                {
                    "tag": "PROBABILITY SURFACE MAP",
                    "title": "Calibrated Origin Likelihood",
                    "points": ["Accuracy: 94.88% (Benchmark Winner)", "Precision: 85.26% | Recall: 64.53%", "F1-Score: 0.7346 | AUC-ROC: 0.9870"],
                    "pill": "High-Confidence Origin Map",
                    "icon": "heatmap"
                },
                {
                    "tag": "CENTROID TRAJECTORY ERROR",
                    "title": "Sub-10 km RMSE Guarantee",
                    "points": ["AST-CLAM Centroid RMSE: 6.86 km", "Random Forest: 29.84 km | XGBoost: 33.69 km", "77.0% lower trajectory dispersion error"],
                    "pill": "RMSE: 6.86 km (< 10 km target)",
                    "icon": "rmse"
                },
                {
                    "tag": "SANCHI REAL-WORLD HIT",
                    "title": "Verified 115m Wreck Hit",
                    "points": ["Origin error: 4.62 km to sunken wreck", "Naive slick centroid baseline: 29.10 km", "84.1% distance reduction achieved!"],
                    "pill": "Disaster Ground Truth Hit",
                    "icon": "hit"
                }
            ]
        }
    ]

    # Y-coordinates for the 4 function cards inside each stage column
    card_y = [7.25, 4.95, 2.65, 0.35]
    card_h = 2.12

    # Render each stage column
    for s_idx, s in enumerate(stages):
        sx = s["x"]
        sw = s["w"]

        # Outer Column Container
        col_container = FancyBboxPatch((sx, 0.20), sw, 9.95,
                                       boxstyle="round,pad=0.06,rounding_size=0.18",
                                       facecolor=s["light"], edgecolor=s["border"], linewidth=1.5, zorder=1)
        ax.add_patch(col_container)

        # Stage Header Banner (cleanly seated at top of column)
        head_banner = FancyBboxPatch((sx + 0.1, 9.45), sw - 0.2, 0.60,
                                     boxstyle="round,pad=0.04,rounding_size=0.10",
                                     facecolor=s["theme"], edgecolor='none', zorder=2)
        ax.add_patch(head_banner)

        # Header Text
        ax.text(sx + sw/2, 9.85, f"{s['id']}: {s['title']}",
                fontfamily=FONT_FAMILY, fontsize=10.2, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=3)
        ax.text(sx + sw/2, 9.60, s['sub'],
                fontfamily=FONT_FAMILY, fontsize=8.2, fontweight='normal', color='#FEF08A' if '3' in s['id'] else '#D1FAE5' if '2' in s['id'] or '5' in s['id'] else '#DBEAFE',
                ha='center', va='center', zorder=3)

        # 4 Inner Function Cards
        for c_idx, c in enumerate(s["cards"]):
            cy = card_y[c_idx]

            # Card background with border
            card_box = FancyBboxPatch((sx + 0.12, cy), sw - 0.24, card_h,
                                      boxstyle="round,pad=0.04,rounding_size=0.09",
                                      facecolor='#FFFFFF', edgecolor=s["border"], linewidth=1.1, zorder=2)
            ax.add_patch(card_box)

            # Category / Tag Pill
            tag_text = c["tag"]
            tag_w = len(tag_text) * 0.070 + 0.28
            tag_pill = FancyBboxPatch((sx + 0.20, cy + card_h - 0.28), tag_w, 0.22,
                                      boxstyle="round,pad=0.02,rounding_size=0.05",
                                      facecolor=s["badge"], edgecolor='none', zorder=3)
            ax.add_patch(tag_pill)
            ax.text(sx + 0.20 + tag_w/2, cy + card_h - 0.17, tag_text,
                    fontfamily=FONT_FAMILY, fontsize=6.6, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)

            # Card Title
            ax.text(sx + 0.20, cy + card_h - 0.48, c["title"],
                    fontfamily=FONT_FAMILY, fontsize=9.4, fontweight='bold', color='#0F172A', va='center', zorder=3)

            # Bullets
            by = cy + card_h - 0.72
            for pt in c["points"]:
                ax.text(sx + 0.22, by, f"• {pt}",
                        fontfamily=FONT_FAMILY, fontsize=7.4, fontweight='normal', color='#334155', va='center', zorder=3)
                by -= 0.25

            # Bottom Summary Pill
            pill_bg = FancyBboxPatch((sx + 0.20, cy + 0.10), sw - 0.40, 0.26,
                                     boxstyle="round,pad=0.02,rounding_size=0.06",
                                     facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=0.8, zorder=3)
            ax.add_patch(pill_bg)
            ax.text(sx + sw/2, cy + 0.23, c["pill"],
                    fontfamily=FONT_FAMILY, fontsize=7.2, fontweight='bold', color=s["theme"], ha='center', va='center', zorder=4)

    # =========================================================================
    # 3. INTER-STAGE PIPELINE FLOW CONNECTORS (Clean Vector Arrows & Badges)
    # =========================================================================
    transitions = [
        (4.65, 5.18, "Raw Grids\n& Meshes", "#1E3A8A"),
        (9.33, 9.86, "Cleaned\nPartitions", "#065F46"),
        (14.01, 14.54, "29-D Latent\nTensor X", "#9A3412"),
        (18.94, 19.46, "Calibrated\nPredictions", "#581C87")
    ]

    for x1, x2, label, col in transitions:
        # Draw 4 clean horizontal flow arrows connecting the card levels
        for y_flow in [8.31, 6.01, 3.71, 1.41]:
            arr = FancyArrowPatch((x1 + 0.04, y_flow), (x2 - 0.04, y_flow),
                                  arrowstyle='-|>', mutation_scale=15,
                                  color=col, linewidth=2.2, zorder=5)
            ax.add_patch(arr)

        # Center transfer badge
        mx = (x1 + x2) / 2
        trans_box = FancyBboxPatch((mx - 0.24, 4.40), 0.48, 0.85,
                                   boxstyle="round,pad=0.03,rounding_size=0.08",
                                   facecolor='#FFFFFF', edgecolor=col, linewidth=1.3, zorder=6)
        ax.add_patch(trans_box)
        ax.text(mx, 4.82, label,
                fontfamily=FONT_FAMILY, fontsize=6.8, fontweight='bold', color=col,
                ha='center', va='center', multialignment='center', zorder=7)

    # Save to high-DPI image
    plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0.04, facecolor='#FFFFFF')
    plt.close()
    print(f"[SUCCESS] Advanced System Architecture Diagram saved to: {output_path}")

if __name__ == '__main__':
    out = os.path.join(r"c:\Users\Jayalakshmi\oil_spill\results", "system_architecture_diagram.png")
    generate_pipeline_diagram(out)
