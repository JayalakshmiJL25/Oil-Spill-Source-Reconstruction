"""
Elite AI Publication-Grade System Architecture & Pipeline Diagram Generator
Project: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations
Theme: Visual, Modular Deep Learning Architecture for Review 2 (Slide 5)
Outputs:
  - results/system_architecture_diagram.png
  - results/architecture_pipeline_slide5.png
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Rectangle, Wedge, PathPatch
from matplotlib.path import Path

def draw_quiver(ax, x, y, w, h, col):
    """Draws a mini vector wind/current field."""
    xs = np.linspace(x + 0.15*w, x + 0.85*w, 4)
    ys = np.linspace(y + 0.15*h, y + 0.85*h, 3)
    for px in xs:
        for py in ys:
            angle = np.deg2rad(25 + 15 * np.sin(px + py))
            dx = 0.15 * w * np.cos(angle)
            dy = 0.15 * h * np.sin(angle)
            arr = FancyArrowPatch((px, py), (px + dx, py + dy),
                                  arrowstyle='->', mutation_scale=8,
                                  color=col, linewidth=1.2, zorder=5)
            ax.add_patch(arr)

def draw_sar_slick(ax, cx, cy, rx, ry, col):
    """Draws a multi-contour oil slick polygon."""
    angles = np.linspace(0, 2*np.pi, 24, endpoint=False)
    # Outer contour
    radii = rx * (1.0 + 0.28 * np.sin(3*angles) - 0.18 * np.cos(5*angles))
    poly_pts = [[cx + r * np.cos(a), cy + r * np.sin(a) * (ry/rx)] for a, r in zip(angles, radii)]
    poly = Polygon(poly_pts, closed=True, facecolor='#1E293B', edgecolor=col, linewidth=1.5, zorder=5)
    ax.add_patch(poly)
    # Inner dense core
    radii_in = 0.5 * rx * (1.0 + 0.2 * np.cos(2*angles))
    poly_pts_in = [[cx + r * np.cos(a), cy + r * np.sin(a) * (ry/rx)] for a, r in zip(angles, radii_in)]
    poly_in = Polygon(poly_pts_in, closed=True, facecolor='#0F172A', edgecolor='#EF4444', linewidth=1.0, zorder=6)
    ax.add_patch(poly_in)

def draw_network_layers(ax, x, y, w, h):
    """Draws a mini neural Conv1D / LSTM block."""
    # Feature maps
    colors = ['#38BDF8', '#818CF8', '#C084FC']
    for i, c in enumerate(colors):
        rect = FancyBboxPatch((x + i*0.14, y + i*0.08), w*0.7, h*0.7,
                              boxstyle="round,pad=0.02,rounding_size=0.04",
                              facecolor=c, edgecolor='#FFFFFF', linewidth=1.0, alpha=0.9, zorder=5+i)
        ax.add_patch(rect)

def draw_attention_grid(ax, x, y, size):
    """Draws an attention heatmap matrix."""
    n = 4
    dx = size / n
    np.random.seed(42)
    weights = np.array([
        [0.85, 0.12, 0.02, 0.01],
        [0.10, 0.78, 0.08, 0.04],
        [0.05, 0.15, 0.65, 0.15],
        [0.02, 0.05, 0.20, 0.73]
    ])
    for r in range(n):
        for c in range(n):
            val = weights[r, c]
            col = plt.cm.plasma(val)
            rect = Rectangle((x + c*dx, y + (n - 1 - r)*dx), dx*0.9, dx*0.9,
                             facecolor=col, edgecolor='#FFFFFF', linewidth=0.5, zorder=6)
            ax.add_patch(rect)

def build_elite_diagram(output_path):
    fig = plt.figure(figsize=(24, 11.8), dpi=300, facecolor='#F8FAFC')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 11.8)
    ax.axis('off')

    FONT = 'Arial'

    # =========================================================================
    # TOP MASTHEAD BANNER
    # =========================================================================
    mast = FancyBboxPatch((0.5, 10.45), 23.0, 1.05,
                          boxstyle="round,pad=0.06,rounding_size=0.15",
                          facecolor='#002B49', edgecolor='#001726', linewidth=1.8, zorder=2)
    ax.add_patch(mast)

    ax.text(0.85, 11.14, "OVERALL SYSTEM ARCHITECTURE & DATA PIPELINE",
            fontfamily=FONT, fontsize=20, fontweight='bold', color='#FFFFFF', va='center', zorder=3)
    ax.text(0.85, 10.74, "Adaptive Oil Spill Source Reconstruction via Multi-Temporal Remote Sensing & AST-CLAM Neural Core",
            fontfamily=FONT, fontsize=11.5, fontweight='normal', color='#93C5FD', va='center', zorder=3)

    # Badges
    badges = [
        ("SRM BATCH 10", "#1D4ED8"),
        ("21CSC314P BIG DATA ESSENTIALS", "#047857"),
        ("END-TO-END PIPELINE", "#B45309")
    ]
    bx = 23.1
    for b_text, b_color in reversed(badges):
        bw = len(b_text) * 0.105 + 0.38
        bx -= bw
        bp = FancyBboxPatch((bx, 10.74), bw - 0.12, 0.45,
                            boxstyle="round,pad=0.04,rounding_size=0.08",
                            facecolor=b_color, edgecolor='none', zorder=3)
        ax.add_patch(bp)
        ax.text(bx + (bw - 0.12)/2, 10.96, b_text,
                fontfamily=FONT, fontsize=8.5, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=4)
        bx -= 0.1

    # =========================================================================
    # 5 STAGES COLUMN DEFINITIONS
    # =========================================================================
    # Stage X ranges:
    # Col 1: 0.50 -> 4.70 (w=4.20)
    # Col 2: 5.25 -> 9.45 (w=4.20)
    # Col 3: 10.00 -> 14.20 (w=4.20)
    # Col 4: 14.75 -> 19.15 (w=4.40)
    # Col 5: 19.70 -> 23.50 (w=3.80)

    col_configs = [
        {"x": 0.50, "w": 4.25, "theme": "#1E3A8A", "light": "#EFF6FF", "border": "#3B82F6", "badge": "#2563EB",
         "num": "STAGE 1", "title": "MULTI-SOURCE INGESTION", "sub": "Satellite & Metocean Observation Layer"},
        
        {"x": 5.30, "w": 4.25, "theme": "#065F46", "light": "#F0FDF4", "border": "#10B981", "badge": "#059669",
         "num": "STAGE 2", "title": "BIG DATA PREPROCESSING", "sub": "Distributed PyArrow Cleansing Pipeline"},
        
        {"x": 10.10, "w": 4.25, "theme": "#9A3412", "light": "#FFF7ED", "border": "#F97316", "badge": "#EA580C",
         "num": "STAGE 3", "title": "TRI-BRANCH EMBEDDING", "sub": "Decoupled Physics Feature Latent Space"},
        
        {"x": 14.90, "w": 4.35, "theme": "#581C87", "light": "#FAF5FF", "border": "#8B5CF6", "badge": "#7C3AED",
         "num": "STAGE 4", "title": "NOVEL AST-CLAM CORE", "sub": "Adaptive Spatio-Temporal Neural Backbone"},
        
        {"x": 19.80, "w": 3.70, "theme": "#166534", "light": "#F0FDF4", "border": "#22C55E", "badge": "#15803D",
         "num": "STAGE 5", "title": "DECISION SUPPORT & HIT", "sub": "Origin Localization & Real Wreck Hit"}
    ]

    for cfg in col_configs:
        cx = cfg["x"]
        cw = cfg["w"]
        # Outer box
        out_box = FancyBboxPatch((cx, 0.20), cw, 9.95,
                                 boxstyle="round,pad=0.06,rounding_size=0.18",
                                 facecolor=cfg["light"], edgecolor=cfg["border"], linewidth=1.6, zorder=1)
        ax.add_patch(out_box)

        # Header pill
        hp = FancyBboxPatch((cx + 0.12, 9.45), cw - 0.24, 0.60,
                            boxstyle="round,pad=0.04,rounding_size=0.10",
                            facecolor=cfg["theme"], edgecolor='none', zorder=2)
        ax.add_patch(hp)

        ax.text(cx + cw/2, 9.85, f"{cfg['num']}: {cfg['title']}",
                fontfamily=FONT, fontsize=10.2, fontweight='bold', color='#FFFFFF', ha='center', va='center', zorder=3)
        ax.text(cx + cw/2, 9.60, cfg['sub'],
                fontfamily=FONT, fontsize=8.0, fontweight='normal',
                color='#FEF08A' if '3' in cfg['num'] else '#D1FAE5' if '2' in cfg['num'] or '5' in cfg['num'] else '#DBEAFE',
                ha='center', va='center', zorder=3)

    # =========================================================================
    # STAGE 1 CONTENT (INGESTION CARDS WITH VISUAL GRAPHICS)
    # =========================================================================
    # Card 1.1: Sentinel-1 SAR
    c1_1 = FancyBboxPatch((0.65, 7.25), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=1.1, zorder=2)
    ax.add_patch(c1_1)
    ax.text(0.80, 9.15, "SATELLITE REMOTE SENSING", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#2563EB', zorder=3)
    ax.text(0.80, 8.85, "Sentinel-1 SAR Slick Contours", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(0.80, 8.55, "• C-Band SAR multi-temporal slicks", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 8.32, "• 20,951 spatial candidate grid cells", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 8.09, "• Observed polygon diffusion axes", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Visual SAR Slick icon
    draw_sar_slick(ax, 3.95, 8.45, 0.42, 0.28, '#38BDF8')
    # Bottom pill
    bp1_1 = FancyBboxPatch((0.80, 7.37), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#EFF6FF', edgecolor='#BFDBFE', linewidth=0.8, zorder=3)
    ax.add_patch(bp1_1)
    ax.text(2.62, 7.50, "Dual-Polarization C-Band SAR Slicks", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#1E3A8A', ha='center', va='center', zorder=4)

    # Card 1.2: ERA5 Wind
    c1_2 = FancyBboxPatch((0.65, 4.95), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=1.1, zorder=2)
    ax.add_patch(c1_2)
    ax.text(0.80, 6.85, "ATMOSPHERIC REANALYSIS", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#2563EB', zorder=3)
    ax.text(0.80, 6.55, "ECMWF ERA5 Wind Fields", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(0.80, 6.25, "• Hourly 10m wind vectors (u10, v10)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 6.02, "• 0.25° x 0.25° spatial grid resolution", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 5.79, "• Dynamic gust variance & windage", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Visual Wind Quiver
    draw_quiver(ax, 3.55, 5.80, 0.85, 0.70, '#0284C7')
    # Bottom pill
    bp1_2 = FancyBboxPatch((0.80, 5.07), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#EFF6FF', edgecolor='#BFDBFE', linewidth=0.8, zorder=3)
    ax.add_patch(bp1_2)
    ax.text(2.62, 5.20, "Hourly Boundary Layer Wind Fields", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#1E3A8A', ha='center', va='center', zorder=4)

    # Card 1.3: CMEMS Currents
    c1_3 = FancyBboxPatch((0.65, 2.65), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=1.1, zorder=2)
    ax.add_patch(c1_3)
    ax.text(0.80, 4.55, "OCEAN HYDRODYNAMICS", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#2563EB', zorder=3)
    ax.text(0.80, 4.25, "CMEMS Ocean Current Fields", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(0.80, 3.95, "• Hourly surface velocities (u, v)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 3.72, "• 0.083° Copernicus hydrodynamic mesh", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 3.49, "• Wave Stokes drift & 3% windage", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Streamline graphic
    draw_quiver(ax, 3.55, 3.50, 0.85, 0.70, '#0D9488')
    # Bottom pill
    bp1_3 = FancyBboxPatch((0.80, 2.77), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#EFF6FF', edgecolor='#BFDBFE', linewidth=0.8, zorder=3)
    ax.add_patch(bp1_3)
    ax.text(2.62, 2.90, "Copernicus Physical Ocean Reanalysis", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#1E3A8A', ha='center', va='center', zorder=4)

    # Card 1.4: Sanchi Tanker Ground Truth
    c1_4 = FancyBboxPatch((0.65, 0.35), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=1.1, zorder=2)
    ax.add_patch(c1_4)
    ax.text(0.80, 2.25, "GROUND TRUTH DISASTER BENCHMARK", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#2563EB', zorder=3)
    ax.text(0.80, 1.95, "Sanchi Tanker AIS Track", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(0.80, 1.65, "• Audited AIS drift before sinking", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 1.42, "• Sinking point: 28.375°N, 125.942°E", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(0.80, 1.19, "• 115m sea-depth wreck anchor", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Anchor marker
    ax.plot([3.95], [1.50], marker='*', markersize=14, color='#EF4444', zorder=6)
    ax.text(3.95, 1.25, "115m Wreck", fontfamily=FONT, fontsize=6.8, fontweight='bold', color='#DC2626', ha='center', zorder=6)
    # Bottom pill
    bp1_4 = FancyBboxPatch((0.80, 0.47), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#EFF6FF', edgecolor='#BFDBFE', linewidth=0.8, zorder=3)
    ax.add_patch(bp1_4)
    ax.text(2.62, 0.60, "Sanchi Real Disaster Ground Truth", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#1E3A8A', ha='center', va='center', zorder=4)

    # =========================================================================
    # STAGE 2 CONTENT (BIG DATA PREPROCESSING CARDS)
    # =========================================================================
    # Card 2.1: Apache PyArrow
    c2_1 = FancyBboxPatch((5.45, 7.25), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c2_1)
    ax.text(5.60, 9.15, "DISTRIBUTED I/O ENGINE", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#059669', zorder=3)
    ax.text(5.60, 8.85, "Apache PyArrow Partitioning", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(5.60, 8.55, "• Multi-partition Hive Parquet tables", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 8.32, "• 60.5M records read across 5 folds", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 8.09, "• Zero spill-to-spill data leakage", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Graphic: Parquet cylinder stack
    for pi in range(3):
        pc = FancyBboxPatch((8.60, 8.10 + pi*0.22), 0.65, 0.16, boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#10B981', edgecolor='#047857', linewidth=0.8, zorder=5)
        ax.add_patch(pc)
    bp2_1 = FancyBboxPatch((5.60, 7.37), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp2_1)
    ax.text(7.42, 7.50, "Scalable PyArrow Distributed Tables", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # Card 2.2: Schema & Singularity Cleanse
    c2_2 = FancyBboxPatch((5.45, 4.95), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c2_2)
    ax.text(5.60, 6.85, "SCHEMA & SINGULARITY CLEANSE", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#059669', zorder=3)
    ax.text(5.60, 6.55, "Range & Outlier Normalization", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(5.60, 6.25, "• Synchronized UTC observation time", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 6.02, "• Bound f_drift_ratio within [0.0, 10.0]", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 5.79, "• Suppresses division-by-zero singularities", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp2_2 = FancyBboxPatch((5.60, 5.07), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp2_2)
    ax.text(7.42, 5.20, "Singularity-Free Range Clipping", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # Card 2.3: Physics-Informed Null Imputation
    c2_3 = FancyBboxPatch((5.45, 2.65), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c2_3)
    ax.text(5.60, 4.55, "DOMAIN PHYSICS IMPUTATION", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#059669', zorder=3)
    ax.text(5.60, 4.25, "Physical Grid Null Imputation", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(5.60, 3.95, "• f_rank_in_hour -> 999.0 (0 particles)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 3.72, "• k=1 single-snapshot drift error -> 0.0", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 3.49, "• Preserves real ocean advection dynamics", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp2_3 = FancyBboxPatch((5.60, 2.77), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp2_3)
    ax.text(7.42, 2.90, "Physics-Informed Parameter Imputation", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # Card 2.4: Adaptive Energy Thresholding
    c2_4 = FancyBboxPatch((5.45, 0.35), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c2_4)
    ax.text(5.60, 2.25, "SPATIAL CANDIDATE FILTER", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#059669', zorder=3)
    ax.text(5.60, 1.95, "Adaptive Energy Thresholding", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(5.60, 1.65, "• 80th-percentile energy contour masking", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 1.42, "• Eliminates 82.3% non-source sea cells", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(5.60, 1.19, "• Focuses gradient backward propagation", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp2_4 = FancyBboxPatch((5.60, 0.47), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp2_4)
    ax.text(7.42, 0.60, "80th-Percentile Candidate Spatial Mask", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # =========================================================================
    # STAGE 3 CONTENT (TRI-BRANCH DECOUPLING CARDS)
    # =========================================================================
    # Card 3.1: Branch 1 - Spatial Geometry (14-D)
    c3_1 = FancyBboxPatch((10.25, 7.25), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#F97316', linewidth=1.1, zorder=2)
    ax.add_patch(c3_1)
    ax.text(10.40, 9.15, "BRANCH 1: SPATIAL GEOMETRY (14-D)", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#EA580C', zorder=3)
    ax.text(10.40, 8.85, "Spatial Geometry Sub-Space", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(10.40, 8.55, "• Distance to slick polygon centroid (km)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 8.32, "• Particle cloud spread & dispersion radius", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 8.09, "• Polygon major/minor axes & bearing", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp3_1 = FancyBboxPatch((10.40, 7.37), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FFF7ED', edgecolor='#FED7AA', linewidth=0.8, zorder=3)
    ax.add_patch(bp3_1)
    ax.text(12.22, 7.50, "14 Geometric Feature Dimensions", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#9A3412', ha='center', va='center', zorder=4)

    # Card 3.2: Branch 2 - Dynamic Forcing (10-D)
    c3_2 = FancyBboxPatch((10.25, 4.95), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#F97316', linewidth=1.1, zorder=2)
    ax.add_patch(c3_2)
    ax.text(10.40, 6.85, "BRANCH 2: HYDRODYNAMICS (10-D)", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#EA580C', zorder=3)
    ax.text(10.40, 6.55, "Dynamic Forcing Sub-Space", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(10.40, 6.25, "• Wind velocity magnitude W_mag (m/s)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 6.02, "• CMEMS ocean current speed C_mag", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 5.79, "• Combined 3% windage advection vectors", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp3_2 = FancyBboxPatch((10.40, 5.07), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FFF7ED', edgecolor='#FED7AA', linewidth=0.8, zorder=3)
    ax.add_patch(bp3_2)
    ax.text(12.22, 5.20, "10 Hydrodynamic Dimensions", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#9A3412', ha='center', va='center', zorder=4)

    # Card 3.3: Branch 3 - Drift Mismatch (5-D)
    c3_3 = FancyBboxPatch((10.25, 2.65), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#F97316', linewidth=1.1, zorder=2)
    ax.add_patch(c3_3)
    ax.text(10.40, 4.55, "BRANCH 3: DRIFT RESIDUALS (5-D)", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#EA580C', zorder=3)
    ax.text(10.40, 4.25, "Advective Divergence Sub-Space", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(10.40, 3.95, "• East/North drift mismatch (f_drift_err)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 3.72, "• Advective velocity divergence delta-u, delta-v", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 3.49, "• Lagrangian particle drift ratio", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp3_3 = FancyBboxPatch((10.40, 2.77), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FFF7ED', edgecolor='#FED7AA', linewidth=0.8, zorder=3)
    ax.add_patch(bp3_3)
    ax.text(12.22, 2.90, "5 Residual Mismatch Dimensions", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#9A3412', ha='center', va='center', zorder=4)

    # Card 3.4: Unified Tensor Projection
    c3_4 = FancyBboxPatch((10.25, 0.35), 3.95, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#F97316', linewidth=1.1, zorder=2)
    ax.add_patch(c3_4)
    ax.text(10.40, 2.25, "LATENT TENSOR CONCATENATION", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#EA580C', zorder=3)
    ax.text(10.40, 1.95, "Fused 29-D Feature Tensor", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(10.40, 1.65, "• Standardized multi-modal projection", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 1.42, "• Tensor representation: X in R^{B x T x 29}", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(10.40, 1.19, "• Retrograde time window: t=0 -> -120h", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp3_4 = FancyBboxPatch((10.40, 0.47), 3.65, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FFF7ED', edgecolor='#FED7AA', linewidth=0.8, zorder=3)
    ax.add_patch(bp3_4)
    ax.text(12.22, 0.60, "Unified 29-D Latent Representation", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#9A3412', ha='center', va='center', zorder=4)

    # =========================================================================
    # STAGE 4 CONTENT (NOVEL AST-CLAM CORE CARDS)
    # =========================================================================
    # Card 4.1: Spatio-Temporal Conv1D
    c4_1 = FancyBboxPatch((15.05, 7.25), 4.05, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#8B5CF6', linewidth=1.1, zorder=2)
    ax.add_patch(c4_1)
    ax.text(15.20, 9.15, "LOCAL RECEPTIVE FIELD", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#7C3AED', zorder=3)
    ax.text(15.20, 8.85, "Spatio-Temporal Conv1D", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(15.20, 8.55, "• Multi-scale 1D spatial convolutions", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 8.32, "• Kernel size = 3, Hidden channels = 64", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 8.09, "• Captures candidate marine neighborhood", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Neural layer graphic
    draw_network_layers(ax, 18.25, 8.10, 0.65, 0.45)
    bp4_1 = FancyBboxPatch((15.20, 7.37), 3.75, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FAF5FF', edgecolor='#DDD6FE', linewidth=0.8, zorder=3)
    ax.add_patch(bp4_1)
    ax.text(17.07, 7.50, "Dilated Multi-Channel Convolutions", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#581C87', ha='center', va='center', zorder=4)

    # Card 4.2: Bidirectional ConvLSTM
    c4_2 = FancyBboxPatch((15.05, 4.95), 4.05, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#8B5CF6', linewidth=1.1, zorder=2)
    ax.add_patch(c4_2)
    ax.text(15.20, 6.85, "RETROGRADE DYNAMICS", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#7C3AED', zorder=3)
    ax.text(15.20, 6.55, "Bidirectional ConvLSTM", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(15.20, 6.25, "• Dual forward/backward temporal recurrence", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 6.02, "• Backward-in-time drift trajectory (0 -> -120h)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 5.79, "• Dual cell state memory gating (64-D)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Recurrence arrows
    arr_f = FancyArrowPatch((18.15, 6.05), (18.85, 6.05), arrowstyle='->', mutation_scale=10, color='#8B5CF6', linewidth=1.5, zorder=5)
    arr_b = FancyArrowPatch((18.85, 5.85), (18.15, 5.85), arrowstyle='->', mutation_scale=10, color='#C084FC', linewidth=1.5, zorder=5)
    ax.add_patch(arr_f)
    ax.add_patch(arr_b)
    bp4_2 = FancyBboxPatch((15.20, 5.07), 3.75, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FAF5FF', edgecolor='#DDD6FE', linewidth=0.8, zorder=3)
    ax.add_patch(bp4_2)
    ax.text(17.07, 5.20, "Bidirectional Trajectory Recurrence", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#581C87', ha='center', va='center', zorder=4)

    # Card 4.3: Adaptive Environmental Uncertainty Attention (AEU-Attn)
    c4_3 = FancyBboxPatch((15.05, 2.65), 4.05, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#8B5CF6', linewidth=1.1, zorder=2)
    ax.add_patch(c4_3)
    ax.text(15.20, 4.55, "NOVEL UNCERTAINTY GATING", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#7C3AED', zorder=3)
    ax.text(15.20, 4.25, "AEU-Attention Mechanism", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(15.20, 3.95, "• Query: Spatial state | Key/Val: Drift error", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 3.72, "• Downweights noisy vectors in turbulent seas", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 3.49, "• Preserves multi-snapshot consensus", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    # Graphic: Attention Heatmap matrix
    draw_attention_grid(ax, 18.25, 3.50, 0.65)
    bp4_3 = FancyBboxPatch((15.20, 2.77), 3.75, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FAF5FF', edgecolor='#DDD6FE', linewidth=0.8, zorder=3)
    ax.add_patch(bp4_3)
    ax.text(17.07, 2.90, "Dynamic Environmental Uncertainty Attention", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#581C87', ha='center', va='center', zorder=4)

    # Card 4.4: Decoupled Latent Heads
    c4_4 = FancyBboxPatch((15.05, 0.35), 4.05, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#8B5CF6', linewidth=1.1, zorder=2)
    ax.add_patch(c4_4)
    ax.text(15.20, 2.25, "MULTI-OBJECTIVE PROJECTION", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#7C3AED', zorder=3)
    ax.text(15.20, 1.95, "Decoupled Latent Heads", fontfamily=FONT, fontsize=9.8, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(15.20, 1.65, "• Classification Head: Source probability P(y)", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 1.42, "• Continuous Regression Head: Origin offset", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    ax.text(15.20, 1.19, "• Preserves physical spatial topology", fontfamily=FONT, fontsize=7.6, color='#334155', zorder=3)
    bp4_4 = FancyBboxPatch((15.20, 0.47), 3.75, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#FAF5FF', edgecolor='#DDD6FE', linewidth=0.8, zorder=3)
    ax.add_patch(bp4_4)
    ax.text(17.07, 0.60, "Dual Classification & Offset Heads", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#581C87', ha='center', va='center', zorder=4)

    # =========================================================================
    # STAGE 5 CONTENT (DECISION SUPPORT & RECONSTRUCTION HIT)
    # =========================================================================
    # Card 5.1: Dual Loss
    c5_1 = FancyBboxPatch((19.95, 7.25), 3.40, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c5_1)
    ax.text(20.10, 9.15, "DUAL LOSS CONVERGENCE", fontfamily=FONT, fontsize=7.0, fontweight='bold', color='#059669', zorder=3)
    ax.text(20.10, 8.85, "Focal + Smooth L1 Huber", fontfamily=FONT, fontsize=9.6, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(20.10, 8.55, "• Focal Loss (alpha=0.75, gamma=2.0)", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 8.32, "• Solves 1:5 background imbalance", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 8.09, "• Euclidean distance regression", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    bp5_1 = FancyBboxPatch((20.10, 7.37), 3.10, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp5_1)
    ax.text(21.65, 7.50, "Dual-Task Convergence", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # Card 5.2: Probability Surface
    c5_2 = FancyBboxPatch((19.95, 4.95), 3.40, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c5_2)
    ax.text(20.10, 6.85, "PROBABILITY SURFACE MAP", fontfamily=FONT, fontsize=7.0, fontweight='bold', color='#059669', zorder=3)
    ax.text(20.10, 6.55, "Calibrated Origin Likelihood", fontfamily=FONT, fontsize=9.6, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(20.10, 6.25, "• Accuracy: 94.88% (Winner)", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 6.02, "• Precision: 85.26% | Recall: 64.53%", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 5.79, "• F1-Score: 0.7346 | ROC: 0.9870", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    bp5_2 = FancyBboxPatch((20.10, 5.07), 3.10, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp5_2)
    ax.text(21.65, 5.20, "High-Confidence Origin Map", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # Card 5.3: Centroid RMSE
    c5_3 = FancyBboxPatch((19.95, 2.65), 3.40, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c5_3)
    ax.text(20.10, 4.55, "CENTROID TRAJECTORY ERROR", fontfamily=FONT, fontsize=7.0, fontweight='bold', color='#059669', zorder=3)
    ax.text(20.10, 4.25, "Sub-10 km RMSE Guarantee", fontfamily=FONT, fontsize=9.6, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(20.10, 3.95, "• AST-CLAM Centroid: 6.86 km", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 3.72, "• Random Forest: 29.84 km RMSE", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 3.49, "• 77.0% lower dispersion error", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    bp5_3 = FancyBboxPatch((20.10, 2.77), 3.10, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp5_3)
    ax.text(21.65, 2.90, "RMSE: 6.86 km (< 10 km target)", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # Card 5.4: Sanchi Hit
    c5_4 = FancyBboxPatch((19.95, 0.35), 3.40, 2.12, boxstyle="round,pad=0.04,rounding_size=0.09",
                          facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.1, zorder=2)
    ax.add_patch(c5_4)
    ax.text(20.10, 2.25, "SANCHI REAL-WORLD HIT", fontfamily=FONT, fontsize=7.0, fontweight='bold', color='#059669', zorder=3)
    ax.text(20.10, 1.95, "Verified 115m Wreck Hit", fontfamily=FONT, fontsize=9.6, fontweight='bold', color='#0F172A', zorder=3)
    ax.text(20.10, 1.65, "• 4.62 km to sunken wreck", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 1.42, "• Naive slick centroid: 29.10 km", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    ax.text(20.10, 1.19, "• 84.1% distance reduction!", fontfamily=FONT, fontsize=7.4, color='#334155', zorder=3)
    # Origin Target Bullseye Graphic
    ax.plot([22.75], [1.50], marker='o', markersize=14, markerfacecolor='none', markeredgecolor='#EF4444', markeredgewidth=1.8, zorder=6)
    ax.plot([22.75], [1.50], marker='o', markersize=7, markerfacecolor='#EF4444', markeredgecolor='#EF4444', zorder=7)
    bp5_4 = FancyBboxPatch((20.10, 0.47), 3.10, 0.26, boxstyle="round,pad=0.02,rounding_size=0.06",
                           facecolor='#F0FDF4', edgecolor='#A7F3D0', linewidth=0.8, zorder=3)
    ax.add_patch(bp5_4)
    ax.text(21.65, 0.60, "Disaster Ground Truth Hit", fontfamily=FONT, fontsize=7.2, fontweight='bold', color='#065F46', ha='center', va='center', zorder=4)

    # =========================================================================
    # PIPELINE INTER-STAGE ROUTING CONNECTORS (VIBRANT GRADIENT ARROWS & BADGES)
    # =========================================================================
    connectors = [
        (4.75, 5.30, "Raw Grids\n& Meshes", "#1E3A8A"),
        (9.55, 10.10, "Cleaned\nPartitions", "#065F46"),
        (14.35, 14.90, "29-D Latent\nTensor X", "#9A3412"),
        (19.25, 19.80, "Calibrated\nPredictions", "#581C87")
    ]

    for x1, x2, label, col in connectors:
        for y_flow in [8.31, 6.01, 3.71, 1.41]:
            arr = FancyArrowPatch((x1 + 0.05, y_flow), (x2 - 0.05, y_flow),
                                  arrowstyle='-|>', mutation_scale=16,
                                  color=col, linewidth=2.4, zorder=5)
            ax.add_patch(arr)

        mx = (x1 + x2) / 2
        lbl_box = FancyBboxPatch((mx - 0.25, 4.40), 0.50, 0.85,
                                 boxstyle="round,pad=0.03,rounding_size=0.08",
                                 facecolor='#FFFFFF', edgecolor=col, linewidth=1.4, zorder=6)
        ax.add_patch(lbl_box)
        ax.text(mx, 4.82, label,
                fontfamily=FONT, fontsize=6.8, fontweight='bold', color=col,
                ha='center', va='center', multialignment='center', zorder=7)

    # Export high resolution
    plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0.04, facecolor='#FFFFFF')
    plt.close()
    print(f"[SUCCESS] Elite System Architecture Diagram generated: {output_path}")

if __name__ == '__main__':
    p1 = os.path.join(r"c:\Users\Jayalakshmi\oil_spill\results", "system_architecture_diagram.png")
    p2 = os.path.join(r"c:\Users\Jayalakshmi\oil_spill\results", "architecture_pipeline_slide5.png")
    build_elite_diagram(p1)
    build_elite_diagram(p2)
