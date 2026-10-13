"""
High-Fidelity Presentation Generator Matching Sample PPT Exactly
Project: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations
Template: SRM Institute of Science and Technology Official Review 2 Template (Matching Sample Reference)
Authors: Jayalakshmi T, Sachin P, Shivaani M, Varsha U (Guided by Dr. Banu Priya Prathaban)
"""

import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = r"c:\Users\Jayalakshmi\oil_spill"
RESULTS_DIR = os.path.join(BASE_DIR, "results")
OUTPUT_PPTX = os.path.join(BASE_DIR, "Review_2_Oil_Spill_Final.pptx")

# Color Palette: Exact SRM Sample Palette
SRM_NAVY = RGBColor(0, 51, 102)        # #003366 - Header Navy
SRM_BLUE = RGBColor(14, 76, 146)       # #0e4c92 - Secondary Blue
TEXT_DARK = RGBColor(34, 34, 34)       # #222222 - Body Text
TEXT_MUTED = RGBColor(80, 80, 80)     # #505050 - Subtitle Text
WHITE = RGBColor(255, 255, 255)
TABLE_ALT = RGBColor(240, 244, 248)    # #f0f4f8 - Light Table Row
SUCCESS_GREEN = RGBColor(34, 139, 34)  # #228b22 - 100% Completed
PROGRESS_ORANGE = RGBColor(217, 119, 6)# #d97706 - In Progress

LOGO_PATH = os.path.join(RESULTS_DIR, "srm_logo1.png")
ARCH_IMG = os.path.join(RESULTS_DIR, "system_architecture_diagram.png")
PREPROC_IMG = os.path.join(RESULTS_DIR, "preprocessing_slide_graph.png")
CONF_IMG = os.path.join(RESULTS_DIR, "classification_confusion_matrix.png")
COMP_IMG = os.path.join(RESULTS_DIR, "comparison_barchart.png")


def build_deck():
    prs = Presentation()
    # 16:9 Widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_slide_header(slide, title_text):
        # Slide Title on top-left
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(9.5), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Arial"
        p.font.size = Pt(21)
        p.font.bold = True
        p.font.color.rgb = SRM_NAVY
        
        # SRM Logo on top-right
        if os.path.exists(LOGO_PATH):
            slide.shapes.add_picture(LOGO_PATH, Inches(10.6), Inches(0.35), width=Inches(2.0))

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Exact matching Sample Slide 1)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    if os.path.exists(LOGO_PATH):
        s1.shapes.add_picture(LOGO_PATH, Inches(10.5), Inches(0.4), width=Inches(2.1))
        
    # Project Title
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(1.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations and Environmental Uncertainty"
    p1.font.name = "Arial"
    p1.font.size = Pt(23)
    p1.font.bold = True
    p1.font.color.rgb = SRM_NAVY

    # Batch and Review Tag
    p1_sub = tf1.add_paragraph()
    p1_sub.text = "BATCH 10 | 21CSC314P - Big Data Essentials | Project Review 2"
    p1_sub.font.name = "Arial"
    p1_sub.font.size = Pt(13)
    p1_sub.font.bold = True
    p1_sub.font.color.rgb = SRM_BLUE
    p1_sub.space_before = Pt(8)

    # Guidance Section (Left)
    g_box = s1.shapes.add_textbox(Inches(0.8), Inches(3.4), Inches(5.5), Inches(3.0))
    tfg = g_box.text_frame
    tfg.word_wrap = True
    pg_head = tfg.paragraphs[0]
    pg_head.text = "UNDER THE GUIDANCE OF"
    pg_head.font.name = "Arial"
    pg_head.font.size = Pt(11)
    pg_head.font.bold = True
    pg_head.font.color.rgb = SRM_NAVY
    
    pg_name = tfg.add_paragraph()
    pg_name.text = "Dr. BANU PRIYA PRATHABAN"
    pg_name.font.name = "Arial"
    pg_name.font.size = Pt(15)
    pg_name.font.bold = True
    pg_name.font.color.rgb = SRM_NAVY
    pg_name.space_before = Pt(4)

    pg_role = tfg.add_paragraph()
    pg_role.text = "Assistant Professor\nDepartment of Computer Science & Engineering\nSchool of Computing, SRMIST"
    pg_role.font.name = "Arial"
    pg_role.font.size = Pt(11)
    pg_role.font.color.rgb = TEXT_DARK
    pg_role.space_before = Pt(4)

    # Team Members Section (Right)
    m_box = s1.shapes.add_textbox(Inches(6.8), Inches(3.4), Inches(5.7), Inches(3.0))
    tfm = m_box.text_frame
    tfm.word_wrap = True
    pm_head = tfm.paragraphs[0]
    pm_head.text = "TEAM MEMBERS"
    pm_head.font.name = "Arial"
    pm_head.font.size = Pt(11)
    pm_head.font.bold = True
    pm_head.font.color.rgb = SRM_NAVY

    members = [
        "• JAYALAKSHMI T  (RA2411031010115)",
        "• SACHIN P  (RA2411031010117)",
        "• SHIVAANI M  (RA2411031010119)",
        "• VARSHA U  (RA2411031010120)"
    ]
    for m in members:
        pm = tfm.add_paragraph()
        pm.text = m
        pm.font.name = "Arial"
        pm.font.size = Pt(11.5)
        pm.font.color.rgb = TEXT_DARK
        pm.space_before = Pt(4)

    # =========================================================================
    # SLIDE 2: CONTENTS (Exact matching Sample Slide 2)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "Contents")

    c_box = s2.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(5.6))
    tfc = c_box.text_frame
    tfc.word_wrap = True
    
    contents_items = [
        "Dataset",
        "Proposed Model",
        "Overall System Architecture Diagram",
        "Preprocessing (Give information on Big Data Analysis and its steps)",
        "Results of Preprocessing (Insert graphs and table)",
        "Classification (Give information on your novel/proposed model/classifier)",
        "Results of Classification using proposed model (Insert graphs and table)",
        "Comparison with the existing classifier models (Insert graphs and table)",
        "Plan of Action/Member Tasks",
        "References",
        "Attach Geotagged photo taken during Review 2 presentation",
        "Attach Google Google Colab Implementation link"
    ]
    for i, item in enumerate(contents_items):
        p = tfc.paragraphs[0] if i == 0 else tfc.add_paragraph()
        p.text = item
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # =========================================================================
    # SLIDE 3: DATASET PROFILE & BIG DATA SOURCE (Exact matching Sample Slide 3)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "Dataset Profile & Big Data Source")

    ds_box = s3.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(5.8))
    tf_ds = ds_box.text_frame
    tf_ds.word_wrap = True

    sections = [
        ("SANCHI MULTI-TEMPORAL REPOSITORY & BIG DATA ARCHIVE", [
            ("Source Repositories", "Sentinel-1 SAR (IW GRD), ERA5 (ECMWF), CMEMS (Copernicus Marine)"),
            ("Domain Focus", "Multi-Temporal Satellite Observations for Marine Oil Spill Back-Reconstruction"),
            ("Comprehensive Big Data Volume", "60,539,017 candidate grid cell rows across 5 whole-spill folds (2.39 GB Parquet)"),
            ("Sample Training Table", "3,467,398 rows across 645 partitions (100% true positives + 5% hash-sampled negatives)"),
            ("Real Disaster Case Event", "Sanchi Tanker Disaster (20,951 candidate cells, 2 slicks, 632 audited trajectory logs)"),
            ("Core Physical Attributes", "Candidate Lat/Lon, Slick Distance, Bearing, Cloud Spread, Wind Speed/Dir, Ocean Currents")
        ]),
        ("OBSERVATION TAXONOMY & SPATIAL-TEMPORAL TARGETS", [
            ("Candidate Source Positives (y=1)", "Candidate cell <= 10 km from true origin AND release time <= 3 hours (Ground Truth Release)"),
            ("Candidate Ocean Negatives (y=0)", "Background non-source advection cells across the marine domain (Extreme 1:100 Imbalance)")
        ]),
        ("DYNAMIC ENVIRONMENTAL FORCING PARAMETERS", [
            ("ERA5 Atmospheric Reanalysis", "Hourly single-level 10m wind vector components (u10, v10) at 0.25° resolution"),
            ("CMEMS Global Ocean Physics", "Daily surface current velocity components (u, v) at 0.083° resolution capturing mesoscale eddies"),
            ("Advective Drift Residuals", "Snapshot k observed slick center minus advected position (f_drift_err_east, f_drift_err_north)")
        ])
    ]

    is_first = True
    for sec_title, bullet_pairs in sections:
        p_sec = tf_ds.paragraphs[0] if is_first else tf_ds.add_paragraph()
        is_first = False
        p_sec.text = sec_title
        p_sec.font.name = "Arial"
        p_sec.font.size = Pt(11)
        p_sec.font.bold = True
        p_sec.font.color.rgb = SRM_NAVY
        p_sec.space_before = Pt(8)

        for label, val in bullet_pairs:
            p_b = tf_ds.add_paragraph()
            p_b.text = f"• {label}:   {val}"
            p_b.font.name = "Arial"
            p_b.font.size = Pt(10)
            p_b.font.color.rgb = TEXT_DARK
            p_b.space_before = Pt(2)

    # =========================================================================
    # SLIDE 4: PROPOSED MODEL (Exact matching Sample Slide 4)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "Proposed Model: Adaptive Spatial-Temporal ConvLSTM (AST-CLAM)")

    pm_box = s4.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(5.8))
    tf_pm = pm_box.text_frame
    tf_pm.word_wrap = True

    pm_sections = [
        ("Why Novel Adaptive Spatial-Temporal Architecture?", [
            "Conventional Lagrangian models (GNOME, OpenDrift) assume deterministic drift and fail under high sea turbulence.",
            "Standard single-frame detection networks (MCAN, Attention U-Net) perform static segmentation without temporal back-prediction.",
            "AST-CLAM integrates spatial convolution, temporal recurrent dynamics, and dynamic environmental attention in a unified framework."
        ]),
        ("Tri-Branch Feature Decoupling & Alignment", [
            "Branch 1 (Spatial Geometry - 14 Dims): Embeds slick centroid distance, particle cloud dispersion, and elongation.",
            "Branch 2 (Hydrodynamic Forcing - 10 Dims): Encodes ERA5 wind speed/direction, CMEMS currents, and 3% windage drift velocity.",
            "Branch 3 (Drift Mismatch Residuals - 5 Dims): Isolates advective trajectory divergence vectors (f_drift_err_east, f_drift_err_north)."
        ]),
        ("Adaptive Environmental Uncertainty Attention (AEU-Attn)", [
            "Computes dynamic attention between candidate trajectory states (Query) and environmental mismatch vectors (Key, Value).",
            "When drift mismatch indicates severe forcing turbulence, AEU-Attn dynamically attenuates noisy advection vectors.",
            "Amplifies multi-snapshot spatial consensus, ensuring sub-10 km centroid trajectory localization."
        ]),
        ("Dual-Task Optimization Benefits", [
            "Jointly optimizes Focal Cross-Entropy Loss (alpha=0.75, gamma=2.0) to eliminate background class imbalance.",
            "Auxiliary continuous Euclidean distance Huber Loss forces latent embeddings to obey physical spatial topology.",
            "Achieves 94.88% Accuracy, 0.7346 F1-Score, and drops Centroid Trajectory Error from 30+ km down to 6.86 km RMSE."
        ])
    ]

    is_first = True
    for sec_title, bullets in pm_sections:
        p_sec = tf_pm.paragraphs[0] if is_first else tf_pm.add_paragraph()
        is_first = False
        p_sec.text = sec_title
        p_sec.font.name = "Arial"
        p_sec.font.size = Pt(11)
        p_sec.font.bold = True
        p_sec.font.color.rgb = SRM_NAVY
        p_sec.space_before = Pt(8)

        for b in bullets:
            p_b = tf_pm.add_paragraph()
            p_b.text = f"• {b}"
            p_b.font.name = "Arial"
            p_b.font.size = Pt(9.5)
            p_b.font.color.rgb = TEXT_DARK
            p_b.space_before = Pt(2)

    # =========================================================================
    # SLIDE 5: OVERALL SYSTEM ARCHITECTURE DIAGRAM (Exact matching Sample Slide 5)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "Overall System Architecture Diagram")

    # High-resolution, vector-like, perfectly fitted diagram
    if os.path.exists(ARCH_IMG):
        s5.shapes.add_picture(ARCH_IMG, Inches(0.8), Inches(1.3), width=Inches(11.73), height=Inches(5.6))

    # =========================================================================
    # SLIDE 6: PREPROCESSING (Exact matching Sample Slide 6)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "Preprocessing (Big Data Analysis & Pipeline Steps)")

    pp_box = s6.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(5.8))
    tf_pp = pp_box.text_frame
    tf_pp.word_wrap = True

    pp_steps = [
        ("Step 1: Partitioned Big Data Log Ingestion",
         "Mechanism: Apache PyArrow Distributed Dataset Engine",
         "Ingested multi-partition Hive Parquet tables across 5 whole-spill folds. Loaded Fold 0 (659,295 candidate rows) in 0.65 seconds without CPU memory bottleneck. Partitioning by whole spills prevents cross-spill data leakage."),
        
        ("Step 2: Schema Normalization & Singularity Suppression",
         "Mechanism: Vectorized Physical Range Clipping & Time Alignment",
         "Synchronized UTC timestamps across satellite observation intervals and ERA5 hourly forcing. Resolved drift ratio division-by-zero singularities by bounding f_drift_ratio within [0.0, 10.0]."),
         
        ("Step 3: Physical Grid Parameter Imputation",
         "Mechanism: Domain-Specific Missing Value Handling (100% Resolved)",
         "• f_rank_in_hour (120,466 nulls): Missing when snapshot k has 0 particles in that grid cell. Physically imputed with 999.0 (unranked cell).\n• f_drift_err_east_km / north (132,577 nulls): Missing for k=1 (single snapshot). Imputed with 0.0 km mismatch and 1.0 nominal ratio."),
         
        ("Step 4: Adaptive Spatial-Temporal Thresholding & Feature Assembly",
         "Mechanism: Dynamic Otsu-Like Percentile Scoring & Interaction Engineering",
         "Engineered 5 physical interaction features: total forcing velocity, multi-snapshot consensus ratio, and wind-slick bearing alignment. Applied dynamic 80th-percentile thresholding, filtering out 80% empty ocean background.")
    ]

    is_first = True
    for s_title, s_mech, s_desc in pp_steps:
        p_t = tf_pp.paragraphs[0] if is_first else tf_pp.add_paragraph()
        is_first = False
        p_t.text = s_title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_NAVY
        p_t.space_before = Pt(8)

        p_m = tf_pp.add_paragraph()
        p_m.text = s_mech
        p_m.font.name = "Arial"
        p_m.font.size = Pt(9.5)
        p_m.font.bold = True
        p_m.font.color.rgb = SRM_BLUE
        p_m.space_before = Pt(1)

        p_d = tf_pp.add_paragraph()
        p_d.text = s_desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_DARK
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 7: RESULTS OF PREPROCESSING (Exact matching Sample Slide 7)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "Results of Preprocessing (Feature & Class Balance)")

    # Top text
    top_b = s7.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.7), Inches(0.85))
    tf_tb = top_b.text_frame
    tf_tb.word_wrap = True
    pt_h = tf_tb.paragraphs[0]
    pt_h.text = "GROUND-TRUTH SPATIAL CANDIDATE TIER DISTRIBUTION"
    pt_h.font.name = "Arial"
    pt_h.font.size = Pt(10)
    pt_h.font.bold = True
    pt_h.font.color.rgb = SRM_NAVY

    tiers = [
        "• True Source Candidates (y=1): 13.9%:   91,561 cells within 10 km of true spill origin and 3h release period.",
        "• Background Ocean Cells (y=0): 86.1%:   567,734 background cells filtered out by adaptive spatial thresholding."
    ]
    for t_str in tiers:
        pt = tf_tb.add_paragraph()
        pt.text = t_str
        pt.font.name = "Arial"
        pt.font.size = Pt(9)
        pt.font.color.rgb = TEXT_DARK
        pt.space_before = Pt(1)

    # Middle side-by-side graph
    if os.path.exists(PREPROC_IMG):
        s7.shapes.add_picture(PREPROC_IMG, Inches(0.8), Inches(2.05), width=Inches(6.4), height=Inches(3.3))

    # Right side: Table matching Sample Slide 7 Table exactly
    rows_s7 = [
        ["Records Processed (Fold 0)", "659,295 cells"],
        ["Ground Truth Positives (y=1)", "91,561 (13.9%)"],
        ["Candidate Negatives (y=0)", "567,734 (86.1%)"],
        ["Missing Grid Parameters Handled", "518,197 cells (100%)"],
        ["Missing f_rank_in_hour Imputed", "120,466 (Rank 999.0)"],
        ["Missing k=1 Drift Mismatch Imputed", "132,577 (0.0km / 1.0)"],
        ["Engineered Interaction Features", "5 Features Added"],
        ["Adaptive Threshold (80th Pct)", "0.1448 score"],
        ["End-to-End Ingestion Runtime", "1.48 seconds"]
    ]

    t_shape = s7.shapes.add_table(10, 2, Inches(7.4), Inches(2.05), Inches(5.1), Inches(4.8))
    table = t_shape.table
    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(1.9)

    h_cells = ["Preprocessing Metric", "Observed Value"]
    for idx, hc in enumerate(h_cells):
        c = table.cell(0, idx)
        c.text = hc
        c.fill.solid()
        c.fill.fore_color.rgb = SRM_NAVY
        for p in c.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for r_idx, r_data in enumerate(rows_s7):
        for c_idx, val in enumerate(r_data):
            c = table.cell(r_idx + 1, c_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = TABLE_ALT if r_idx % 2 == 0 else WHITE
            for p in c.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9)
                p.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 8: CLASSIFICATION (NOVEL PROPOSED MODEL) (Exact matching Sample Slide 8)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_header(s8, "Classification (Novel / Proposed Classifier Engine)")

    cl_box = s8.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(5.8))
    tf_cl = cl_box.text_frame
    tf_cl.word_wrap = True

    cl_sections = [
        ("MATHEMATICAL FORMULATION OF NOVEL AST-CLAM ENGINE", [
            "P_hat(y=1 | x) = sigma( ClassifierHead( AEU_Attn( Conv1D(x), BiLSTM(x), EnvContext ) ) )",
            "Where x in R^29 represents the decoupled spatial, hydrodynamic, and drift mismatch feature vector.",
            "AEU_Attn computes: Attn(Q, K, V) = Softmax( Q K^T / sqrt(d_k) ) * V * UncertaintyGate(EnvContext)",
            "UncertaintyGate dynamically scales trajectory confidence based on drift mismatch norm ||e_drift||."
        ]),
        ("DUAL-TASK OBJECTIVE FUNCTION (FOCAL LOSS + DISTANCE REGULARIZATION)", [
            "Total Loss: L_total = L_Focal + lambda * L_Huber",
            "Focal Classification Loss: L_Focal = -alpha * (1 - p_t)^gamma * log(p_t)  [alpha=0.75, gamma=2.0]",
            "Smooth L1 Huber Loss: Regularizes the auxiliary centroid head to predict continuous Euclidean distance offset (km).",
            "Prevents false positive hallucinations by penalizing predictions situated far from candidate contours."
        ]),
        ("OPTIMAL ARCHITECTURAL CONFIGURATION", [
            ("Number of Input Features", "29 Dimensions (14 Spatial + 10 Environmental + 5 Drift Mismatches)"),
            ("Conv1D Filter Kernels", "3 kernels with Batch Normalization & GELU activations"),
            ("Temporal LSTM Layers", "2 Bidirectional Layers with 64 hidden units per direction"),
            ("Attention Mechanism", "4-Head Adaptive Environmental Uncertainty Attention (AEU-Attn)"),
            ("Optimization Algorithm", "AdamW (lr=0.005, weight_decay=1e-4) with Cosine Annealing"),
            ("Inference Latency", "Sub-second inference per whole-spill candidate grid")
        ])
    ]

    is_first = True
    for item in cl_sections:
        p_sec = tf_cl.paragraphs[0] if is_first else tf_cl.add_paragraph()
        is_first = False
        p_sec.text = item[0]
        p_sec.font.name = "Arial"
        p_sec.font.size = Pt(11)
        p_sec.font.bold = True
        p_sec.font.color.rgb = SRM_NAVY
        p_sec.space_before = Pt(8)

        if isinstance(item[1][0], tuple):
            for k, v in item[1]:
                p_b = tf_cl.add_paragraph()
                p_b.text = f"• {k}:   {v}"
                p_b.font.name = "Arial"
                p_b.font.size = Pt(9.5)
                p_b.font.color.rgb = TEXT_DARK
                p_b.space_before = Pt(2)
        else:
            for b in item[1]:
                p_b = tf_cl.add_paragraph()
                p_b.text = f"• {b}"
                p_b.font.name = "Arial"
                p_b.font.size = Pt(9.5)
                p_b.font.color.rgb = TEXT_DARK
                p_b.space_before = Pt(2)

    # =========================================================================
    # SLIDE 9: RESULTS OF CLASSIFICATION USING PROPOSED MODEL (Exact matching Sample Slide 9)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_header(s9, "Results of Classification Using Proposed Model")

    # Left: Confusion Matrix Plot
    if os.path.exists(CONF_IMG):
        s9.shapes.add_picture(CONF_IMG, Inches(0.8), Inches(1.3), width=Inches(5.6), height=Inches(5.4))

    # Right: Metric Table + Insights (matching Sample Slide 9)
    metric_rows = [
        ["Overall Model Accuracy", "94.88%"],
        ["Weighted Precision", "0.8526"],
        ["Weighted Recall", "0.6453"],
        ["Weighted F1-Score", "0.7346"],
        ["AUC-ROC Score", "0.9870"],
        ["Centroid Trajectory RMSE", "6.86 km (Target: < 10 km)"],
        ["Real Sanchi Wreck Hit Error", "4.62 km (Verified 115m Wreck)"],
        ["Relative Distance Reduction", "84.1% vs Naive Slick Center"]
    ]

    t_s9_shape = s9.shapes.add_table(9, 2, Inches(6.8), Inches(1.3), Inches(5.7), Inches(3.2))
    t_s9 = t_s9_shape.table
    t_s9.columns[0].width = Inches(3.4)
    t_s9.columns[1].width = Inches(2.3)

    for idx, hc in enumerate(["Evaluation Metric", "Proposed AST-CLAM Score"]):
        c = t_s9.cell(0, idx)
        c.text = hc
        c.fill.solid()
        c.fill.fore_color.rgb = SRM_NAVY
        for p in c.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for r_idx, r_data in enumerate(metric_rows):
        for c_idx, val in enumerate(r_data):
            c = t_s9.cell(r_idx + 1, c_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = TABLE_ALT if r_idx % 2 == 0 else WHITE
            for p in c.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9)
                p.font.bold = (r_idx in [0, 3, 5, 6])
                p.font.color.rgb = SUCCESS_GREEN if (r_idx in [0, 3, 5, 6] and c_idx == 1) else TEXT_DARK

    # Bottom Right: Critical Insights Box
    ins_box = s9.shapes.add_textbox(Inches(6.8), Inches(4.7), Inches(5.7), Inches(2.0))
    tf_ins = ins_box.text_frame
    tf_ins.word_wrap = True
    p_ins_h = tf_ins.paragraphs[0]
    p_ins_h.text = "CRITICAL MODEL INFERENCE INSIGHTS"
    p_ins_h.font.name = "Arial"
    p_ins_h.font.size = Pt(10)
    p_ins_h.font.bold = True
    p_ins_h.font.color.rgb = SRM_NAVY

    insights = [
        "• High True Positive Concentration: Confusion matrix confirms clean separation of origin candidates with 94.88% accuracy.",
        "• Sub-10km Localization Success: Centroid Trajectory RMSE dropped to 6.86 km, satisfying the operational evaluation criterion.",
        "• Real Disaster Ground Truth Recovery: Successfully localized the real Sanchi wreck location to within 4.62 km (an 84.1% distance reduction over naive centroids)."
    ]
    for ins in insights:
        pi = tf_ins.add_paragraph()
        pi.text = ins
        pi.font.name = "Arial"
        pi.font.size = Pt(8.5)
        pi.font.color.rgb = TEXT_DARK
        pi.space_before = Pt(3)

    # =========================================================================
    # SLIDE 10: COMPARISON WITH EXISTING CLASSIFIER MODELS (Exact matching Sample Slide 10)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_header(s10, "Comparison with Existing Classifier Models")

    # Top Bar Chart (matching Sample Slide 10)
    if os.path.exists(COMP_IMG):
        s10.shapes.add_picture(COMP_IMG, Inches(0.8), Inches(1.2), width=Inches(11.73), height=Inches(3.2))

    # Bottom Left Table
    comp_rows = [
        ["Deep MLP", "88.65%", "0.4729", "0.3637", "35.21 km", "58.69 km"],
        ["Attention U-Net (2022)", "88.64%", "0.4390", "0.1948", "29.86 km", "37.48 km"],
        ["Standard ConvLSTM", "89.06%", "0.5062", "0.1949", "30.79 km", "50.97 km"],
        ["XGBoost (GBDT)", "89.26%", "0.5254", "0.3081", "33.69 km", "33.13 km"],
        ["Random Forest", "89.53%", "0.5268", "0.4889", "29.84 km", "25.79 km"],
        ["Proposed AST-CLAM", "94.88%", "0.8526", "0.7346", "6.86 km", "4.62 km"]
    ]

    t_s10_shape = s10.shapes.add_table(7, 6, Inches(0.8), Inches(4.55), Inches(7.5), Inches(2.4))
    t_s10 = t_s10_shape.table
    widths_s10 = [Inches(2.1), Inches(1.0), Inches(1.0), Inches(1.0), Inches(1.2), Inches(1.2)]
    for idx, w in enumerate(widths_s10):
        t_s10.columns[idx].width = w

    for idx, hc in enumerate(["Model Architecture", "Acc (%)", "Prec", "F1", "RMSE (km)", "Sanchi Err"]):
        c = t_s10.cell(0, idx)
        c.text = hc
        c.fill.solid()
        c.fill.fore_color.rgb = SRM_NAVY
        for p in c.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for r_idx, r_data in enumerate(comp_rows):
        is_prop = (r_idx == 5)
        for c_idx, val in enumerate(r_data):
            c = t_s10.cell(r_idx + 1, c_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor(230, 245, 230) if is_prop else (TABLE_ALT if r_idx % 2 == 0 else WHITE)
            for p in c.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(8.5)
                p.font.bold = is_prop
                p.font.color.rgb = SUCCESS_GREEN if is_prop and c_idx >= 1 else TEXT_DARK

    # Bottom Right Takeaways
    tk_box = s10.shapes.add_textbox(Inches(8.5), Inches(4.55), Inches(4.0), Inches(2.4))
    tf_tk = tk_box.text_frame
    tf_tk.word_wrap = True
    p_tk_h = tf_tk.paragraphs[0]
    p_tk_h.text = "COMPARATIVE BENCHMARK TAKEAWAYS"
    p_tk_h.font.name = "Arial"
    p_tk_h.font.size = Pt(9.5)
    p_tk_h.font.bold = True
    p_tk_h.font.color.rgb = SRM_NAVY

    takeaways = [
        "• +5.35% Accuracy vs Best Baseline: Reaches 94.88%, effectively suppressing noisy ocean background false positives.",
        "• +0.2457 F1 Improvement: Outperforms Random Forest (0.4889) and XGBoost (0.3081) by dynamic multi-snapshot consensus.",
        "• 4.3x Lower Trajectory Error: Drops Centroid RMSE from 29.84 km down to 6.86 km, meeting sub-10 km requirements.",
        "• Decisive Sanchi Disaster Recovery: Hits 4.62 km to the true wreck, beating naive center (29.1 km) by 84.1%."
    ]
    for tk in takeaways:
        ptk = tf_tk.add_paragraph()
        ptk.text = tk
        ptk.font.name = "Arial"
        ptk.font.size = Pt(8.5)
        ptk.font.color.rgb = TEXT_DARK
        ptk.space_before = Pt(3)

    # =========================================================================
    # SLIDE 11: PLAN OF ACTION / MEMBER TASKS (Exact matching Sample Slide 11)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_slide_header(s11, "Plan of Action / Member Tasks & Progress")

    tasks_data = [
        ["1", "SACHIN P\n(RA2411031010117)", "Data Ingestion & Distributed Preprocessing:\n• PyArrow Big Data extraction (60.5M rows across 5 folds)\n• Physical parameter imputation (Rank 999.0, Drift 1.0)\n• Adaptive spatial thresholding (80th percentile candidate mask)", "100% Completed", SUCCESS_GREEN],
        ["2", "SHIVAANI M\n(RA2411031010119)", "Literature Benchmarking & Comparative Analysis:\n• Evaluation of 5 baseline models (RF, XGBoost, MLP, ConvLSTM, U-Net)\n• Strict whole-spill partitioned validation (zero data leakage)\n• Statistical comparative evaluation and metrics documentation", "100% Completed", SUCCESS_GREEN],
        ["3", "JAYALAKSHMI T\n(RA2411031010115)", "Proposed Model Architecture & Optimization:\n• Novel AST-CLAM deep learning model development\n• Adaptive Environmental Uncertainty Attention (AEU-Attn) design\n• Dual-Task Focal Loss + continuous distance Huber optimization", "100% Completed", SUCCESS_GREEN],
        ["4", "VARSHA U\n(RA2411031010120)", "Visualization Dashboard & Review Compilation:\n• Power BI interactive spatial oil spill trajectory dashboard\n• Hydrodynamic wind and current velocity overlay mapping\n• Review 2 PPT compilation & PBL 3 Final Dashboard integration", "60% (In Progress)", PROGRESS_ORANGE]
    ]

    t_s11_shape = s11.shapes.add_table(5, 4, Inches(0.8), Inches(1.4), Inches(11.73), Inches(5.4))
    t_s11 = t_s11_shape.table
    widths_s11 = [Inches(0.7), Inches(2.6), Inches(6.43), Inches(2.0)]
    for idx, w in enumerate(widths_s11):
        t_s11.columns[idx].width = w

    headers_s11 = ["S.No", "Team Member & Reg. No", "Assigned Technical Responsibilities", "Review 2 Status"]
    for idx, hc in enumerate(headers_s11):
        c = t_s11.cell(0, idx)
        c.text = hc
        c.fill.solid()
        c.fill.fore_color.rgb = SRM_NAVY
        for p in c.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for r_idx, r_data in enumerate(tasks_data):
        for c_idx in range(4):
            c = t_s11.cell(r_idx + 1, c_idx)
            c.text = r_data[c_idx]
            c.fill.solid()
            c.fill.fore_color.rgb = TABLE_ALT if r_idx % 2 == 0 else WHITE
            for p in c.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9)
                p.font.bold = (c_idx in [0, 3])
                p.font.color.rgb = r_data[4] if c_idx == 3 else TEXT_DARK

    # =========================================================================
    # SLIDE 12: REFERENCES (Exact matching Sample Slide 12)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_slide_header(s12, "References")

    r_box = s12.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(5.8))
    tf_ref = r_box.text_frame
    tf_ref.word_wrap = True

    references = [
        "[1] S. El Mohtar, B. Ait-El-Fquih, O. Knio, I. Lakkis, and I. Hoteit, 'Bayesian identification of oil spill source parameters from image contours,' Marine Pollution Bulletin, vol. 169, Art. no. 112514, 2021.",
        "[2] M. A. E. R. Hammoud, I. Lakkis, O. Knio, and I. Hoteit, 'Moving source identification in an uncertain marine flow: Mediterranean Sea application,' Ocean Engineering, vol. 220, Art. no. 108435, 2021.",
        "[3] Y. Li, X. Lyu, A. C. Frery, and P. Ren, 'Oil spill detection with multiscale conditional adversarial networks with small-data training,' Remote Sensing, vol. 13, no. 12, Art. no. 2378, 2021.",
        "[4] Y. Chen and Z. Wang, 'Marine oil spill detection from SAR images based on Attention U-Net model using polarimetric and wind speed information,' IJERPH, vol. 19, no. 19, Art. no. 12315, 2022.",
        "[5] Y. Li, W. Huang, X. Lyu, S. Liu, Z. Zhao, and P. Ren, 'An adversarial learning approach to forecasted wind field correction with an application to oil spill drift prediction,' IJAEOG, vol. 112, Art. no. 102924, 2022.",
        "[6] A. S. Dhavalikar and P. C. Choudhari, 'Prediction of oil spill trajectory on the ocean surface using mathematical modeling,' IEEE JSTARS, vol. 15, pp. 2482–2493, 2022.",
        "[7] L. F. Tessarolo et al., 'A surface Lagrangian algorithm applied to the 2019 South Atlantic oil spill,' Ocean Engineering, vol. 268, Art. no. 113505, 2023.",
        "[8] F. Chen, H. Balzter, F. Zhou, P. Ren, and H. Zhou, 'DGNet: Distribution guided efficient learning for oil spill image segmentation,' IEEE TGRS, vol. 61, pp. 1–14, 2023.",
        "[9] C. Li et al., 'A self-evolving deep learning algorithm for automatic oil spill detection in Sentinel-1 SAR images,' Remote Sensing of Environment, vol. 299, Art. no. 113872, 2023.",
        "[10] P. Cervantes-Hernández et al., 'Combined use of SAR images and numerical simulations to identify source and trajectories of oil spills,' Marine Pollution Bulletin, vol. 199, Art. no. 115981, 2024.",
        "[11] S. El Mohtar, O. Le Maître, O. Knio, and I. Hoteit, 'Iterative data-driven construction of surrogates for an efficient Bayesian identification of oil spill source parameters,' Computational Geosciences, vol. 28, pp. 681–696, 2024.",
        "[12] T. V. La et al., 'Monitoring of spatio-temporal variations of oil slicks via collocation of multi-source satellite images,' Remote Sensing, vol. 16, no. 16, Art. no. 3110, 2024."
    ]

    for i, ref in enumerate(references):
        pr = tf_ref.paragraphs[0] if i == 0 else tf_ref.add_paragraph()
        pr.text = ref
        pr.font.name = "Arial"
        pr.font.size = Pt(8.5)
        pr.font.color.rgb = TEXT_DARK
        pr.space_before = Pt(3)

    # =========================================================================
    # SLIDE 13: GEOTAGGED PHOTO (Exact matching Sample Slide 13)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_slide_header(s13, "Geotagged Photo")

    ph_card = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.2), Inches(1.5), Inches(8.93), Inches(5.3))
    ph_card.fill.solid()
    ph_card.fill.fore_color.rgb = TABLE_ALT
    ph_card.line.color.rgb = SRM_NAVY
    ph_card.line.width = Pt(1.5)
    tf_ph = ph_card.text_frame
    tf_ph.word_wrap = True

    pph = tf_ph.paragraphs[0]
    pph.text = "📷\n\nAttach Geotagged Photo Taken During Review 2 Presentation"
    pph.font.name = "Arial"
    pph.font.size = Pt(16)
    pph.font.bold = True
    pph.font.color.rgb = SRM_NAVY
    pph.alignment = PP_ALIGN.CENTER

    pph_sub = tf_ph.add_paragraph()
    pph_sub.text = "\n[Insert photo taken in lab/classroom with visible GPS latitude, longitude, and timestamp stamp]"
    pph_sub.font.name = "Arial"
    pph_sub.font.size = Pt(11)
    pph_sub.font.color.rgb = TEXT_MUTED
    pph_sub.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 14: IMPLEMENTATION LINK (Exact matching Sample Slide 14)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_slide_header(s14, "GitHub Implementation Link")

    gh_box = s14.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(5.8))
    tf_gh = gh_box.text_frame
    tf_gh.word_wrap = True

    p_gh_h = tf_gh.paragraphs[0]
    p_gh_h.text = "NOTEBOOK MODULE HIGHLIGHTS & EXECUTION INSTRUCTIONS:"
    p_gh_h.font.name = "Arial"
    p_gh_h.font.size = Pt(11)
    p_gh_h.font.bold = True
    p_gh_h.font.color.rgb = SRM_NAVY

    gh_bullets = [
        "• Local Repository Mirror: Included in workspace as data_preprocessing.py, model_architecture.py, and train_and_benchmark.py.",
        "• Distributed Pipeline Setup: Utilizes Apache PyArrow Parquet engine for high-throughput Hive partitioned reading (60.5M records).",
        "• Automated Data Pipeline: Executes Section 1 through Section 5: Data Ingestion -> Parameter Imputation -> Adaptive Thresholding -> AST-CLAM.",
        "• Reproducible Artifacts: Exports preprocessing_metrics.csv, preprocessing_plots.png, and model_comparison_charts.png at 300 DPI.",
        "• 6-Model Comparative Benchmarks: Evaluates all 6 algorithms on identical whole-spill splits, reporting Accuracy, Precision, Recall, F1, and Centroid RMSE."
    ]
    for b in gh_bullets:
        pb = tf_gh.add_paragraph()
        pb.text = b
        pb.font.name = "Arial"
        pb.font.size = Pt(10)
        pb.font.color.rgb = TEXT_DARK
        pb.space_before = Pt(6)

    p_url = tf_gh.add_paragraph()
    p_url.text = "\nGitHub Implementation URL:               https://github.com/Jayalakshmi-TR/Oil-Spill-Source-Reconstruction.git"
    p_url.font.name = "Arial"
    p_url.font.size = Pt(12)
    p_url.font.bold = True
    p_url.font.color.rgb = SRM_NAVY
    p_url.space_before = Pt(20)

    # =========================================================================
    # SLIDE 15: THANK YOU (Exact matching Sample Slide 15)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    if os.path.exists(LOGO_PATH):
        s15.shapes.add_picture(LOGO_PATH, Inches(4.7), Inches(2.2), width=Inches(3.9))

    ty_b = s15.shapes.add_textbox(Inches(2.0), Inches(4.5), Inches(9.33), Inches(1.5))
    tf_ty = ty_b.text_frame
    tf_ty.word_wrap = True
    pty = tf_ty.paragraphs[0]
    pty.text = "THANK YOU"
    pty.font.name = "Arial"
    pty.font.size = Pt(38)
    pty.font.bold = True
    pty.font.color.rgb = SRM_NAVY
    pty.alignment = PP_ALIGN.CENTER

    prs.save(OUTPUT_PPTX)
    print(f"[SUCCESS] Sample-matched presentation generated cleanly at: {OUTPUT_PPTX}")


if __name__ == "__main__":
    build_deck()
