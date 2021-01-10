from django.db import models

# Create your models here.
class SkillModel(models.Model):
    is_player = models.BooleanField(verbose_name = "Are you a gamer?")
    action_latency = models.FloatField(null = True, blank = True, verbose_name = "Action latency (ms)")
    apm = models.FloatField(null = True, blank = True, verbose_name = "Actions per minute")
    gap_between_pacs = models.FloatField(null = True, blank = True, verbose_name = "Mean duration between PACs (ms)")
    number_of_pacs = models.FloatField(null = True, blank = True, verbose_name = "Number of PACs per timestamp")
    select_by_hotkeys = models.FloatField(null = True, blank = True, verbose_name = "Number of unit or building selections made using hotkeys per timestamp")
    assign_to_hotkeys = models.FloatField(null = True, blank = True, verbose_name = "Number of units or buildings assigned to hotkeys per timestamp")
    name = models.CharField(max_length = 130, verbose_name = "Username")