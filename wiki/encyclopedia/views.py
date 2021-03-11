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
