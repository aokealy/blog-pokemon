from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserUpdateForm

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
      if request.method == 'POST':
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('account')
      else:
        user_form = UserUpdateForm(instance=request.user)
      context = {
        'user_form':user_form,
        
    }

      return render(request, 'accounts/account.html', context)    



    
