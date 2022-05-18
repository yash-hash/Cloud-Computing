from django.db import models


event_choices = (("Event", "Event"), ("Ceremony","Ceremony"),("Workshop","Workshop"))


class Event(models.Model):
    """Model For Event"""

    event_id = models.CharField(max_length=10, editable=False, unique=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices = event_choices)
    date = models.DateField()
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    imp_notes = models.TextField()
    EXpected_no_of_candidates = models.IntegerField()
    stationary_requirements = models.TextField()
    is_event_online = models.BooleanField()
    stay = models.BooleanField()
    travel = models.BooleanField()
    projector= models.BooleanField()
    av_setup = models.BooleanField()
    infrastructural_requirements = models.TextField()
    event_images = models.ImageField()
    banner = models.ImageField()
    attendees_from_evolvingx = models.IntegerField()
    Event_summary = models.TextField(blank = True)
    institutiion_sponsor_id = models.ForeignKey('institution.InstitutionSponsor', on_delete=models.PROTECT, related_name='e_sponsor')
    regions_id = models.ForeignKey('address.Region', on_delete = models.PROTECT, related_name='e_region')
    # local_sponosor_amount
    # event_status = models.CharField(max_length = 10, choices = status_choices)
    created_date = models.DateTimeField()
    created_by = models.ForeignKey('champion.Champion', on_delete = models.PROTECT, related_name = 'event_champ_id')
    updated_date = models.DateTimeField()
    # updated_by

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_eventid()

    def set_eventid(self):
        """Image_ID Function"""
        if not self.event_id:
            event_id = 'EVENT' + "_" + str(self.id)
            event = Event.objects.get(id=self.id)
            event.event_id = event_id
            event.save()

    def __str__(self):
        return str(self.event_id)


class RegionalEvent(models.Model):
    """Model for Regional Event"""
    event_id = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices = event_choices)
    date = models.DateField()
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    imp_notes = models.TextField()
    Expected_no_of_candidates = models.IntegerField()
    stationary_requirements = models.TextField()
    is_event_online = models.BooleanField()
    stay = models.BooleanField()
    travel = models.BooleanField()
    projector= models.BooleanField()
    AV_setup = models.BooleanField()
    infrastructural_requirements = models.TextField()
    event_images = models.ImageField()
    banner = models.ImageField()
    attendees_from_evolvingx = models.IntegerField()
    Event_summary = models.TextField(blank = True)
    institutiion_sponsor_id = models.ForeignKey('institution.InstitutionSponsor', on_delete=models.PROTECT, related_name='reg_sponsor')
    region = models.ForeignKey('address.Region', on_delete = models.PROTECT, related_name = 'reg_region')
    # regional_sponsor_amount
    # event_status = models.BooleanField(max_length = 10, choices = status_choices)
    created_date = models.DateTimeField()
    created_by = models.ForeignKey('champion.Champion', on_delete = models.PROTECT, related_name = 'reg_champ_id')
    updated_date = models.DateTimeField()
    # updated_by

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_eventid()

    def set_eventid(self):
        """Image_ID Function"""
        if not self.event_id:
            event_id = 'REG_EVENT' + "_" + str(self.id)
            regional_event = RegionalEvent.objects.get(id=self.id)
            regional_event.event_id = event_id
            regional_event.save()

    def __str__(self):
        return str(self.event_id)
