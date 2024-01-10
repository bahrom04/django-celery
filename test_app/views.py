from django.http import HttpResponse
from test_app.tasks import get_image


def index(request):
     if request.method == "GET":
          get_image.delay()
     return HttpResponse("Downloading...")