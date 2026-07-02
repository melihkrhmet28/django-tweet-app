from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {'tweets': all_tweets}
    return render(request, 'tweetapp/listtweet.html', tweet_dict)

@login_required(login_url='/login')
def addtweet(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        models.Tweet.objects.create(username=request.user, message=message)
        return redirect('tweetapp:listtweet')
    else:
        return render(request, 'tweetapp/addtweet.html')

@login_required(login_url='/login')
def addtweet_with_form(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.username = request.user
            tweet.save()
            return redirect('tweetapp:listtweet')
    else:
        form = AddTweetForm()
    return render(request, 'tweetapp/addtweetbyform.html', {'form': form})
    
@login_required(login_url='/login')
def addtweet_with_model_form(request):
    if request.method == 'POST':
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.username = request.user
            tweet.save()
            return redirect('tweetapp:listtweet')
    else:
        form = AddTweetModelForm()
    return render(request, 'tweetapp/addtweetmodel.html', {'form': form})
@login_required(login_url='/login')  
def deletetweet(request, tweet_id):
    if request.method == 'POST':
        tweet = models.Tweet.objects.get(id=tweet_id)
        if tweet.username == request.user:
            tweet.delete()
    return redirect('tweetapp:listtweet')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')#her çalıştırıldığında tekrar hesaplanır
    template_name = 'registration/signup.html'