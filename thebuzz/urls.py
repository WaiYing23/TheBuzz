# bees_project/urls.py
from django.conf.urls import url
from thebuzz import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^game/$', views.GamePageView.as_view()),
    url(r'^facts/$', views.FactsPageView.as_view()), # Add this /about/ route
    url(r'^howtohelp/$', views.HowToHelpPageView.as_view()),
    url(r'^credits/$', views.CreditsPageView.as_view()),
]
