from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework import mixins
from .forms import *
from .serializers import *
from django.views.generic import UpdateView, DetailView

# Create your views here.
"""Edit  user"""


class CreateUserUpdate(UpdateView):
    model = CreatedUsers
    fields = ['username', 'groups']
    template_name = 'main/FirstPage.html'


"""Edit group"""


class CreateGroupUpdate(UpdateView):
    model = CreatedGroup
    fields = ['group']
    template_name = 'main/SecondPage.html'


""" for user templates"""


class FirstPage(generics.GenericAPIView,
                mixins.CreateModelMixin,
                mixins.ListModelMixin,
                ):
    serializer_class = CreateUsersSerializer
    queryset = CreatedUsers.objects.all()

    @staticmethod
    def get(request):
        form = CreateUsersForm
        model = CreatedUsers.objects.all().values('id', 'username', 'created_date', 'groups__group')
        data = {'form': form,
                'model': model}
        CreatedUsers.objects.filter(id=request.GET.get('delete')).delete()
        return render(request, "main/FirstPage.html", data)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return redirect('first_page')


"""class for group templates"""


class SecondPage(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = CreatedGroup.objects.all()
    serializer_class = CreateGroupSerializer

    @staticmethod
    def get(request):
        form = CreateGroupForm
        model = CreatedGroup.objects.values()
        data = {'model': model,
                'form': form}
        CreatedGroup.objects.filter(id=request.GET.get('delete_group')).delete()
        return render(request, 'main/SecondPage.html', data)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return redirect('second_page')
