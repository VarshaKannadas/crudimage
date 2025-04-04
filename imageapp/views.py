import os
from django.shortcuts import render,redirect
from.models import Products

# Create your views here.
def index(request):
    return render(request,'add_product.html')

def add_product(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        price=request.POST['price']
        quantity=request.POST['quantity']
        image=request.FILES.get('file')
        prd=Products(product_name=product_name,price=price,quantity=quantity,image=image)
        prd.save()
        return redirect('show_product')
def show_product(request):
    prdts=Products.objects.all()
    return render(request,'show_product.html',{'prdtd':prdts})
def editpage(request,pk):
    prdts=Products.objects.get(id=pk)
    return render(request,'Edit.html',{'prdts':prdts})
def edit_product(request,pk):
    if request.method=='POST':
        prdcts=Products.objects.get(id=pk)
        prdcts.product_name=request.POST.get('product_name')
        prdcts.price=request.POST.get('price')
        prdcts.quantity=request.POST.get('quantity')
        if len(request.FILES)!=0:
            if len(prdcts.image)>0:
                os.remove(prdcts.image.path)
            prdcts.image=request.FILES.get('file')
        prdcts.save()
        return redirect('show_product')
    return render(request,'Edit.html')

def delete(request,pk):
    p=Products.objects.get(id=pk)
    if p.image and os.path.isfile(p.image.path):
        os.remove(p.image.path)
    p.delete()
    return redirect('show_product')
    