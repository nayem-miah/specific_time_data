from django.shortcuts import render
from .models import Nimosoft
import datetime


# Create your views here.

def data(request):
# from 1990-2-14 to 2010-2-24 data only shows here
    data = Nimosoft.objects.filter(birth_date__gte = datetime.date(1990,2,14)).exclude(birth_date__gte = datetime.date(2010,2,24))
    context={
        'data': data
    }
    return render(request, template_name='index.html', context= context)
    
