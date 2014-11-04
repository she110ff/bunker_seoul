from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import TimelineView


urlpatterns = [
    url(r'^timeline/$', TimelineView.as_view()),

]
