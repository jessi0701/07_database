from django.shortcuts import render,redirect
from .models import Genre,Movie,Score
from .forms import MovieForm, ScoreForm
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html',{'movies':movies})
    
def read(request,id):
    movie = Movie.objects.get(id=id)
    score_form = ScoreForm()
    scores = Score.objects.all()
    return render(request, 'movie/read.html',{'movie':movie , 'score_form':score_form, 'scores':scores})
    
def delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("movie:list")
    
def new_score(request,id):
    if request.method == 'POST':
       score_form = ScoreForm(request.POST)
       if score_form.is_valid():
           score = score_form.save(commit=False)
           score.movie_id = Movie.objects.get(id=id)
           score.save()
           return redirect("movie:read", id)
    else:
        score_form=ScoreForm()
    return render(request, 'movie/read.html',{'score_form':score_form})
    
def delete_score(request,id,idid):
    score = Score.objects.get(id=idid)
    score.delete()
    return redirect('movie:read',id)
    
       
    