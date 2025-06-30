import google.generativeai as genai 

genai.configure(api_key = "your api key")
model=genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("you are a virtual assistant named jarvis")
    


print(response.text)