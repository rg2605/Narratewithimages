from django.shortcuts import render
import os
import json
from django.utils import timezone
#from .synth import Synthesizer, checkpoint
from main import imager
from .forms import ContentForm
from .models import Images
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile 

def home(request):
    if request.method == "POST":
        form=ContentForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            print('post = =', post.text)
            
            x = post.text
            documents = imager(x)
            print('documents done')
            print('docs = ', documents)
            imagecount = len(documents)
            #Synthesizer.synthesize(post.text,post.title)
            return render(request , 'narration/list.html' , {'documents':documents , 'imagecount' : imagecount, "form":form})
    else:    
        form=ContentForm()
    return render(request, "narration/home.html", {"form":form})
