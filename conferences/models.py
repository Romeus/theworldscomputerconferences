from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255,
                            help_text="Category name")
    description = models.TextField(help_text="Category description")


class ConferenceType(models.Model):
    name = models.CharField(max_length=255,
                            help_text="The name of the conference")
    announce = models.TextField(
        help_text="Short description of the conference")
    description = models.TextField(
        help_text="Description of the conference")
    url = models.URLField(
        help_text="Url of the conference")
    mascot = models.ImageField(upload_to="mascots/",
                               help_text="Mascot of the conference")
    started_since = models.DateTimeField(
        help_text="Date of the conference's first meeting")
    regular = models.BooleanField(help_text="Is conference regular?",
                                  default=True)
    place_address = models.BooleanField(
        help_text="Does conference has the regular place?",
        default=True)
    regular_time = models.BooleanField(
        help_text="Does the conference has regular meeting time?",
        default=True)
    stopped = models.BooleanField(
        help_text="Does conference don't spend anymore?",
        default=False)
    categories = models.ManyToManyField(Category,
                                        help_text="Conferences's categories")


class Place(models.Model):
    name = models.CharField(max_length=255,
                            help_text="Place's name")
    description = models.TextField(help_text="Place description")
    address = models.TextField(help_text="Place address")
    latitude = models.FloatField(help_text="Place latitude")


class Conference(models.Model):
    date_from = models.DateTimeField(help_text="Start date")
    date_to = models.DateTimeField(help_text="End date")
    conference_type = models.ForeignKey(ConferenceType)
    place = models.ForeignKey(Place)


class Feedback(models.Model):
    name = models.CharField(max_length=255,
                            help_text="Your name")
    phone = models.CharField(max_length=255,
                             help_text="Your phone number",
                             blank=True)
    email = models.EmailField(help_text="Your email", blank=True)
    message = models.TextField(help_text="Your message")
