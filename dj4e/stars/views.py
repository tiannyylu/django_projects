from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from stars.models import Star, Constellation
from stars.forms import ConstellationForm

# Create your views here.

class StarList(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Constellation.objects.all().count();
        al = Star.objects.all();
        ctx = { 'constellation_count': mc, 'star_list': al };
        return render(request, 'stars/star_list.html', ctx)

class ConstellationView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Constellation.objects.all();
        ctx = { 'constellation_list': ml };
        return render(request, 'stars/constellation_list.html', ctx)

class ConstellationCreate(LoginRequiredMixin, View):
    template = 'stars/constellation_form.html'
    success_url = reverse_lazy('stars')
    def get(self, request) :
        form = ConstellationForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = ConstellationForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        constellation = form.save()
        return redirect(self.success_url)

class ConstellationUpdate(LoginRequiredMixin, View):
    model = Constellation
    success_url = reverse_lazy('stars')
    template = 'stars/constellation_form.html'
    def get(self, request, pk) :
        constellation = get_object_or_404(self.model, pk=pk)
        form = ConstellationForm(instance=constellation)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        constellation = get_object_or_404(self.model, pk=pk)
        form = ConstellationForm(request.POST, instance = constellation)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class ConstellationDelete(LoginRequiredMixin, DeleteView):
    model = Constellation
    success_url = reverse_lazy('stars')
    template = 'stars/constellation_confirm_delete.html'

    def get(self, request, pk) :
        constellation = get_object_or_404(self.model, pk=pk)
        form = ConstellationForm(instance=constellation)
        ctx = { 'constellation': constellation }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        constellation = get_object_or_404(self.model, pk=pk)
        constellation.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class StarCreate(LoginRequiredMixin,CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')

class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars')
