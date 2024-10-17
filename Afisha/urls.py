from django.contrib import admin
from django.urls import path
from django.urls import path, include

import movie_app
import users
from movie_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movie_app/', include('movie_app.urls')),


    # directors
    # path('api/v1/director/', include(movie_app.urls)),
    # path('api/v1/director/<int:id>/', include(movie_app.urls)),
    #
    # # movies
    # path('api/v1/movies/', include(movie_app.urls)),
    # path('api/v1/movies/<int:id>/', include(movie_app.urls)),
    #
    # # reviews
    # path('api/v1/reviews/', include(movie_app.urls)),
    # path('api/v1/reviews/<int:id>/', include(movie_app.urls)),
    path('api/v1/users/', include('users.urls')),

    # Optional: Root URL for the API
    # path('', views.api_root),  # Add this to handle the empty path
]
