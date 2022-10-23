from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from markdown2 import Markdown
from django import forms
from . import util
import random




class NewTitleForm(forms.Form):
    title_entry_add = forms.CharField(required=True)
    description_add = forms.CharField(label = "Add Description", widget=forms.Textarea(attrs={"rows":2, "cols":10}), required=True)


def index(request):
    case_matching_list = []
    lower_case_list_entries = []
    if request.method == 'POST':
        substring = request.POST.get('q').lower()
        lower_case_list_entries = [item.lower() for item in util.list_entries()]
        case_matching_list = [i for i in lower_case_list_entries if substring in i]
        #print(case_matching_list)
        if len(case_matching_list) == 1:
            return HttpResponseRedirect("/wiki/" + case_matching_list[0])
        elif len(case_matching_list) > 1:
            return render(request, "encyclopedia/index.html", {
                "entries": [item.capitalize() for item in case_matching_list]
            })
        else:
            return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title_to_display(request, title):
    if request.method == 'POST':
        content = util.get_entry(title)
        form = NewTitleForm(request.POST)
        if form.is_valid():
            util.save_entry(form.cleaned_data['title_entry_add'], form.cleaned_data['description_add'])
            # return render(request, "encyclopedia/error.html", {
            #     "item_to_display": markdowner.convert(util.get_entry(title))
            # })
    else:
        entry_check = util.get_entry(title)
        if entry_check is None:
            return render(request, "encyclopedia/error.html")

    markdowner = Markdown()
    markdowner.convert(util.get_entry(title))

    return render(request, "encyclopedia/title.html", {
        "item_to_display": markdowner.convert(util.get_entry(title))
        })


def new_page(request):
    if request.method == 'POST':
        entryForm = NewTitleForm(request.POST)
        if entryForm.is_valid():
            #print(entryForm.cleaned_data)
            if entryForm.cleaned_data['title_entry_add'].lower() not in [item.lower() for item in util.list_entries()]:
                util.save_entry(entryForm.cleaned_data['title_entry_add'], entryForm.cleaned_data['description_add'])
                return HttpResponseRedirect("/wiki/" + entryForm.cleaned_data['title_entry_add'])
            else:
                return render(request, "encyclopedia/duplicate_entry.html")
        else:
            entryForm = NewTitleForm()

    return render(request, "encyclopedia/new_page.html", {
        "title_entry_form": NewTitleForm()
    })

def edit_page(request):
    if request.method == 'POST':
        title = request.META.get('HTTP_REFERER').split('/')[-1]
        content = util.get_entry(title)
        print(content)
        form = NewTitleForm(initial={'title_entry_add': title,'description_add':content})
        return render(request, 'encyclopedia/edit_page.html',{
            "edit_form": form,
            "title":title
        })

def random_entry(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect("/wiki/" + title)



    


    


