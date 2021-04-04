from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request,'generator/home.html')

def password(request):

	chars=list('abcdefghijklmnopqrstuvwxyz')

	thepassword=''

	length=int(request.GET.get('length',12))

	if request.GET.get('capital'):
		chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('numbers'):
		chars.extend(list('1234567890'))
	if request.GET.get('spechar'):
		chars.extend(list('!@#$%^&*()'))

	for x in range(length):
		thepassword+=random.choice(chars)

	return render(request,'generator/pass.html',{'password':thepassword})

def about(request):
	return render(request,'generator/about.html')
