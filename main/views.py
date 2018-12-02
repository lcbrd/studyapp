from django.shortcuts import render
from main.models import User
from django.http import HttpResponseRedirect
# Create your views here.


def is_login_func(func):
    
    def r_func(request):
        if request.COOKIES.get('una') == None:
            return HttpResponseRedirect('/login/')
        else:
            return func(request)
    return r_func

def loginhtml(request):
    global is_login
    if request.method == 'POST':
        msg = '登陆错误，请重试'
        post_dict = request.POST.dict()
        getuser= User.objects.filter(user_name=post_dict['uname'])
        if(len(getuser)==1):
            if(post_dict['pwd'] == getuser[0].password):
                respone = HttpResponseRedirect('/overview/')
                respone.set_cookie('una',getuser[0].user_name)
                return respone
            else:
                return render(request,'login.html',{'msg':'登陆错误，请重试'})
        else:
            return render(request,'login.html',{'msg':'登陆错误，请重试'})
    return render(request,'login.html',{'msg':''})

@is_login_func
def overview(request):

    return render(request,'overview.html')


