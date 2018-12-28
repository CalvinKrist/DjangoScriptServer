from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from rest_framework.decorators import api_view
from django.core import serializers
import json
from django.forms.models import model_to_dict
from django.views.generic import ListView

class ClientListView(ListView):
    model = Client
