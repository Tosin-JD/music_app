from django.shortcuts import render
from django.views import generic
from tracks.models import Track

# Create your views here.
class HomePage(generic.ListView):
    model = Track
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context['latest_tracks'] = Track.objects.all()[:5]
        return context


class AboutPage(generic.TemplateView):
    template_name = 'main/about.html'

