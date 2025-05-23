from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    BLOG_TYPE_CHOICES = [
        ('commerce', 'commerce'),
        ('energy', 'energy'),
        ('esports', 'esports'),
        ('fintech', 'fintech'),
        ('healthcare', 'healthcare'),
        ('realestate', 'realestate'),
        ('tour', 'tour'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=False, blank=True)
    image = models.ImageField(upload_to="blog/images/blog_images")
    content = models.TextField()
    short_description = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Unknown Author")
    author_description = models.TextField(default="No description available.")
    author_image = models.ImageField(
    upload_to='blog/images/author_images/',
    default='blog/images/author_images/default_author_image.png',
    blank=True, null=True
    )
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    blog_type = models.CharField(
        max_length=20, choices=BLOG_TYPE_CHOICES, default='healthcare'
    )  # Default value corrected

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Section(models.Model):
    blog = models.ForeignKey(Blog, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=False, blank=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
