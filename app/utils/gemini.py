#Gemini
import os
from dotenv import load_dotenv
load_dotenv() 

# Setup GEMINI API
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash") 

def gemini_advice(age, gender, result):
    prompt = f"""You are being used in Skin Disease Classification Project. 
            Your role is to provide  1)advice 2)Remedies and 3)Medicine to the user based on the provided 
            data:

            - age: {age}
            - Gender: {gender}
            - Identified Disease: {result}

            Answer in structured format. Keep the respons size around 7-8 lines.
            """
    try:
        advice = model.generate_content(prompt)
        advice = advice.candidates[0].content.parts[0].text.replace('*', '')
        return advice
    except Exception as e:
        return "Error generating advice!"

