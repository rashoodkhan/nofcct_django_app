from django.shortcuts import render, get_object_or_404

from blog.models import *
import datetime

# Create your views here.

def index(request):
    if request.method == 'POST':
        return search(request)

    return render(request,'blog/index.html',{})

def blogview(request):
    if request.method == 'POST':
        return search(request)

    blog_posts = Blog.objects.all().order_by('-date_posted')

    return render(request,'blog/blog.html',{
        'posts' : blog_posts
    })

def search(request):
    key = request.POST['key']
    posts = Blog.objects.all()
    events = Event.objects.all()
    key = str(key).lower()

    req_posts = []
    req_events = []

    for post in posts:
        title = str(post.title)
        content = str(post.content)

        title = title.lower()
        content = content.lower()

        if title.count(key) > 0 or content.count(key):
            req_posts.append(post)

    for event in events:
        name = str(event.name)
        venue = str(event.venue)
        end_date = event.end_date.date()
        cur_date = datetime.date.today()

        name = name.lower()
        venue = venue.lower()

        if name.count(key) or venue.count(key):
            if end_date - cur_date >= datetime.timedelta(0):
                req_events.append(event)

    return render(request,'blog/search.html',{
        'posts' : req_posts,
        'events' : req_events
    })

def blog_detail(request,blog_id):
    if request.method == 'POST':
        return search(request)

    blog = get_object_or_404(Blog,id=blog_id)
    return render(request,'blog/blog_detail.html',{
        'blog' : blog
    })

def event_view(request):
    if request.method == 'POST':
        return search(request)

    events = Event.objects.all()
    return render(request,'blog/event.html',{
        'events' : events
    })

def event_detail(request, event_id):
    if request.method == 'POST':
        return search(request)

    event = get_object_or_404(Event,id=event_id)
    return render(request,'blog/event_detail.html',{
        'event' : event
    })
