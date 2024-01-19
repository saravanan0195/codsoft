#task-1 of building the rule based chatbot

def simple_chatbot(user_input):
    # Convert user input to lowercase 
    user_input = user_input.lower()

    # Rule-based responses
    if 'hello' in user_input or 'hi' in user_input:
        return "hi ! welcome back......"
    
    elif 'hey'in user_input:
        return "Hi there! How can I help you today?"
    
    elif 'how are you' in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif 'goodbye' in user_input or 'bye' in user_input:
        return "Goodbye! Feel free to reach out if you have more questions."

    elif 'tell me a joke' in user_input:
        return "Certainly, I'll do my best to make you laugh. Here's a funny one:\nWhy did the bicycle fall over?\nBecause it was two-tired!"
    
    elif 'thanks' in user_input or 'thank you' in user_input:
        return "You're welcome! If you need assistance, just ask."

    elif 'your name' in user_input:
        return "I'm just a simple chatbot.my boss named me as 'MIA'.so call me as mia"

    elif 'what can you do' in user_input:
        return "I can provide information, answer questions, or just chat with you. Feel free to ask anything!"
    
    elif 'how was the weather today' in user_input:
        return "It was nice and sunny! with 26^c, I wish you could've gone outside."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Example usage
print("Chatbot: Hello! I'm a simple rule-based chatbot. Type 'exit' to end the conversation.")

#starting while loop to interact with chatbot continuously
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
             
                             #task 1 successfully ends........
