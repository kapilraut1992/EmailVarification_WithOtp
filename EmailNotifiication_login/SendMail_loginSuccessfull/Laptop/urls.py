from django.urls import path
from . views import Add_Laptop,show_Laptop,Lap_update,Lap_delete

urlpatterns = [
    path('add/',Add_Laptop.as_view(),name='add_laptop'),
    path('show/',show_Laptop.as_view(),name='show_laptop'),
    path('update/<int:id>/',Lap_update.as_view(),name='update'),
    path('delete/<int:id>/',Lap_delete.as_view(),name='delete')
]