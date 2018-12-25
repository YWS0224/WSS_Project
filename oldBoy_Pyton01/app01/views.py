from django.shortcuts import render
import datetime
# Create your views here.


def show_time(request):
    time = datetime.datetime.now()
    return render(request, 'Show_Time.html', locals())
