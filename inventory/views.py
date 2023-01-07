from django.shortcuts import render,redirect, HttpResponseRedirect
from .forms import Shopify_Inventory
from .models import User
from django.contrib import messages
from django.http import JsonResponse
import json



# Create your views here.

# This Function will Add new Item and Show all Item
def add_show(request):
    if request.method == 'POST':
        fm = Shopify_Inventory(request.POST)
        if fm.is_valid():
            In = fm.cleaned_data['Item_name']
            Ts = fm.cleaned_data['Total_Stock_In_KG']
            Rs = fm.cleaned_data['Price_Per_KG'] 
            reg = User(Item_name=In,Total_Stock_In_KG=Ts,Price_Per_KG=Rs)
            reg.save()
            messages.success(request,'Item Added Successfully....')
            fm = Shopify_Inventory()
            
    else:
        fm = Shopify_Inventory()
    stud = User.objects.all()  
    return render(request, 'inventory/addandshow.html',{'form':fm,
    'stu':stud})

    # This function will Update/Edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Shopify_Inventory(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Item Updated Successfully....')
    else:
        pi = User.objects.get(pk=id)
        fm = Shopify_Inventory(instance=pi)        
    return render(request, 'inventory/updatesitems.html',{'form':fm})    

    # This Function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

    # Create your views here:-
def json(request):
    data = list(User.objects.values())
    return JsonResponse(data, safe=False)        

    