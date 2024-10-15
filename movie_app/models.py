from django.db import models


# Abstract model to share common fields across other models
class AbstractModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

# Category model inheriting from AbstractModel
class Category(AbstractModel):
    view_count = models.IntegerField(default=0)

# SearchTag model inheriting from AbstractModel
class SearchTag(AbstractModel):
    pass

# Director model with a foreign key to Category
class Director(models.Model):
    name = models.CharField(max_length=195, null=True, blank=True)  # Added blank=True for forms
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Movie model with a many-to-many relationship to SearchTag and a foreign key to Director
class Movie(models.Model):
    title = models.CharField(max_length=195, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(null=True)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(SearchTag, blank=True)

    created =models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            total_stars = sum(review.stars for review in reviews)
            return total_stars / reviews.count()
        return None  # Or return 0 or any default value you prefer

# Tuple for review star ratings
STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
)

# Review model with stars, text, and foreign keys to Movie and Director
class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    stars = models.IntegerField(choices=STARS, default=5)
    is_active_reviews = models.BooleanField(default=True)
    created_review= models.DateTimeField(null=True
                                         )
    review_update = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"Review for {self.movie.title}"
