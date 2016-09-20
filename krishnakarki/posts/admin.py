from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ["title","updated", "timestamp"]
	list_filter = ["updated", "timestamp"]
	list_display_links = ["updated"]
	search_fields = ["title", "content"]
	list_editable = ["title"]

	class meta:
		"""docstring for meta"""
		model = Post


admin.site.register(Post,PostModelAdmin)