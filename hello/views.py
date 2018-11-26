from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

def load_html(html_file):
    with open(html_file) as file_obj:
        file = file_obj.read()

    return file
def index(request):
    return HttpResponse(load_html('index.html'))
