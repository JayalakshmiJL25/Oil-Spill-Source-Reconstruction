"""
Automated PowerPoint Presentation Generator for Review 2
Project: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations
Template: SRM Institute of Science and Technology Official Review 2 Template
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
OUTPUT_PPTX = os.path.join(BASE_DIR, "Review_2_Oil_Spill_Presentation.pptx")

# Color Palette: SRM Royal Academic Theme
SRM_BLUE = RGBColor(0, 51, 102)        # #003366 - Deep Navy
SRM_ACCENT = RGBColor(30, 90, 160)     # #1e5aa0 - Academic Blue
DARK_GRAY = RGBColor(40, 40, 40)       # #282828 - Body text
LIGHT_BG = RGBColor(248, 250, 252)     # #f8fafc - Card background
WHITE = RGBColor(255, 255, 255)
GREEN = RGBColor(39, 174, 96)          # #27ae60 - Success highlight
GOLD = RGBColor(212, 160, 23)          # #d4a017 - Accent gold
CARD_BORDER = RGBColor(218, 225, 233)


def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    logo_path = os.path.join(RESULTS_DIR, "srm_logo1.png")
    has_logo = os.path.exists(logo_path)

    def add_header(slide, title_text, category_text="Review 2 Evaluation"):
        # Header background banner
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(9.5), Inches(0.9))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_sub = tf.paragraphs[0]
        p_sub.text = category_text.upper()
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(10)
        p_sub.font.bold = True
        p_sub.font.color.rgb = GOLD
        
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = SRM_BLUE
        
        # Add SRM Logo
        if has_logo:
            slide.shapes.add_picture(logo_path, Inches(10.8), Inches(0.35), width=Inches(1.8))

        # Thin divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.73), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = CARD_BORDER
        line.line.color.rgb = CARD_BORDER

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    
    # Top banner card
    top_shape = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.3))
    top_shape.fill.solid()
    top_shape.fill.fore_color.rgb = SRM_BLUE
    top_shape.line.fill.background()

    # SRM Logo on Title Slide
    if has_logo:
        s1.shapes.add_picture(logo_path, Inches(5.4), Inches(0.8), width=Inches(2.5))

    # Title box
    tbox = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(2.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations and Environmental Uncertainty"
    p.font.name = "Arial"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = SRM_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf1.add_paragraph()
    p2.text = "Review 2 Presentation"
    p2.font.name = "Arial"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = GOLD
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(12)

    # Info Cards Container (Two columns)
    # Faculty Guide Card
    c1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.3), Inches(4.8), Inches(2.3))
    c1.fill.solid()
    c1.fill.fore_color.rgb = LIGHT_BG
    c1.line.color.rgb = CARD_BORDER
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    
    p_g_head = tf_c1.paragraphs[0]
    p_g_head.text = "FACULTY GUIDE"
    p_g_head.font.name = "Arial"
    p_g_head.font.size = Pt(11)
    p_g_head.font.bold = True
    p_g_head.font.color.rgb = GOLD
    
    p_g_name = tf_c1.add_paragraph()
    p_g_name.text = "Dr. Banu Priya Prathaban"
    p_g_name.font.name = "Arial"
    p_g_name.font.size = Pt(15)
    p_g_name.font.bold = True
    p_g_name.font.color.rgb = SRM_BLUE
    p_g_name.space_before = Pt(6)
    
    p_g_dept = tf_c1.add_paragraph()
    p_g_dept.text = "Department of Computer Science & Engineering\nSRM Institute of Science and Technology"
    p_g_dept.font.name = "Arial"
    p_g_dept.font.size = Pt(11)
    p_g_dept.font.color.rgb = DARK_GRAY
    p_g_dept.space_before = Pt(4)

    # Team Members Card
    c2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(4.3), Inches(4.8), Inches(2.3))
    c2.fill.solid()
    c2.fill.fore_color.rgb = LIGHT_BG
    c2.line.color.rgb = CARD_BORDER
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    
    p_m_head = tf_c2.paragraphs[0]
    p_m_head.text = "TEAM MEMBERS (NAMES & REG NOS)"
    p_m_head.font.name = "Arial"
    p_m_head.font.size = Pt(11)
    p_m_head.font.bold = True
    p_m_head.font.color.rgb = GOLD
    
    members = [
        ("Jayalakshmi T", "RA2411031010115", "Proposed Model Dev"),
        ("Sachin P", "RA2411031010117", "Data Engineering"),
        ("Shivaani M", "RA2411031010119", "Comparative Analysis"),
        ("Varsha U", "RA2411031010120", "Visualization & Dashboard")
    ]
    for name, reg, role in members:
        pm = tf_c2.add_paragraph()
        pm.text = f"• {name}  ({reg})  —  {role}"
        pm.font.name = "Arial"
        pm.font.size = Pt(10.5)
        pm.font.color.rgb = DARK_GRAY
        pm.space_before = Pt(2)

    # =========================================================================
    # SLIDE 2: CONTENTS SLIDE (Exact Template Checklist)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Contents / Agenda", "Review 2 Presentation Structure")

    contents_list = [
        "1. Dataset (Synthetic v4 Big Data & Sanchi Real Disaster Archives)",
        "2. Proposed Model (Adaptive Spatial-Temporal ConvLSTM with Attention)",
        "3. Overall System Architecture Diagram (Layer 1 to Layer 5 Workflow)",
        "4. Preprocessing: Big Data Analysis & Pipeline Steps",
        "5. Results of Preprocessing (Inserted Quantitative Table & Visual Dashboard)",
        "6. Classification: Novel Proposed Classifier (AST-CLAM Architecture)",
        "7. Results of Classification Using Proposed Model (Accuracy, F1, RMSE)",
        "8. Comparison with Existing Classifier Models (RF, XGB, MLP, ConvLSTM, U-Net)",
        "9. Plan of Action / Member Tasks Breakdown",
        "10. References (Key High-Impact Literature Citations)",
        "11. Attach Geotagged Photo Taken During Review 2 Presentation",
        "12. Attach Google Colab Implementation Link"
    ]

    # Split contents into two neat columns
    col1_items = contents_list[:6]
    col2_items = contents_list[6:]

    for col_idx, items in enumerate([col1_items, col2_items]):
        left_x = Inches(0.8 + col_idx * 5.9)
        cbox = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(1.6), Inches(5.7), Inches(5.4))
        cbox.fill.solid()
        cbox.fill.fore_color.rgb = LIGHT_BG
        cbox.line.color.rgb = CARD_BORDER
        tf_c = cbox.text_frame
        tf_c.word_wrap = True
        
        for i, item in enumerate(items):
            p_item = tf_c.paragraphs[0] if i == 0 else tf_c.add_paragraph()
            p_item.text = item
            p_item.font.name = "Arial"
            p_item.font.size = Pt(11.5)
            p_item.font.bold = (i in [1, 2, 4, 6, 7]) # Highlight primary technical items
            p_item.font.color.rgb = SRM_BLUE if (i in [1, 2, 4, 6, 7]) else DARK_GRAY
            p_item.space_before = Pt(12)

    # =========================================================================
    # SLIDE 3: 1. DATASET
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "1. Dataset Specifications & Big Data Inventory", "Data Engineering")

    # 4 Dataset Cards
    ds_cards = [
        ("Comprehensive Big Data Table (v4 Full)", 
         "• 60,539,017 candidate grid rows across 5 whole-spill folds.\n"
         "• Stored in Apache Parquet (115 partitions, 2.39 GB on disk).\n"
         "• 1,000 synthetic spills under realistic 2018 East China Sea conditions.\n"
         "• Positive class ratio: 0.77% (cell <= 10 km and release <= 3 h).", 
         Inches(0.8), Inches(1.6)),
        
        ("Stratified Training Table (v4 Sample)", 
         "• 3,467,398 rows across 645 partitions (238.2 MB).\n"
         "• Retains 100% true positives + exactly 5% hash-sampled negatives.\n"
         "• Balanced sample weights (w_sample_weight) correct for negative sampling.\n"
         "• Partitions strictly split train/test by id_fold (zero spill leakage).", 
         Inches(6.8), Inches(1.6)),
         
        ("Real-World Sanchi Disaster Event Archive", 
         "• 20,951 candidate cells from Sentinel-1 SAR and VIIRS observations.\n"
         "• 632 audited tanker drift timestamps with AIS velocity alignment.\n"
         "• Benchmarked against verified wreck location at 115 m depth (28.375°N, 125.942°E).\n"
         "• 2 distinct satellite slicks captured on 18 Jan 2018.", 
         Inches(0.8), Inches(4.3)),
         
        ("Multi-Source Environmental Reanalysis Forcing", 
         "• ERA5 Atmospheric Reanalysis: Hourly 10m wind fields (u10, v10) at 0.25°.\n"
         "• CMEMS Physical Ocean Reanalysis: Surface current velocities (u, v) at 0.083°.\n"
         "• Stokes drift wave radiation stress and windage coefficient (3%).\n"
         "• Dynamic hourly forcing uncertainty wandering around drawn mean.", 
         Inches(6.8), Inches(4.3))
    ]

    for title, desc, x, y in ds_cards:
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.7), Inches(2.5))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = CARD_BORDER
        tf = box.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_BLUE
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = DARK_GRAY
        p_d.space_before = Pt(6)

    # =========================================================================
    # SLIDE 4: 2. PROPOSED MODEL
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "2. Proposed Novel Deep Learning Model (AST-CLAM)", "Novel Deep Learning Architecture")

    # Overview banner
    ov = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.73), Inches(1.1))
    ov.fill.solid()
    ov.fill.fore_color.rgb = SRM_BLUE
    ov.line.fill.background()
    tf_ov = ov.text_frame
    tf_ov.word_wrap = True
    p_ov_t = tf_ov.paragraphs[0]
    p_ov_t.text = "AST-CLAM: Adaptive Spatial-Temporal Convolutional LSTM with Attention Mechanisms"
    p_ov_t.font.name = "Arial"
    p_ov_t.font.size = Pt(15)
    p_ov_t.font.bold = True
    p_ov_t.font.color.rgb = WHITE
    p_ov_d = tf_ov.add_paragraph()
    p_ov_d.text = "A physics-informed deep learning architecture designed to overcome environmental forcing divergence in satellite oil spill source reconstruction."
    p_ov_d.font.name = "Arial"
    p_ov_d.font.size = Pt(11)
    p_ov_d.font.color.rgb = RGBColor(220, 230, 242)
    p_ov_d.space_before = Pt(4)

    # 3 Architectural Innovations Cards
    innovations = [
        ("1. Tri-Branch Dynamic Decoupling", 
         "• Spatial Branch (14 dims): Encodes slick polygon centroid, particle dispersion radius, and cluster spread.\n"
         "• Environmental Branch (10 dims): Embeds ERA5 wind vectors, CMEMS currents, and 3% windage advection.\n"
         "• Drift Mismatch Branch (5 dims): Explicitly isolates advective trajectory divergence vectors (f_drift_err).",
         Inches(0.8), Inches(2.9)),
        
        ("2. Adaptive Uncertainty Attention (AEU-Attn)",
         "• Calculates dynamic cross-attention between spatial candidate states (Q) and environmental forcing uncertainty (K, V).\n"
         "• When drift mismatch indicates high sea-state turbulence, the attention gate downweights noisy advection.\n"
         "• Amplifies multi-snapshot consensus to preserve trajectory integrity.",
         Inches(4.8), Inches(2.9)),
         
        ("3. Dual-Task Multi-Objective Heads",
         "• Classification Head: Outputs source probability P(y_is_source=1) optimized via Focal Cross-Entropy Loss (alpha=0.75, gamma=2.0).\n"
         "• Centroid Offset Regression Head: Predicts continuous Euclidean distance offset (km) trained with Smooth L1 Huber Loss.\n"
         "• Ensures latent space is physically consistent with spatial coordinates.",
         Inches(8.8), Inches(2.9))
    ]

    for title, desc, x, y in innovations:
        box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.73), Inches(4.1))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = CARD_BORDER
        tf = box.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(12.5)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_BLUE
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = DARK_GRAY
        p_d.space_before = Pt(8)

    # =========================================================================
    # SLIDE 5: 3. OVERALL SYSTEM ARCHITECTURE DIAGRAM
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "3. Overall System Architecture & Data Pipeline", "System Engineering Workflow")

    layers = [
        ("Layer 1: Ingestion", "Sentinel-1 SAR Slicks\nERA5 Wind (u10, v10)\nCMEMS Ocean Currents\nSanchi Audited AIS Tracks", Inches(0.8)),
        ("Layer 2: Big Data Preproc", "PyArrow Distributed Engine\nNoise Cleaning & Scaling\nPhysical Grid Imputation\nAdaptive Thresholding", Inches(3.2)),
        ("Layer 3: Tri-Branch Fusion", "Spatial Geometry (14 dims)\nHydrodynamic Field (10 dims)\nDrift Mismatches (5 dims)\nConcatenation & Norm", Inches(5.6)),
        ("Layer 4: AST-CLAM Core", "Spatio-Temporal Conv1D\nBidirectional LSTM Core\nAEU-Attn Uncertainty Gating\nDual Classification/Offset", Inches(8.0)),
        ("Layer 5: Decision Output", "Calibrated Source Map\nSub-10km Centroid RMSE\nOrigin Localization Hit\nReal Wreck Recovery", Inches(10.4))
    ]

    for title, desc, x in layers:
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.15), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG
        card.line.color.rgb = SRM_ACCENT
        tf = card.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_BLUE
        p_t.alignment = PP_ALIGN.CENTER
        
        # Inner box
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = DARK_GRAY
        p_d.space_before = Pt(16)
        p_d.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 6: 4. PREPROCESSING (BIG DATA ANALYSIS & STEPS)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "4. Preprocessing: Big Data Analysis & Pipeline Steps", "Data Engineering")

    steps = [
        ("Step 1: Partitioned Big Data Extraction & Profiling",
         "• Scanned and profiled full dataset archives (60.5M records) and representative sample folds.\n"
         "• Utilized Apache PyArrow Parquet engine to read Hive-partitioned files (Fold 0: 659,295 cells in 0.65s).\n"
         "• Enforced strict whole-spill partitioning by id_fold (0..4) to guarantee zero data leakage."),
        
        ("Step 2: Systematic Noise Cleaning & Outlier Suppression",
         "• Identified physical anomalies and corrupted boundary values across spatial-temporal grid coordinates.\n"
         "• Handled drift ratio singularities (division by near-zero displacement) clipped to nominal [0.0, 10.0].\n"
         "• Synchronized UTC time stamps across satellite observation frames and hourly ERA5 reanalysis."),
         
        ("Step 3: Physical Grid Parameter Imputation",
         "• f_rank_in_hour (120,466 nulls): Missing when snapshot k has 0 particles in that grid cell. Physically imputed with 999.0 (unranked / zero-priority candidate).\n"
         "• f_drift_err (132,577 nulls): Missing for k=1 (single snapshot). Imputed with neutral baseline (0.0 km east/north mismatch, 1.0 nominal ratio)."),
         
        ("Step 4: Adaptive Spatial-Temporal Thresholding & Feature Engineering",
         "• Engineered 5 hydrodynamic interaction features: total forcing velocity, multi-snapshot consensus ratio, wind alignment.\n"
         "• Implemented dynamic quantile adaptive thresholding (80th percentile) combining particle share with Euclidean proximity, filtering 80% empty ocean background.")
    ]

    for i, (title, desc) in enumerate(steps):
        y_pos = Inches(1.6 + i * 1.35)
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y_pos, Inches(11.73), Inches(1.2))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = CARD_BORDER
        tf = box.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_BLUE
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = DARK_GRAY
        p_d.space_before = Pt(3)

    # =========================================================================
    # SLIDE 7: 5. RESULTS OF PREPROCESSING (TABLE)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "5. Results of Preprocessing: Quantitative Metrics Table", "Data Engineering")

    # Table with 10 metrics
    rows = [
        ["Total Processed Records (Fold 0)", "659,295", "Hive-partitioned Parquet (200 Spills)"],
        ["Ground Truth Source Positives (y=1)", "91,561 (13.89%)", "Cell <= 10 km from source, release <= 3 h"],
        ["Candidate Negatives (y=0)", "567,734 (86.11%)", "Background ocean grid cells"],
        ["Missing Grid Parameters Handled", "518,197 cells", "100% resolved without synthetic data drop"],
        ["Missing f_rank_in_hour Imputed", "120,466 cells", "Physical rank 999.0 (Unranked cell)"],
        ["Missing k=1 Drift Mismatch Imputed", "132,577 cells", "0.0 km east/north, 1.0 nominal ratio"],
        ["Engineered Interaction Features", "5 Features Added", "Windage speed, consensus ratio, alignment"],
        ["Adaptive Segmentation Threshold", "0.1448", "80th percentile dynamic confidence"],
        ["Segmented High-Potential Cells", "131,859 cells", "Candidate region for deep learning"],
        ["End-to-End Preprocessing Runtime", "1.48 s", "High-throughput PyArrow execution"]
    ]

    table_shape = s7.shapes.add_table(11, 3, Inches(0.8), Inches(1.6), Inches(11.73), Inches(5.2))
    table = table_shape.table
    table.columns[0].width = Inches(4.5)
    table.columns[1].width = Inches(2.5)
    table.columns[2].width = Inches(4.73)

    headers = ["Preprocessing Parameter / Metric", "Value", "Operational / Physical Interpretation"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = SRM_BLUE
        for p in cell.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for row_idx, r in enumerate(rows):
        for col_idx, val in enumerate(r):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BG if row_idx % 2 == 0 else WHITE
            for p in cell.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9.5)
                p.font.color.rgb = DARK_GRAY

    # =========================================================================
    # SLIDE 8: 5. RESULTS OF PREPROCESSING (GRAPHS)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "5. Results of Preprocessing: Visual Analytics Dashboard", "Data Engineering")

    preproc_plot = os.path.join(RESULTS_DIR, "preprocessing_plots.png")
    if os.path.exists(preproc_plot):
        s8.shapes.add_picture(preproc_plot, Inches(0.8), Inches(1.5), width=Inches(8.5))
    
    # Text sidebar explaining 4 panels
    sb = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(1.5), Inches(3.0), Inches(5.4))
    sb.fill.solid()
    sb.fill.fore_color.rgb = LIGHT_BG
    sb.line.color.rgb = CARD_BORDER
    tf_sb = sb.text_frame
    tf_sb.word_wrap = True
    
    p_sb_h = tf_sb.paragraphs[0]
    p_sb_h.text = "Dashboard Insights:"
    p_sb_h.font.name = "Arial"
    p_sb_h.font.size = Pt(12)
    p_sb_h.font.bold = True
    p_sb_h.font.color.rgb = SRM_BLUE
    
    notes = [
        "Panel (A): Shows 100% resolution of missing rank and drift values.",
        "Panel (B): ERA5 wind speed (mean ~6.8 m/s) and CMEMS current speed (mean ~0.22 m/s) distributions.",
        "Panel (C): Clear bimodal separation of particle consensus between true source and background.",
        "Panel (D): Dispersion across ensemble levels confirms 10km source radius bounding."
    ]
    for n in notes:
        pn = tf_sb.add_paragraph()
        pn.text = n
        pn.font.name = "Arial"
        pn.font.size = Pt(9.5)
        pn.font.color.rgb = DARK_GRAY
        pn.space_before = Pt(8)

    # =========================================================================
    # SLIDE 9: 6. CLASSIFICATION (NOVEL PROPOSED MODEL)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "6. Classification: Novel Proposed Classifier (AST-CLAM)", "Novel Deep Learning Architecture")

    # Math & Mechanism breakdown
    arch_cards = [
        ("Feature Input Formulation (29 Dimensions)",
         "• Spatial Geometry (14 features): f_dist_slick_km, f_dist_cloud_km, f_share_mean_1k, f_cloud_spread_km, etc.\n"
         "• Hydrodynamic Forcing (10 features): f_wind_speed_ms, f_current_speed_ms, fe_total_forcing_speed, fe_wind_alignment.\n"
         "• Drift Residuals (5 features): f_drift_err_east_km, f_drift_err_north_km, f_drift_ratio, fe_has_drift_vector.",
         Inches(0.8), Inches(1.6)),
         
        ("Spatio-Temporal Sequence Modeling",
         "• Spatio-Temporal Conv1D: Multi-channel 1D convolutions extract local candidate cell interactions.\n"
         "• Bidirectional Temporal LSTM: 2-layer BiLSTM captures retrograde temporal sequence dynamics (t = 0 to -120 h).\n"
         "• Models physical trajectory momentum and non-linear advective transport.",
         Inches(6.8), Inches(1.6)),
         
        ("Adaptive Environmental Uncertainty Attention (AEU-Attn)",
         "• Query (Q): Spatio-temporal candidate trajectory hidden state.\n"
         "• Key (K) & Value (V): Dynamic environmental forcing vectors & drift error residuals.\n"
         "• Formula: Context = Softmax(Q K^T / sqrt(d_k)) * V * UncertaintyGate(env_context).\n"
         "• Attenuates erroneous drift trajectories under turbulent sea states; amplifies multi-snapshot consensus.",
         Inches(0.8), Inches(4.3)),
         
        ("Dual-Task Optimization Objective",
         "• Total Loss = L_Focal + lambda * L_Huber\n"
         "• L_Focal = -alpha * (1 - p_t)^gamma * log(p_t)  [alpha=0.75, gamma=2.0, combats 1:100 imbalance].\n"
         "• L_Huber: Smooth L1 distance error regression on continuous source distance (km).\n"
         "• Forces latent embeddings to obey physical spatial Euclidean geometry.",
         Inches(6.8), Inches(4.3))
    ]

    for title, desc, x, y in arch_cards:
        box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.7), Inches(2.5))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = CARD_BORDER
        tf = box.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = "Arial"
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_BLUE
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = DARK_GRAY
        p_d.space_before = Pt(4)

    # =========================================================================
    # SLIDE 10: 7. RESULTS OF CLASSIFICATION USING PROPOSED MODEL
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "7. Results of Classification: Proposed AST-CLAM Performance", "Evaluation & Metric Verification")

    # 4 Metric Highlights
    metrics_hl = [
        ("Accuracy", "94.88%", "+5.35% higher than best baseline", GREEN),
        ("Precision", "85.26%", "Low false alarm candidate rate", SRM_BLUE),
        ("Recall", "64.53%", "Captures true source cells reliably", SRM_BLUE),
        ("F1-Score", "0.7346", "+0.2457 higher than Random Forest", GREEN),
        ("AUC-ROC", "0.9870", "Near-perfect ranking capability", SRM_BLUE),
        ("Centroid RMSE", "6.86 km", "Sub-10km operational requirement met", GREEN)
    ]

    for i, (m_title, m_val, m_sub, col) in enumerate(metrics_hl):
        row_i = i // 3
        col_i = i % 3
        x = Inches(0.8 + col_i * 3.95)
        y = Inches(1.6 + row_i * 2.6)
        
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.8), Inches(2.3))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG
        card.line.color.rgb = CARD_BORDER
        tf = card.text_frame
        tf.word_wrap = True
        
        p_t = tf.paragraphs[0]
        p_t.text = m_title.upper()
        p_t.font.name = "Arial"
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = SRM_BLUE
        
        p_v = tf.add_paragraph()
        p_v.text = m_val
        p_v.font.name = "Arial"
        p_v.font.size = Pt(32)
        p_v.font.bold = True
        p_v.font.color.rgb = col
        p_v.space_before = Pt(4)
        
        p_s = tf.add_paragraph()
        p_s.text = m_sub
        p_s.font.name = "Arial"
        p_s.font.size = Pt(10)
        p_s.font.color.rgb = DARK_GRAY
        p_s.space_before = Pt(4)

    # =========================================================================
    # SLIDE 11: 8. COMPARISON WITH EXISTING CLASSIFIER MODELS (TABLE)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "8. Benchmark Comparison with 5 Existing Classifier Models", "Comparative Analysis")

    # Benchmarking Table
    bench_rows = [
        ["Random Forest", "Ensemble Bagging", "89.53%", "52.68%", "45.61%", "0.4889", "0.8969", "29.84 km", "25.79 km"],
        ["XGBoost", "Gradient Boosted Trees", "89.26%", "52.54%", "21.80%", "0.3081", "0.8532", "33.69 km", "33.13 km"],
        ["Deep MLP", "Feedforward DNN", "88.65%", "47.29%", "29.54%", "0.3637", "0.8145", "35.21 km", "58.69 km"],
        ["Standard ConvLSTM", "Spatio-Temporal Net", "89.06%", "50.62%", "12.07%", "0.1949", "0.7841", "30.79 km", "50.97 km"],
        ["Attention U-Net", "Chen & Wang (2022)", "88.64%", "43.90%", "12.52%", "0.1948", "0.7828", "29.86 km", "37.48 km"],
        ["Proposed AST-CLAM", "Novel Adaptive Attention", "94.88%", "85.26%", "64.53%", "0.7346", "0.9870", "6.86 km", "4.62 km"]
    ]

    t_shape = s11.shapes.add_table(7, 9, Inches(0.8), Inches(1.6), Inches(11.73), Inches(4.5))
    t = t_shape.table
    widths = [Inches(1.8), Inches(1.5), Inches(1.1), Inches(1.1), Inches(1.1), Inches(1.1), Inches(1.1), Inches(1.4), Inches(1.5)]
    for idx, w in enumerate(widths):
        t.columns[idx].width = w

    t_headers = ["Model", "Category", "Accuracy", "Precision", "Recall", "F1-Score", "AUC-ROC", "Centroid RMSE", "Sanchi Wreck Err"]
    for c_idx, th in enumerate(t_headers):
        c = t.cell(0, c_idx)
        c.text = th
        c.fill.solid()
        c.fill.fore_color.rgb = SRM_BLUE
        for p in c.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for r_idx, row in enumerate(bench_rows):
        is_novel = (r_idx == 5)
        for c_idx, val in enumerate(row):
            c = t.cell(r_idx + 1, c_idx)
            c.text = val
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor(235, 245, 235) if is_novel else (LIGHT_BG if r_idx % 2 == 0 else WHITE)
            for p in c.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9.5)
                p.font.bold = is_novel
                p.font.color.rgb = GREEN if is_novel and c_idx >= 2 else DARK_GRAY

    # Footer callout
    fcall = s11.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.73), Inches(0.6))
    p_fc = fcall.text_frame.paragraphs[0]
    p_fc.text = "★ Benchmark Conclusion: Proposed AST-CLAM decisively outperforms all 5 baseline models across every quantitative metric and reduces Sanchi wreck localization error from 29.10 km (naive) to 4.62 km (84.1% distance reduction)."
    p_fc.font.name = "Arial"
    p_fc.font.size = Pt(10)
    p_fc.font.bold = True
    p_fc.font.color.rgb = GREEN

    # =========================================================================
    # SLIDE 12: 8. COMPARISON WITH EXISTING CLASSIFIER MODELS (GRAPHS)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "8. Benchmark Comparison: Visual Evaluation Dashboard", "Comparative Analysis")

    comp_plot = os.path.join(RESULTS_DIR, "model_comparison_charts.png")
    if os.path.exists(comp_plot):
        s12.shapes.add_picture(comp_plot, Inches(0.8), Inches(1.5), width=Inches(8.5))

    # Sidebar notes
    sb12 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.5), Inches(1.5), Inches(3.0), Inches(5.4))
    sb12.fill.solid()
    sb12.fill.fore_color.rgb = LIGHT_BG
    sb12.line.color.rgb = CARD_BORDER
    tf_sb12 = sb12.text_frame
    tf_sb12.word_wrap = True
    
    p_h12 = tf_sb12.paragraphs[0]
    p_h12.text = "Visual Findings:"
    p_h12.font.name = "Arial"
    p_h12.font.size = Pt(12)
    p_h12.font.bold = True
    p_h12.font.color.rgb = SRM_BLUE
    
    c_notes = [
        "Panel (A) ROC Curves: AST-CLAM curve dominates the top-left quadrant (AUC = 0.9870).",
        "Panel (B) PR Curves: Sustained high precision across recall levels (Average Precision = 0.812).",
        "Panel (C) Grouped Bar Chart: AST-CLAM leads across Accuracy, Precision, Recall, and F1.",
        "Panel (D) Centroid Trajectory RMSE: AST-CLAM achieves 6.86 km (red bar), well below the 10km target threshold."
    ]
    for cn in c_notes:
        pcn = tf_sb12.add_paragraph()
        pcn.text = cn
        pcn.font.name = "Arial"
        pcn.font.size = Pt(9.5)
        pcn.font.color.rgb = DARK_GRAY
        pcn.space_before = Pt(8)

    # =========================================================================
    # SLIDE 13: 9. PLAN OF ACTION / MEMBER TASKS
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "9. Plan of Action & Team Member Task Progress", "Project Management")

    tasks_table = [
        ["Sachin P (RA2411031010117)", "Data Engineering", "Big Data ingestion (60.5M rows), Parquet partitioning, missing parameter physical imputation, adaptive thresholding", "Completed (Review 2)", GREEN],
        ["Shivaani M (RA2411031010119)", "Comparative Model Analysis", "Benchmark evaluation of RF, XGBoost, Deep MLP, Standard ConvLSTM, Attention U-Net against AST-CLAM", "Completed (Review 2)", GREEN],
        ["Jayalakshmi T (RA2411031010115)", "Proposed Model Development", "Novel AST-CLAM architecture design, AEU-Attention module, Dual-Task Focal + Huber distance loss optimization", "Completed (Review 2)", GREEN],
        ["Varsha U (RA2411031010120)", "Visualization & Dashboard", "Interactive Power BI spatial trajectory dashboard, hydrodynamic wind/current overlay, web UI deployment", "In Progress (PBL 3 Final)", GOLD]
    ]

    t_s13 = s13.shapes.add_table(5, 5, Inches(0.8), Inches(1.6), Inches(11.73), Inches(4.5))
    tbl13 = t_s13.table
    w13 = [Inches(2.5), Inches(2.0), Inches(4.73), Inches(1.5), Inches(1.0)]
    tbl13.columns[0].width = Inches(2.5)
    tbl13.columns[1].width = Inches(1.8)
    tbl13.columns[2].width = Inches(5.0)
    tbl13.columns[3].width = Inches(2.43)

    h13 = ["Member Name & Reg No", "Responsibility Domain", "Key Technical Contributions Executed", "Status"]
    for c_idx, th in enumerate(h13):
        c = tbl13.cell(0, c_idx)
        c.text = th
        c.fill.solid()
        c.fill.fore_color.rgb = SRM_BLUE
        for p in c.text_frame.paragraphs:
            p.font.name = "Arial"
            p.font.size = Pt(10.5)
            p.font.bold = True
            p.font.color.rgb = WHITE

    for r_idx, row in enumerate(tasks_table):
        for c_idx in range(4):
            c = tbl13.cell(r_idx + 1, c_idx)
            c.text = row[c_idx]
            c.fill.solid()
            c.fill.fore_color.rgb = LIGHT_BG if r_idx % 2 == 0 else WHITE
            for p in c.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(9.5)
                p.font.color.rgb = row[4] if c_idx == 3 else DARK_GRAY
                p.font.bold = (c_idx in [0, 3])

    # Note on PBL 3
    pbl_note = s13.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.73), Inches(0.6))
    p_pbl = pbl_note.text_frame.paragraphs[0]
    p_pbl.text = "ℹ Evaluator Directive: Review 2 focuses on Big Data preprocessing, novel deep learning architecture, and 5-model comparative benchmarking. Interactive visualization dashboard will be presented in PBL Review 3."
    p_pbl.font.name = "Arial"
    p_pbl.font.size = Pt(9.5)
    p_pbl.font.color.rgb = SRM_BLUE

    # =========================================================================
    # SLIDE 14: 10. REFERENCES
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "10. Key References (Literature Benchmark)", "References")

    refs = [
        "[1] S. El Mohtar et al., 'Bayesian identification of oil spill source parameters from image contours,' Marine Pollution Bulletin, vol. 169, Art. no. 112514, 2021.",
        "[2] M. A. E. R. Hammoud et al., 'Moving source identification in an uncertain marine flow: Mediterranean Sea application,' Ocean Engineering, vol. 220, Art. no. 108435, 2021.",
        "[3] Y. Li et al., 'Oil spill detection with multiscale conditional adversarial networks with small-data training,' Remote Sensing, vol. 13, no. 12, Art. no. 2378, 2021.",
        "[4] Y. Chen and Z. Wang, 'Marine oil spill detection from SAR images based on Attention U-Net model using polarimetric and wind speed information,' IJERPH, vol. 19, no. 19, Art. no. 12315, 2022.",
        "[5] Y. Li et al., 'An adversarial learning approach to forecasted wind field correction with an application to oil spill drift prediction,' IJAEOG, vol. 112, Art. no. 102924, 2022.",
        "[6] A. S. Dhavalikar and P. C. Choudhari, 'Prediction of oil spill trajectory on the ocean surface using mathematical modeling,' IEEE JSTARS, vol. 15, 2022.",
        "[7] L. F. Tessarolo et al., 'A surface Lagrangian algorithm applied to the 2019 South Atlantic oil spill,' Ocean Engineering, vol. 268, Art. no. 113505, 2023.",
        "[8] F. Chen et al., 'DGNet: Distribution guided efficient learning for oil spill image segmentation,' IEEE TGRS, vol. 61, 2023.",
        "[9] C. Li et al., 'A self-evolving deep learning algorithm for automatic oil spill detection in Sentinel-1 SAR images,' Remote Sensing of Environment, vol. 299, Art. no. 113872, 2023.",
        "[10] P. Cervantes-Hernández et al., 'Combined use of SAR images and numerical simulations to identify source and trajectories of oil spills,' MPB, vol. 199, Art. no. 115981, 2024.",
        "[11] S. El Mohtar et al., 'Iterative data-driven construction of surrogates for efficient Bayesian identification of oil spill source parameters,' Computational Geosciences, 2024.",
        "[12] T. V. La et al., 'Monitoring of spatio-temporal variations of oil slicks via the collocation of multi-source satellite images,' Remote Sensing, vol. 16, no. 16, Art. no. 3110, 2024."
    ]

    r_box = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.73), Inches(5.3))
    r_box.fill.solid()
    r_box.fill.fore_color.rgb = LIGHT_BG
    r_box.line.color.rgb = CARD_BORDER
    tf_r = r_box.text_frame
    tf_r.word_wrap = True

    for i, ref in enumerate(refs):
        pr = tf_r.paragraphs[0] if i == 0 else tf_r.add_paragraph()
        pr.text = ref
        pr.font.name = "Arial"
        pr.font.size = Pt(9)
        pr.font.color.rgb = DARK_GRAY
        pr.space_before = Pt(3)

    # =========================================================================
    # SLIDE 15: 11. ATTACH GEOTAGGED PHOTO
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "11. Geotagged Photo Verification", "Evaluation Evidence")

    # Placeholder Box for Geotagged Photo
    ph_box = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(1.8), Inches(8.93), Inches(4.5))
    ph_box.fill.solid()
    ph_box.fill.fore_color.rgb = LIGHT_BG
    ph_box.line.color.rgb = SRM_ACCENT
    ph_box.line.width = Pt(2)
    tf_ph = ph_box.text_frame
    tf_ph.word_wrap = True
    
    p_ph1 = tf_ph.paragraphs[0]
    p_ph1.text = "📷 [Attach Geotagged Photo Taken During Review 2 Presentation]"
    p_ph1.font.name = "Arial"
    p_ph1.font.size = Pt(16)
    p_ph1.font.bold = True
    p_ph1.font.color.rgb = SRM_BLUE
    p_ph1.alignment = PP_ALIGN.CENTER
    
    p_ph2 = tf_ph.add_paragraph()
    p_ph2.text = "\n\nInstructions for Team:\n1. Capture presentation photo in classroom / lab using GPS/Geotag camera app.\n2. Ensure Latitude, Longitude, Date, and Timestamp are stamped on photo.\n3. Replace this placeholder container with your actual captured photo."
    p_ph2.font.name = "Arial"
    p_ph2.font.size = Pt(12)
    p_ph2.font.color.rgb = DARK_GRAY
    p_ph2.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 16: 12. ATTACH GOOGLE COLAB IMPLEMENTATION LINK
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "12. Code Implementation & Execution Links", "Source Code Deliverables")

    link_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.8), Inches(10.33), Inches(4.8))
    link_box.fill.solid()
    link_box.fill.fore_color.rgb = LIGHT_BG
    link_box.line.color.rgb = SRM_BLUE
    tf_lk = link_box.text_frame
    tf_lk.word_wrap = True

    p_lk_h = tf_lk.paragraphs[0]
    p_lk_h.text = "🔗 Google Colab & Repository Implementation Links"
    p_lk_h.font.name = "Arial"
    p_lk_h.font.size = Pt(16)
    p_lk_h.font.bold = True
    p_lk_h.font.color.rgb = SRM_BLUE
    p_lk_h.alignment = PP_ALIGN.CENTER

    links_info = [
        "\n• Google Colab Pipeline Link: [Insert Google Colab Shared Link Here]",
        "• Local Workspace Repository: C:\\Users\\Jayalakshmi\\oil_spill\\",
        "• Data Preprocessing Pipeline: data_preprocessing.py",
        "• Novel Deep Learning Architecture: model_architecture.py",
        "• Benchmark Evaluation Engine: train_and_benchmark.py",
        "• Generated Evaluation Deliverables: results\\ (Metrics CSV, PNG charts, Markdown reports)"
    ]
    for li in links_info:
        pli = tf_lk.add_paragraph()
        pli.text = li
        pli.font.name = "Arial"
        pli.font.size = Pt(12)
        pli.font.color.rgb = DARK_GRAY
        pli.space_before = Pt(8)

    # =========================================================================
    # SLIDE 17: THANK YOU SLIDE
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    if has_logo:
        s17.shapes.add_picture(logo_path, Inches(5.4), Inches(1.5), width=Inches(2.5))
        
    ty_box = s17.shapes.add_textbox(Inches(2.0), Inches(2.8), Inches(9.33), Inches(2.5))
    tf_ty = ty_box.text_frame
    tf_ty.word_wrap = True
    
    p_ty = tf_ty.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.font.name = "Arial"
    p_ty.font.size = Pt(36)
    p_ty.font.bold = True
    p_ty.font.color.rgb = SRM_BLUE
    p_ty.alignment = PP_ALIGN.CENTER
    
    p_qa = tf_ty.add_paragraph()
    p_qa.text = "Questions & Feedback"
    p_qa.font.name = "Arial"
    p_qa.font.size = Pt(18)
    p_qa.font.bold = True
    p_qa.font.color.rgb = GOLD
    p_qa.alignment = PP_ALIGN.CENTER
    p_qa.space_before = Pt(10)

    # Save presentation
    prs.save(OUTPUT_PPTX)
    print(f"[SUCCESS] Presentation generated cleanly at: {OUTPUT_PPTX}")


if __name__ == "__main__":
    create_presentation()
