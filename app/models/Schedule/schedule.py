# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Schedule(models.Model):
    """
    Class defining the Schedule model

    t.string   "event_type", limit: 255
    t.date     "date_begin"
    t.date     "date_end"
    t.string   "event_name", limit: 255
    t.string   "event_desc", limit: 255
    t.integer  "user_id",    limit: 4
    t.datetime "created_at"
    t.datetime "updated_at"
    """

    def __str__(self):
        return self.user.__str__() + " Schedule Summary: \n" \
               + "\nEvent Type: " + str(self.event_type) \
               + "\nEvent Name: " + str(self.event_name) \
               + "\nEvent Description: " + str(self.event_desc) + "\n"

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date_begin = models.DateField()
    date_end = models.DateField()
    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    event_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_schedules"
