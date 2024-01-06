from django.urls import path
from .views import PostListView,PostDetailView

app_name = 'blog'  # here for namespacing of urls.it was not in chp 5 i added it purposely


urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
]
