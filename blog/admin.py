from django.contrib import admin

# Register your models here.

# lin,leo - import our Post class, so it is editable in the admin page
from .models import Post  # . before models implies current working directory

admin.site.register(Post)
