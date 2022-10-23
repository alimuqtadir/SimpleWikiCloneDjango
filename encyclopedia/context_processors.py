from ast import Name
from django import forms
from django.shortcuts import render, HttpResponseRedirect

class NameForm(forms.Form):
    search_entry = forms.CharField(label="search", max_length=20)

# def search_for_entry(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             print(form.cleaned_data)
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             #return HttpResponseRedirect('/thanks/')
#             print("its done")
#             return HttpResponseRedirect(form.cleaned_data["search_entry"])

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         return render(request, "encyclopedia/index.html", {
#         "form" : NameForm()
#         })
        


def search_for_entry(request):
    return {'form': NameForm()}