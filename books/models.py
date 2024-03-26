from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2) # Mony(ashar) -> decimal
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) #if book was deleted the comment also delete too.
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments') # yani in class chiye Book mishe? => comments pas ketab3.comments => miad mibine ke baraye ketab3 che text hast neshon mide.
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recomend = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

