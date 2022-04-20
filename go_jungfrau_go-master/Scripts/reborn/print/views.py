from django.shortcuts import render


# Create your views here.

def helloword(request):
    return render(request,'helloword.html')

def navi(request):
    return render(request,'navi.html')

def marker(request):
    return render(request,'marker.html')

