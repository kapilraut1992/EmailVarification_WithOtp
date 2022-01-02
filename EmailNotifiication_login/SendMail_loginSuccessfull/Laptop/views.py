from django.shortcuts import render,redirect
from.forms import LaptopForm
from .models import Laptop
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Add_Laptop(LoginRequiredMixin,View):
    def get(self,request):
        form=LaptopForm()
        template='Laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)

    def post(self,request):
        form=LaptopForm(request.POST)
        if form.is_valid():
            print('data from front end',form)
            form.save()
            return redirect('show_laptop')
        template='Laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)

class show_Laptop(View):
    def get(self,request):
        laptop=Laptop.objects.all()
        template='Laptop/showlaptop.html'
        context={'laptop':laptop}
        return render(request,template,context)

class Lap_update(LoginRequiredMixin,View):
    def get(self,request,id):
        lap_obj=Laptop.objects.get(id=id)
        form=LaptopForm(instance=lap_obj)
        template='Laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)


    def post(self,request,id):
        lap_obj=Laptop.objects.get(id=id)
        form=LaptopForm(request.POST,instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
        template='Laptop/addlaptop.html'
        context={'form':form}
        return render(request,template,context)

class Lap_delete(LoginRequiredMixin,View):
    def get(self,request,id):
        lap=Laptop.objects.get(id=id)
        template='Laptop/confirm_delete.html'
        context={'lap':lap}
        return render(request,template,context)

    def post(self,request,id):
        lap=Laptop.objects.get(id=id)
        lap.delete()
        lap.save()
        return redirect('show_laptop')

