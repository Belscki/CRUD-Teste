from django.urls import path
from . import views

urlpatterns = [
    path("postblog/", views.PostBlogListCreate.as_view(), name="postblog-view-create")
]

