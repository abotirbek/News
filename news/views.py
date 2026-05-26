from django.shortcuts import render, redirect
from .models import News
# Create your views here.

def get_news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/list.html',context)

def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            News.objects.create(
                title = title,
                content = content
            )
            return redirect('create')
    else:
        return render(request, 'news/create.html')