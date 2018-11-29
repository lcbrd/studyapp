from django.shortcuts import render
from main.models import User
# Create your views here.
def loginhtml(request):
    if request.method == 'POST':
        u = User.objects.get(user_name=request.POST.
        print(u.password)
    return render(request,'login.html',{'title':123})