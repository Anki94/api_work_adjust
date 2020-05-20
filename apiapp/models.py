from django.db import models
import pandas as pd
import csv
#your_dataframe = pd.read_csv(input('path_to_csv'))

# Create your models here.
class Dataset(models.Model):

########
    '''def get_all_products():
        items = []
        with open('/home/ankita.kapoor/dataset.csv','r') as fp:
            # You can also put the relative path of csv file
            # with respect to the manage.py file
            reader1 = csv.reader(fp, delimiter=';')
            for value in reader1:
                items.append(value)
        return items'''
#######


    date=models.DateField()
    channel=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    os=models.CharField(max_length=50)
    impressions=models.IntegerField(default=0)
    clicks=models.IntegerField(default=0)
    installs=models.IntegerField(default=0)
    spend=models.DecimalField(max_digits=25,decimal_places=2)
    revenue=models.DecimalField(max_digits=25,decimal_places=2)