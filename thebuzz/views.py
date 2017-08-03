# Create your views here.
# thebuzz/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class GamePageView(TemplateView):
    template_name = "game.html"

class FactsPageView(TemplateView):
    template_name = "facts.html"

class HowToHelpPageView(TemplateView):
    template_name = "howtohelp.html"

class CreditsPageView(TemplateView):
    template_name = "credits.html"
