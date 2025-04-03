import os  # For accessing environment variables
import chainlit as cl  # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict  # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
import requests

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@function_tool("generate_website_code")
def generate_website_code(type="portfolio") -> str:
    """
    Generates HTML and CSS code for a simple website or portfolio.
    
    Args:
        type (str): The type of website ("portfolio" or "business"). Defaults to "portfolio".

    Returns:
        str: HTML and CSS code for the requested website.
    """
    if type == "portfolio":
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My Portfolio</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; }
                header { background: #333; color: white; padding: 20px; }
                section { margin: 20px; }
            </style>
        </head>
        <body>
            <header>
                <h1>Welcome to My Portfolio</h1>
            </header>
            <section>
                <p>Check out my work and projects here.</p>
            </section>
        </body>
        </html>
        """
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Business Website</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; }
                header { background: blue; color: white; padding: 20px; }
                section { margin: 20px; }
            </style>
        </head>
        <body>
            <header>
                <h1>Welcome to Our Business</h1>
            </header>
            <section>
                <p>Learn more about our services.</p>
            </section>
        </body>
        </html>
        """


agent = Agent(
    name="Website Generator Agent",
    instructions="""You are an agent designed to generate website code.

Your responsibilities:
1. If the user asks for a portfolio or website, generate HTML and CSS code.
2. If the user requests other types of responses, politely inform them that you only generate website code.
""",
    model=model,
    tools=[generate_website_code],
)

# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):
    result = await cl.make_async(Runner.run_sync)(agent, input=[{"role": "user", "content": message.content}])
    response_text = result.final_output
    await cl.Message(content=response_text).send()