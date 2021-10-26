from rest_framework import filters
from django.db.models import Sum, F, DurationField, ExpressionWrapper
from django.utils.dateparse import parse_date, parse_datetime

class ActivityFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        expression = F('finish_time') - F('start_time')
        wrapped_expression = ExpressionWrapper(expression, DurationField())

        date_clause = request.query_params.get('by_date')

        if date_clause:

            wrapped_date = parse_date(date_clause)
            
            queryset = queryset\
                .filter(start_time__date=wrapped_date)
        
        hour_clause = request.query_params.get('by_hour')

        if hour_clause:

            wrapped_hour = parse_datetime(hour_clause)

            queryset = queryset\
                .filter(start_time__lte=wrapped_hour)\
                .filter(finish_time__gte=wrapped_hour)
        
        queryset = queryset.values('activity_type')\
                .annotate(total_calories=Sum('calories_amount'))\
                .annotate(duration=Sum(wrapped_expression))
        
        return queryset


