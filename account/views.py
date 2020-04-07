from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.fields['username'].widget.attrs = {'class': 'form-control'}
        form.fields['password1'].widget.attrs = {'class': 'form-control'}
        form.fields['password2'].widget.attrs = {'class': 'form-control'}
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'account/singup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('login')
