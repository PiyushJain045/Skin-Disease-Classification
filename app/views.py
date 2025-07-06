from django.shortcuts import render
from django.views import View
from .utils.predict import predict_image
from .utils.gemini import gemini_advice
from django.http import JsonResponse

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
            advice = gemini_advice(age, gender, result)
            
            # Final Response
            response = {
                "result": result,
                "advice": advice
            }

            return render(request, "partials/result.html", response)
        
        except Exception as e:
            print(f"[ERROR]: {str(e)}")
            return JsonResponse(
                {"error": "Something went wrong. Please try again later."},
                status=500
            )