from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from social import models,forms
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

class Wall(LoginRequiredMixin, ListView):
    #queryset = models.Post.objects.all()
    template_name = "social/wall.html"
    context_object_name = "posts"
    login_url = "login/"

    def get_queryset(self):
        return models.Post.objects.filter(
            (Q(user__person1 = self.request.user.pk) or Q(user__person2 = self.request.user.pk)) and ~Q(user = self.request.user)
        ).order_by("-created_at")

class Profile(LoginRequiredMixin, ListView):
    login_url = "login/"
    template_name = "social/profile.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user).order_by("-created_at")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data["post_form"] = forms.PostForm()
        return data

class Post(View):
    def post(self, request):
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()

        return redirect("/profile/")

class PostLike(View):
    model = models.Post
    def post(self, request, pk):
        models.Like.objects.create(post=self.model.objects.get(pk = pk), user=request.user)
        return HttpResponse(code = 204)

class PostComment(View):
    model = models.Post
    form = forms.PostComment
    def post(self, request, pk):
        post = self.model.objects.get(pk = pk)
        form = self.form(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponse(code = 204)
        print(form.errors)
        return HttpResponse(code = 400)
