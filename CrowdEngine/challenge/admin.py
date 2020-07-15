from django.contrib import admin

from .models import Challenge, Category


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "body", "date_pub",)
    #search_fields = ("text",)
    #list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "challenges")
    #search_fields = ("title",)
    #list_filter = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Challenge, ChallengeAdmin)
