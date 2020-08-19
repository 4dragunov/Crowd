from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', challenges_list, name='challenges_list_url'),
    path('challenge/create/', login_required(ChallengeCreate.as_view()), name='challenge_create_url'),
    path('challenge/<str:slug>/update/', login_required(ChallengeUpdate.as_view()), name='challenge_update_url'),
    path('challenge/<str:slug>/delete/', login_required(ChallengeDelete.as_view()), name='challenge_delete_url'),
    path('challenge/<str:slug>', challenge_detail, name='challenge_detail_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/create/', login_required(CategoryCreate.as_view()), name='category_create_url'),
    path('category/<str:slug>/update/', login_required(CategoryUpdate.as_view()), name='category_update_url'),
    path('category/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('category/<str:slug>/delete/', login_required(CategoryDelete.as_view()), name='category_delete_url'),
    path('challenge/<str:slug>/answers', login_required(answers_list), name='answers_list_url'),
    path('challenge/<str:slug>/answer_create', login_required(AnswerCreate.as_view()), name='answer_create_url'),

]