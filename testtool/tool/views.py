from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def pdf(request):
    fp = open('/data/httpd/gametest/testtool/tool/cs.htm')
    t = template.Template(fp.read())
    t= loader.get_template('/data/httpd/gametest/testtool/tool/cs.htm')
    fp.close()
    return HttpResponse(t)



    