from django.urls import path
from .import views


urlpatterns=[
			path('',views.index,name='index'),
			path('check/',views.check,name='check'),
			path('check/<dept>/<year>/',views.subjects,name='subjects'),
			path('check/<dept>/<year>/<subject>/',views.resources,name='resources'),
			path('check/<dept>/<year>/<subject>/<resource>/',views.resource,name='resource'),
			path('check/<dept>/<year>/<subject>/<resource>/uploadFile/',views.uploading,name='uploading'),
			path('check/<dept>/<year>/<subject>/<resource>/<resource_name>/',views.pdf_response,name='slide'),
			]
			 