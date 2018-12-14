from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess,os

# Create your views here.
@csrf_exempt
def flush(request):
    dir = '/data/appsystem/apps'
    os.chdir(dir)
    cmd = 'ls'
    output = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    data = output.stdout.readlines()
    return HttpResponse(data)
