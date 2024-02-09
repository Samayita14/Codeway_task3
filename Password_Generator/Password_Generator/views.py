from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def homepage(request):
    return render(request, 'index.html')

def generatepwd(request):
    length=int(request.POST.get('charlen'))
    letters = string.ascii_letters
    spc = string.punctuation

    pwd = ""
    letters+=spc
    while len(pwd)<length:
        c = random.choice(letters)
        pwd+=c

    data={'pwdlength':length,'password':pwd}
    return render(request, 'index.html', data)
