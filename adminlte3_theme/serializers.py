from rest_framework import serializers
from .models import confrence

class confrenceserializer(serializers.ModelSerializer):
    class Meta:
        model=confrence
        fields=('confrence_ID','date','venu','image','confrence_Overview','register','travel_information')