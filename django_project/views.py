# I HAVE CREATED THIS FILE - HENIL
from django.http import HttpResponse
from django.shortcuts import render

def index(request) :
    return render(request,'index.html')

def analyzer(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    removeSpace = request.POST.get('removeSpace','off')
    charCount = request.POST.get('charCount','off')

    punctuations = '''.,?!:;'"-–—()[]{}/\..@#$%&*_+=<>^~|`«»…§¶©®™°•'''
    count=0
    
    if removepunc == 'on' :
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
                'purpose':'Remove Punctuations',
                'analyzed_text':analyzed,
                'count':count
            }
        djtext = analyzed

    if uppercase == "on" :
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {
                'purpose':'Remove Punctuations',
                'analyzed_text':analyzed,
                'count':count
            }
        djtext = analyzed

    if removeSpace == "on" :
        analyzed = ""
        for char in djtext:
            if char not in " ":
                analyzed = analyzed + char

        params = {
                'purpose':'Remove Punctuations',
                'analyzed_text':analyzed,
                'count':count
            }
        djtext = analyzed

    if charCount == "on":
        for char in djtext:
            count = count + 1

        params = {
                'purpose':'Remove Punctuations',
                'analyzed_text':analyzed,
                'count':count
            }
        djtext = analyzed
    
    if removepunc != "on" and removeSpace != "on" and uppercase != "on" and charCount != "on" :
        return HttpResponse('ERROR')
    

    return render(request,'analyze.html',params)