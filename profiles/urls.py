from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_create_view, name='create'),
    path('details/', views.ProfileDetailView.as_view(), name='details'),
    path('edit/', views.ProfileEditView.as_view(), name='edit'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete'),
]