from rest_framework import serializers
from .models import confrence

class confrenceserializer(serializers.ModelSerializer):
    class Meta:
        model=confrence
        fields=('confrence_ID','date','venu','confrence_Overview','registration','travel_information')