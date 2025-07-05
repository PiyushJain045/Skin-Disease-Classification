from django.shortcuts import render
from django.views import View



class Home(View):
    def get(self, request):
        print("INSIDE HOME GET")

        return render(request, "index.html")

    def post(self, request):
        pass