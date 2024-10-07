from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Category(AbstractModel):
    view_count = models.IntegerField(default=0)


class SearchTag(AbstractModel):
    pass

class Director(models.Model):
    name = models.CharField(max_length=195, null=True)


    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=195, null=True)
    description = models.TextField( null=True)
    duration = models.IntegerField( null=True)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE, null = True )
    genre = models.ForeignKey(Category, on_delete=models.CASCADE,
                              null=True)
    tags = models.ManyToManyField(SearchTag, blank=True, null=True)

    def __str__(self):
        return self.title

STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),

)

class Review(models.Model):
    text = models.TextField( null=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    stars = models.IntegerField(choices=STARS, null=True, default=5)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='all_reviews', null=True)


    def __str__(self):
        return f"Review for {self.movie.title}"


