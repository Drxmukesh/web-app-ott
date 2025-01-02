from django.shortcuts import render
from .models import Video

def home(request):
    videos = Video.objects.all()  # Fetch all videos
    context = {
        'videos': videos,
    }
    return render(request, 'videos/home.html', context)

def category(request, category_name):
    videos = Video.objects.filter(category=category_name)  # Filter videos by category
    context = {
        'videos': videos,
        'category_name': category_name,
    }
    return render(request, 'videos/category.html', context)