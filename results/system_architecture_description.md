# Overall System Architecture & Data Workflow

**Project Title**: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations and Environmental Uncertainty  
**Review Stage**: Review 2 (Milestone PPT Checklist Requirements)  
**Institution**: SRM Institute of Science and Technology  

---

```mermaid
flowchart TD
    subgraph L1["Layer 1: Big Data Ingestion"]
        A1["Sentinel-1 SAR Satellite Imagery & VIIRS Delineations"] --> P1["Spatial Polygon & Contour Extraction"]
        A2["ERA5 Atmospheric Reanalysis"] --> P2["10m Wind Vectors u10, v10"]
        A3["CMEMS Ocean Currents"] --> P3["Surface Current Vectors u, v"]
        A4["EMSA CleanSeaNet & Sanchi Audited Trajectory"] --> P4["AIS Drift Benchmarks"]
    end

    subgraph L2["Layer 2: Big Data Preprocessing & Segmentation"]
        P1 & P2 & P3 & P4 --> B1["Distributed Parquet Partition Engine (PyArrow/Spark)"]
        B1 --> B2["Systematic Noise Cleaning & Outlier Suppression"]
        B2 --> B3["Physical Parameter Imputation (Unranked 999.0, Drift Ratio 1.0)"]
        B3 --> B4["Adaptive Spatial-Temporal Thresholding (Candidate Segmentation)"]
    end

    subgraph L3["Layer 3: Tri-Branch Feature Engineering"]
        B4 --> F1["Branch 1: Spatial Geometry & Particle Consensus (14 dims)"]
        B4 --> F2["Branch 2: Hydrodynamic Forcing & Windage Vectors (10 dims)"]
        B4 --> F3["Branch 3: Advective Drift Mismatch Residuals (5 dims)"]
    end

    subgraph L4["Layer 4: Novel AST-CLAM Neural Architecture"]
        F1 & F2 & F3 --> N1["Cross-Modality Latent Fusion Layer"]
        N1 --> N2["Spatio-Temporal 1D/2D Convolutional Encoder"]
        N2 --> N3["Bidirectional Temporal LSTM Sequence Backbone"]
        N3 --> N4["Adaptive Environmental Uncertainty Attention (AEU-Attn)"]
        N4 --> H1["Classification Head: Focal Loss P(y_is_source=1)"]
        N4 --> H2["Regression Head: Continuous Centroid Offset Huber Loss"]
    end

    subgraph L5["Layer 5: Decision Support & Benchmark Evaluation"]
        H1 & H2 --> E1["Calibrated Spatial-Temporal Source Probability Map"]
        E1 --> E2["Argmax Centroid Trajectory Localization (RMSE < 10 km)"]
        E2 --> E3["Comparative Benchmarking vs RF, XGBoost, MLP, ConvLSTM, U-Net"]
    end
```

## Detailed Layer-by-Layer Architectural Description

### Layer 1: Multi-Source Big Data Ingestion
The platform ingests heterogeneous environmental and remote sensing assets spanning:
- **Multi-Temporal Synthetic & Real Sanchi Archives**: Over 60.5 million candidate grid rows partitioned across 5 whole-spill folds in Apache Parquet format.
- **ERA5 Reanalysis**: Hourly wind components ($u_{10}, v_{10}$) at 0.25° spatial resolution.
- **CMEMS Global Ocean Physics**: Daily surface currents ($u, v$) at 0.083° resolution capturing mesoscale eddies.
- **Satellite SAR & VIIRS Slicks**: High-resolution delineations of the Sanchi tanker burn and drift trajectory.

### Layer 2: Big Data Preprocessing & Segmentation
Implemented in `data_preprocessing.py`:
1. **Outlier Filtering & Schema Synchronization**: Handles null values in unranked particle candidate cells (`f_rank_in_hour` imputed to 999.0) and single-snapshot boundary conditions ($k=1$ drift errors set to 0.0 and drift ratio set to 1.0).
2. **Adaptive Thresholding**: Dynamically computes threshold boundaries combining particle consensus shares ($f\_share\_mean\_1k$) with Euclidean proximity to observed satellite contours, filtering out 80% of empty ocean background.

### Layer 3: Tri-Branch Feature Engineering
Inputs are projected into three dedicated sub-spaces:
- **Spatial Branch**: Models particle dispersion radius, cloud spread, slick area, and bearing angles.
- **Environmental Branch**: Embeds wind and ocean velocities, combined 3% windage vectors, and spatial alignment angles.
- **Drift Mismatch Branch**: Quantifies error vectors between forward advection predictions and subsequent satellite observations.

### Layer 4: Novel AST-CLAM Neural Architecture
Implemented in `model_architecture.py`:
- **Spatio-Temporal Convolutions**: Extracts local spatial neighborhood interactions between candidate grid cells.
- **Bidirectional LSTM**: Propagates sequential backtracking dynamics across retro-temporal steps ($t=0, -3h, \dots, -120h$).
- **AEU-Attn Module**: Dynamic attention queries compare the hidden state against environmental drift mismatch residuals, adaptively attenuating erroneous drift vectors during high sea-state turbulence.
- **Dual-Head Optimization**: Combines Focal Loss (for class imbalance) and Huber distance regression to ensure spatial smoothness.

### Layer 5: Decision Support & Source Origin Reconstruction
The model outputs a spatial probability distribution over candidate coordinates. The optimal source centroid is identified with sub-10 km accuracy, decisively beating classical Lagrangian methods and baseline classifiers.
