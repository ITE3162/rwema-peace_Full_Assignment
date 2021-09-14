from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from Author.models import Post
from Author.forms import PostForms


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Logged in successful')
            return redirect('dashboard')
        else:
            print('Invalid credentials')
            return redirect('login')
    else:
        return render(request, "Author/login.html")


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['password1']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                        last_name=lastname)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request, "Author/register.html")


def dashboard(request):
    return render(request, "Author/dashboard.html")


def createblog(request):
    if request.method == 'POST':
        if request.POST.get('Title') and request.POST.get('Genre') and request.POST.get(
                'Description') and request.FILES.get('Poster') and request.POST.get('Release'):
            saveblog = Post()
            saveblog.Title = request.POST['Title']
            saveblog.Genre = request.POST['Genre']
            saveblog.Description = request.POST['Description']
            saveblog.Poster = request.FILES['Poster']
            saveblog.Release = request.POST['Release']
            saveblog.Author = request.user
            saveblog.save()
            print('Blog created successfully')
            return redirect('dashboard')
        else:
            print('Something went wrong')
            return redirect('create')
    return render(request, "Author/addblog.html")


def blogs(request):
    author = request.user
    context = Post.objects.filter(Author=author)
    posts = {'posts': context}
    return render(request, "Author/blogs.html", posts)


def postedit(request, id):
    instance = Post.objects.get(id=id)
    editinfo = {'editinfo': instance}
    if request.method == "POST":
        form = PostForms(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            print("Updated successfully")
            return redirect("blogs")
        else:
            print("Couldn't update")
    return render(request, "Author/editblog.html", editinfo)


def postdelete(request, eid):
    postdel = Post.objects.get(id=eid)
    postdel.delete()
    return redirect("blog-list")


def logout(request):
    auth.logout(request)
    return redirect('/')
