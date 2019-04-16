from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from pets.models import Pet, Kind
from pets.forms import KindForm

# Create your views here.

class PetList(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Kind.objects.all().count();
        al = Pet.objects.all();
        ctx = { 'kind_count': mc, 'pet_list': al };
        return render(request, 'pets/pet_list.html', ctx)

class KindView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Kind.objects.all();
        ctx = { 'kind_list': ml };
        return render(request, 'pets/kind_list.html', ctx)

class KindCreate(LoginRequiredMixin, View):
    template = 'pets/kind_form.html'
    success_url = reverse_lazy('pets')
    def get(self, request) :
        form = KindForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = KindForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        kind = form.save()
        return redirect(self.success_url)

class KindUpdate(LoginRequiredMixin, View):
    model = Kind
    success_url = reverse_lazy('pets')
    template = 'pets/kind_form.html'
    def get(self, request, pk) :
        kind = get_object_or_404(self.model, pk=pk)
        form = KindForm(instance=kind)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        kind = get_object_or_404(self.model, pk=pk)
        form = KindForm(request.POST, instance = kind)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class KindDelete(LoginRequiredMixin, DeleteView):
    model = Kind
    success_url = reverse_lazy('pets')
    template = 'pets/kind_confirm_delete.html'

    def get(self, request, pk) :
        kind = get_object_or_404(self.model, pk=pk)
        form = KindForm(instance=kind)
        ctx = { 'kind': kind }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        kind = get_object_or_404(self.model, pk=pk)
        kind.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class PetCreate(LoginRequiredMixin,CreateView):
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pets')

class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pets')

class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    fields = '__all__'
    success_url = reverse_lazy('pets')
