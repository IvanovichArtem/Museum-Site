from django.db import models
from user.models import User


# Create your models here.
class ExhibitionType(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name

class Exhibition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age_limit = models.IntegerField(default=16)
    place = models.CharField(max_length=40, default='Музей')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    img = models.ImageField(upload_to="exhibition_images")
    type = models.ForeignKey(to="ExhibitionType", on_delete=models.CASCADE)
    tickets_quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class BasketQuerrySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    
    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerrySet.as_manager()
    
    def __str__(self) -> str:
        return f"User {self.user} | Exhibition {self.exhibition}"
    
    def sum(self):
        return self.exhibition.price * self.quantity
    