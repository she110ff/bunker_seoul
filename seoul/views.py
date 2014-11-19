import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView
from mezzanine.conf import settings
from .models import UserCategory
from cartridge.shop.models import Category

from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import requires_csrf_token
from django.http import (HttpResponse, HttpResponseServerError,
                         HttpResponseNotFound)

from mezzanine.conf import settings
from mezzanine.core.forms import get_edit_form
from mezzanine.core.models import Displayable, SitePermission
from mezzanine.utils.cache import add_cache_bypass
from mezzanine.utils.views import is_editable, paginate, render, set_cookie

def user_subscription(request):
    res = {"result": "fail", "value":"null"}
    if request.method == 'POST':
        try:
            action = request.POST.get('action')
            category_id = request.POST.get('category_id')
            uc, created = UserCategory.objects.get_or_create(user=request.user)
            category = Category.objects.get(id=category_id)
            if action == 'add':
                uc.categories.add(category)
            else:
                uc.categories.remove(category)
            res = {"result": "success", "action":action}
            HttpResponse(json.dumps(res), content_type="application/json")
        except Exception as e:
            print str(e)

    return HttpResponse(json.dumps(res), content_type="application/json")

def pull_git(request):
    import os
    import subprocess as sp
    output = sp.Popen(["git", "pull", "origin", "master", "-f"], stdout=sp.PIPE).communicate()[0]
    res = {"result": output, "value":"null"}
    return HttpResponse(json.dumps(res), content_type="application/json")


@requires_csrf_token
def page_not_found(request, template_name="errors/404.html"):
    """
    Mimics Django's 404 handler but with a different template path.
    """
    context = RequestContext(request, {
        "STATIC_URL": settings.STATIC_URL,
        "request_path": request.path,
    })
    t = get_template(template_name)
    return HttpResponseNotFound(t.render(context))


@requires_csrf_token
def server_error(request, template_name="errors/500.html"):
    """
    Mimics Django's error handler but adds ``STATIC_URL`` to the
    context.
    """
    context = RequestContext(request, {"STATIC_URL": settings.STATIC_URL})
    t = get_template(template_name)
    return HttpResponseServerError(t.render(context))
