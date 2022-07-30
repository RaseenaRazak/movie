from django.shortcuts import render, redirect

# Create your views here.
from movieapp.forms import MovieForm
from movieapp.models import Movie


def index(request):
    movie = Movie.objects.all()
    dict_movie = {'movie_list': movie}
    return render(request, 'index.html', dict_movie)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def add_movie(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, 'add.html')

def update(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form' : form, 'movie' : movie})

def delete(request,movie_id):
    if request.method=='POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
