from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from movies.models import Movie
from profiles.models import Profile
from reviews.models import Review
from reviews.forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'reviews/review-add-page.html'

    def form_valid(self, form):
        movie = get_object_or_404(Movie, pk=self.kwargs['movie_pk'])
        profile = Profile.objects.first()
        if profile is None:
            form.add_error(None, 'Create a profile before writing a review.')
            return self.form_invalid(form)

        form.instance.movie = movie
        form.instance.profile = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = get_object_or_404(Movie, pk=self.kwargs['movie_pk'])
        context['profile'] = Profile.objects.first()
        return context

    def get_success_url(self):
        return reverse_lazy('movies:details', kwargs={'pk': self.kwargs['movie_pk']})


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review-details-page.html'
    context_object_name = 'review'


class ReviewEditView(UpdateView):
    model = Review
    form_class = ReviewEditForm
    template_name = 'reviews/review-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('movies:details', kwargs={'pk': self.object.movie.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews/review-delete-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewDeleteForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('movies:details', kwargs={'pk': self.object.movie.pk})
