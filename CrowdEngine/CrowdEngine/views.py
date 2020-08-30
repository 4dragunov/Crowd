from django.shortcuts import redirect, render
from challenge.models import Challenge, Answer, User
from django.db.models import Avg, Max, Min, Sum
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


User = get_user_model()

def redirect_crowd(request):
    data = 123
    challenge_count = Challenge.objects.all().count()
    answers_count = Answer.objects.all().count()
    #users_count = User.count()
    # users_count = Challenge.objects.filter(au).count()
    total_users = User.objects.aggregate(total_users=Count('id'))['total_users'],
    challenge_users = Challenge.objects.all().aggregate(challenge_users = Count('challenge_author'))['challenge_users'],
    answer_users = Answer.objects.all().aggregate(answer_users = Count('author'))['answer_users'],
    prize_amount = Challenge.objects.all().aggregate(prize_amount = Sum('prize'))['prize_amount']
#
    return render(request, 'main.html', context={'data': data, 'challenge_count' : challenge_count,
                                                 'answers_count' : answers_count, 'prize_amount':prize_amount,
                                                 'total_users': total_users, 'challenge_users' :challenge_users})


def about_us(request):
    data = 123
    return render(request, "about.html")