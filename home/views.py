from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from home.forms import RegiForm
from home.models import Datastrore, Friendlist


class home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        forms = RegiForm()
        datastore = Datastrore.objects.all().order_by('-created')

        users = User.objects.exclude(id=request.user.id)
        friend = Friendlist.objects.get(current_user=request.user)
        friends = friend.user.all()
        args = {'form': forms, 'post': datastore, 'user': users,'friend' : friends}
        return render(request, self.template_name, args)

    def post(self, request):
        froms = RegiForm(request.POST)
        if froms.is_valid():
            post = froms.save(commit=False)
            post.user = request.user
            froms.save()
            text = froms.cleaned_data['post']

        args = {'form': froms, 'text': text}

        return render(request, self.template_name, args)


def Create(request, operation, pk):
    friends = User.objects.get(pk=pk)
    if operation == 'add':
        Friendlist.Create_list(request.user, friends)
    elif operation == 'remove':
        Friendlist.Remove_list(request.user, friends)
    return redirect('home:home')
