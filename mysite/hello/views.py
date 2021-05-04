from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    html = '<li><a href="/hello">Test the session</a></li>'
    resp = HttpResponse('view count='+str(num_visits) + html)
    resp.set_cookie('dj4e_cookie', '29cb2d8a', max_age=1000)
    return resp