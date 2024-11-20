from flask import Flask, request, render_template, jsonify
import pandas as pd
from fuzzywuzzy import process

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("faq_data.csv")

# Define chatbot response function
def chatbot_response(query):
    question_list = df['question'].tolist()
    best_match, score = process.extractOne(query, question_list)
    if score > 50:
        response = df.loc[df['question'] == best_match, 'answer'].values[0]
        return response
    else:
        return "Sorry, I don't understand your question."

# Define routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        # Get the user input from the request
        user_input = request.json.get("user_input")  # Use JSON to receive data
        
        # Get the chatbot's response
        response = chatbot_response(user_input)
        
        # Return the response as JSON
        return jsonify({"response": response})

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({"error": str(e)}), 500

# Error handler for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
