from django.shortcuts import render,redirect
from .forms import RegisterForm,changeUserdata
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash


# Create your views here.

def home(request):
    return render(request,'home.html')


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account created successfully !')
                # messages.warning(request,'Account created successfully !')
                # messages.info(request,'Account created successfully !')
                form.save(commit=True)
                # form.save(commit=False)
                # print(form.cleaned_data)
        else:
            form=RegisterForm()
        return render(request, 'signup.html',{'form':form})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name,password=userpass)
                # chk krtechi user database a ache ki na ! 
                
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form =AuthenticationForm()

        return render(request,'./login.html',{'form':form})
    else:
        return redirect('profile')


def profile(request):
    # if request.user.is_authenticated: 
    #     # by this code, annonymas user failed to get access 🐸
    #     return render(request,'profile.html',{'user':request.user})
    # else:
    #     return redirect('login')
    if request.user.is_authenticated:
        if request.method=="POST":
            form=changeUserdata(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Account Updated successfully !')
                form.save(commit=True)
        else:
             form = changeUserdata(instance=request.user)  # Pass the instance here
        return render(request, 'profile.html',{'form':form})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')


def pass_change(request):

    if  request.user.is_authenticated:
        if request.method=='POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)# password update krbe...! 
                # update_session_auth_hash(request,form.cleaned_data['user'])# password update krbe...! 
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')


def pass_change2(request):

    if  request.user.is_authenticated:
        if request.method=='POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)# password update krbe...! 
                # update_session_auth_hash(request,form.cleaned_data['user'])# password update krbe...! however it showing problem..! 
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')

   

# def change_user_data(request):
    

