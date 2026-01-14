The IDS captures traffic using Wireshark/Scapy,
extracts packet-level features,
applies machine learning models,
and raises alerts for anomalous behavior.

ml-ids/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── traffic.pcap
│   ├── processed/
│   │   └── dataset.csv
│
├── src/
│   ├── packet_capture.py
│   ├── feature_extraction.py
│   ├── preprocess.py
│   ├── train_ml.py
│   ├── train_dl.py
│   ├── ids_engine.py
│   └── alert.py
│
├── models/
│   ├── random_forest.pkl
│   └── deep_ids_model.h5
│
├── notebooks/
│   └── traffic_analysis.ipynb
│
└── docs/
    └── architecture.md
