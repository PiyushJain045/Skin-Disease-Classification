from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    age = serializers.IntegerField(
        required=True,
        min_value=2,
        max_value=100,
        help_text="Patient's age (2-100)"
    )
    gender = serializers.ChoiceField(
        required=True,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        help_text="Patient's gender"
    )
    image = serializers.ImageField(
        required=True,
        help_text="Image of the skin condition"
    )