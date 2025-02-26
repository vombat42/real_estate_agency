from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView

from .forms import EstateCreateForm
from .models import Estate


def index(request):
    return render(request, 'realtor/home.html', context={'title': 'Риелтор - Главная',})

# PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView
class EstateCreateView(CreateView):
    form_class = EstateCreateForm
    template_name = 'realtor/create.html'
    title_page = 'Добавление объекта недвижимсоти'
    permission_required = 'realtor.create_estate' # <приложение>.<действие>_<таблица>
    extra_context = {
        'title': 'Добавление объекта',
    }

    def form_valid(self, form):
        estate = form.save(commit=False)
        if not estate.creator:
            estate.creator = self.request.user
        estate.modifier = self.request.user
        return super().form_valid(form)


class EstateCreateView2(CreateView):
    model = Estate
    fields = '__all__'
    template_name = 'realtor/create2.html'
    success_url = reverse_lazy('realtor:home')
    extra_context = {
        'title': 'Добавление объекта',
    }


class ShowEstate(DetailView):
    model = Estate
    template_name = 'realtor/estate.html'
    slug_url_kwarg = 'estate_slug'
    context_object_name = 'estate'


class EstatesList(LoginRequiredMixin, ListView):
    model = Estate
    template_name = 'realtor/home.html'
    context_object_name = 'estates'
    extra_context = {
        'title': 'Риэлтор - Главная страница',
        # 'styles': 'tasks/css/styles.css',
    }
