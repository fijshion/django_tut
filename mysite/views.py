from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template.loader import render_to_string


def handle404(request):
    return HttpResponseNotFound(render_to_string('mysite/handle404.html'))


def handle500(request):
    return HttpResponseServerError(render_to_string('mysite/handle500.html'))