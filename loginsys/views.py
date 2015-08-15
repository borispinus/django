from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/note/all')
        else:
            args['login_error'] = 'User not found'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html',args)


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')

def register(request):
    args={}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save();
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'],password = new_user_form.cleaned_data['password2'])
            auth.login(request,new_user)
            return redirect('/note/all')
        else:
            args['form'] = new_user_form
            return render_to_response('login.html', args)
    return render_to_response('register.html',args)


