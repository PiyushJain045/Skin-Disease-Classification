from django.shortcuts import render
from django.views import View
from .utils.predict import predict_image

# Image processing
import base64
from io import BytesIO


class Home(View):
    def get(self, request):
        print("INSIDE HOME GET")
        return render(request, "index.html")

    def post(self, request):
        print("INSIDE HOME POST")

        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        print(age, gender, image)
        result,_ = predict_image(image)

        response = {
            "result": result,
        }

        return render(request, "partials/result.html", response)