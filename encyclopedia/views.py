from django.shortcuts import render
import markdown as md
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = md.markdown(util.get_entry(title))
    
    return render(request, "encyclopedia/entry.html", {
        "entry_title": title,
        "entry_content": html_content
    })

def search(request):
    results = []
    
    query = ''
       
    if request.method =="GET":
        query = request.GET.get('q')
        if query == '':
            query = 'None'
    entry = util.get_entry(query)
    if entry:
        reversed_url = reverse('entry', args={query})
        return HttpResponseRedirect(reversed_url)
    else:    
        results = util.search_entry(query)
        util.DEBUG(f"views.py: results={str(results)}")    
    return render(request, "encyclopedia/search_result.html", {
        "search_entry": query,
        "search_list":results
    })


