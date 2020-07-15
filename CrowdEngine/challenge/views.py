from django.shortcuts import render, redirect
from .models import Challenge, Category
from django.views.generic import View
from .forms import CategoryForm, ChallengeForm


def challenges_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenge/index.html', context={'challenges': challenges})


def challenge_detail(request, slug):
    challenge = Challenge.objects.get(slug__iexact=slug)
    return render(request, 'challenge/challenge_detail.html', context={'challenge': challenge})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'challenge/categories_list.html', context={'categories': categories})


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    return render(request, 'challenge/categories_detail.html', context={'category': category})


class CategoryCreate(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'challenge/category_create.html', context={'form' : form})

    def post(self,request):
        bound_form = CategoryForm(request.POST)

        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        return render(request, 'challenge/category_create.html', context={'form' : bound_form})

class ChallengeCreate(View):
    def get(self, request):
        form = ChallengeForm()
        return render(request, 'challenge/challenge_create.html', context={'form' : form})

    def post(self,request):
        bound_form = ChallengeForm(request.POST)

        if bound_form.is_valid():
            new_challenge = bound_form.save()
            return redirect(new_challenge)
        return render(request, 'challenge/challenge_create.html', context={'form': bound_form})