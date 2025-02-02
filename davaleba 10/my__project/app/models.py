from django.db import models
from django.db.models import Count

class CategoryManager(models.Manager):
    def with_item_count(self):
        return self.annotate(item_count=Count('products'))  

class Category(models.Model):
    name = models.CharField(max_length=255)

    objects = CategoryManager()  

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
categories = Category.objects.with_item_count()

for category in categories:
    print(f" {category.name},  {category.item_count}")

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def with_tag_count(self):
        return self.annotate(tags_count=Count('tags')) 

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', related_name="products", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="products")  
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProductManager()  

    def __str__(self):
        return self.name

products = Product.objects.with_tag_count()

for product in products:
    print(f" {product.name}, {product.tags_count}")




class TagManager(models.Manager):
    def popular_tags(self, min_items):
        return self.annotate(product_count=Count('products')).filter(product_count__gte=min_items)

class Tag(models.Model):
    name = models.CharField(max_length=255)

    objects = TagManager() 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', related_name="products", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="products")  
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


popular_tags = Tag.objects.popular_tags(2)

for tag in popular_tags:
    print(f" {tag.name},  {tag.product_count}")

