from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.

def Home(request):
    page = "<html><head><title>test page</title></head><body><h1>Hello World</h1></html>"
    return HttpResponse(page) 

def Other(request):
    return render(request, "otherPage.html", {"title": "Other Page", "message": "Hello World!"})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})