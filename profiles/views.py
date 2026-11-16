from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView
from profiles.models import Profile
from profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm


def get_profile():
    return Profile.objects.first()


def profile_create_view(request):
    profile = get_profile()
    if profile:
        return redirect('profiles:details')

    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.activated_at = timezone.now().date()
            new_profile.save()
            return redirect('movies:home')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create-page.html', context)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details-page.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['reviews'] = self.object.reviews.select_related('movie').all()
            context['reviews_count'] = self.object.reviews.count()
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit-page.html'
    success_url = reverse_lazy('profiles:details')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile-delete-page.html'
    success_url = reverse_lazy('movies:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfileDeleteForm(instance=self.object)
        return context

    def get_object(self, queryset=None):
        return get_profile()
