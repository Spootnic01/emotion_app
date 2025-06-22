# Emotion Analyzer with LIA

This is a Python FastAPI web application that analyzes emotions from text input using:

- Transformer-based emotion classifier (`j-hartmann/emotion-english-distilroberta-base`)
- LIA-style lexical category analysis with Empath

## Features

- Enter text via a web form
- Get emotion probabilities and lexical category counts
- Visualize results using Chart.js with Bootstrap UI

## Installation

```bash
git clone https://github.com/yourusername/emotion-lia-analyzer.git
cd emotion-lia-analyzer
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
