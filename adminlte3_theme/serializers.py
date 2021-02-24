from rest_framework import serializers
from .models import confrence

class confrenceserializer(serializers.ModelSerializer):
    class Meta:
        model=confrence
        fields=('name','city','roll')