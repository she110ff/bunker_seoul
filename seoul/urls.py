from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^timeline/$', login_required(TemplateView.as_view(template_name="seoul/timeline.html"))),
    url(r'^privacy/$', TemplateView.as_view(template_name="seoul/privacy.html")),
    url(r'^subscription/list/$', login_required(TemplateView.as_view(template_name="seoul/subscription.html"))),
    url(r'^recommend/$', login_required(TemplateView.as_view(template_name="seoul/recommend.html"))),
    url(r'^user/subscription/$', login_required(views.user_subscription)),
    url(r'^product/like/$', login_required(views.user_like_product)),
    url(r'^product/subscription/$', login_required(views.sub_products)),
    url(r'^pull/git/$', views.pull_git),


]
