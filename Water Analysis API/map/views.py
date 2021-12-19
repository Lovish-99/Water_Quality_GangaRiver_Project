from django.shortcuts import render
from django.http import HttpResponse
from .models import insertddl
from .models import insertgraph2
from django.contrib import messages
import csv
import pandas as pd
from .locatemap import *

def home(request):
    if request.method == "POST":
        if request.POST.get('pname') and request.POST.get('yesno'):
            savevalue=insertddl()
            savevalue.pname=request.POST.get('pname')
            savevalue.yesno=request.POST.get('yesno')
            savevalue.save()
            parameter = savevalue.pname
            val = savevalue.yesno 

            if val == "Site1A":
                context = locate_map1(parameter, val)
            elif val == "Site1B":
                context = locate_map2(parameter, val)
            elif val == "Site1C":
                context = locate_map3(parameter, val)
            else:
                context = locate_map4(parameter, val)

            #notifier()
            #returning the values that we want to represent in index1.html page
            return render(request, 'index1.html', context)
    else:
        #create a folium map 
        f = folium.Figure(height=517, width=934)
        #setting the location of a map for 'India'
        m = folium.Map(location=[22.9734, 78.6569], zoom_start=5).add_to(f)
        m = m._repr_html_()
        context = {'m' : m}
        return render(request, 'index1.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    if request.method == "POST":
        if request.POST.get('service1') and request.POST.get('service2') and request.POST.get('service3'):
            savevalue=insertgraph2()
            savevalue.service1=request.POST.get('service1')
            savevalue.service2=request.POST.get('service2')
            savevalue.service3=request.POST.get('service3')
            savevalue.save()
            g1  = savevalue.service1
            g2  = savevalue.service2
            g3  = savevalue.service3
            g4 = int(g3)
            if g1 == "Site1A":
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'".format(g2,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS/Runtime/Location's.csv")
                d3=df5['Name Of The River'].tolist()
                g5 = d3[g4]
            elif g1 == "Site1B":
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'".format(g2,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS/Runtime2/Location's.csv")
                d3=df5['Name Of The River'].tolist()
                g5 = d3[g4]
            elif g1 == "Site1C":
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'".format(g2,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS/Runtime3/Location's.csv")
                d3=df5['Name Of The River'].tolist()
                g5 = d3[g4]
            else:
                g2a = g2.replace("/","_")
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS1/{}/Location{}/Data.jpeg'".format(g2a,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS1/Location's.csv")
                d3=df5['Location'].tolist()
                g5 = d3[g4]
            context = {
                'g' : g,
                'g1' : g1,
                'g2' : g2,
                'g3' : g5
            }
            return render(request, 'services.html',context)
    else:
        return render(request, 'services.html')