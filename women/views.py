from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):  # HttpRequest Содержит информацию о запросе 
    return HttpResponse("Страница приложения women")
    
def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")
