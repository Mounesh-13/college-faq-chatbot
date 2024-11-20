import csv
from fuzzywuzzy import process

# Load the FAQ data from the CSV
faq_data = []
with open('faq_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        faq_data.append(row)

# Function to handle chatbot responses
def chatbot_response(user_query):
    # Search for the best match using fuzzy matching
    questions = [faq['question'] for faq in faq_data]
    match, score = process.extractOne(user_query, questions)
    
    if score > 70:  # Match threshold
        for faq in faq_data:
            if faq['question'] == match:
                return faq['answer']
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Test the chatbot interaction
if __name__ == "__main__":
    print("Welcome to the FAQ Chatbot! Type 'exit' to end.")
    while True:
        user_query = input("Ask a question: ")
        if user_query.lower() == 'exit':
            break
        response = chatbot_response(user_query)
        print("Chatbot:", response)
