from django.contrib import admin
from .models import (BookModel, AuthorModel, BookCategoryModel, CustomUser)
admin.site.register(BookModel)
admin.site.register(BookCategoryModel)
admin.site.register(CustomUser)
