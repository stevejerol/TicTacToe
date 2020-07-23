from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.
def ticview(request):
    return render(request, 'index.html')