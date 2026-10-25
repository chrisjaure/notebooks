I'm testing [marimo](https://marimo.io/) as a replacement for Google Opal.

I liked Opal because I could create multi-step workflows and evaluate the output between each step; that made debugging easy. It worked really well for my particular use case, but Google killed it without a proper replacement (skills are not a replacement!).

Rather than switch to something heavy-weight and AI-specific, I decided to try out marimo (a modern jupyter notebook alternative) for these reasons:

- The editor shows global variables for easy debugging between steps.
- The editor has type hints which I need as a beginner.
- It has no AI abstraction so I can use whatever I want. Free AI tools are good enough to help me code the basics that I can then extend to learn from.
- It has an app mode like Opal.

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
