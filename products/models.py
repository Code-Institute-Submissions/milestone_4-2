from django.db import models


PRODUCT_INCLUDED_FEATURES_CHOICES = [
    ('free_initial', 'Free Initial 15 Minute Consult'),
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
    price = models.DecimalField(max_digits=6, decimal_places=2,)
    features = models.TextField(choices=PRODUCT_INCLUDED_FEATURES_CHOICES)
    image = models.ImageField(upload_to='media/products', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_features_display_list(self):
        feature_list = []
        d = dict(PRODUCT_INCLUDED_FEATURES_CHOICES)
        for feature in self.features:
            if feature in d:
                feature_list.append(d[feature])
            else:
                feature_list.append(feature)
        return feature_list