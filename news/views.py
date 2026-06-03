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

def get_new(request, pk=None):
    new = News.objects.get(pk=pk)
    return render(request, 'news/detail.html',{'new':new})

def update_new(request, pk):
    new = News.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title',new.title)
        content = request.POST.get('content',new.content)
        if title and content:
            new.title = title
            new.content = content
            new.save()
            return redirect('news')
    else:
        return render(request,'news/update.html',{'new':new})

def delete_new(request, pk):
    new = News.objects.get(pk=pk)
    if request.method == 'POST':
        new.delete()
        return redirect('news')
    else:
        return render(request, 'news/delete.html',{'new':new})