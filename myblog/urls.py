from django.urls import path
#from . import views
from .views import HomeView
from  .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/',AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name="delete-post"),
    path('add_category/',AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>',CategoryView, name="category"),
    path('category-list/',CategoryListView, name="category-list"),
    path('like/<int:pk>',LikeView, name="like_post"),
]