I'm testing marimo out as a replacement for Google Opal.

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

