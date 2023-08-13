from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "mail": "testingpage@umail.org",
            "address": "15Pl Andromeda Galaxy",
            "phone": "+931 526 132 7368 "
        })
        return context
    
class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price":450},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":300},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":80},
    {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":20}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        try:
            if 1<= int(id) <= len(Product.products):
                viewData = {}
                product = Product.products[int(id)-1]
                viewData["title"] = product["name"] + " - Online Store"
                viewData["subtitle"] = product["name"] + " - Product information"
                viewData["product"] = product
                return render(request, self.template_name, viewData)
            else:
                return HttpResponseRedirect(reverse('home'))
        except ValueError:
            return HttpResponseRedirect(reverse('home'))
        
class ProductForm(forms.Form):
        name = forms.CharField(required=True)
        price = forms.FloatField(required=True)

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect('created')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        
class ProductCreatedView(View):
    template_name = 'products/created.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Product Created"
        return render(request, self.template_name, viewData)