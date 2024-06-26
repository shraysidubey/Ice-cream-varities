from django.shortcuts import render, HttpResponse
from home.models import Contact, Blog
from datetime import datetime
from django.contrib import messages

def index(request):
    data = {
        'name' : "shraysi",
        'age' : 28,
        'hobbies': "dancing"

    }
    return render(request, 'index.html', {'data':data})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request, 'contact.html')

def blog(request):
    if request.method == "POST":
        
        blog_name = request.POST.get('blog_name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        blogs = Blog(blog_name=blog_name, category=category, description=description)
        blogs.save()
    else:
        all_blogs = Blog.objects.all()
    return render(request, 'blog.html', {'all_blogs':all_blogs})