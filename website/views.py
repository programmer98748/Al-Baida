from django.shortcuts import render
from dashboard.models import *

from django.http import HttpRequest

# Create your views here.




def index(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)
    images = Image.objects.all()  # Get all images initially

    homepage = Pages.objects.all()

    if selected_category:
        projects = Project.filter(category__name=selected_category)
   
    context = {"images": images, "categories":categories, "homepage":homepage}
    return render(request, 'website/index.html', context)

def portfolio_details(request, slug):
    if(Category.objects.filter(slug=slug)):
        images = Image.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = { 'category':category, 'images':images}
        return render(request, 'website/portfolio-details.html', context)
  #  else:
      #  return HttpResponseRedirect('/dashboard/login')
     
   

def contact(request):
    return render(request , 'website/contact.html') 

def about(request):
    about = PageAbout.objects.all()
    context = {
        'about':about,
    }

    return render(request, 'website/about.html',context)


def portfolio(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)
    images = Image.objects.all()  # Get all images initially

    if selected_category:
        images = Image.filter(category__name=selected_category)

    
    context = {"images": images, "categories":categories}
    return render(request, 'website/portfolio.html',context)



def filter_images(request):
    if request.is_ajax():
        category_id = request.GET.get('category')
        images = Image.objects.filter(category_id=category_id)
        image_urls = [image.image.url for image in images]
        return JsonResponse({'images': image_urls})
    else:
        return HttpResponseBadRequest()    
        
                                             