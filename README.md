# Data Hack - FraunhoferIDMT_DynamicBeats

This repository provides a pipeline to predict figure skating moves from pre-extracted skeleton data(https://github.com/CMU-Perceptual-Computing-Lab/openpose) using a pretrained MDR-GCN model(https://github.com/dingyn-Reno/MDR-GCN). The pipeline outputs time-stamped moves in JSON format. Than integrated them with prompt to generate music using InspireMusic(https://github.com/FunAudioLLM/FunMusic) that syncs with video.

---

## 📂 Repository Structure

repo/
├── data/ # Pre-extracted skeleton data (.npy files)
├── model/ # Pretrained model file (.pt)
├── outputs/ # JSON outputs from predictions
├── src/ # Python scripts
│ └── inference.py # Run predictions
└── README.md

---

## ⚡ Features

- Predicts figure skating moves from skeleton data.
- Applies independent penalties for over-represented moves.
- Merges consecutive moves of the same type.
- Outputs time-stamped predictions in JSON format.
- Configurable for different videos, models, and intervals.

---

## 🏃‍♂️ How to Run

# 1. Clone the repository
git clone https://github.com/yourusername/SkatingMovePrediction.git
cd SkatingMovePrediction

# 2. Run the inference script
python src/inference.py
