from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='author_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.book.title}"
