from django.views.generic import TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Box, Filebox
from .forms import BoxCreateForm, FileboxCreateForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['boxes'] = self.request.user.box_set.all()
        return context


class BoxCreate(CreateView):
    model = Box
    form_class = BoxCreateForm
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(BoxCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        super(BoxCreate, self).form_valid(form)
        self.object.members.add(self.request.user)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class FileboxCreate(CreateView):
    model = Filebox
    form_class = FileboxCreateForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.upload_by = self.request.user
        return super(FileboxCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(FileboxCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
