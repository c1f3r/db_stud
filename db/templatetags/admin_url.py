from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag()
def edit_link(instance):

    #
    model = instance.__class__.__name__.lower()
    if model == 'user':
        url = reverse("admin:auth_user_change", args=(instance.pk,))
    else:
        url = reverse("admin:db_%s_change" % model, args=(instance.pk,))
    return url