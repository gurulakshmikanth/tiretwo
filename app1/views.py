from django.shortcuts import render

# Create your views here.
def login(request):
    
    d={'name':'kanth','age':22}
    return render(request,'login.html',context=d)