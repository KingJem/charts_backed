from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
import json
from rest_framework.viewsets import ModelViewSet
from plot.serializers import ItemSerializer, FileSerializer, ModelMapSerializer
from plot import models


class Plot(View):
    def get(self, request):
        data = {
            "msg": "success",
            "level1": {"legend": ["cutin", "路口", "紧急cutin"],
                       "series": {"data": [
                           {"value": "234", "name": "cutin"},
                           {"value": "100", "name": "路口"},
                           {"value": "200", "name": "紧急cutin"}

                       ]}},
            "level2": {
                "cutin": {"data": {"legend": ["cutin二级分类1", "cutin二级分类2", "cutin二级分类3"],
                                   "series": {
                                       "data": [
                                           {"value": "234", "name": "cutin二级分类1"},
                                           {"value": "100", "name": "cutin二级分类2"},
                                           {"value": "200", "name": "cutin二级分类3"}

                                       ]}}},
                "紧急cutin": {"data": {"legend": ["紧急cutin二级分类1", "紧急cutin二级分类2", "紧急cutin二级分类3"],
                                     "series": {
                                         "data": [
                                             {"value": "234", "name": "紧急cutin二级分类1"},
                                             {"value": "100", "name": "紧急cutin二级分类2"},
                                             {"value": "200", "name": "紧急cutin二级分类3"}
                                         ]}}},
                "路口": {"data": {"legend": ["路口二级分类1", "路口二级分类2", "路口二级分类3"],
                                "series": {
                                    "data": [
                                        {"value": "234", "name": "路口二级分类1"},
                                        {"value": "100", "name": "路口二级分类2"},
                                        {"value": "200", "name": "路口二级分类3"}
                                    ]}}},
            }
        }
        return HttpResponse(json.dumps(data))

    def post(self, request):
        pass


class ItemView(ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = ItemSerializer


class FileView(ModelViewSet):
    queryset=models.Item.objects.all()
    serializer_class=FileSerializer

class ModelMapView(ModelViewSet):
    queryset=models.Item.objects.all()
    serializer_class=ModelMapSerializer