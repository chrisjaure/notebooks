I'm testing marimo out as a replacement for Google Opal.

This is the workflow I want to recreate:

[ User Input (Transcript) ]
            │
            ▼
┌──────────────────────────────────────┐
│  Step 1: Summarize Podcast           │
│  (Formats transcript into structured │
│   markdown research template)        │
└──────────────────┬───────────────────┘
                   │
                   ├──────────────────────────────────┐
                   ▼                                  ▼
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│  Step 2: Synthesize Content          │  │                                      │
│  (Extracts key concepts & crafts     │  │                                      │
│   image generation prompt)           │  │                                      │
└──────────────────┬───────────────────┘  │                                      │
                   │                      │                                      │
                   ▼                      │                                      │
┌──────────────────────────────────────┐  │                                      │
│  Step 3: Design Infographic          │  │                                      │
│  (Generates tall 1-page visual based │  │                                      │
│   on prompt & hand-drawn styleguide) │  │                                      │
└──────────────────┬───────────────────┘  │                                      │
                   │                      │                                      │
                   └──────────────────┬───┘                                      │
                                      ▼                                          ▼
                         ┌────────────────────────────────────────────────────────┐
                         │  Step 4: Create Final Webpage                          │
                         │  (Combines summary text & infographic image into       │
                         │   a responsive HTML/Tailwind web preview)              │
                         └────────────────────────────────────────────────────────┘

---

Output template:

```
## Core Insight
<!--
One sentence: What is the fundamental truth about human nature discovered in this episode?
-->

## Ground Truth
 <!--
One or two sentences: Who was the researcher, what did they produce, and why was it important?  
-->

### Theory
<!--
Identify and summarize the overarching cognitive systems, theories, or structural metaphors. Map out the system and how it explains human behavior beyond a single study. Use a structure that is appropriate for the theory. Strive for readability.
-->

### Data
<!--
Identify the landmark studies, clinical research, or scientific frameworks that prove the core insight. Identify the distinct, named metrics, mechanisms, or behavioral principles discovered by the researchers (mirroring a study's key findings).

For each mechanism, use a main bullet point with bold text, followed by specific nested sub-bullets:
- **Name of Mechanism/Core Concept**: Define the psychological mechanism, bias, or cultural phenomenon in one clear sentence using terminology from the podcast.
	- *The Evidence:* The laboratory experiment, historical event, data set, or real-world case study used to demonstrate it. Use validating details, quotes, and examples, not generic descriptions.
	- *The Insight:* The counter-intuitive takeaway, metric surge, or unexpected human behavior that shatters conventional wisdom.

For the name of the mechanism or core concept, use terms and language from the podcast. Don't fabricate names. Strive for readability.
-->

## Researcher's Lens
<!--
If applicable, capture the personal story, confession, or realization the researcher shared about their own life. Two paragraphs:
1. What was their personal struggle or behavioral loop?
2. How did their own scientific framework help them realize they were falling prey to the phenomenon?
-->
## Key Quotes
<!-- Find 2-3 key quotes that exemplify the main theme -->
  > 

## Practical Tips
<!-- How can I apply this to my life. 3-5 bullet points. -->

## Resonance
<!--
First paragraph: How does this scientific data support, clarify, or re-frame my Stoic principles? Second paragraph: How does this scientific data support, clarify, or re-frame my personalist philosophical principles?

Be objective.
-->
```

---

Styleguide:

```
'Playful and human-styled' design aesthetic.

This style should be characterized by an organic, hand-drawn feel, featuring soft lines, rounded shapes, and a warm, vibrant color palette. Incorporate friendly and approachable typography along with whimsical, stylized illustrations of people and icons. The overall mood should be creative, inviting, and expressive, avoiding a cold or overly formal corporate look.
```
