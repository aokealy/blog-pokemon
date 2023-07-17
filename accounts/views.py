from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserUpdateForm, AccountUpdateForm

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
        account_form = AccountUpdateForm(request.POST or None, request.FILES or None, instance=request.user.accountmodel)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('account')
      else:
        user_form = UserUpdateForm(instance=request.user)
        account_form = AccountUpdateForm(instance=request.user.accountmodel)
      context = {
        'user_form':user_form,
        'account_form':account_form
    }

      return render(request, 'accounts/account.html', context)    
