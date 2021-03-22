from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from coins.models import Image

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


def file_upload(request):
    if request.method == "POST":
        image_file = request.FILES.get('file')
        Image.create(image=image_file)
        return HttpResponse('')

    return JsonResponse({'post': 'false'})
