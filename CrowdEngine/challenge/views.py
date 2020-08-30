from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Challenge, Category, Answer, AnswerLike, Comment
from django.views.generic import View
from .forms import CategoryForm, ChallengeForm, AnswerForm, CommentForm
from .utils import ObjectDetailMixin, ObjectUpdateMixin, ObjectDeleteMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.utils import timezone

User = get_user_model()

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
            new_answer.author = request.user
            new_answer.challenge = challenge
            new_answer.save()

            return redirect('answers_list_url', challenge.slug)
        return render(request, 'challenge/answer_create.html', context={'form': form,
                                                                        'challenge':challenge})
def answerEdit(request, slug, pk):
    is_form_edit = True
    answer = get_object_or_404(Answer, challenge__slug=slug,
                             pk__iexact=pk)
    challenge = get_object_or_404(Challenge, slug__iexact=slug)
    if answer.author == request.user:
        form = AnswerForm(request.POST or None,
                        files=request.FILES or None, instance=answer)
        if form.is_valid():
            post = form.save()
            return redirect('answer_detail_url', slug, pk)
        form = AnswerForm(instance=answer)

        return render(request, "challenge/answer_create.html",
                      context={'form': form,
                               "is_form_edit": is_form_edit,
                               'challenge': challenge})
    else:
        return redirect('main_url')

def answers_list(request, slug):
    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]
    top_challenges = Challenge.objects.order_by("answers")[:3]
    challenge = get_object_or_404(Challenge,slug__iexact=slug)
    answers = Answer.objects.filter(challenge__slug=slug).annotate(cnt=(
        Count('likes'))).order_by('-cnt')
    paginator = Paginator(answers,
                          4)  # показывать по 10 записей на странице.
    page_number = request.GET.get(
        'page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(
        page_number)  # получить записи с нужным смещением


    return render(request, 'challenge/answers_list.html', context={'answers': answers,
                                                                   'top_categories':top_categories,
                                                                   'top_challenges':top_challenges,
                                                                   'challenge':challenge,
                                                                   'page':page,
                                                                   'paginator':paginator})
def add_comment(request, slug, pk):
    answer = get_object_or_404(Answer, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        new_comment = form.save(commit=False)
        form.instance.author = request.user
        form.instance.answer = answer
        new_comment.save()
        return redirect('answer_detail_url', slug, pk)
    return render(request, "challenge/answer_detail.html", context={"form": form})

def del_comment(request, slug, pk, pk_comment):
    answer = get_object_or_404(Answer, pk=pk)
    comment = answer.comments.filter(pk=pk_comment)
    comment.delete()
    return redirect('answer_detail_url', slug, pk)

@login_required
def answerAddLike(request, slug, pk, url):

    answer = get_object_or_404(Answer, pk=pk)
    challenge = get_object_or_404(Challenge, slug__iexact=slug)
    AnswerLike.objects.get_or_create(user=request.user, answer=answer,
                                     challenge=challenge)
    return redirect(url, slug=slug)


@login_required
def answerDelLike(request, slug, pk, url):
    answer = get_object_or_404(Answer, pk=pk)
    challenge = get_object_or_404(Challenge, slug__iexact=slug)
    answer_like = AnswerLike.objects.get(user=request.user, answer=answer, challenge=challenge)
    answer_like.delete()
    return redirect(url, slug=slug)


def challenges_list(request):
    user = request.user
    challenges = Challenge.objects.all().order_by('-date_pub')
    paginator = Paginator(challenges,
                          4)  # показывать по 10 записей на странице.
    page_number = request.GET.get(
        'page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(
        page_number)  # получить записи с нужным смещением
    top_challenges = Challenge.objects.order_by("answers")[:3]
    #top_categories = Challenge.objects.all().annotate(cnt=Count('categories'))
    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]
    date = timezone.now().date()
    return render(request, 'challenge/challenge_list.html',
                  context={'challenges': challenges,
                  'top_challenges' : top_challenges,
                   'top_categories' : top_categories,
                    'page': page, 'paginator': paginator,
                           'date':date,
                           'user':user
                           })

def challenge_detail(request, slug):

    challenge = get_object_or_404(Challenge, slug__iexact=slug)
    top_challenges = Challenge.objects.order_by("answers")[:3]
    answers = Answer.objects.filter(challenge__slug=slug).annotate(cnt=(
        Count('likes'))).order_by('-cnt')[:3]
    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]

    return render(request, 'challenge/challenge_detail.html',
                  context={'challenge': challenge,
                  'top_challenges' : top_challenges,
                   'top_categories' : top_categories,
                    'answers': answers,

                           })


def answer_detail(request, slug, pk):
    answer = get_object_or_404(Answer, pk=pk)
    challenge = get_object_or_404(Challenge, slug__iexact=slug)
    top_challenges = Challenge.objects.order_by("answers")[:2]
    top_categories = Category.objects.all().annotate(cnt=Count(
        'challenges')).order_by('-cnt')[:3]
    form = CommentForm()
    items = answer.comments.all().order_by("-created")

    return render(request, 'challenge/answer_detail.html',
                  context={'answer':answer,
                           'challenge':challenge,
                           'top_challenges': top_challenges,
                           'top_categories': top_categories,
                           'form':form,
                           'items':items
                           })

def categories_list(request):
    categories = Category.objects.all().annotate(cnt=Count(
        'challenges')).order_by('-cnt')
    top_challenges = Challenge.objects.order_by("answers")[:3]
    # top_categories = Challenge.objects.all().annotate(cnt=Count('categories'))
    top_categories = Category.objects.all().annotate(cnt=Count('challenges')).order_by('-cnt')[:4]
    return render(request, 'challenge/categories_list.html',
                  context={'categories': categories,
                           'top_challenges': top_challenges,
                           'top_categories': top_categories,

                           })

def categoryDetail(request, slug):
    category = get_object_or_404(Category, slug__iexact=slug)
    challenges = category.challenges.all()
    paginator = Paginator(challenges,
                          4)  # показывать по 10 записей на странице.
    page_number = request.GET.get(
        'page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(
        page_number)  # получить записи с нужным смещением
    top_challenges = Challenge.objects.order_by("answers")[:3]
    # top_categories = Challenge.objects.all().annotate(cnt=Count('categories'))
    top_categories = Category.objects.all().annotate(
        cnt=Count('challenges')).order_by('-cnt')[:4]
    return render(request, 'challenge/categories_detail.html',
                  context={'top_challenges': top_challenges,
                           'top_categories': top_categories,
                           'page': page, 'paginator': paginator,
                           'category':category})


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
            new_challenge = bound_form.save(commit=False)
            bound_form.instance.challenge_author = request.user
            new_challenge.save()
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