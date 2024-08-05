from django.contrib import admin
from .models import Book,Author
# Register your models here.
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display=['title','pub_date','author']

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display=['name','dob']