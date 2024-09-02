import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
NewsAPI = "08ae3b299a544dd0a40914e6ce8ec767"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def AiProcess(command):
    
    client = genai.configure(api_key= "")
    model = genai.GenerativeModel("gemini-1.5-flash")    
    chat = model.start_chat(
        history=[
            {"role": "model", "parts": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
        # {"role": "user", "parts": "write a poem on stars"},
        ]
    )
    response = chat.send_message(command)
    return response.text

def processCommand(c):
    print(f"Processing command: {c}") 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")  
        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")  
          
    elif "open git" in c.lower():
        webbrowser.open("https://github.com")    
            
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 
     
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NewsAPI}")
        if r.status_code == 200:
            data = r.json() 
            articles = data.get('articles', [])
            
            for article in articles:
                speak(article['title'])    
                
    else:
        output = AiProcess(c)
        speak(output)              

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    
    while True:
        #Listen for the wake word "JARVIS"
        #obtain audio from microphone
        r = sr.Recognizer()
       
   
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            
            word = r.recognize_google(audio)
            print(f"Recognized word: {word}") 
            
            if(word.lower() == "jarvis"):
                speak("Yes sir")
                
                #Listen for command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Jarvis Activated....")
                    audio = r.listen(source)
                    command  = r.recognize_google(audio)
            
                    processCommand(command)
                
            
        except Exception as e:
            print("Error; {0}".format(e))
                   