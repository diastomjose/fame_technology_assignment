# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,View
from . models import roomsModel



from rest_framework import viewsets
from rooms.serializers import UserSerializer

# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = roomsModel.objects.all()
    serializer_class = UserSerializer


class Index(TemplateView):
	template_name = 'index.html'

class EnterRoomsView(CreateView):
	model = roomsModel
	fields = ['room_no','room_cost','room_status']
	template_name = 'enterdetails.html'
	success_url = reverse_lazy('/')


class ListroomsView(ListView):
	model = roomsModel
	template_name = 'listdetails.html'

class BookingView(View):
	model = roomsModel
 
	template_name = 'booking.html'
	def get (self,request):
		obj1 = roomsModel.objects.all()
		context = {
		'obj1' : obj1
		}
		return render(request,self.template_name,context)

	def post(self,request):
		rno = request.POST.get('roomno')

		obj1 = roomsModel.objects.get(room_no = rno)
		obj1.room_status='booked'
		obj1.save()


		return redirect('/rooms/viewrooms')