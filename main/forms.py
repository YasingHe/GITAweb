from django import forms
from .models import Comments,Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'
        lables = {
            'name' : '昵称',
            'qq' : 'QQ',
            'messages' : '留言',
        }
        widgets = {
            "name" : forms.TextInput(attrs={
                'class':'field half',
                'placeholder': '请输入昵称'
            }),
            "qq" : forms.TextInput(attrs={
                'class':'field half',
                'placeholder': '请输入QQ'
            }),
            "messages" : forms.TextInput(attrs={
                'class':'field',
                'placeholder': '请输入留言'
            })
        }
