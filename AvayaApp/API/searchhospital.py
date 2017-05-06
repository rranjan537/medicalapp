from AvayaApp.models import Hospital
from django.contrib.postgres.search import SearchQuery

def SearchHospital(self, request, format=None):
    data = Hospital.objects.filter(Specialization__startswith=request['SearchKey'])
    data = data.order_by('Distance')
    return (data)