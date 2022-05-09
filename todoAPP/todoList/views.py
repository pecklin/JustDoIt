from django.shortcuts import render
from .models import Daily
# from django.http import HttpResponse
# Create your views here.

def index(request):
    Daily_list = Daily.objects.order_by('-date')
    context = {'dailyList':Daily_list}
    return render(request, 'todoAPP/dailyList.html', context)
    # return HttpResponse("HI It's Test")
    