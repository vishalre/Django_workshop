from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(requests):
    # field1=requests.GET['field1']
    field2=requests.GET['field2']
    operation=requests.GET['optradio']
    result=0
    if operation == '+':
        result= int(field1) + int(field2)
    elif operation == '-':
        result= int(field1) - int(field2)
    elif operation == '*':
        result = int(field1) * int( field2)
    else:
        result = int(field1) / int(field2)
    # return HttpResponse('hello')
    return render(requests, 'calc/calculator.html', {'result':result})

def homepage(requests):

    return render(requests, 'calc/home.html')
