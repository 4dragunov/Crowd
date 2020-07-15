from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge, Category
from django.views.generic import View
from .forms import CategoryForm, ChallengeForm
from .utils import ObjectDetailMixin

def challenges_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenge/index.html', context={'challenges': challenges})


# def challenge_detail(request, slug):
#     challenge = Challenge.objects.get(slug__iexact=slug)
#     return render(request, 'challenge/challenge_detail.html', context={'challenge': challenge})
# и тогда в urls обработчик challenge_detail

class ChallengeDetail(ObjectDetailMixin, View):
    model = Challenge
    template = 'challenge/challenge_detail.html'

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'challenge/categories_list.html', context={'categories': categories})


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'challenge/categories_detail.html'
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