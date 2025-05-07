from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import DistractionBlock

# View to get distraction blocking settings
def get_blocking_settings(request):
    if request.method == 'GET':
        settings = DistractionBlock.objects.all()
        return JsonResponse({'settings': list(settings.values())})

# View to update distraction blocking settings
def update_blocking_settings(request):
    if request.method == 'POST':
        data = request.POST
        # Logic to update distraction blocking settings
        # Example: Assuming `DistractionBlock` has fields like `name` and `status`
        for key, value in data.items():
            DistractionBlock.objects.update_or_create(
                name=key,
                defaults={'status': value}
            )
        return JsonResponse({'status': 'success'})

# Profile overview view
@login_required
def profile_overview(request):
    return render(request, 'profile_overview.html', {'user': request.user})

# Profile edit view
@login_required
def edit_profile(request):
    return render(request, 'profile_update.html', {'user': request.user})

# Profile update view
@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        # Update user fields
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        # Update profile fields (assuming a related Profile model exists)
        profile = user.profile  # Assuming `Profile` is a OneToOneField related to User
        profile.phone_number = request.POST.get('phone_number')
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        # Save changes
        user.save()
        profile.save()

        return redirect('profile_overview')
    return redirect('edit_profile')
