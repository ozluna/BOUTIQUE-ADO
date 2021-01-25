from django.db import models

# Create your models here.
# null=True means is optional


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    # friendly name is for the friendly looking on the front
    # end which is already in the json file name and
    # friendly_name fields

    def __str__(self):
        return self.name
        # We'll also create a string method here.
        # Which takes in the category model itself.
        # And just returns self.name

    def get_friendly_name(self):
        return self.friendly_name
        # I'm also going to make a quick model method here which is the same
        #  thing as the string method
        # except this one is going to return the friendly name if we want it.
        # so return self.friendly_name.


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # each product requires a name, a description, and a price.
    # everything else is optional with null = true

    def __str__(self):
        return self.name
