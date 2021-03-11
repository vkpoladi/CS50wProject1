from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django import forms

#import installed Markdown2 and save in variable
#this will be used to convert markdown entry files to html
#pip install markdown2
from markdown2 import Markdown
markdowner = Markdown()

#Create form class to use for new.html page
class NewPageForm(forms.Form):
    new_title = forms.CharField(label="Entry Title")
    new_text = forms.CharField(label="Entry Text")


# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    md_entry = util.get_entry(title)
    if md_entry == None:
        return HttpResponse(f"ERROR: {title} page not found in Encyclopedia")
    else:
        return render(request, "encyclopedia/entries.html", {
            "title":markdowner.convert(md_entry),
            "heading":title
    })

def search(request):
    title = request.GET["q"]
    md_entry = util.get_entry(title)
    if util.get_entry(title) != None:
        return render(request, "encyclopedia/entries.html", {
            "title":markdowner.convert(md_entry),
            "heading":title
        })
    else:
        entries = util.list_entries()
        similar_entries = []
        for entry in entries:
            if title in entry:
                similar_entries.append(entry)

        return render(request, "encyclopedia/search.html", {
            "search_word":title,
            "similar_entries": similar_entries 
        })

def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            new_title = form.cleaned_data["new_title"]
            new_text = form.cleaned_data["new_text"]
            entries = util.list_entries()

            if new_title not in entries:
                util.save_entry(new_title,new_text)
                md_entry = util.get_entry(new_title)
                return render(request, "encyclopedia/entries.html", {
                    "title":markdowner.convert(md_entry),
                    "heading":new_title
                })
            else:
                return HttpResponse("Error. Encyclopedia entry already exists.")

        else:   
            return render(request, "encyclopedia/new.html", {
                "form":form
            })
    
    return render(request, "encyclopedia/new.html", {
        "form":NewPageForm()
    })
