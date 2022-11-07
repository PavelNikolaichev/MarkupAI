from http.client import HTTPResponse

from django.shortcuts import render

from model.views import AIModel


# Create your views here.

def index(request) -> HTTPResponse:
    """
    A function that handles GET request.
    :param request:
    :return:
    """
    model = AIModel()

    result = model.perform(request.GET['text'])

    return render(request, 'index.html', {'result': result})
