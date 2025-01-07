from cms.models.pluginmodel import CMSPlugin
from django.db import models

class TrainingPluginModel(CMSPlugin):
    tr_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    trainer_id = models.PositiveIntegerField(default=0)
    ref_link = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    skill_id = models.PositiveIntegerField(default=0)
    current_level_cd = models.CharField(max_length=30, default='')
    target_level_cd = models.CharField(max_length=30, default='')
    project_id = models.CharField(max_length=200, default='')
    event_dt = models.DateTimeField()
    event_type_cd = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    user_id_arr = models.CharField(max_length=5000, default='')
    status_cd = models.CharField(max_length=200, default='status.draft')
    obj_cd = models.CharField(max_length=50, default='content.training')
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    feedback_show_yn = models.CharField(max_length=1, default='Y')
    external_survey_url = models.CharField(max_length=200, default='')
    external_survey_yn = models.CharField(max_length=1, default='N')
    trainer_id_arr = models.CharField(max_length=5000, default='')
    show_yn = models.CharField(max_length=1, default='Y')
    program_id = models.PositiveIntegerField(default=0)
    module_id = models.PositiveIntegerField(default=0)
    co_author_id_arr = models.CharField(max_length=1000, default='')
    

    def __str__(self):
        return self.title