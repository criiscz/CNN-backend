import os.path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from django.apps import AppConfig

from django.conf import settings


class IcApiConfig(AppConfig):
    name = 'ic_api'
    MODEL_FILE = os.path.join(settings.MODELS, "model.h5")
    model = load_model(MODEL_FILE)

    def predict(self, img_url, size=(100,100)):
        test_image = image.load_img(img_url, target_size=size)
        test_image = image.img_to_array(test_image)
        result = self.model.predict(test_image)

        if result[0][0] > 0.5:
            return 'arachnid'
        elif result[0][1] > 0.5:
            return 'insect'
        elif result[0][2] > 0.5:
            return 'crustacean'
        elif result[0][3] > 0.5:
            return 'centipede'
