# Created by mdobaid
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print(request.GET.get('text', 'default'))
    return render(request, 'index.html')


def analyze(request):
    #Ge the text
    text = request.GET.get('text', 'default')
    
    #Checkbox valuse
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    characterCounter = request.GET.get('charactercounter')
    
    analyzed_text = ""
    if removepunc == 'on':
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~/"
        for char in text:
            if char not in punctuations:
                analyzed_text += char
    if fullcaps == 'on':
        analyzed_text=analyzed_text.upper()
    if characterCounter == 'on':
        text=analyzed_text
        analyzed_text = f"The length of string {text} is {len(analyzed_text)}"
    else:
        analyzed_text = text
    params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed_text}
    return render(request, 'analyze.html', params)
