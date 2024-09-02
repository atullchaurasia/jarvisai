import google.generativeai as genai

client = genai.configure(
    api_key= "AIzaSyCEwiHhPKhaGrpvfa9vEHfPg8yER9O9rGE"
)

model = genai.GenerativeModel("gemini-1.5-flash")    
chat = model.start_chat(
    history=[
        {"role": "model", "parts": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
       # {"role": "user", "parts": "write a poem on stars"},
    ]
)

response = chat.send_message("introduce yourself")
print(response.text)

