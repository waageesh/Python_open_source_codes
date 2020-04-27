from django.shortcuts import render
from .serializers import *

# Create your views here.
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CovidView(APIView):

    def get(self, APIView):
        # import ipdb; ipdb.set_trace()
        covid = Covid.objects.all()
        serializer = CovidSerializer(covid, many=True)
        return Response(serializer.data)

        