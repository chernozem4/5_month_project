from django.contrib import admin
from django.urls import path
from movie_app import views
from movie_app.views import director_list_api_view, director_detail_api_view, movies_list_api_view, movies_detail_api_view, reviews_list_api_view, reviews_detail_api_view
urlpatterns = [
    path('admin/', admin.site.urls),

    #directors
    path('api/v1/director', views.director_list_api_view),
    path('api/v1/director/<int:id>/', views.director_detail_api_view),

    #movies
    path('api/v1/movies', views.movies_list_api_view),
    path('api/v1/movies/<int:id>/', views.movies_detail_api_view),

    #reviews
    path('api/v1/reviews', views.reviews_list_api_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_api_view)
]
