from django.urls import path
from .views import *


urlpatterns = [
    path('', challenges_list, name='challenges_list_url'),

    path('challenge/create/', ChallengeCreate.as_view(), name='challenge_create_url'),
    path('challenge/<str:slug>/update/', ChallengeUpdate.as_view(), name='challenge_update_url'),
    path('challenge/<str:slug>/delete/', ChallengeDelete.as_view(), name='challenge_delete_url'),
    path('challenge/<str:slug>', ChallengeDetail.as_view(), name='challenge_detail_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url'),
    path('challenge/<str:slug>/answers', answers_list, name='answers_list_url'),
    path('challenge/<str:slug>/answer_create', AnswerCreate.as_view(), name='answer_create_url'),
]