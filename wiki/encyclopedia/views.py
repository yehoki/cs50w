from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
from markdown2 import Markdown
import random


class NewTaskForm(forms.Form):
    entry_title = forms.CharField(label="Title")
    entry_content = forms.CharField(widget = forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    if util.get_entry(title) == None:
        return Http404
    else:
        markdowner = Markdown()
        get_entry = util.get_entry(title)
        get_entry = markdowner.convert(get_entry)
        return render(request, "encyclopedia/title.html", {
            "texting": get_entry, "title": title
        })


def edit_page(request, title):

    if request.method == "POST":

        form = NewTaskForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["entry_title"]

            content = form.cleaned_data["entry_content"]

            util.save_entry(title, content)

            return HttpResponseRedirect(reverse("index"))

    else:
        current_text = util.get_entry(title)
        form = NewTaskForm({'entry_title': title, 'entry_content': current_text})
        return render(request, "encyclopedia/edit.html",{
            "form": form
        })

def new_page(request):
    if request.method == "POST":
    
        form = NewTaskForm(request.POST)
        if form.is_valid():
            
            title = form.cleaned_data["entry_title"]
            
            content = form.cleaned_data["entry_content"]
            
            util.save_entry(title, content)
            
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "encyclopedia/new_page.html", {
            "form": NewTaskForm()
        })


def search(request):

    query_dict = request.GET
    query = query_dict.get("q").lower()
    entries = util.list_entries()
    query_list = []
    for entry in entries:
        if query in entry.lower():
            query_list.append(entry)
    return render(request, "encyclopedia/search.html",{
        "entries": query_list
    })

def random_page(request):
    number = util.list_entries()
    random_number = random.randint(0, len(number) - 1)
    entry = Markdown().convert(util.get_entry(number[random_number]))

    return render(request, "encyclopedia/title.html",{
        "title": number[random_number], "texting": entry
    })