from django import template
from ..models import AnswerLike
register = template.Library()


@register.simple_tag(takes_context=True)
def is_liked(context, answer_id):
        answer_likes = False
        request = context['request']
        if AnswerLike.objects.filter(user=request.user,
                             answer=answer_id).exists():
                answer_likes = True

        return (answer_likes)

@register.simple_tag()
def count_likes(answer_id):
        return AnswerLike.objects.filter(answer=answer_id).count()