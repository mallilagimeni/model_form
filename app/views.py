from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TO=TopicForm(request.POST)
        if TO.is_valid():
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}

            return render(request,'display.html',d1)
    return render(request,'insert_topic.html',d)


def inser_webpage(request):
    WTO=webpageForm()
    d={'WTO':WTO}
    if request.method=='POST':
        WO=webpageForm(request.POST)
        if WO.is_valid():
            WO.save()

            return HttpResponse('success')
    return render(request,'inser_webpage.html',d)


def insert_access(request):
    AFO=accessForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AO=accessForm(request.POST)
        if AO.is_valid():
            AO.save()
            return HttpResponse('Success')
    return render(request,'insert_access.html',d)