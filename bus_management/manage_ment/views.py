from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse('WELCOME TO IIUC BUS SYSTEM')

from .models import Bus
from django.db import connection

def bus_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Buses")
        buses = cursor.fetchall()  # Returns raw tuples of data
    return render(request, 'bus_list.html', {'buses': buses})
