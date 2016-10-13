from django.forms import ModelForm
from .models import Box, Filebox
from django.contrib.auth.models import User


class BoxCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(BoxCreateForm, self).__init__(*args, **kwargs)
        self.fields["members"].queryset = User.objects.exclude(id=self.request.user.id)

    class Meta:
        model = Box
        fields = ['name', 'members']


class FileboxCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FileboxCreateForm, self).__init__(*args, **kwargs)
        self.fields["box"].queryset = Box.objects.filter(members=self.request.user)

    class Meta:
        model = Filebox
        fields = ['name', 'file_box', 'box']
