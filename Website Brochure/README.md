# 🏢 Website Brochure Generator 🚀

## 📌 Overview
This project generates a **company brochure** using **Large Language Models (LLMs)** by scraping relevant website pages and structuring the information for prospective clients, investors, and recruits.

### **🔹 Features**
✔ **Scrapes website content** using `BeautifulSoup`.  
✔ **Extracts important links** (About, Careers, etc.) from the website.  
✔ **Uses `llama3.2` (Ollama) to summarize** the website data into a brochure.  
✔ **Streams responses in real-time** while generating output.  
✔ **Clickable links in VS Code** for easy navigation.  
✔ **Saves the brochure to `brochure.md`** for a clean formatted view.

---

## ⚙️ **Installation & Setup**

### ** Clone the Repository**

git clone https://github.com/your-username/Projects.git
cd Projects/Website Brochure


### **Create a Virtual Environment**
python -m venv venv


### **Activate it:**
venv\Scripts\activate


### **Install Dependencies**
pip install -r requirements.txt


🛠️ Usage

Generate a Brochure for Any Company
**Run the script:**
python main.py

By default, it generates a brochure for Anthropic:
stream_brochure("Anthropic", "https://anthropic.com")

Modify the function call to use any other company:
eg:
stream_brochure("OpenAI", "https://openai.com")

### **Output :**
The brochure streams in real-time in the terminal.
The final output is saved as brochure.md for better viewing in VS Code.




📄 Example Output
**In VS Code Terminal:**

===== Generating Company Brochure... =====

# Claude.ai Brochure

## Overview

Welcome to Claude.ai, a cutting-edge technology company dedicated to helping businesses and individuals navigate the complexities of data processing and analysis. Our mission is to harness the power of artificial intelligence to deliver insightful solutions that drive growth and success.

### About Us

 Claude.ai is committed to fostering a culture of innovation, collaboration, and continuous learning. We believe in empowering our team members to thrive in a dynamic environment that encourages creativity, open communication, and mutual respect.

## What We Do

With a focus on AI-powered solutions, we help clients to:

* Analyze complex data sets
* Identify trends and patterns
* Make informed decisions with confidence
* Drive business growth through data-driven insights

### Our Approach

We take a customer-centric approach, delivering tailored solutions that meet the unique needs of our clients. Our technology is designed to be flexible, scalable, and secure, ensuring seamless integration into existing workflows.

## What Our Customers Say

At Claude.ai, we're proud to have empowered numerous businesses and individuals with our cutting-edge AI solutions.

"(Claude.ai) has revolutionized the way we approach data analysis. Their expertise has been invaluable in helping us unlock new insights."

 - [Customer Testimonial]

## Careers at Claude.ai

If you're passionate about AI, innovation, and collaboration, we encourage you to join our team. As a forward-thinking organization, we offer:

* Competitive salaries and benefits
* Opportunities for professional growth and development
* A dynamic work environment that fosters creativity and innovation

We are currently hiring talented individuals in the following roles: [list job openings]

## Join Us

At Claude.ai, we're proud to have empowered numerous businesses and individuals with our cutting-edge AI solutions.

"(Claude.ai) has revolutionized the way we approach data analysis. Their expertise has been invaluable in helping us unlock new insights."

 - [Customer Testimonial]

## Careers at Claude.ai

If you're passionate about AI, innovation, and collaboration, we encourage you to join our team. As a forward-thinking organization, we offer:

* Competitive salaries and benefits
* Opportunities for professional growth and development
* A dynamic work environment that fosters creativity and innovation

We are currently hiring talented individuals in the following roles: [list job openings]

## Join Us
## Careers at Claude.ai

If you're passionate about AI, innovation, and collaboration, we encourage you to join our team. As a forward-thinking organization, we offer:

* Competitive salaries and benefits
* Opportunities for professional growth and development
* A dynamic work environment that fosters creativity and innovation

We are currently hiring talented individuals in the following roles: [list job openings]

## Join Us
* Competitive salaries and benefits
* Opportunities for professional growth and development
* A dynamic work environment that fosters creativity and innovation
* 
Ready to be part of a vibrant community that's shaping the future of AI? Explore our current job openings and stay up-to-date on company news and updates.

[Visit our careers page](link)

(Note: Job openining information can be added as per the actual requirement and availability. The job sections in this brochure will only be present if there are any specific job openings available.)   

===== Brochure Generation Complete! =====





🚀 Future Improvements

✅ Support multi-page company reports.
✅ Add PDF export functionality.
✅ Improve tone & formatting options for the brochure.

🤝 Contributing

Feel free to submit issues, suggest improvements, or contribute! Open a Pull Request (PR) with your ideas. 🚀



