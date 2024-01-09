from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('all_class/<int:id>', views.all_class, name='all_class'),
    path('details/<int:id>', views.details, name='datails'),
    path('search/<str:s_val>', views.search, name='search'),
]