import google.generativeai as genai
genai.configure(api_key="AIzaSyBL5IY37VvsHmjIB5d_nbE_Cu9YvyCX6Ok")
model = genai.GenerativeModel("gemini-2.0-flash")
def chat():
    print("Gemini chatbot ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = model.generate_content(user_input)
        print("Chatbot:", response.text, "\n")
chat()