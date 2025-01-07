
from django.core.management.base import BaseCommand
from training.models import TrainingPluginModel
from datetime import datetime

class Command(BaseCommand):
    help = 'Adds demo data to the TrainingPluginModel'

    def handle(self, *args, **kwargs):
        demo_data = [
            {
                'title': 'Python for Beginners',
                'trainer_id': 1,
                'ref_link': 'https://example.com/python-beginners',
                'description': 'A comprehensive guide to Python programming for beginners.',
                'skill_id': 101,
                'current_level_cd': 'Beginner',
                'target_level_cd': 'Intermediate',
                'project_id': 'project-001',
                'event_dt': datetime(2023, 10, 15, 10, 0),
                'event_type_cd': 'Workshop',
                'location': 'Online',
                'user_id_arr': '1,2,3',
                'status_cd': 'status.published',
                'obj_cd': 'content.training',
                'start_time': '10:00 AM',
                'end_time': '12:00 PM',
                'feedback_show_yn': 'Y',
                'external_survey_url': '',
                'external_survey_yn': 'N',
                'trainer_id_arr': '1,2',
                'show_yn': 'Y',
                'program_id': 1,
                'module_id': 1,
                'co_author_id_arr': '',
            },
            # Add more demo data entries as needed
        ]

        for data in demo_data:
            TrainingPluginModel.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('Successfully added demo data'))