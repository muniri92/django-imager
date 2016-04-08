from django.db import models

# Create your models here.

class Photo(models.Model):
	"""

    Photo represents an individual picture uploaded by a user.
    It will contain the image file itself, plus metadata about that file. 
    Photos are owned by a single Imager user.

    Meta-data should include a title and a description, a date_uploaded, date_modified and date_published field. 

    You should also have a ‘published’ field
    which takes one of several possible values
    (‘private’, ‘shared’, ‘public’).

    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_uploaded = models.DateField()
    date_modified = models.DateField()
    date_published = models.DateField()
    published = models.CharField(max_length=30)  # takes one of several possible values (‘private’, ‘shared’, ‘public’)


class Album(models.Model):
    """

    """
