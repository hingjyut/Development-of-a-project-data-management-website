from django.shortcuts import render
from .models import Membre
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MembreForm

def membre_create_view(request):
    form = MembreForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MembreForm()
    context = {
        'form': form
    }
    return render(request, "membre/membre_create.html", context)


def membre_detail_view(request,id):
    obj = get_object_or_404(Membre, id=id) #get data from database
    # context = {
    #     'title': obj.title,
    #     'decription': obj.decription,
    # }
    context = {
        'object': obj
    }
    return render(request, "membre/membre_detail.html", context)


#deleting project from database
def membre_delete_view(request, id):
    obj = get_object_or_404(Membre, id=id)
    #POST request
    if request.method == "POST":
        #confirming delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "membre/membre_delete.html", context)


def membre_list_view(request):
    queryset = Membre.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "membre/membre_list.html", context)


def membre_update_view(request, id=id):
    obj = get_object_or_404(Membre, id=id)
    form = MembreForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context= {
            'form': form
        }
    return render(request,"membre/membre_create.html", context)


def render_initial_data(request):
    initial_data = {
        'nom': "My this awesome title"
    }
    obj = Membre.objects.get(id=1)
    form = MembreForm(request.POST or None, initial= initial_data, instance= obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "membre/membre_create.html", context)


def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product,id=id)
    try:
        obj = Membre.objects.get(id=id)
    except Membre.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "membre/membre_detail.html", context)
