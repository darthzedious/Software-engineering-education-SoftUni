from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from FurryFunnies.post_app.forms import PostCreateForm, PostEditForm, PostDeleteForm
from FurryFunnies.post_app.models import Post
from FurryFunnies.utils.get_profile import get_author_obj


# Create your views here.


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post/details-post.html'
    pk_url_kwarg = 'post_id'
    # context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_author_obj()
        return super().form_valid(form)

class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'post_id'
    template_name = 'post/edit-post.html'
    success_url = reverse_lazy('dashboard')

class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)