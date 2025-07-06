from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import PredictionInputSerializer
from app.utils.predict import predict_image
from app.utils.gemini import gemini_advice

class PredictAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def get_serializer(self):
        return PredictionInputSerializer()
    
    def get(self, request):
        serializer = PredictionInputSerializer()
        return Response(serializer.data)

    
    def post(self, request):
        try:
            serializer = PredictionInputSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {"error": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

            validated_data = serializer.validated_data
            age = validated_data['age']
            gender = validated_data['gender']
            image = validated_data['image']

            # Prediction
            result, _ = predict_image(image)

            # Advice
            advice = gemini_advice(age, gender, result)

            return Response(
                {
                    "result": result,
                    "advice": advice
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": "Something went wrong.", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )