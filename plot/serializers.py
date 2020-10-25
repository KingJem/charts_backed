from rest_framework import serializers
from plot import models


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'
        depth = 4  # 跨表 （与下方被注释部分目的一样）
        # exclude=('name')  # 与field不能同时


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
        depth = 4 # 跨表 （与下方被注释部分目的一样）
        # exclude=('name')  # 与field不能同时用


class ModelMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelMap
        fields = '__all__'
        depth = 4  # 跨表 （与下方被注释部分目的一样）
        # exclude=('name')  # 与field不能同时用
