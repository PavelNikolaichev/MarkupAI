import json
from http.client import HTTPResponse

from django.http import JsonResponse
from django.views import View

from MarkupAI.settings import YA_API_KEY
from bridge.forms import TextInputForm
from model.views import AIModel
import requests

from django.shortcuts import render


class GeoCoderHandler:
    def __init__(self):
        pass

    def geocode(self, text: str):

        # How it should actually work
        # performed = [model.perform(line) for line in text.splitlines()]

        # res = [requests
        # .get(f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={str}&format=json') for str in performed]]
        res = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={YA_API_KEY}&geocode={text}&format=json')

        return res.json()


class GeoCoderView(View):
    def get(self, request):
        context = {
            'api_key': YA_API_KEY,
            'has_data': False,
            'form': TextInputForm()
        }
        return render(request, 'index.html', context)

    def post(self, request):
        handler = GeoCoderHandler()

        text = request.POST.get('Text')
        res = []

        for line in text.splitlines():
            if line == '':
                continue

            performed = AIModel().perform(line)
            geocoded = handler.geocode(performed)

            res.append({
                'innerText': line,
                'coords': geocoded['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[::-1]
            })

        print(res)

        context = {
            'api_key': YA_API_KEY,
            'marks': res,
            'has_data': True
        }

        return JsonResponse(context)

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
