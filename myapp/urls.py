from django.urls import path
from .views import AllPostListView, CreatePostView, MyPostListView, PostDetailView, LikePostView, CommentView

urlpatterns = [
    path('allpost/', AllPostListView.as_view(), name='all-posts'),               
    path('create/', CreatePostView.as_view(), name='create-post'),         
    path('myposts/', MyPostListView.as_view(), name='my-posts'),                
    path('myposts/<int:pk>/', PostDetailView.as_view(), name='edit-delete-post'),  
    path('like/<int:pk>/', LikePostView.as_view(), name='like-post'),  
    path('comment/<int:pk>/', CommentView.as_view(), name='comment-post'),  
]
