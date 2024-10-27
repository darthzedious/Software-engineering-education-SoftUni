from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from FurryFunnies.post_app.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'