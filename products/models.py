from django.db import models
from multiselectfield import MultiSelectField


SESSION_FEATURES = [
    ('free_initial', 'Free 15 Minute Initial Consult'),
    ('one_hour', 'One Hour of Games Based Training Sessions'),
    ('three_hours', 'Three Hours of Games Based Training Sessions'),
    ('five_hours', 'Five Hours of Games Based Training Sessions'),
    ('training_plan', 'Detailed Training Plan'),
    ('follow_up', 'Follow Up Phone Call'),
    ('facebook_group', 'Access To Private Facebook Training Group'),
]

# Create your models here.


class Training(models.Model):

    name = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = MultiSelectField(choices=SESSION_FEATURES)

    def __str__(self):
        return self.name

    def get_features(self):
        feature_list = []
        d = dict(SESSION_FEATURES)
        for feature in self.features:
            if feature in d:
                feature_list.append(d[feature])
            else:
                feature_list.append(feature)
        return feature_list

