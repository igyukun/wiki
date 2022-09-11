import re
import datetime as d
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def search_entry(query):
    """
    The function returns a list of all entries
    containing the requested string as a substring. Otherwise None is returned.
    """
    search_results = []
    
    for entry in list_entries():
        if entry.lower().find(query.lower()) != -1:
            search_results.append (entry)
            
    if len(search_results) == 0:
        # DEBUG(f"utils.py: {search_results}")
        return None
    else:
        # DEBUG(f"utils.py: {search_results}")
        return search_results


def DEBUG(txt):
    """_summary_
    This function prints text, passed as an argument into the 
    'debug.txt' file, preceeded with the current timestamp
    Args:
        txt (string): debug text
    """
    with open('debug.txt', 'a') as f:
        f.write(f"{d.datetime.now()}:{txt}\n")
