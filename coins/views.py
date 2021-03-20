from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


def file_upload(request):
    if request.method == "POST":
        my_file = request.FILES.get('file')
        # Image.objects.create(upload=my_file)
        return HttpResponse('')

    return JsonResponse({'post': 'false'})
