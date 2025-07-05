from django.shortcuts import render
from django.views import View
from .utils.predict import predict_image



class Home(View):
    def get(self, request):
        print("INSIDE HOME GET")

        return render(request, "index.html")

    def post(self, request):
        print("INSIDE HOME POST")
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        # print(age, gender, image)
        print(predict_image(image))

        return render(request, "index.html")