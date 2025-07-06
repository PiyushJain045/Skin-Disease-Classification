from django.shortcuts import render
from django.views import View
from .utils.predict import predict_image
from django.http import JsonResponse

#Gemini
import os
from dotenv import load_dotenv
load_dotenv() 

# Setup GEMINI API
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash") 

class Home(View):
    def get(self, request):
        print("INSIDE HOME GET")
        return render(request, "index.html")

    def post(self, request):
        try:
            print("INSIDE HOME POST")

            age = request.POST.get('age')
            gender = request.POST.get('gender')
            image = request.FILES.get('image')

            print(age, gender, image)

            # Image Prediction
            result,_ = predict_image(image)

            # Advice
            prompt = f"""You are being used in Skin Disease Classification Project. 
            Your role is to provide  1)advice 2)Remedies and 3)Medicine to the user based on the provided 
            data:

            - age: {age}
            - Gender: {gender}
            - Identified Disease: {result}

            Answer in structured format. Keep the respons size around 7-8 lines.
            """

            advice = model.generate_content(prompt)

            # Final Response
            response = {
                "result": result,
                "advice": advice.candidates[0].content.parts[0].text.replace('*', '')
            }

            return render(request, "partials/result.html", response)
        
        except Exception as e:
            print(f"[ERROR]: {str(e)}")
            return JsonResponse(
                {"error": "Something went wrong. Please try again later."},
                status=500
            )