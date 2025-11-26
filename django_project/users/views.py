'''
* added UserUpdateForm and ProfileUpdateForm to the import from .forms
    new forms are just created from forms.py.
'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account is ready! 🎉, now Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required #django signal
def profile(request):
    # creating instances
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    # Pass to the template, so the form can be accessed
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)