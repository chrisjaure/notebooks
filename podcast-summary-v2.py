import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    import io
    import marimo as mo
    from google import genai
    from google.genai import types
    from PIL import Image

    # Initialize Google GenAI client (uses GEMINI_API_KEY env variable)
    client = genai.Client()
    return Image, client, io, mo, types


@app.cell
def _(mo):
    mo.md("""
    # ConceptSketch: Podcast & Article Infographic Generator

    Instantly transform your articles and podcasts into structured summaries and playful infographics.
    """)
    return


@app.cell
def node1(mo):
    # Node 1: User Input
    transcript_input = mo.ui.text_area(
        label="Podcast Transcript / Article Content",
        placeholder="Paste your transcript or article text here...",
        full_width=True,
        rows=20
    ).form(submit_button_label="Generate Infographic & Webpage")
    transcript_input
    return (transcript_input,)


@app.cell
def _():
    # Assets / Templates from DAG
    output_template = """
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
    """

    styleguide = """
    'Playful and human-styled' design aesthetic.

    This style should be characterized by an organic, hand-drawn feel, featuring soft lines, rounded shapes, and a warm, vibrant color palette. Incorporate friendly and approachable typography along with whimsical, stylized illustrations of people and icons. The overall mood should be creative, inviting, and expressive, avoiding a cold or overly formal corporate look.
    """
    return output_template, styleguide


@app.cell
def node2(client, mo, output_template, transcript_input, types):
    # Node 2: Summarize Podcast (gemini-2.5-pro / text-3-pro)
    mo.stop(not transcript_input.value)

    with mo.status.spinner(title="Step 1: Summarizing content..."):
        _summary_response = client.models.generate_content(
            model="gemini-pro-latest",
            contents=f"""
            OBJECTIVE: Summarize the content from input strictly following the structure of template.
            TASKS:
            - Analyze the retrieved content thoroughly.
            - Format the final output precisely according to the template provided below. Ensure every section of the template is addressed using details from the content.

            <input>{transcript_input.value}</input>
            <template>{output_template}</template>
            """,
            config=types.GenerateContentConfig(
                system_instruction="You are working as part of an AI system. Provide direct structured output without preamble."
            ),
        )
        summary_text = _summary_response.text
    return (summary_text,)


@app.cell
def node3(client, mo, summary_text):
    # Node 3: Synthesize Content
    with mo.status.spinner(title="Step 2: Synthesizing visual prompt..."):
        _prompt_response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=f"""
            OBJECTIVE: Analyze the provided content to create a detailed visual description for a playful, human-styled infographic.
            OUTPUT FORMAT: Provide a descriptive prompt intended for an image generation tool. You are done when you have provided both the summary and the visual description.

            Summary text: {summary_text}
            """,
        )
        visual_prompt = _prompt_response.text
    return (visual_prompt,)


@app.cell
def node4(Image, client, io, mo, styleguide, types, visual_prompt):
    # Node 4: Design Infographic
    with mo.status.spinner(
        title="Step 3: Designing Infographic..."
    ):
        _image_result = client.models.generate_content(
            model="gemini-3-pro-image",
            contents=f"""
            OBJECTIVE: Generate a high-quality, detailed infographic that visually summarizes the key themes and concepts provided in the user input.
            CONSTRAINTS:
            - Number of Images: Generate exactly one single image.
            - Visual Style: Follow `styleguide`
            - Aspect ratio: 9:16

            COMPOSITION & STYLE:
            - Create the infographic based on the specific details and instructions found in `visual_prompt`.
            - Translate the main ideas and summary points into a cohesive visual narrative. 
            - The layout should be logically organized, using decorative elements, soft-edged containers, and illustrative arrows to guide the viewer through the information.
            - Each visual element should reinforce the core concepts mentioned in the visual prompt, ensuring the final output is both informative and visually engaging.

            IMPORTANT: Generate exactly one image.
            <visual_prompt>{visual_prompt}</visual_prompt>
            <styleguide>{styleguide}</styleguide>
            """,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE'],
                image_config=types.ImageConfig(
                    aspect_ratio='9:16',
                ),
            ),
        )

        generated_image = None
        for _part in _image_result.parts:
            if _part.inline_data:
                generated_image = Image.open(io.BytesIO(_part.as_image().image_bytes))
                break
    return (generated_image,)


@app.cell
def _(generated_image, mo, summary_text):
    mo.vstack([
        mo.md("# Output Summary"),
        mo.image(src=generated_image),
        mo.md(summary_text)
    ])
    return


if __name__ == "__main__":
    app.run()
