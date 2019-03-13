
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.defaults import page_not_found
from django.utils import timezone
from .models import Question,Contestant,SetNo
from .forms import ContestantForm
from random import randint


# Create your views here.
def assignset(year):
    year = int(year)
    if year == 1:set_no = randint(1,2)
    elif year==2:set_no = randint(3,4)
    else: set_no = randint(5,6)
    setobj = SetNo.objects.get(setno = set_no)
    return setobj

def index(request):
    if request.method == "POST":
        form = ContestantForm(request.POST)
        if form.is_valid():
            cont = form.save(commit=False)
            cont.setno = assignset(request.POST.get('year',''))
            cont.save()
            resposne = HttpResponseRedirect('set/'+str(cont.setno)+'/ques/welcome')
            resposne.set_cookie('user_id', cont.pk)
            return resposne
    else:
        form = ContestantForm()
    return render(request, 'homepage.html', {'form':form})

def welcome(request, set_no):
    return render(request, 'rules.html')

def ans_not_found(request):
    return render(request, 'notfound.html', status=404)


def generateques(request, set_no, ans):
    user_id = request.COOKIES['user_id']
    user = Contestant.objects.get(pk = user_id)
    present_time = timezone.now()
    if(user.endtime < present_time):
        return render(request , 'timeout.html')
    if(user.setno.setno != set_no):
        return render(request, 'wrongset.html')
    try:
        qs = Question.objects.get(setno = set_no, ans_text = ans)
        q_no = qs.ques_img[3]
        ques_img = qs.ques_img
        ques_text = qs.ques_text
        meme_no = randint(1,5)
    except Question.DoesNotExist:
        meme_no = randint(1,9)
        return render(request, 'notfound.html', {'meme_no':meme_no})
    user.points = q_no
    user.save()
    return render(request, 'questions.html', {'q_no':q_no, 'ques_img':ques_img, 'ques_text':ques_text, 'meme_no':meme_no})
