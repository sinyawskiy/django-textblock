# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.template import Context, Template
from statictext.models import Statictext


register = template.Library()

@register.simple_tag(takes_context=True)
def render_statictext(context, key):
    """
    Returns static text from db for the required key
    """
    try:
        statictext = Statictext.objects.get(key=key)
    except Statictext.DoesNotExist:
        if settings.DEBUG:
            raise
        else:
            return u''
    else:
        return Template(statictext.text).render(Context(context))