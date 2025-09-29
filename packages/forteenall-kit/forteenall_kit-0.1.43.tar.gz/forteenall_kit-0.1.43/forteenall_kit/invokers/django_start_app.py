from ..feature import KitFeature



class DjangoAppFeatureData:
    
    pass

class Feature(KitFeature):
    
    def __init__(self, app_name):
        feature_type = 'django_start_app'
        super().__init__(app_name=app_name, feature_type=feature_type)
    
    def execute(self):
        pass