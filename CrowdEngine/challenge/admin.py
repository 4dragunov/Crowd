from django.contrib import admin

from .models import Challenge, Category, Answer


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "body", "date_pub",)
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
    list_display = ('title', 'challenge',)


admin.site.register(Challenge, ChallengeAdmin)
