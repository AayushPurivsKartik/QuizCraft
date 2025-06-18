#!/usr/bin/env bash
pip install -r requirements.txt
# Install spaCy model during build
python -m spacy download en_core_web_sm

# Download NLTK data
python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"
