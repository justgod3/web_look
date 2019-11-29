import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def angul(request):
    '''

    :param request:
    :return:
    '''
    return  render(request,'index/an_test.html')

def an_test(request):
    '''

    :param request:
    :return:
    '''
    data = json.loads(request.body)
    # data = request.body
    print(data)
    return  HttpResponse("ok")