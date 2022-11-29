from http.client import HTTPResponse

from django.views import View

from MarkupAI.settings import YA_API_KEY
from bridge.forms import TextInputForm
from model.views import AIModel
import requests

from django.shortcuts import render


class GeoCoderHandler:
    def __init__(self):
        pass

    def geocode(self, text: str) -> requests.Response.json:
        model = AIModel()

        # How it should actually work
        # performed = model.perform(text)

        # res = [requests
        # .get(f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={str}&format=json') for str in performed]]

        performed = model.perform(text)[0]

        res = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={YA_API_KEY}&geocode={performed}&format=json')

        return res.json()


class GeoCoderView(View):
    def get(self, request):
        context = {
            'has_data': False,
            'form': TextInputForm()
        }
        return render(request, 'index.html', context)

    def post(self, request):
        text = request.POST.get('Text')
        # handler = GeoCoderHandler()
        # res = handler.geocode(text)
        result = AIModel().perform(text)

        context = {
            'marked_map': result,
            'form': TextInputForm(),
            'has_data': True
        }
        return render(request, 'index.html', context)

    # def index(request) -> HTTPResponse:
    #     """
    #     A function that handles GET request.
    #     :param request:
    #     :return:
    #     """
    #
    #     context = {}
    #
    #     if request.method == 'GET':
    #         model = AIModel()
    #
    #         context['result'] = model.perform(request.GET['text'])
    #
    #     return render(request, 'index.html', context)
