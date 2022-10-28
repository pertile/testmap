from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.models import UserProfile
from base.serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        print(profile_form.is_valid())
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='index')
        else:
            print(profile_form.errors)
            # for i in profile_form.errors.items:
            #     print(i.value)
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'registration/profile.html', {'profile_form': profile_form})

@api_view(['GET'])
def listUsers(request):
    profiles = UserProfile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)