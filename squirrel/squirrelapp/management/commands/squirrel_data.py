import csv
import datetime as dt
from django.core.management.base import BaseCommand
from squirrelapp.models import Squirrels
from django.conf import settings
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
                        
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
                s = Squirrels(
                    Squirrel_Id = item['Unique_Squirrel_ID'],
                    Latitude = item['Latitude'],
                    Longitude = item['Longitude'],
                    Shift = item['Shift'],
                    Date = dt.datetime.strptime(item['Date'].strip(),'%Y-%m-%d').date(),
                    Age = item['Age'],
                    Fur_Colour = item['Primary_Fur_Colour'],
                    Location = item['Location'],
                    Specific_Location = item['Specific_location'],
                    Running = item['Running'],
                    Chasing = item['Chasing'],
                    Climbing = item['Climbing'],
                    Eating = item['Eating'],
                    Foraging = item['Foraging'],
                    Other_Activities = item['Other_Activities'],
                    kuk = item['Kuks'],
                    quaas = item['Quaas'],
                    moan = item['Moans'],
                    Tail_flags = item['Tail_flags'],
                    Tail_twitch = item['Tail_twitches'],
                    Approaches = item['Approaches'],
                    Indifferent = item['Indifferent'],
                    Runs_from = item['Runs_from'],
                )
                s.save()

