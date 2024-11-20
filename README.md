# college-faq-chatbot
# FAQ Chatbot

A simple FAQ chatbot built with Flask and FuzzyWuzzy to provide automated responses based on a pre-defined FAQ dataset.

## Prerequisites
- Python 3.6+
- pip (Python package installer)

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/faq-chatbot.git
   cd faq-chatbot
Create Virtual Environment (optional)

bash
Copy code
python -m venv venv
Activate Virtual Environment

Windows: .\venv\Scripts\activate
Mac/Linux: source venv/bin/activate
Install Dependencies

bash
Copy code
pip install flask pandas fuzzywuzzy python-Levenshtein

Prepare FAQ Dataset Ensure faq_data.csv is in the project directory, formatted with question and answer columns.

Run the App

bash

Copy code

python app.py

Access at http://127.0.0.1:5000/.

Test Cases
Q: "How to reset my password?"
A: "To reset your password, go to settings and click 'Reset Password'."

Q: "What is your return policy?"
A: "Our return policy lasts 30 days from the purchase date."

Q: "How do I contact support?"
A: "Sorry, I don't understand your question."

License
MIT License

python
Copy code

This concise README explains the project setup, installation, and provides key test cases, all within a compact 30-line format. Adjust the GitHub repository URL as necessary.





