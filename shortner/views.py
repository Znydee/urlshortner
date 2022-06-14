from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Link
import uuid
from django.contrib import messages
# Create your views here.
def home(request):        
    return render(request, "shortner/index.html")
    
def create_short_link(request):
    if request.method == "POST":
        initial_link = request.POST["long_link"]
        generated_short_link = str(uuid.uuid4())[:6]
        Link(link=initial_link,short_link=generated_short_link).save()
        messages.success(request,'link has successfully been shortened')
        return HttpResponse(generated_short_link)
        
def go(request,link):
    url_link_to_obj = Link.objects.get(short_link = link)
    return redirect(url_link_to_obj.link)

