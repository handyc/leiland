from django.core.management.base import BaseCommand

from webapp.models import Dataset

import csv
import time

class Command(BaseCommand):
    help = 'creates DB from csv file'

    def handle(self, *args, **options):
        file = open("database.csv")
        csvreader = csv.reader(file, delimiter=';')

        Dataset.objects.all().delete()
        Author.objects.all().delete()
        CorpusType.objects.all().delete()
        DataFormat.objects.all().delete()
        DataType.objects.all().delete()
        Domain.objects.all().delete()
        Gender.objects.all().delete()
        LanguageProficiency.objects.all().delete()
        Language.objects.all().delete()
        Location.objects.all().delete()
        Modality.objects.all().delete()

        #Dataset.objects.all().delete()
        #Dataset.objects.all().delete()

        rows = []
        #d = dict()
        for row in csvreader:
            #print("hello")
            dataset = Dataset(title=title,
                years = years,
                author = author,

