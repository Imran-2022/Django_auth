from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def home(request):
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
    return render(request, 'home.html',{'form':form})
