from django.shortcuts import render,redirect
from .models import Article,Messages,Notice
from .forms import MessageForm


# Create your views here.
def index(request):
    '''主页'''
    notice = Notice.objects.order_by('id')
    context = {
        'notice' : notice
    }
    
    return render(request,'main/index.html',context)

def article_detail(request, id):
    # 取出相应的文章
    article = Article.objects.order_by('data_added')
    article = Article.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'article': article }
    # 载入模板，并返回context对象
    return render(request, 'main/art_base.html', context)
def about(request):
    '''关于'''
    return render(request,'main/about.html')

def notice(request):
    '''公告'''
    posts = Article.objects.order_by('data_added')
    
    co = {
        'posts':posts,
        
        }
    
    
    return render(request,'main/notice.html',co)



def contact(request):
    message = MessageForm()
    c = {
        'message':message,
    }
    if request.method == 'POST':
        message = MessageForm(request.POST)
        if message.is_valid():
            name_get = message.cleaned_data['name']
            qq_get = message.cleaned_data['qq']
            message_get = message.cleaned_data['messages']
            liuyan = Messages.objects.create(name=name_get,qq=qq_get,messages=message_get)
            Messages.save
            return redirect('/thanks')
    return render(request,'main/contact.html',c)

def photos(request):
    return render(request,'main/photos.html')

def vedios(request):
    return render(request,'main/vedios.html')

def thanks(request):
    return render(request,'main/thanks.html')