from django.db import models
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os.path
from django.conf import settings


class Model:

    MODEL_FILE = os.path.join(settings.MODELS, "model.h5")
    model = load_model(MODEL_FILE)

    def predict(self, img_url, size=(100,100)):
        test_image = image.load_img(img_url, target_size=size)
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = self.model.predict(test_image)
        print(result)

        max_value = max(result[0])

        if result[0][0] == max_value:
            return 'arachnid', max_value
        elif result[0][1] == max_value:
            return 'insect', max_value
        elif result[0][2] == max_value:
            return 'centipede', max_value
        elif result[0][3] == max_value:
            return 'crustacean', max_value
