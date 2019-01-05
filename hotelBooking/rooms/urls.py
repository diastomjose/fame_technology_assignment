from django .conf.urls import url,include
# from customer.views import

from rooms import views 
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [

 
 url(r'^createrooms$',views.EnterRoomsView.as_view(),name = 'createrooms'),
 url(r'^viewrooms$',views.ListroomsView.as_view(),name = 'viewrooms'),
 url(r'^booking$',views.BookingView.as_view(),name = 'booking'),


	

]
