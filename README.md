# PDF Anonymizer

A Python tool that automatically detects and anonymizes named entities (persons, organizations, locations) in PDF files using NLP.

## Features

- Extracts text from PDF files
- Detects named entities using spaCy's English language model
- Replaces names, organizations and locations with `****`
- Outputs a new anonymized PDF file

## Technologies

- Python
- spaCy
- pypdf

## Usage

```bash
pip install spacy pypdf
python -m spacy download en_core_web_sm
python main.py
```

## Status

> This project is a work in progress. The anonymized text is currently not re-embedded into the PDF layout correctly. Planned improvement: use a PDF rendering library to properly overlay anonymized text.

## Known Issues

- Anonymized text is not visually replaced in the PDF output, only processed in memory