from rest_framework import serializers
from .models import Dataset

class datasetserializer(serializers.ModelSerializer):
    date=serializers.DateField()
    channel=serializers.CharField(max_length=100)
    country=serializers.CharField(max_length=50)
    os=serializers.CharField(max_length=50)
    impressions=serializers.IntegerField(default=0)
    clicks=serializers.IntegerField(default=0)
    installs=serializers.IntegerField(default=0)
    spend=serializers.DecimalField(max_digits=25,decimal_places=2)
    revenue=serializers.DecimalField(max_digits=25,decimal_places=2)
    



    


    class Meta:
            model=Dataset
            fields = ['date','channel','country','os','impressions','clicks','installs','spend','revenue']