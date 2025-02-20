 Creator - Atharva Mahindrakar. 
 Created on 10.02.2025
 
 🦙 LLM Website Summarizer 🚀

 📌 Overview
This project uses **Large Language Models (LLMs)** to **summarize website content** using `Ollama` and `BeautifulSoup` for web scraping.

- **Web Scraping:** Extracts website text using `BeautifulSoup`
- **LLM Processing:** Summarizes the content using `llama3.2` (Ollama API)
- **Terminal Output:** Displays summarized content in the console


 ⚙️ Installation & Setup

 1️⃣ Clone the Repository

Activate a virtual environment

2️⃣ Install Dependencies
pip install -r requirements.txt


🛠️ Usage
Run the Script using the following command -
python main.py


Example Output
==================================================
Summary for https://example.com
==================================================
This website contains information about...
==================================================



Modify the Website URL
To summarize a different webpage, modify this line in main.py:
display_summary("https://your-website.com")


🔑 Environment Variables (Optional)
If you're using a paid API key (like OpenAI's GPT), create a .env file in the project directory and add:
OPENAI_API_KEY=your-api-key-here
Then, uncomment the load_dotenv() lines in main.py.


👨‍💻 Contributing
Feel free to fork this repository and submit pull requests! 🚀
