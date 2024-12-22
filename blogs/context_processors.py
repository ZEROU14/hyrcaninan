from .models import Blogs


# context_processors.py

def blog(request):
    
    first_blog = Blogs.objects.first()
    if first_blog is None:
        blogs_id = ""
    else:
        blogs_id = first_blog.id

    return {
        'blogs': first_blog,
        'blogs_id': blogs_id,
        'other_blogs': Blogs.objects.all()[1:4]
    }
