from rest_framework import serializers
from .models import Task


class  TaskSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Task   
        fields = '__all__'
