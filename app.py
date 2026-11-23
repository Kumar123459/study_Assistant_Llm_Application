
import gradio as gr
from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Study Assistant
def study_assistant(user_prompt):

    if not user_prompt.strip():
        return "Please enter a question."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

# Gradio interface
demo = gr.Interface(
    fn=study_assistant,
    inputs=gr.Textbox(
        lines=3,
        label="Ask your question",
        placeholder="Explain LangChain in simple words..."
    ),
    outputs=gr.Textbox(label="AI Response"),
    title="Ai Study Assistant",
    description="Your personal Gemini-powered learning assistant"
)

# Launch app
demo.launch(server_name="0.0.0.0", server_port=7860, share=True)

