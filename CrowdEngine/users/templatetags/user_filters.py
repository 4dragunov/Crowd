from django import template
# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр

register = template.Library()


@register.filter
def addclass(field, css):
        return field.as_widget(attrs={"class": css})

# синтаксис @register... , под которой описан класс addclass() -
# это применение "декораторов", функций, обрабатывающих функции
# мы скоро про них расскажем. Не бойтесь соб@к


        # request = context['request']
        # try:
        #         answer_likes = AnswerLike.objects.get(user=request.user,
        #                                               answer=answer_id)

