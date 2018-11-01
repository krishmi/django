from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Subjects,Upload
from .forms import UploadForm
import os

# Create your views here.

def index(request):
	return render(request,'JUAPP/index.html')

def check(request):
	department=request.POST.get('dept')
	year=request.POST.get('year')
	return HttpResponseRedirect(department+'/'+year+'/')

def subjects(request,dept,year):
	sub=Subjects.objects.filter(dept=dept,year=year)
	return render(request,'JUAPP/subjects.html',{'dept':dept,'year':year,'subs':sub,})

def resources(request,dept,year,subject):
	return render(request,'JUAPP/resources.html',{'sub':subject,})

def pdf_response(request,subject,year,dept,resource,resource_name):
	with open('/home/krishna/django/media/JUAPP/'+subject+'/'+resource+'/'+resource_name, 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline'
		return response
	pdf.closed

def resource(request,dept,year,subject,resource):
	files=os.listdir('/home/krishna/django/media/JUAPP/'+subject+'/'+resource+'/')
	form=UploadForm()
	return render(request,'JUAPP/slides.html',{'files_list':files,'form':form,})

def uploading(request,subject,year,dept,resource):
	inst=Upload()
	inst.subject=subject
	inst.resource=resource
	inst.save();
	upload=UploadForm(request.POST,request.FILES,instance=inst)
	if upload.is_valid():
		upload.save(commit=True)
		return HttpResponseRedirect('/JUAPP/check/'+dept+'/'+year+'/'+subject+'/')
	else:
		return HttpResponseRedirect('/JUAPP/')
	
	