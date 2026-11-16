from django.urls import path, include
from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movies/', include([
        path('create/', views.MovieCreateView.as_view(), name='create'),
        path('genres/create/', views.GenreCreateView.as_view(), name='genre_create'),
        path('genres/<int:pk>/delete/', views.genre_delete, name='genre_delete'),
        path('<int:pk>/', include([
            path('', views.MovieDetailView.as_view(), name='details'),
            path('edit/', views.MovieEditView.as_view(), name='edit'),
            path('delete/', views.MovieDeleteView.as_view(), name='delete'),
        ]))
    ]))
]
