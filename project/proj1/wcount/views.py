from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(requests):
	return render(requests,'wcount/home.html')

def about(requests):
	return render(requests,'wcount/about.html')
 

def count(requests):
	fulltext = requests.GET['text']
	word_count=len(fulltext.split())
	word_dict={}
	for w in fulltext.split():
		if w in word_dict:
			word_dict[w]+=1
		else:
			word_dict[w]=1
	l=[(i,word_dict[i]) for i in word_dict]
	return render(requests,"wcount/count.html",{'fulltext':fulltext
		,'word_count':word_count,'l':l})
