from .models import *
from rest_framework import serializers

class CovidSerializer(serializers.ModelSerializer):
	class Meta:
		model = Covid
		fields = '__all__'