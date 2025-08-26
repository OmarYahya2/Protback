from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', views.UserList.as_view(), name='accounts'),
    path('contact/', views.contact, name='contact'),

]
