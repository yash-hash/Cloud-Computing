from django.db import models
import datetime
import pytz


# Timestamp Code
ct = datetime.datetime.now()
def timestamp(ct):
    """Timestamp Code"""
    ct = str(ct)
    datetime = ct.split(" ")
    date = datetime[0]
    time = datetime[1].split(".")
    final_time = time[0]
    timestamp = date + "_" + final_time
    return timestamp


class CarouselImage(models.Model):
    """Model For Carousel Image in Homepage"""
    image_id = models.CharField(max_length=20, unique=True, editable=False)
    image_event_name = models.CharField(max_length=50, blank=False)
    image_file = models.ImageField()
    date_added = models.DateTimeField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_imageid()

    def set_imageid(self):
        """Image_ID Function"""
        # stamp = timestamp(ct)
        if not self.image_id:
            image_id = 'IMG' + "_" + str(self.id)
            carousel = CarouselImage.objects.get(id=self.id)
            carousel.image_id = image_id
            carousel.save()

    def __str__(self):
        return str(self.image_id)



class SponsorLogo(models.Model):
    """Model for Portal Sponsors"""

    sponsor_choices = [("1","Title"), ("2","Campaign"), ("3","Travel"),
    ("4","Techonology"),("5","Media"), ("6","Regional"),('7','Hospitality')]

    image_id = models.CharField(max_length=20, unique=True, editable=False)
    sponsor_name = models.CharField(max_length=255)
    sponsor_desc = models.TextField()
    image_file = models.ImageField()
    date_added = models.DateTimeField()
    sponsor_type = models.CharField(max_length=20, choices = sponsor_choices)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_imageid()

    def set_imageid(self):
        """Image_ID Function"""
        # stamp = timestamp(ct)
        if not self.image_id:
            image_id = 'IMG' + "_" + str(self.id)
            sponsor = SponsorLogo.objects.get(id=self.id)
            sponsor.image_id = image_id
            sponsor.save()

    def __str__(self):
        return str(self.image_id)



class PartnerLogo(models.Model):
    """Model For Partners of portal"""

    partner_choices = [('1','Outreach'),('2','Youth Empowerment'), ('3', 'Government')]

    image_id = models.CharField(max_length=20, unique=True, editable=False)
    partner_name = models.CharField(max_length = 255)
    partner_desc = models.TextField()
    image_file = models.ImageField()
    date_added = models.DateTimeField()
    partner_type = models.CharField(max_length=10, choices=partner_choices)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_imageid()

    def set_imageid(self):
        """Image_ID Function"""
        # stamp = timestamp(ct)
        if not self.image_id:
            image_id = 'IMG' + "_" + str(self.id)
            partner = PartnerLogo.objects.get(id=self.id)
            partner.image_id = image_id
            partner.save()

    def __str__(self):
        return str(self.image_id)


class YouthIcon(models.Model):
    """Model For Youth Icons"""

    image_id = models.CharField(max_length=20, unique=True, editable=False)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    designation = models.CharField(max_length = 200)
    image_file = models.ImageField()
    date_added = models.DateTimeField()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_imageid()

    def set_imageid(self):
        """Image_ID Function"""
        # stamp = timestamp(ct)
        if not self.image_id:
            image_id = 'IMG' + "_" + str(self.id)
            youthIcon = YouthIcon.objects.get(id=self.id)
            youthIcon.image_id = image_id
            youthIcon.save()

    def __str__(self):
        return str(self.image_id)
