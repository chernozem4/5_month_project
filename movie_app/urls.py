from django.urls import path

from movie_app import views
urlpatterns = [
    path('director/', views.DirectorListCrateAPIView.as_view()),
    path('<int:id>/', views.DirectorDetailAPIView.as_view()),


    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),


    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),


    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view()),


    path('search_tag/', views.SearchTagViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('search_tag/<int:id>/', views.SearchTagViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    }))



]