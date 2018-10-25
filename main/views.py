from django.shortcuts import render

# Create your views here.
def loginhtml(request):
    return render(request,'login.html')