from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('blog/', PostListView.as_view(), name='home'),
    path('blog/<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/new/', PostCreateView.as_view(), name='post-new'),
    path('blog/<int:pk>/<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('blog/<int:pk>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]