class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hello! How can I help you?",
            "how are you": "I'm just a chatbot, but I'm here to assist you.",
            "what's your name": "I'm a rule-based chatbot.",
            "what about codsoft?": "It's amazing!!",
            "who is jass manak?": "He is a popular punjabi singer",
            "what programming languages ai uses?": "Python is widely used for ai, but sometimes C/C++, Java etc. is also used",
            "who is the prime minister of india?": "Mr.Narendra Modi",
            "how many continents are there in the world?": "Seven",
            "name luxuries brands": "Gucci, Kylie Cosmetics, Prada, Dior, Channel, etc.",
            "python ide's name?": "Visual Studio Code, Spyder, Jupyter Notebook, Pycharm etc.",
            "what is your mother's name?": "I'm just a bot, I can't answer that.",
            "bye": "Goodbye! Have a great day!",
        }
    
    def generate_response(self, user_input):
        user_input = user_input.lower()
        
        if "hello" in user_input:
            return "Hello! How can I assist you?"
        elif "how are you" in user_input:
            return "I'm just a chatbot, but I'm here to help!"
        elif "what's your name" in user_input:
            return "I'm a rule-based chatbot."
        elif "what about codsoft?" in user_input:
            return "It's amazing!!"
        elif "who is jass manak?" in user_input:
            return "He is a popular punjabi singer"
        elif "what programming languages ai uses?" in user_input:
            return "Python is widely used for ai, but sometimes C/C++, Java etc. is also used"
        elif "who is the prime minister of india?" in user_input:
            return "Mr.Narendra Modi"
        elif "how many continents are there in the world?" in user_input:
            return  "Seven"
        elif "name luxuries brands" in user_input:
            return "Gucci, Kylie Cosmetics, Prada, Dior, Channel, etc."
        elif "python ide's name?" in user_input:
            return "Visual Studio Code, Spyder, Jupyter Notebook, Pycharm etc."
        elif "what is your mother's name?" in user_input:
            return "I'm just a bot, I can't answer that."
        elif "bye" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I am unable to understand your question."
    
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    
    print("Rule-Based Chatbot: Hello! How can I assist you?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Rule-Based Chatbot: Goodbye!")
            break
        
        response = chatbot.generate_response(user_input)
        print("Rule-Based Chatbot:", response)