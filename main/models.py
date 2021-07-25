from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Tag(models.Model):
    tags = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = '标签'
    def __str__(self):
        return self.tags

class Notice(models.Model):
    notices = models.TextField(max_length=50)
    urls = models.TextField(("图片链接"))
    class Meta:
        verbose_name_plural = '首页图片'
    def __str__(self):
        return self.notices

class Article(models.Model):
    '''公告模型'''
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,verbose_name='标题')
    ftitle = models.CharField(max_length=50,blank=True,null=True,verbose_name='副标题')
    content = RichTextUploadingField(verbose_name='内容')
    data_added = models.DateField(verbose_name='发布时间')
    photos = models.ImageField(verbose_name='头图')
    
    

    class Meta:
        verbose_name_plural = '公告'
        ordering = ['data_added']

    def __str__(self):
        return f'{self.content[:50]}...'

class Comments(models.Model):
    '''评论模型'''
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    text = RichTextUploadingField(verbose_name="评论")
    data_added = models.DateField(verbose_name='发布时间')

    class Meta:
        verbose_name_plural = '评论'

class Messages(models.Model):
    name = models.CharField(max_length=10,verbose_name='昵称',blank=True,null=True)
    qq = models.CharField(max_length=12,verbose_name='QQ',blank=True,null=True)
    messages = RichTextUploadingField(verbose_name='留言',blank=True,null=True)
    class Meta:
        verbose_name_plural = '留言'


    



    