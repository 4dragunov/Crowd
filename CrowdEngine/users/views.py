#  импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

#  функция reverse_lazy позволяет получить URL по параметру "name" функции path()
#  берём, тоже пригодится
from django.urls import reverse_lazy
from challenge.forms import Answer, Challenge

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm
from django.shortcuts import render

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login") #  где login — это параметр "name" в path()
    template_name = "signup.html"
#
# def answer_author_list(request):
#     answers = Answer.objects.filter(author=a)

