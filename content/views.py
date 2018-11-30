from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from rest_framework.decorators import api_view
from django.core import serializers
import json
from django.forms.models import model_to_dict

def load_html(html_file):
    with open(html_file) as file_obj:
        file = file_obj.read()

    return file

def index(request):
    return HttpResponse(load_html('index.html'))

@api_view(['GET'])
def clients(request):
    data = Client.objects.values()
    data = [entry for entry in data]

    response = {"clients" : data}

    return HttpResponse(json.dumps(response))

@api_view(['GET', 'POST', 'PUT'])
def client(request, mac_address):
    # Create client and return blank response
    if request.method == 'PUT':
        client = Client(mac=mac_address, script="net user", script_id=0)
        client.save()
        return HttpResponse()

    if request.method == 'GET':
        # Get all Client objects with mac=mac_address. Include only 'script' and 'script_id' variables
        filter_results = list(Client.objects.filter(mac=mac_address).values('script', 'script_id'))

        if len(filter_results):
            # Turn the list of Client objects into a dict
            results_dict = json.loads(json.dumps({"clients":filter_results}))

            # Get and return first result as a string
            first_result = results_dict['clients'][0]
            return HttpResponse(json.dumps(first_result))
        else:
            return HttpResponse()

    return HttpResponse(mac_address)