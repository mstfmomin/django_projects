
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from cats.models import Breed,  Cat
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from cats.forms import BreedForm, CatForm


class CatList (LoginRequiredMixin, View) :
    def get(self, request) :
        br = Breed.objects.all().count()
        cl = Cat.objects.all()
        ctx = {'breed_count': br, 'cat_list': cl}
        return render (request, 'cats/cat_list.html', ctx)



class BreedList (LoginRequiredMixin, View) :
    def get(self, request) :
        br = Breed.objects.all()
        ctx = {'breed_list': br}
        return render (request, 'cats/breed_list.html', ctx)




class BreedEntry(LoginRequiredMixin, View) :

    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request) :
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)


    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)


class CatEntry(LoginRequiredMixin, View) :

    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request) :
        form = CatForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)


    def post(self, request):
        form = CatForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        cat = form.save()
        return redirect(self.success_url)



# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {'breed': breed}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)


class CatUpdate(LoginRequiredMixin, View):
    model = Cat
    success_url = reverse_lazy('cats:all')
    template = 'cats/cat_form.html'

    def get(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        form = CatForm(instance=cat)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        form = CatForm(request.POST, instance=cat)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class CatDelete(LoginRequiredMixin, View):
    model = Cat
    success_url = reverse_lazy('cats:all')
    template = 'cats/cat_confirm_delete.html'

    def get(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=cat)
        ctx = {'cat': cat}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)