from django.urls import path

from movie_app import views
urlpatterns = [
    path('director/', views.director_list_create_api_view),
    path('<int:id>/', views.director_detail_api_view),
    path('movies/', views.movies_list_create_api_view),
    path('movies/<int:id>/', views.movies_detail_api_view),

    # reviews
    path('reviews/', views.reviews_list_create_api_view),
    path('reviews/<int:id>/', views.reviews_detail_api_view),


]