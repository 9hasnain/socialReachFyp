from django.shortcuts import render
from django.http import HttpResponse
from twitterapp.sentiment import TweetAnalysis

# Create your views here.


def  index(request):

    data = TweetAnalysis()
    list = data.performAnalysis('#pulwamaattack')
    my_dict = {'data': list}


    return render(request, 'twitter.html', context=my_dict)