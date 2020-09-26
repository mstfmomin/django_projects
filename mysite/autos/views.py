from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm, AutoForm

# Create your views here.

# create a view to see car
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


class AutoCreate(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = AutoForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = AutoForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        auto = form.save()
        return redirect(self.success_url)



# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class AutoUpdate(LoginRequiredMixin, View):
    model = Auto
    success_url = reverse_lazy('autos:all')
    template = 'autos/auto_form.html'

    def get(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(request.POST, instance=auto)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)



class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


class AutoDelete(LoginRequiredMixin, View):
    model = Auto
    success_url = reverse_lazy('autos:all')
    template = 'autos/auto_confirm_delete.html'

    def get(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto)
        ctx = {'auto': auto}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        auto.delete()
        return redirect(self.success_url)        