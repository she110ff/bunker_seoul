import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import DetailView, TemplateView
from mezzanine.conf import settings
from .models import UserCategory
from cartridge.shop.models import Category

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

