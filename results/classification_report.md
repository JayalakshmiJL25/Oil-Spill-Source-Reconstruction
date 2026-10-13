# Model Classification & Comparative Benchmark Evaluation Report

**Project Title**: AI-Based Adaptive Oil Spill Source Reconstruction Using Multi-Temporal Satellite Observations and Environmental Uncertainty  
**Evaluation Milestone**: Review 2 Evaluation Criteria  
**Department**: Computer Science & Engineering, SRM Institute of Science and Technology  
**Research Team**: Jayalakshmi T (RA2411031010115), Sachin P (RA2411031010117), Shivaani M (RA2411031010119), Varsha U (RA2411031010120)  
**Supervisor**: Dr. Banu Priya Prathaban  

---

## 1. Executive Summary & Review 2 Milestone Verification

In accordance with the Review 2 evaluation criteria set forth by the committee, our research team has designed, implemented, and benchmarked a novel spatial-temporal deep learning model—**Adaptive Spatial-Temporal Convolutional LSTM with Attention Mechanisms (AST-CLAM)**—against five established state-of-the-art classifier models:
1. **Random Forest Classifier** (classical ensemble baseline)
2. **XGBoost Classifier** (gradient boosted decision trees)
3. **Deep MLP** (feedforward neural network)
4. **Standard ConvLSTM** (recurrent spatio-temporal network without adaptive attention)
5. **Attention U-Net** (Chen & Wang 2022 spatial segmentation baseline)

The benchmark results decisively confirm that our **Proposed AST-CLAM** outperforms all baseline classifiers across all primary quantitative metrics: **Accuracy, Precision, Recall, F1-Score, AUC-ROC, and Centroid Trajectory Error (RMSE)** on both unseen synthetic testing splits and the real-world **2018 Sanchi tanker collision and sinking** validation data.

## 2. Quantitative Comparative Benchmark Performance Table

The table below reports the rigorous evaluation across all 6 models evaluated on unseen test folds (`id_fold=4` whole-spill partition):

| Model Architecture | Model Category | Accuracy | Precision | Recall | F1-Score | AUC-ROC | Centroid RMSE (km) | Median Distance (km) |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Random Forest | Classical Ensemble (Bagging Trees) | 89.53% | 52.68% | 45.61% | 0.4889 | 0.8969 | 29.84 km | 16.45 km |
| XGBoost | Gradient Boosted Decision Trees | 89.26% | 52.54% | 21.80% | 0.3081 | 0.8532 | 33.69 km | 12.33 km |
| Deep MLP | Deep Neural Network (Feedforward) | 88.65% | 47.29% | 29.54% | 0.3637 | 0.8145 | 35.21 km | 16.13 km |
| Standard ConvLSTM | Recurrent Spatio-Temporal Network | 89.06% | 50.62% | 12.07% | 0.1949 | 0.7841 | 30.79 km | 17.04 km |
| Attention U-Net | Spatial Encoder-Decoder with Attention | 88.64% | 43.90% | 12.52% | 0.1948 | 0.7828 | 29.86 km | 15.37 km |
| **Proposed AST-CLAM** | Novel Adaptive Spatio-Temporal Attention Net | **94.88%** | **85.26%** | **64.53%** | **0.7346** | **0.9870** | **6.86 km** | **6.94 km** |


## 3. Real-World Sanchi Tanker Spill Ground Truth Validation

To validate operational efficacy under genuine maritime disaster conditions, all models were evaluated on the **Sanchi tanker collision observation** (`SANCHI_slick_0` & `SANCHI_slick_1`, 18 Jan 2018), benchmarked against the verified wreck location (28.375° N, 125.942° E, located at 115 m depth):

| Model Architecture | Real Sanchi Wreck Error (km) | Relative Distance Reduction vs Naive Slick Center | Operational Source Recovery Status |
|:---|:---:|:---:|:---:|
| *Naive Slick Polygon Centroid* | 29.10 km | Baseline (0.0%) | Coarse approximation |
| *Integrated Lagrangian Density Rule (d)* | 27.30 km | 6.2% reduction | Fails to account for dynamic windage error |
| Random Forest | 25.79 km | 11.4% reduction | Approximated Boundary |
| XGBoost | 33.13 km | -13.9% reduction | Approximated Boundary |
| Deep MLP | 58.69 km | -101.7% reduction | Approximated Boundary |
| Standard ConvLSTM | 50.97 km | -75.2% reduction | Approximated Boundary |
| Attention U-Net | 37.48 km | -28.8% reduction | Approximated Boundary |
| **Proposed AST-CLAM** | **4.62 km** | **84.1% reduction** | Verified Source Cell Hit (<10 km) |


## 4. Algorithmic Novelty & Why AST-CLAM Outperforms Existing Baselines

Standard physical ocean models (OpenDrift, GNOME) and conventional classifiers fail in marine source reconstruction due to three structural weaknesses, which AST-CLAM directly resolves:

1. **Tri-Branch Dynamic Feature Decoupling**: Rather than treating tabular environmental forcing and Lagrangian particles as flat vectors, AST-CLAM explicitly partitions inputs into Spatial Geometry, Hydrodynamic Forcing (ERA5 wind + CMEMS current), and Advective Drift Mismatches.
2. **Adaptive Environmental Uncertainty Attention (AEU-Attn)**: When surface current velocities or windage coefficients exhibit large drift mismatch residuals ($f\_drift\_err$), standard ConvLSTM blindly propagates errors backward. AEU-Attn dynamically detects the divergence and downweights unreliable drift trajectories while amplifying multi-snapshot consensus.
3. **Multi-Task Focal Objective with Continuous Spatial Distance Calibration**: By jointly training on Focal Loss (conquering the 1:100 candidate cell imbalance) and Huber distance regression, the model regularizes its latent space to be physically consistent with spatial Euclidean topology.

## 5. Review 2 Presentation Slide Alignment

- **Slide 4 & 5 (Preprocessing & Big Data Results)**: Documented in `results/preprocessing_metrics.csv` and plotted in `results/preprocessing_plots.png`.
- **Slide 6 (Novel Classifier Description)**: Fully detailed in `model_architecture.py` and `results/system_architecture_description.md`.
- **Slide 7 (Results of Novel Classifier)**: High-resolution training, ROC, and metric distributions in `results/model_comparison_charts.png`.
- **Slide 8 (Comparison with Existing Classifier Models)**: Tables in Section 2 above and visual bar charts in Panel C/D of `results/model_comparison_charts.png`.
