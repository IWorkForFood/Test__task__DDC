from django.contrib.auth.models import User
from News.models import NewsModel
from News.forms import NewsModelForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from NewsProject import tasks
from django.http import HttpResponse
from NewsProject.tasks import send_news_list

def authorsListNews(request):

    news = NewsModel.objects.filter(author=request.user)

    context = {'news': news}
    print(context)

    return render(request, 'News/news_list.html', context=context)


def createNews(request):
    form = NewsModelForm(initial={'publication_date':timezone.now(), 'author': request.user})

    if request.method == 'POST':      

        form = NewsModelForm(request.POST, request.FILES, initial={'publication_date':timezone.now(), 'author': request.user})

        if form.is_valid():
            news = form.save(commit=False)
            # Устанавливаем поле author
            news.author = request.user  # Устанавливаем текущего пользователя как автора
            news.save()
        
            return redirect('/authors_news')
        print(form.errors)
    
    context = {'edit_form':form}
    return render(request, 'News/edit_news.html', context=context)
        

def updateNews(request, pk):

	item = NewsModel.objects.get(id=pk)
	form = NewsModelForm(instance=item)

	if request.method == 'POST':
		form = NewsModelForm(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('/authors_news')

	context = {'edit_form':form}
	return render(request, 'News/edit_news.html', context)

def deleteNews(request, pk):
    item = NewsModel.objects.get(id=pk)
    item.delete()
    return redirect('/authors_news')

def home_view(request):
    whole_news = NewsModel.objects.all()
    context={'news':whole_news}
    return render(request, 'News/home.html', context=context)

def read_news(request, pk):
    item = NewsModel.objects.get(pk=pk)
    context = {'item':item}
    return render(request, 'News/read_news.html', context=context)

def test(request):
    tasks.test_func.delay()
    return HttpResponse('Done')

def send_mail_to_all(request):
    send_news_list.delay()
    return HttpResponse("Sent")