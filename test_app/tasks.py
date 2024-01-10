from time import sleep
import urllib.request
from celery import shared_task


@shared_task()
def get_image():
    url = "https://picsum.photos/200/300"
    for i in range(10):
        image_name = f"C:/Users/magdi/Desktop/workspace/django/mysite/media/{i}.jpg"
        urllib.request.urlretrieve(url, image_name)
        sleep(1)


# https://stackoverflow.com/questions/16174022/download-a-remote-image-and-save-it-to-a-django-model