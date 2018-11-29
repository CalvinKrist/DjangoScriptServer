from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from rest_framework.decorators import api_view
from django.core import serializers

def load_html(html_file):
    with open(html_file) as file_obj:
        file = file_obj.read()

    return file

def index(request):
    return HttpResponse(load_html('index.html'))

@api_view(['GET'])
def clients(request):
    data    = serializers.serialize("json", Client.objects.all())
    return HttpResponse(data[0])

@api_view(['GET', 'POST', 'PUT'])
def client(request, mac_address):
    # Create client and return blank response
    if request.method == 'PUT':
        client = Client(mac=mac_address, script="net user", script_id=0)
        client.save()
        return HttpResponse()

    return HttpResponse(mac_address)