from operator import attrgetter

from django.db.models import Q
from django.shortcuts import render
from Author.models import Post

# Create your views here.


def bloglist(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    blogs = sorted(blogsearch(query), key=attrgetter('created_at'), reverse=True)
    context['blogs'] = blogs
    return render(request, "Blog/bloglist.html", context)


def blogdetails(request, id):
    context = Post.objects.get(id=id)
    a = context.Genre
    context2 = Post.objects.filter(Genre=a).exclude(id=id)
    both = {'related': context2, 'details': context}
    return render(request, "Blog/blogdetails.html", both)


def blogsearch(query=None):
    queryset = []
    queries = query.split(", ")
    for q in queries:
        posts = Post.objects.filter(
            Q(Title__icontains=q) |
            Q(Description__icontains=q) |
            Q(Genre__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))
