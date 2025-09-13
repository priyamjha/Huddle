from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Huddle
from .forms import ItemForm
from .utilities import notify_users


def index(request):
    return render(request, 'huddle/index.html')

def huddle(request):
    # Get Information
    key = request.GET.get('key', '')
    user = request.GET.get('user', '')
    huddle, created = Huddle.objects.get_or_create(key=key)
    
    if created:
        messages.success(request, 'New huddle created.')
        
    # Form submitted
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.huddle = huddle
            item.save()
            
            notify_users(huddle, item.user)
            
            messages.success(request, 'Message Sent!')
            return redirect(f'/huddle?key={key}&user={user}')
        else:
            messages.error(request, 'There was an error with your submission.')
    
    # Render
    return render(request, 'huddle/huddle.html', {
        'user': user,
        'huddle': huddle
        })