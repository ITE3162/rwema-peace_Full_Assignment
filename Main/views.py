from django.contrib import messages
from django.shortcuts import render, redirect
from Main.models import About, Service, Contact
from Author.models import Post, User


# Create your views here.
def home(request):
    about = About.objects.all()
    services = Service.objects.all()
    users = User.objects.all().exclude(is_superuser=True)
    blogs = Post.objects.all()[:3]

    data = {'about': about, 'services': services, 'team': users, 'posts': blogs, }

    if request.method == 'POST':

        if request.POST.get('email') and request.POST.get('subject') and request.POST.get(
                'message'):
            savecontact = Contact()
            savecontact.Email = request.POST['email']
            savecontact.Subject = request.POST['subject']
            savecontact.Message = request.POST['message']
            savecontact.save()
            return redirect('home')
        else:
            print('Something went wrong')
            return redirect('home')
    return render(request, "Main/index.html", data)

