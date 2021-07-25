from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 


app_name = 'main'
urlpatterns = [
    # 主页
    path('',views.index,name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('about',views.about,name='about'),
    path('notice',views.notice,name='notice'),
    path('thanks',views.thanks,name='thanks'),
    path('contact',views.contact,name="contact"),
    path('photos',views.photos,name="photos"),
    path('vedios',views.vedios,name="vedios"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)