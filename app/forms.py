from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class webpageForm(forms.ModelForm):
    class Meta:
        model=WebPage
        fields='__all__'
        #fields=['topic_name','name','url']
        #exclude=['email']
        widgets={'url':forms.PasswordInput}
        labels={'name':'username','topic_name':'TopicName'}
        help_texts={'email':'malli@gmail.com'}

class accessForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
