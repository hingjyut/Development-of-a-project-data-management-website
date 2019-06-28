from django.shortcuts import render
from .models import Direction
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DirectionForm

def direction_create_view(request):
    form = DirectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DirectionForm()
    context = {
        'form': form
    }
    return render(request, "direction/direction_create.html", context)


def direction_detail_view(request,id):
    obj = get_object_or_404(Direction, id=id) #get data from database
    # context = {
    #     'title': obj.title,
    #     'decription': obj.decription,
    # }
    context = {
        'object': obj
    }
    return render(request, "direction/direction_detail.html", context)


#deleting project from database
def direction_delete_view(request, id):
    obj = get_object_or_404(Direction, id=id)
    #POST request
    if request.method == "POST":
        #confirming delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "direction/direction_delete.html", context)


def direction_list_view(request):
    queryset = Direction.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "direction/direction_list.html", context)


def direction_update_view(request, id=id):
    obj = get_object_or_404(Direction, id=id)
    form = DirectionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context= {
            'form': form
        }
    return render(request,"direction/direction_create.html", context)


def render_initial_data(request):
    initial_data = {
        'nom': "My this awesome title"
    }
    obj = Direction.objects.get(id=1)
    form = DirectionForm(request.POST or None, initial= initial_data, instance= obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "direction/direction_create.html", context)


def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product,id=id)
    try:
        obj = Direction.objects.get(id=id)
    except Direction.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "direction/direction_detail.html", context)
