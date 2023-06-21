from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Comment
from .form import CommentForm, PostForm
from django.views import View
from .models import Post


class EditPostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        form = PostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_comments', post_id=post_id)
        return render(request, 'blog/edit_post.html', {'form': form})


class AddPostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/add_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_posts', username=request.user.username)
        return render(request, 'blog/add_post.html', {'form': form})


class PostCommentsView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)
        return render(request, 'blog/post_comments.html', {'post': post, 'comments': comments})


class UserPostsView( View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user)
        context = {
            'username': username,
            'posts': posts,
        }
        return render(request, 'blog/user_posts.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main_page')


class RegistrationView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'blog/registration.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        return render(request, 'blog/registration.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'blog/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        return render(request, 'blog/login.html', {'form': form})


class MainPageView(View):
    def get(self, request):
        all_posts = Post.objects.all().order_by('-time_create')
        paginator = Paginator(all_posts, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        return render(request, 'blog/main_page.html', {'posts': page, 'user': request.user})


class AddCommentView(View):
    def get(self, request, post_id=None, comment_id=None):
        form = CommentForm()
        return render(request, 'blog/add_comment.html', {'form': form, 'post_id': post_id, 'comment_id': comment_id})

    def post(self, request, post_id=None, comment_id=None):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = post_id
            if comment_id:
                comment.related_comment_id = comment_id
            comment.save()
            return redirect('post_comments', post_id=post_id)
        return render(request, 'blog/add_comment.html', {'form': form, 'post_id': post_id, 'comment_id': comment_id})


class EditCommentView(View):
    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(instance=comment)
        return render(request, 'blog/edit_comment.html', {'form': form, 'comment_id': comment_id})

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('post_comments', post_id=comment.post_id)
        return render(request, 'blog/edit_comment.html', {'form': form, 'comment_id': comment_id})


class PostDeleteView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author == request.user:
            post.delete()
        return redirect('main_page')


class CommentDeleteView(View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author == request.user or comment.post.author == request.user:
            comment.delete()
        return redirect('post_comments', post_id=comment.post.pk)