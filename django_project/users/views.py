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
    '''
        Populating the forms with the current user info
        instance = request.user  --> gets the current user
        instance = request.user.profile --> gets the current user's profile.

        Put in a check to see if it is a POST route or not and also see if the forms are valid
    '''
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile)
        ''' check if both forms are valid '''
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            ''' display success message: giving feedback to user '''
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  # Post/Redirect/Get pattern
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    # Pass to the template, so the form can be accessed
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)