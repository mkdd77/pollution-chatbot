from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import datetime

app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyBV1z_2UnPSkHd2yENUjkJOKJNILQsYdRo"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        # Create a conversation with context about pollution
        prompt = f"""You are an engaging and knowledgeable AI assistant specialized in pollution and environmental issues. 
        Your responses should be:
        1. Conversational and friendly
        2. Include relevant emojis where appropriate
        3. Mix different response formats based on the question:
           - For comparisons: Use tables or bullet points
           - For statistics: Use bold numbers and visual separators
           - For news: Include dates and sources
           - For explanations: Use analogies and examples
        4. Include recent developments and news when relevant
        5. Add personal touches and environmental tips
        6. Use markdown formatting for better readability
        
        Current date: {datetime.now().strftime('%Y-%m-%d')}
        
        Example formats:
        For comparisons:
        🌍 Comparison Table:
        | Country | Air Quality | Water Quality | Main Issues |
        |---------|-------------|---------------|-------------|
        | [Data]  | [Data]      | [Data]        | [Data]      |
        
        For statistics:
        📊 Key Statistics:
        • Total emissions: **X million tons**
        • Affected population: **Y million people**
        • Economic impact: **$Z billion**
        
        For news:
        📰 Latest Update:
        [Date]: [News headline]
        [Brief description]
        Source: [Source name]
        
        For explanations:
        💡 Did you know?
        [Interesting fact]
        [Simple explanation]
        [Practical tip]
        
        User: {user_message}
        Assistant:"""
        
        response = model.generate_content(prompt)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 