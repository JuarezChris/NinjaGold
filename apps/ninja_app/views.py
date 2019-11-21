from django.shortcuts import render, redirect
import random


def index(request):
    if 'goldcreated' in request.session:
        request.session['gold'] = request.session['gold'] + request.session['goldcreated']
    else:
        request.session['goldcreated'] = 0
        request.session['gold'] = 0
    return render(request, 'ninja_app/ninja_money.html')


def process_money(request):
        if request.POST['building'] == 'farm':
            request.session['goldcreated'] = random.randint(10, 20)  
        if request.POST['building'] == 'cave':
            request.session['goldcreatd'] = random.randint(5, 10)
        if request.POST['building'] == 'House':
            request.session['goldcreated'] = random.randint(2, 5)
        if request.POST['building'] == 'Casino':
            request.session['goldcreated'] = random.randint(-50, 50)
        return redirect('/')

def destroy(request):
    request.session.flush()
    return redirect('/')
