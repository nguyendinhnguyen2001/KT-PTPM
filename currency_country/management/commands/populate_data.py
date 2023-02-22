import json
import sys
import logging
from dateutil import parser
from django.core.management.base import BaseCommand
from currency_country.models import Country
# cat data_source.json | python manage.py populate_data
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Populating Country data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating User Model
            if data["model"] == "Country":
                country = Country(
                    # country_id=data["id"],
                    country_name=data["country_name"],
                    added_on=data["added_on"],
                    # created_at=parser.parse(data["created_at"]),
                )
                country.save()
                logger.debug("Country populated:{}".format(
                    country.country_name))
