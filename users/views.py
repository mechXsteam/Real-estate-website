from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)
        messages.error(request, 'Testing error message')
        if form.is_valid():
            new_user = form.save()
            # Log in the user, and redirect to the home page
            login(request, new_user)
            return redirect('my_app:index')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
