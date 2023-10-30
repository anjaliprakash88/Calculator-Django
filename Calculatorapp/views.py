from django.shortcuts import render
from django.http import HttpResponse


def calculator(request):
    return render(request, 'calculator.html')


def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        myDict = {
            "q": q,
            "ans": ans,
            "error": False
        }
        return render(request, 'calculator.html', context=myDict)
    except:
        myDict = {
            "error": True,
        }
        return render(request, 'calculator.html', context=myDict)
