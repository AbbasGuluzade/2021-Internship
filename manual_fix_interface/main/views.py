from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import *
from .models import *
from .YYY import *
from .match import match_dict
import ast
import os


def index (request):
    form=PolygonForm()
    match_form = MatchForm()
    return render(request, 'main/myHtml.html', {'form':form, 'match_form':match_form})

def databaseLoad(request):
    BulkInsert()
    return render(request, 'main/success.html')

def get_match(request):
    if request.method == 'POST':
        match_form = MatchForm(data=request.POST or None)
        if match_form.is_valid():

            match_dict[match_form.cleaned_data['text']] = Polygon.objects.get(polygon_id = match_form.cleaned_data['polygon_id_text']).coordinates
            f = open('/home/abbas/Desktop/manual_fix_interface/main/match.py', 'w')
            f.write("match_dict=" + str(match_dict))
            f.close()

    else:
        match_form = MatchForm(request.GET)

    
    return render(request, 'main/myHtml.html', {'match_form': match_form})


def change_polygon_class(request):

    if request.method == 'POST':
        
        form = PolygonForm(data=request.POST or None)
        if form.is_valid():
            p = Polygon.objects.get(polygon_id = form.cleaned_data['polygon_id'])
            
            p.polygon_class = form.cleaned_data['polygon_class']
            p.save()

            temp = elements

            for element in temp:
                if str(element[:-1]) == p.coordinates:
                    element[-1] = form.cleaned_data['polygon_class']


            f = open('/home/abbas/Desktop/manual_fix_interface/main/downloadable_element_array.txt', 'w')
            f.write("const elements = " + str(temp))
            f.close()
            
            f = open('/home/abbas/Desktop/manual_fix_interface/main/YYY.py', 'w')
            f.write("elements=" + str(temp))
            f.close()

    else:
        form = PolygonForm(request.GET)

    return render(request, 'main/myHtml.html', {'form':form})

def pull_polygons_from_database(request):
        
    file_path = os.path.join("/home/abbas/Desktop/manual_fix_interface/main/downloadable_element_array.txt")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/html; charset=UTF-8")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def download_match(request):
    file_path = os.path.join("/home/abbas/Desktop/manual_fix_interface/main/match.py")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/html; charset=UTF-8")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404





