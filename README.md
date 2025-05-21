# 👕 Human-Centric Virtual Try-On Pipeline

A real-time virtual try-on pipeline that enables realistic garment transfer using deep learning. This project builds a complete toolchain around the VITON-HD model architecture, integrating preprocessing, geometric warping, and try-on synthesis into a modular and deployable system.

> 🧠 This project is part of an academic research initiative and has been extended with a modular pipeline, real-time preprocessing, and simplified usability for future experimentation and deployment.

---

## 📌 Features

- ✅ Complete end-to-end pipeline from input images to try-on output
- 👤 Person image + 👚 Cloth image → 👗 Realistic composite
- 🔁 Preprocessing, pose detection, warping, and synthesis integrated
- 🚀 CUDA-accelerated for fast real-time inference
- 🧱 Clean folder structure and modular code

---

## 🧱 Architecture Overview

The system follows a three-stage design:

1. **Preprocessing**
   - Person + clothing image loading
   - Pose keypoint extraction
   - Agnostic person representation

2. **Geometric Matching Module (GMM)**
   - Learns spatial warping using Thin Plate Spline (TPS)
   - Aligns clothing to body pose

3. **Try-On Module (TOM)**
   - Synthesizes final output by combining warped cloth + preserved body parts
   - Generates high-quality, seamless virtual try-on images


```
[Person Image] + [Cloth Image]
         ↓
     [GMM Warping]
         ↓
     [TOM Synthesis]
         ↓
     [Try-On Output]
```

---

## 📁 Project Structure

```
virtual-tryon-pipeline/
├── models/            # Model definitions for GMM and TOM
│   └── checkpoints/   # Place pre-trained .pth files here
├── preprocessing/     # Image preprocessing and human parsing
├── inference/         # Final try-on logic
├── utils/             # Helper scripts
├── output/            # Generated outputs
├── requirements.txt   # Python dependencies
├── main.py            # Entry script (optional for testing)
└── README.md
```

---

## 📥 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/virtual-tryon-pipeline.git
cd virtual-tryon-pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Dataset & Checkpoints

- **VITON-HD Dataset**: [Google Drive](https://www.kaggle.com/datasets/marquis03/high-resolution-viton-zalando-dataset?select=test)
- **Pre-trained Models**:
  - `gmm_final.pth` → `models/checkpoints/GMM/`
  - `tom_final.pth` → `models/checkpoints/TOM/`

> ⚠️ Do **not upload large files** or datasets to GitHub — use `.gitignore`.

---

## ▶️ Inference Example

```bash
python inference/inference.py --person path/to/person.jpg --cloth path/to/cloth.jpg
```

Output will be saved to the `output/` folder.

---

## 🧠 Academic Context

This project was developed as part of a B.Tech design project and supports a research paper titled:

**"Human-Centric Virtual Try-On via Warping and Image Synthesis Networks"**

- Paper link: *[To be added upon acceptance]*  
- Conference/Journal: *[To be announced]*

---

## 📷 Demo Output

| Person Input | Clothing Input | Try-On Output |
|--------------|----------------|----------------|
| ![](path/to/person.jpg) | ![](path/to/cloth.jpg) | ![](path/to/output.jpg) |

> Replace with your actual image links or upload in GitHub issues/wiki.

---

