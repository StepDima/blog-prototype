from django.urls import path
from .views import (
    MainPageView,
    RegistrationView,
    LoginView,
    LogoutView,
    UserPostsView,
    PostCommentsView,
    AddCommentView,
    EditCommentView,
    AddPostView,
    EditPostView,
    PostDeleteView,
    CommentDeleteView,
)

urlpatterns = [
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('', MainPageView.as_view(), name='main_page'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<str:username>/', UserPostsView.as_view(), name='user_posts'),
    path('post/<int:post_id>/comments/', PostCommentsView.as_view(), name='post_comments'),
    path('comment/add/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    path('comment/add/<int:post_id>/<int:comment_id>/', AddCommentView.as_view(), name='add_reply'),
    path('comment/edit/<int:comment_id>/', EditCommentView.as_view(), name='edit_comment'),
    path('edit_post/<int:post_id>/', EditPostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]