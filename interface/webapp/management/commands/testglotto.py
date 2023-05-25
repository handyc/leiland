from django.core.management.base import BaseCommand

from webapp.models import Dataset

from webapp.models import Author

from webapp.models import AnnotationType
from webapp.models import CorpusType
from webapp.models import DataFormat
from webapp.models import DataType
from webapp.models import Domain
from webapp.models import Gender
from webapp.models import LanguageProficiency
from webapp.models import Language
from webapp.models import Location
#from webapp.models import Sublocation
from webapp.models import Modality

import csv
import time

class Command(BaseCommand):
    help = 'creates DB from csv file'

    def handle(self, *args, **options):
        Language.objects.all().delete()

        with open("languoid.csv", "r") as file:
            #csv_entries = csv.reader(file, delimiter=';')
            csv_entries = csv.reader(file, delimiter=',')
            #print(csv_entries)
            #print(csv_entries)

            for row in csv_entries:
                glottocode = row[0]
                name = row[3]
                iso = row[8]
                print(glottocode + " " + name + " " + iso)

                language = Language(name=name,
                    glottocode=glottocode,
                    iso=iso)

                language.save()
