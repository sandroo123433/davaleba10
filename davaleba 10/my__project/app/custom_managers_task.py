from django.core.management.base import BaseCommand
from myapp.models import Category, Product, Tag

class Command(BaseCommand):
    help = "Executes custom manager methods and prints results"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Executing custom manager methods..."))

       
        categories = Category.objects.with_item_count()
        self.stdout.write(self.style.SUCCESS("\nCategories with Item Count:"))
        for category in categories:
            self.stdout.write(f" {category.name},  {category.item_count}")

        
        products = Product.objects.with_tag_count()
        self.stdout.write(self.style.SUCCESS("\nProducts with Tag Count:"))
        for product in products:
            self.stdout.write(f" {product.name},  {product.tags_count}")

      
        min_items = 2
        popular_tags = Tag.objects.popular_tags(min_items)
        self.stdout.write(self.style.SUCCESS(f"\nPopular Tags (min {min_items} items):"))
        for tag in popular_tags:
            self.stdout.write(f" {tag.name}, {tag.product_count}")

        self.stdout.write(self.style.SUCCESS(" Custom manager methods executed successfully!"))
