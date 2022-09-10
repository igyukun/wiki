from django.shortcuts import render
import markdown as md
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
    # with open('search.txt', 'w') as f:
    #     f.write("started\n")
    query = ''
       
    if request.method =="GET":
        query = request.GET.get('q')
        if query == '':
            query = 'None'
        
        # with open('search.txt', 'a') as f:
        #     f.write(query)
    
    util.search_entry(query)
            
    return render(request, "encyclopedia/search_result.html", {
        "search_entry": query
        # "   ": html_content
    })
