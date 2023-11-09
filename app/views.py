from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')
def secound(request):
    return render(request,'secound.html')
def third(request):
    return render(request,'third.html')
def fourth(request):
    return render(request,'fourth.html')