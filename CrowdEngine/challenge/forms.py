from django import forms
from .models import Category, Challenge, Answer, Comment
from django.core.exceptions import ValidationError
from time import time

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title', 'body']

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),

    }
        labels = {
            "title": "Основная идея",
            "body": "Подробное описание"
        }
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'slug']    #'__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Адрес не может быть "Create"')


        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Адрес уже существует. Он должен быть уникальным. У нас есть адрес "{}"'.format(new_slug))

        return new_slug


class ChallengeForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ['title', 'body', 'categories', 'prize', 'date_remaining', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'prize': forms.TextInput(attrs={'class': 'form-control'}),
            'date_remaining': forms.SelectDateWidget(attrs={'class': 'form-control'}),

        }
        labels = {
            "title": "Тема",
            "body": "Текст",
            "categories": "Категория проблемы",
            'prize':"Призовой фонд",
            'date_remaining':"Дата завершения",
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Адрес не может быть "Create"')

        return new_slug

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

        widgets = {
            'text': forms.Textarea(),
        }

        labels = {

            "text": "Текст"
        }


