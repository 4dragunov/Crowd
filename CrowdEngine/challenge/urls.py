from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', challenges_list, name='challenges_list_url'),
    path('challenge/create/', login_required(ChallengeCreate.as_view()), name='challenge_create_url'),
    path('challenge/<str:slug>/update/', login_required(ChallengeUpdate.as_view()), name='challenge_update_url'),
    path('challenge/<str:slug>/delete/', login_required(ChallengeDelete.as_view()), name='challenge_delete_url'),
    path('challenge/<str:slug>', login_required(challenge_detail),
                                                name='challenge_detail_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/create/', login_required(CategoryCreate.as_view()), name='category_create_url'),
    path('category/<str:slug>/update/', login_required(CategoryUpdate.as_view()), name='category_update_url'),
    path('category/<str:slug>/', categoryDetail, name='category_detail_url'),
    path('category/<str:slug>/delete/', login_required(CategoryDelete.as_view()), name='category_delete_url'),
    path('challenge/<str:slug>/answers', login_required(answers_list), name='answers_list_url'),
    path('challenge/<str:slug>/answer_create', login_required(AnswerCreate.as_view()), name='answer_create_url'),
    path('challenge/<str:slug>/answer/<int:pk>/edit/', login_required(answerEdit),
          name='answer_edit_url'),
    path('challenge/<str:slug>/answers/<int:pk>/like/<str:url>', answerAddLike,
          name='answer_add_like_url'),
    path('challenge/<str:slug>/answers/<int:pk>/dislike/<str:url>', answerDelLike,
          name='answer_del_like_url'),
    path('challenge/<str:slug>/answer/<int:pk>/detail', login_required(
        answer_detail), name='answer_detail_url'),
    path("challenge/<str:slug>/answer/<int:pk>/comment", add_comment, name="add_comment"),
    path("challenge/<str:slug>/answer/<int:pk>/comment/<int:pk_comment>/delete", del_comment,
         name="del_comment"),
    #
    # path("<str:username>/follow/", views.profile_follow,
    #      name="profile_follow"),
    # path("<str:username>/unfollow/", views.profile_unfollow,
    #      name="profile_unfollow"),

]