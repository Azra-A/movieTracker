from django.urls import path, include
from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('create/movie-<int:movie_pk>/', views.ReviewCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('details/', views.ReviewDetailView.as_view(), name='details'),
        path('edit/', views.ReviewEditView.as_view(), name='edit'),
        path('delete/', views.ReviewDeleteView.as_view(), name='delete'),
    ]))
]