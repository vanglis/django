#!/usr/bin/env python
#-*-coding:utf-8-*-

from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import loader,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt
import logging

@csrf_exempt
def sendemail(request):
 #t= loader.get_template('content.html')
 subject = request.POST['subject']
 logging.debug(subject)
 message = request.POST['message']
 logging.debug(message)
 recipient1 = request.POST['recipient1']
 recipient2 = request.POST['recipient2']
 recipient3 = request.POST['recipient3']
 logging.debug(recipient1+recipient2+recipient3)
 from_email = 'vanglis@163.com'
 #send_mail(u'邮件标题', u'邮件内容', 'vanglis@163.com',['xiaohanfei539@pingan.com.cn'], fail_silently=False)
 recipient_list = [recipient1, recipient2, recipient3]
 send_mail(subject, message, from_email, recipient_list, fail_silently=False)
 return HttpResponse('send success')
