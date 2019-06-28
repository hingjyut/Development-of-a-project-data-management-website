from django.shortcuts import render,get_object_or_404

from django.urls import reverse
from .forms import FeuilleDeRouteModelForm
from .models import FeuilleDeRoute
#from rest_framwork import
# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

#class FeuilleDeRouteView()


class TryFeuilleDeRouteListView(ListView):
    template_name = 'feuillederoute/contact.html'
    queryset = FeuilleDeRoute.objects.all()


#结束

class FeuilleDeRouteCreateView(CreateView):
    template_name = 'feuillederoute/feuillederoute_create.html'
    form_class = FeuilleDeRouteModelForm
    queryset = FeuilleDeRoute.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_create_view(request):
        queryset = FeuilleDeRoute.objects.all()
        context = {
            "feuillederoute_list": queryset
        }

        return render(request, "feuillederoute/feuillederoute_create.html", context)


    # def get_success_url(self):
    #     return '/'


class FeuilleDeRouteUpdateView(UpdateView):
    template_name = 'feuillederoute/feuillederoute_create.html'
    form_class = FeuilleDeRouteModelForm
    queryset = FeuilleDeRoute.objects.all()

    # success_url = '/'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(FeuilleDeRoute, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class FeuilleDeRouteDeleteView(DeleteView):
    template_name = 'feuillederoute/feuillederoute_delete.html'
    #queryset = FeuilleDeRoute.objects.all()
    #queryset = FeuilleDeRoute.objects.filter(id__gt=1)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(FeuilleDeRoute, id=id_)

    def get_success_url(self):
        return reverse('feuillederoute:feuillederoute-list')


class FeuilleDeRouteListView(ListView):
    template_name = 'feuillederoute/feuillederoute_list.html'
    queryset = FeuilleDeRoute.objects.all()

class FeuilleDeRouteDetailView(DetailView):
    template_name = 'feuillederoute/feuillederoute_detail.html'
    #queryset = FeuilleDeRoute.objects.all()
    # queryset = FeuilleDeRoute.objects.filter(id__gt=1)

    # def get_object(self):
    #     id_ = FeuilleDeRoute.objects.get(id=11)
    #     return get_object_or_404(FeuilleDeRoute, id=id_)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(FeuilleDeRoute, id=id_)

    # def feuillederoute_detail_view(request,id):
    #     obj = get_object_or_404(FeuilleDeRoute, id=id)  # get data from database
    #     # context = {
    #     #     'title': obj.title,
    #     #     'decription': obj.decription,
    #     # }
    #     context = {
    #         'object': obj
    #     }
    #     return render(request, 'index.html', context)

def homeindex_view(request, *args, **kwargs):
	context={}
	return render(request,'homeindex.html',context)