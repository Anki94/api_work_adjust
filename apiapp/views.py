import csv,io
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from apiapp.models import Dataset
from apiapp.serializers import datasetserializer
from apiapp.filter import UserFilter
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.decorators import permission_required

class DatasetList(generics.ListAPIView):
    serializer_class=datasetserializer
    queryset=Dataset.objects.all()
    filter_backends=(DjangoFilterBackend,)
    filter_class=UserFilter
    #permission_classes=(AllowAny,)
    permission_classes=(IsAuthenticated)
    authentication_classes=(SessionAuthentication,BasicAuthentication)


    def get_queryset(self):
        queryset=self.queryset.extra(select={"cpi":"spend/installs"})
        fields=[fields.name for field in Dataset._meta.get_fields()]
        fields.append('cpi')
        print(queryset)
        return queryset



#@permission_required('admin.can_add_log_entry')
def csv_upload(request):
    template='csv_upload.html'
    


    prompt={
        'order': 'order of csv should be date,channel,country,os,impressions,clicks,installs,spend,revenue'
    }



    if request.method=='GET':
        return render(request,template,prompt)

    csv_files=request.FILES['file']

    if not csv_files.name.endswith('.csv'):
        messages.error(request, 'this is not a csv file')
    
    data_set = csv_files.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

   

    for col in csv.reader(io_string,delimiter=','):
    #with open('/home/ankita.kapoor/dataset.csv') as f:
        #reader = csv.reader(f,delimiter=',')
        #io_string = io.StringIO(f)
        #next(io_string)
    #for col in io_string:
        _, created = Dataset.objects.all().get_or_create(
            date=col[0],
            channel=col[1],
            country=col[2],
            os=col[3],
            impressions=col[4],
            clicks=col[5],
            installs=col[6],
            spend=col[7],
            revenue=col[8]
        )
    context = {}
    return render(request,template,context)