from django.contrib import admin

from .models import Challenge, Category, Answer, AnswerLike, Comment



class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "body", "date_pub", "challenge_author", "image")
    #search_fields = ("text",)
    #list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "challenges")
    #search_fields = ("title",)
    #list_filter = ("title",)
    empty_value_display = "-пусто-"

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'challenge', 'author', 'pk')

@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'answer', 'challenge')

# @admin.register(Answer_like)
# class LikeAnswerAdmin(admin.ModelAdmin):
#     list_display = ('answer', 'liked_by', 'like', 'created')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('answer', 'author', 'text')

admin.site.register(Challenge, ChallengeAdmin)

