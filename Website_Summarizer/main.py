# Imports
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

# Create a .env file if you use paid APIs like GPT or LLaMA. Load API keys if necessary.
# This example uses an open-source model from Ollama, so we can comment out this section.

"""
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check API Key
if not api_key:
    print("No API key was found - please check troubleshooting!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start with sk-proj-; please check your key.")
elif api_key.strip() != api_key:
    print("An API key was found, but it contains spaces/tabs. Please remove them.")
else:
    print("API key found and looks good!")
"""

# Define the model being used
MODEL = "llama3.2"
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Define global headers for web scraping
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Define the system prompt (Moved outside of the class to fix the NameError)
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation-related. \
Respond in markdown."

class Website:
    def __init__(self, url):
        """
        Create a Website object from the given URL using BeautifulSoup.
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        self.title = soup.title.string if soup.title else "No title found"
        
        # Remove unnecessary elements (scripts, styles, images, inputs)
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        
        self.text = soup.body.get_text(separator="\n", strip=True)


# Function to create a user prompt
def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website are as follows; \
please provide a short summary in markdown. \
If it includes news or announcements, summarize those too.\n\n"
    user_prompt += website.text
    return user_prompt


# Function to create message format for OpenAI API
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},  # No more NameError
        {"role": "user", "content": user_prompt_for(website)}
    ]


# Function to summarize a webpage using LLM
def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages_for(website)
    )
    return response.choices[0].message.content

# Function to display summary properly in a normal Python script
def display_summary(url):
    summary = summarize(url)
    print("\n" + "="*50)
    print(f"Summary for {url}:")
    print("="*50)
    print(summary)
    print("="*50 + "\n")



# Run the summarization function on the given website
display_summary("https://www.magna.com/careers")
