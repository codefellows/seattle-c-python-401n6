from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from .models import Thing
from .forms import ThingCreateForm, ThingUpdateForm


class ThingListView(ListView):
    template_name = "things-list.html"
    model = Thing
    context_object_name = 'things'


class ThingDetailView(DetailView):
    template_name = "things-detail.html"
    model = Thing


class ThingCreateView(CreateView):
    template_name = "things-create.html"
    model = Thing
    form_class = ThingCreateForm


class ThingUpdateView(UpdateView):
    template_name = "things-update.html"
    model = Thing
    form_class = ThingUpdateForm


class ThingDeleteView(DeleteView):
    template_name = "things-delete.html"
    model = Thing
    success_url = reverse_lazy("thing_list")


class ThingAboutView(TemplateView):
    template_name = "things-about.html"
