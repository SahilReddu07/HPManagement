from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def hhome(request):
    return render(request,'hhome.html')
def dhome(request):
    return render(request,'dhome.html')
def refferal(request):
    return render(request,'refferal.html')
