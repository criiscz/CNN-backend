from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from .models import Model

from .apps import *
# Create your views here.
class Prediction(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    def put(self, request, *args, **kwargs):
        if request.data['file'] is None:
            return Response({"message":"No image uploaded."})
        img = request.data['file']
        print(img)
        path = default_storage.save('tmp/image.jpg', ContentFile(img.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        model = Model()
        predict, value = model.predict(tmp_file)
        print(predict)

        return Response({"predict":predict, "value":value}, status=200)



