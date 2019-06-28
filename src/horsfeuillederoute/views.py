from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import HorsFeuilleDeRoute
from .forms import HorsFeuilleDeRouteModelForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


class HorsFeuilleDeRouteListView(ListView):
    template_name = 'horsfeuillederoute/horsfeuillederoute_list.html'
    queryset = HorsFeuilleDeRoute.objects.all()


class HorsFeuilleDeRouteCreateView(CreateView):
    template_name = 'horsfeuillederoute/horsfeuillederoute_create.html'
    form_class = HorsFeuilleDeRouteModelForm
    queryset = HorsFeuilleDeRoute.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_create_view(request):
        queryset = HorsFeuilleDeRoute.objects.all()
        context = {
            "feuillederoute_list": queryset
        }

        return render(request, "horsfeuillederoute/horsfeuillederoute_create.html", context)


    # def get_success_url(self):
    #     return '/'

class HorsFeuilleDeRouteDetailView(DetailView):
    template_name = 'horsfeuillederoute/horsfeuillederoute_detail.html'
    #queryset = FeuilleDeRoute.objects.all()
    # queryset = FeuilleDeRoute.objects.filter(id__gt=1)

    # def get_object(self):
    #     id_ = FeuilleDeRoute.objects.get(id=11)
    #     return get_object_or_404(FeuilleDeRoute, id=id_)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(HorsFeuilleDeRoute, id=id_)

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


class HorsFeuilleDeRouteUpdateView(UpdateView):
    template_name = 'horsfeuillederoute/horsfeuillederoute_create.html'
    form_class = HorsFeuilleDeRouteModelForm
    queryset = HorsFeuilleDeRoute.objects.all()

    # success_url = '/'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(HorsFeuilleDeRoute, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class HorsFeuilleDeRouteDeleteView(DeleteView):
    template_name = 'horsfeuillederoute/horsfeuillederoute_delete.html'
    #queryset = FeuilleDeRoute.objects.all()
    #queryset = FeuilleDeRoute.objects.filter(id__gt=1)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(HorsFeuilleDeRoute, id=id_)

    def get_success_url(self):
        return reverse('horsfeuillederoute:horsfeuillederoute-list')

