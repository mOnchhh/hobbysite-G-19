from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

@login_required
def update_profile(request):

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()
        
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Error updating your profile.')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'accounts/update_profile.html', {'form': form})


