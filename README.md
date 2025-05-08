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

