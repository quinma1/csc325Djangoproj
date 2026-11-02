from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return HttpResponse("Welcome to the About Page!")

@api_view(["GET"])
def info(request):
        return Response({"course": "CSC325", "project": "Django CI/CD", 'student': 'Matt'}) 