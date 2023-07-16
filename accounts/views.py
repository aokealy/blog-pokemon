from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register(request):
     if request.method == 'POST':
          form = RegisterForm(request.POST)
          if form.is_valid():
            form.save()
            return redirect('login')
     else:
          form = RegisterForm()  
             
     context = {
        'form': form,
    }
     return render(request, 'accounts/register.html', context)

def account(request):
     return render(request, 'accounts/account.html')     
