from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.models import User
from mezzanine.conf import settings


class TimelineView(TemplateView):
    template_name = "seoul/timeline.html"
