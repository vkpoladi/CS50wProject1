from django.shortcuts import render
from django.http import HttpResponse
from . import util

#import installed Markdown2 and save in variable
#this will be used to convert markdown entry files to html
#pip install markdown2
from markdown2 import Markdown
markdowner = Markdown()


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