from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    stock = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='books/', blank=True)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    def total_price(self):
        return self.book.price * self.quantity


