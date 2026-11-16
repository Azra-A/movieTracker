from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from movies.models import Movie, Genre
from movies.forms import MovieCreateForm, MovieEditForm, MovieDeleteForm, GenreForm
from profiles.models import Profile


class HomeView(ListView):
    model = Movie
    template_name = 'home-page.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.all().order_by('-release_year', 'title')
        genre_filter = self.request.GET.get('genre')
        sort_by = self.request.GET.get('sort')

        if genre_filter:
            queryset = queryset.filter(genres__name=genre_filter)

        if sort_by == 'oldest':
            queryset = queryset.order_by('release_year')
        elif sort_by == 'title':
            queryset = queryset.order_by('title')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['genres'] = Genre.objects.all()
        context['selected_genre'] = self.request.GET.get('genre', '')
        context['selected_sort'] = self.request.GET.get('sort', '')
        return context


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/movie-add-page.html'
    success_url = reverse_lazy('movies:home')


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie-details-page.html'
    context_object_name = 'movie'


class MovieEditView(UpdateView):
    model = Movie
    form_class = MovieEditForm
    template_name = 'movies/movie-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('movies:details', kwargs={'pk': self.object.pk})


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie-delete-page.html'
    success_url = reverse_lazy('movies:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MovieDeleteForm(instance=self.object)
        return context


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre-add-page.html'
    success_url = reverse_lazy('movies:genre_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.order_by('name')
        return context


@require_POST
def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genre.delete()
    return redirect('movies:genre_create')

