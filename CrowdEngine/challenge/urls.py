from django.urls import path
from .views import *


urlpatterns = [
    path('', challenges_list, name='challenges_list_url'),
    path('challenge/create/', ChallengeCreate.as_view(), name='challenge_create_url'),
    path('challenge/<str:slug>', challenge_detail, name='challenge_detail_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/', category_detail, name='category_detail_url'),


]