import random

class FinTechChatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What financial information can I help you with?",
            "Welcome! How may I support you regarding our financial services?"
        ]
        self.loan_info = "We offer personal loans with interest rates starting at 5% APR. You can apply directly on our website."
        self.credit_report_info = "Credit reports provide a summary of your credit history. You can request a free credit report once a year from major credit bureaus."
        self.interest_rate_info = "Interest rates vary based on the loan type and your credit score. Would you like more information on specific rates?"
        self.support_info = "If you need further assistance, please contact our support team at support@fintechcompany.com or call 123-456-7890."

    def get_response(self, user_input):
        user_input = user_input.lower()

        if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            return random.choice(self.greetings)
        elif "loan" in user_input or "personal loan" in user_input:
            return self.loan_info
        elif "credit report" in user_input or "credit score" in user_input:
            return self.credit_report_info
        elif "interest rate" in user_input or "rate" in user_input:
            return self.interest_rate_info
        elif "support" in user_input or "contact" in user_input:
            return self.support_info
        else:
            return "I'm sorry, I couldn't understand your request. Could you please provide more details?"

if __name__ == "__main__":
    chatbot = FinTechChatbot()
    print("FinTech Chatbot is now online. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for reaching out! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
