from django.shortcuts import render

# Create your views here.
def home_posts(request):
    return render(request, 'index.html')