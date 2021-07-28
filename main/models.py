from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

# 标签
class Tag(models.Model):
    tags = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = '标签'
    def __str__(self):
        return self.tags


# 首页大图
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


class Messages(models.Model):
    username = models.CharField(max_length=10,verbose_name='昵称',blank=True,null=True)
    qq = models.CharField(max_length=12,verbose_name='QQ',blank=True,null=True)
    content = RichTextUploadingField(verbose_name='留言',blank=True,null=True)
    publish=models.DateTimeField()
    
    class Meta:
        verbose_name_plural = '留言'

    def __str__(self) -> str:
        tpl = '<Message:[username={username}, content={content}, publish={publish}]>'
        return tpl.format(username=self.username, content=self.content, publish=self.publish)


    



    