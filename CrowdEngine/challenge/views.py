from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Challenge, Category, Answer
from django.views.generic import View
from .forms import CategoryForm, ChallengeForm, AnswerForm
from .utils import ObjectDetailMixin, ObjectUpdateMixin, ObjectDeleteMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

class AnswerCreate(View):

    def get(self, request, slug):
        challenge = Challenge.objects.get(slug__iexact=slug)
        form = AnswerForm()
        return render(request, 'challenge/answer_create.html', context={'form': form,
                                                                        'challenge':challenge})


    def post(self, request, slug):
        challenge = Challenge.objects.get(slug__iexact=slug)
        form = AnswerForm(request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.challenge = challenge
            new_answer.save()

            return redirect('answers_list_url', challenge.slug)
        return render(request, 'challenge/answer_create.html', context={'form': form,
                                                                        'challenge':challenge})

def answers_list(request, slug):
    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]
    top_challenges = Challenge.objects.order_by("answers")[:3]

    answers = Answer.objects.filter(challenge__slug=slug)
    return render(request, 'challenge/answers_list.html', context={'answers': answers,
                                                                   'top_categories':top_categories,
                                                                   'top_challenges':top_challenges})


def challenges_list(request):
    challenges = Challenge.objects.all()
    top_challenges = Challenge.objects.order_by("answers")[:3]
    #top_categories = Challenge.objects.all().annotate(cnt=Count('categories'))
    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]
    return render(request, 'challenge/challenge_list.html',
                  context={'challenges': challenges,
                  'top_challenges' : top_challenges,
                   'top_categories' : top_categories})



# class ChallengeDetail(ObjectDetailMixin, View):
#     model = Challenge
#     template = 'challenge/challenge_detail.html'

def challenge_detail(request, slug):
    #answer_like = Answer_like.objects.get(answer=answer)
    #answer_like = Answer_like.objects.filter(answer=slug)
    #print(answer_like)
    challenge = get_object_or_404(Challenge, slug__iexact=slug)
    top_challenges = Challenge.objects.order_by("answers")[:3]
    answers = Answer.objects.filter(challenge__slug=slug).annotate(cnt=(Count('answer_like')-Count('answer_dislike'))).order_by("-cnt")[:5]

   # answer_like = Answer_like.objects.filter(answer__answer=slug)

    #answer_like = Answer_like.objects.all()
   # print(answer_like)
    #answer_like = Answer.objects.filter(challenge__slug=slug)



    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]
    return render(request, 'challenge/challenge_detail.html',
                  context={'challenge': challenge,
                  'top_challenges' : top_challenges,
                   'top_categories' : top_categories,
                           'answers': answers,
                           })




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

class ChallengeUpdate(ObjectUpdateMixin, View):

    model = Challenge
    model_form = ChallengeForm
    template = 'challenge/challenge_update_form.html'

class CategoryUpdate(ObjectUpdateMixin, View):

    model = Category
    model_form = CategoryForm
    template = 'challenge/category_update_form.html'

class CategoryDelete(ObjectDeleteMixin, View):

    model = Category
    template = 'challenge/category_delete_form.html'
    redirect_url = 'categories_list_url'

class ChallengeDelete(ObjectDeleteMixin, View):
    model = Challenge
    template = 'challenge/challenge_delete_form.html'
    redirect_url = 'challenges_list_url'



    # def get(self, request, slug):
    #     category = Category.objects.get(slug__iexact=slug)
    #     bound_form = CategoryForm(instance=category)
    #     return render(request, 'challenge/category_update_form.html', context={'form': bound_form, 'category' : category})
    #
    # def post(self, request, slug):
    #     category = Category.objects.get(slug__iexact=slug)
    #     bound_form = CategoryForm(request.POST,instance=category)
    #
    #     if bound_form.is_valid():
    #         new_category = bound_form.save()
    #         return redirect(new_category)
    #     return render(request, 'challenge/category_update_form.html', context={'form': bound_form, 'category' : category})