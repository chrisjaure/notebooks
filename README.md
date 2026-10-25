I'm testing [marimo](https://marimo.io/) as a replacement for Google Opal.

This is the workflow I want to recreate:

```
[ User Input (Transcript) ]
            │
            ▼
┌──────────────────────────────────────┐
│  Step 1: Summarize Podcast           │
│  (Formats transcript into structured │
│   markdown research template)        │
└──────────────────┬───────────────────┘
                   │
                   ├──────────────────────┐
                   ▼                      │
┌──────────────────────────────────────┐  │
│  Step 2: Synthesize Content          │  │
│  (Extracts key concepts & crafts     │  │
│   image generation prompt)           │  │
└──────────────────┬───────────────────┘  │
                   │                      │
                   ▼                      │
┌──────────────────────────────────────┐  │
│  Step 3: Design Infographic          │  │
│  (Generates tall 1-page visual based │  │
│   on prompt & hand-drawn styleguide) │  │
└──────────────────┬───────────────────┘  │
                   │                      │
                   │   ┌──────────────────┘
                   ▼   ▼               
┌──────────────────────────────────────┐
│  Step 4: Output Results              │
│  (Combines summary text & infographic│
│   for copy/pasting into notes)       │
└──────────────────────────────────────┘
```

## Prerequisites

Uses [`google-genai`](https://googleapis.github.io/python-genai/) so you need to export your [Gemini API Key](https://aistudio.google.com/api-keys):

```
export GEMINI_API_KEY='your-api-key'
```

## Usage

1. Start the app:
```
uv run marimo run podcast-summary-v2.py
```

2. Paste a transcript from your favorite podcast like [HiddenBrain](https://www.hiddenbrain.org/).
