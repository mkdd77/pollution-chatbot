The Pollution Awareness Chatbot is an AI-based conversational tool designed to educate users about various types of pollution and promote eco-friendly habits. This chatbot serves as a virtual assistant that provides instant and accurate information on pollution-related topics, including air, water, soil, noise, and plastic pollution. It aims to spread awareness, encourage responsible behavior, and offer practical solutions to help reduce pollution on an individual and community level.

Key features of the chatbot include:

Real-time Q&A about pollution and its effects

Practical eco-friendly tips and solutions

User-friendly chat interface

Educational content for schools or awareness campaigns

Customizable knowledge base for specific regions or events
💻 Technologies Used
Flask – Backend server
HTML/CSS – Frontend templates
Tailwind CSS – UI framework
JavaScript (Vanilla) – AJAX for async interaction
Gemini API – Core analysis engine (Generative AI)
Base64 – Image encoding

⚙️ Installation
Prerequisites
Python 3.8+
pip
Steps
# Clone the repository
git clone https://github.com/mkdd77/pollution-chatbot.git

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the app
python app.py
Visit http://127.0.0.1:5000 in your browser.

📦 Requirements
Flask
google-generativeai
Werkzeug
Create a file requirements.txt:

flask==3.0.2
google-generativeai==0.3.2
python-dotenv==1.0.1 
🤖 LLM API Integration
This app uses Gemini 1.5 Flash from Google via google-generativeai.

import google.generativeai as genai
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')
Prompts like:

detect the pollution information all over the world and give different differnt sollution to control pollution 
📜 Prompt Engineering
We use a static prompt enriched with user input. Based on what’s provided (text, image, or both), the Gemini model evaluates content and responds with clear, quantifiable results.

Example format:

🌍 Comparison Table:
        | Country | Air Quality | Water Quality | Main Issues |
        |---------|-------------|---------------|-------------|
        | [Data]  | [Data]      | [Data]        | [Data]      |
        
This is displayed back in the UI as a bot message.



created by mayank
