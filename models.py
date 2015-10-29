# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
try:
    from tinymce.models import HTMLField
except ImportError:
    from django.models import TextField as HTMLField


class Statictext(models.Model):
    """
    Static text used it templates
    """
    key = models.CharField(_(u'key'), max_length=70, unique=True,
                           help_text=_(u'This value is used in the code. Do not touch it!'))
    text = HTMLField(_(u'text'), blank=True, null=True)
    comment = models.CharField(_(u'comment'), max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.comment)

    class Meta:
        verbose_name = _(u'static text')
        verbose_name_plural = _(u'static texts')
