from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=16)

    def __str__(self):
        return f"({self.username})"

class Artist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    
class Track(models.Model):
    id = models.BigAutoField(primary_key=True)
    isrc = models.CharField(length=12, unique=True)

class Album(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)


# FALTA IMPLEMENTAR OS MODELOS - UMA FAIXA -> UM -> ALBUM -> MUITOS ARTISTAS -> PAIS OU REGIÃO de lançamento

# class Category(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     category = models.CharField(max_length=64)

#     def __str__(self):
#         return f"{self.category}"


# class Product(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=64)
#     description = models.CharField(max_length=128, blank=True)
#     category = models.ForeignKey(
#         Category, 
#         default=0, 
#         on_delete=models.SET_DEFAULT, 
#         related_name='related'
#     )
#     img_url = models.URLField()
#     created_at_at = models.DateTimeField(auto_now_add=True)

# class Listing(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(max_length=64, blank=True)
#     minimum_bid = models.DecimalField(max_digits=24, decimal_places=2)
#     watchlist = models.ManyToManyField(User, blank=True, related_name='watchlist')
#     finished_at = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Bid(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     bid_value = models.DecimalField(max_digits=24, decimal_places=2) 
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
#     created_at = models.DateTimeField(auto_now_add=True)

# class Comment(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     comment = models.CharField(max_length=300)
#     autor = models.ForeignKey(User, default=0,on_delete=models.SET_DEFAULT)
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)