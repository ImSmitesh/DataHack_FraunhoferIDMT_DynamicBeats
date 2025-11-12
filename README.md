# Data Hack - FraunhoferIDMT_DynamicBeats

This repository provides a pipeline to predict figure skating moves from pre-extracted skeleton data(https://github.com/CMU-Perceptual-Computing-Lab/openpose) using a pretrained MDR-GCN model(https://github.com/dingyn-Reno/MDR-GCN). The pipeline outputs time-stamped moves in JSON format. Than integrated them with prompt to generate music using InspireMusic(https://github.com/FunAudioLLM/FunMusic) that syncs with video.

---

## Repository Structure

```plaintext
repo/
├── data/                # Pre-extracted skeleton data (.npy files)            
├── model/               # Pretrained model file (.pt)
├── outputs/             # JSON outputs from predictions     
├── src/                 # Python scripts
├──  └── inference.py    # Run predictions 
└── README.md            # Project documentation
```

---

## Features

- Loades keypoints extracted from video for each frame from data/ folder.
- Filter to get keypoints of only perfomer.
- Post-processing skeleton to feed into model for prediction.
- Predicts move by feeding model chunks of 500 frames.
- Outputs .json file saved in output/ folder with moves predicted for each chunk of frames.

- The part which calculates the skeleton data using Openpose and post-processing of those keypoints works independently from this repo, it would be integrated and add to this repo soon.

---

## How to Use

# 1. Clone the repository

```bash
git clone https://github.com/yourusername/SkatingMovePrediction.git

cd SkatingMovePrediction
```

# 2. Run the inference script

```bash
python src/inference.py
```
