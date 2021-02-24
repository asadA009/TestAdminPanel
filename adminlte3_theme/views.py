from django.shortcuts import render
from .forms import confrenceForm
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import confrence
from .serializers import confrenceserializer
# Create your views here.

class confrenceView(viewsets.ModelViewSet):
    queryset=confrence.objects.all()
    serializer_class=confrenceserializer
