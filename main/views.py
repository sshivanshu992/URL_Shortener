from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Shortner
from .forms import ShortnerForm
from django.conf import settings
import uuid

class Index(View):
    form_class = ShortnerForm
    initial = {'key': 'value'}
    template_name = 'shortener/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("url")
            if Shortner.objects.filter(url=url).exists():
                queryset = Shortner.objects.get(url=url)
                uid = queryset.link
            else:
                uid = str(uuid.uuid4())[:6]
                new_url = Shortner(url=url,link=uid)
                new_url.save()

        if settings.DEBUG:
            domain = 'http://127.0.0.1:8000/'
        else:
            domain = 'http://' + ''.join(settings.ALLOWED_HOSTS)+'/'

        context = { 'form': form, 
                    'shortenlink':uid,
                    'inputurl':url,
                    'domain' :  domain
                    }
        return render(request, self.template_name, context)


def golink(request, pk):
    url_detail = get_object_or_404(Shortner, link=pk)
    return redirect(url_detail.url)
