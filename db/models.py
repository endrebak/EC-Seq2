from django.db import models

# Create your models here.

class Gene(models.Model):

    name = models.TextField()

    logfc = models.FloatField()
    t = models.FloatField()
    p_value = models.FloatField()
    adj_p_val = models.FloatField()
    b = models.FloatField()
    eciivsd_logfc = models.FloatField()
    eciivsd_aveexpr = models.FloatField()
    eciivsd_t = models.FloatField()
    eciivsd_p_value = models.FloatField()
    eciivsd_adj_p_val = models.FloatField()
    eciivsd_b = models.FloatField()
    mecvslec_logfc = models.FloatField()
    mecvslec_aveexpr = models.FloatField()
    mecvslec_t = models.FloatField()
    mecvslec_p_value = models.FloatField()
    mecvslec_adj_p_val = models.FloatField()
    mecvslec_b = models.FloatField()
    ovsy_logfc = models.FloatField()
    ovsy_aveexpr = models.FloatField()
    ovsy_t = models.FloatField()
    ovsy_p_value = models.FloatField()
    ovsy_adj_p_val = models.FloatField()
    ovsy_b = models.FloatField()
