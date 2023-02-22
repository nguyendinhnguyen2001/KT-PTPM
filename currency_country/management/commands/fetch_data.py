import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from currency_country.models import Country

# python manage.py fetch_data > data_source.json


class Command(BaseCommand):
    help = "Extracting user data to JSON format"

    def handle(self, *args, **options):
        # Get User Data from User Model in monolith
        country = Country.objects.all().values()
        for country_data in country:
            data = {
                "model": "Country",
                "id": country_data['id'],
                # "id": user_data.id,
                # "username": user_data.flip_collection.id,
                "country_name": country_data['country_name'],
                "local_currency": country_data['local_currency'],
                "added_on": country_data['added_on']
                # "mobile_number": user_data.flip_image.id,
                # "created_at": user_data.created_at,
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")
