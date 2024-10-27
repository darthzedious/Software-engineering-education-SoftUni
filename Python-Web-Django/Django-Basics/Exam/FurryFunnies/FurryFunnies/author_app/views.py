from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunnies.author_app.forms import AuthorCreateForm, AuthorEditForm
from FurryFunnies.author_app.models import Author
from FurryFunnies.utils.get_profile import get_author_obj


class CreateAuthorView(CreateView):
    model = Author
    template_name = 'author/create-author.html'
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dashboard')

class DetailsAuthorView(DetailView):
    template_name = 'author/details-author.html'

    def get_object(self, queryset=None):
        return get_author_obj()


# class EditAuthorView(UpdateView):
#     template_name = 'author/edit-author.html'
#     model = Author
#     form_class = AuthorEditForm
#     success_url = reverse_lazy('details-author')
#
def edit_profile(request):
    profile = get_author_obj()

    form = AuthorEditForm(instance=profile)
    if request.method == 'POST':
        form = AuthorEditForm(request.POST, instance=profile)
        if form.is_valid():

            form.save()

            return redirect('details-author')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'author/edit-author.html', context)


class AuthorDeleteView(DeleteView):
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author_obj()