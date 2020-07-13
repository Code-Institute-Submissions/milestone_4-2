from django.db import models

SESSIONS_FEATURES = [
    ('free_initial_15_minute_consult', 'Free Initial 15 Minute Consultation'),
    ('one_hour_of_games_based_training', 'One Hour of Games Based Training'),
    ('three_hours_of_games_based_training', 'Three Hours of Games Based Training'),
    ('five_hours_of_games_based_training', 'Five Hours of Games Based Training'),
    ('detailed_training_plan', 'Detailed Training Plan'),
    ('follow_up_phonecall', 'Follow Up Phonecall'),
    ('access_to_private_facebook_group', 'Access to Private Facebook Group'),
]   


# Create your models here.

class Training(models.Model):

    class Meta:
        verbose_name_plural = 'Training Sessions'
        
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField(choices=SESSIONS_FEATURES)
    image = models.ImageField(upload_to='media/products', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_features(self):
        feature_list = []
        d = dict(SESSIONS_FEATURES)
        for feature in self.features:
            if feature in d:
                feature_list.append(d[feature])
            else:
                feature_list.append(feature)
        return feature_list