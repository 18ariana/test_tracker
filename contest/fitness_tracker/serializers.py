from fitness_tracker.models import *
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):

    start_time = serializers.DateTimeField()
    finish_time = serializers.DateTimeField()
    activity_type = serializers.CharField()
    distance = serializers.FloatField()
    calories_amount = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Activity
        fields = ('start_time', 'finish_time', 'user', \
             'activity_type', 'distance', 'calories_amount',
        )


class ActivityListSerializer(ActivitySerializer):
    activity_type = serializers.CharField()
    total_calories = serializers.CharField(read_only=True)
    duration = serializers.CharField(read_only=True)

    class Meta:
        model = Activity
        fields = (
             'activity_type', 'total_calories', 'duration',
        )