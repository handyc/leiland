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
        Dataset.objects.all().delete()

        with open("database.csv", "r") as file:
            csv_entries = csv.reader(file, delimiter=';')
            #print(csv_entries)
            #print(csv_entries)

            for row in csv_entries:
                name = row[99]
                metadata = row[99]

                contact = row[74]
                author = row[1]

                cmdi_identifier = row[102]
                collection_bank = row[103]

                annotation_types = row[1]
                domains = row[1]
                corpus_types = row[1]
                genders = row[1]
                modalities = row[1]
                location = row[1]
                sublocation = row[1]

                data_formats = row[1]
                #data_subformats = row[1]

                languages = row[1]
                data_types = row[1]
                language_proficiencies = row[1]
                availability = row[1]
                #accessnote = row[1]

                contacttest=''.join(row[3])
                #print(contacttest.split(',')[0])

                splitter = contacttest.split(',')[0]
                #print(contact)

                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)
                #print(name)

                title = "1"
                years = "1"
                contact = "1"
                author = "1"
                annotation_types = "1"
                domains = "1"
                glottocodes = "1"
                availability = "1"

                dataset = Dataset(title=title,
                    years=years,
                    contact=contact,
                    author=author,
                    annotation_types=annotation_types,
                    domains=domains,
                    glottocodes=glottocodes,
                    availability=availability)

                dataset.save()


