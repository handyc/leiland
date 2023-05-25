from django.core.management.base import BaseCommand
from webapp.models import Dataset

import csv
import time
import io

class Command(BaseCommand):
    help = 'Ingests CSV datasets into Django DB'

    def handle(self, *args, **options):
        #file = open("database.csv")
        file = io.open("database.csv", encoding='utf-8')
        csvreader = csv.reader(file,  delimiter=';')
        Dataset.objects.all().delete()

        rows = []
        d = dict()
        for row in csvreader:
            #print(row[0])
            #for column in row[0]:
            #print(', '.join(row))

            #print("nothing?:", row[0])

            #print("Author:", row[1])
            author = row[1]

            #print("dataset contact:", row[2])
            #contact = row[2]
            #contact = row[2]
            #contact = row[74]
            contact = row[76]

            

            publisher=row[82]

            #print("dataset creation date?:", row[3])
            # years = row[3]

            #print("Language name:", row[4])
            languages = row[4]

            #print("Description:", row[5])
            description = row[5]

            #print("ISO Language Code:", row[6])
            #print("languages involved?:", row[7])
            iso_language_code = row[6]

            #print("Corpus type:", row[8])
            corpus_types = row[8]

            corpus_note = row[9]

            #print("addl language info?:", row[9])

            #print("Location:", row[10])
            sublocation = row[10]
            location = row[12]

            #print("Software:", row[10])
            #software = row[10]
            software = row[46]

            #print("Location(b):", row[11])
            #print("PlaceName:", row[12])
            #print("Location(more):", row[13])
            #print("Location(more2):", row[14])

            #print("subdisciplines?:", row[15])
            #print("Subdisciplines:", row[16])
            #print("Subdisciplines(c):", row[17])

            #print("domain?:", row[18])
            #print("Non-linguistic fields?:", row[19])
            #print("Domain:", row[20])
            #domains = row[20]
            domains = row[16]

            #print("Data Type:", row[21])
            #print("Data Type(2):", row[22])
            data_types = row[21]

            #print("Modality:", row[23])
            #print("Modality(b):", row[24])
            modalities = row[23]

            #print("Data Format:", row[25])
            #print("Data Format(b):", row[26])
            #print("Data Format(c):", row[27])
            #print("Data Format(d):", row[28])
            #print("Data Format(e):", row[29])
            #print("Data Format(f):", row[30])
            #print("Data Format(g):", row[31])
            data_formats = row[25]
            data_size = row[32]

            #print("Size of dataset:", row[32])
            #print("Size of dataset(b):", row[33])
            #print("Size of dataset(c):", row[34])
            #print("Size of dataset(d):", row[35])
            #print("Size of dataset(e):", row[36])

            #print("Dataset structure:", row[37])
            #print("Dataset structure(b):", row[38])

            #print("Collection methods?:", row[39])
            #print("Collection methods(b)?:", row[40])
            #print("Collection methods(c)?:", row[41])
            #print("Collection methods(d):", row[42])
            #print("Collection methods(e):", row[43])
            #print("Collection methods(f):", row[44])
            #print("Collection methods(g):", row[45])

            #print("Software tools developed:", row[46])
            #print("Software used:", row[47])
            #print("Software tools developed(b?):", row[48])
            #print("Software tools developed(c?):", row[49])
            #print("Software tools developed(d?):", row[50])
            #print("Software tools developed(e?):", row[51])
            #print("Software tools developed(f?):", row[52])

            #print("Software documentation:", row[53])
            #print("Software documentation(b):", row[54])

            #print("Proficiency of speakers:", row[55])
            language_proficiencies = row[55]

            #print("Data pertains to L1/L2/L3 (yes/no)?:", row[56])

            #print("Proficiencies tested (yes/no)?:", row[57])
            #print("Proficiencies tested?(b):", row[58])

            #print("Number of participants:", row[59])

            #print("Age of participants:", row[60])
            #print("Age of participants(b):", row[61])
            #print("Age of participants(c):", row[62])

            #print("Gender of speakers:", row[63])
            #print("Gender of participants:", row[64])
            #print("Gender of participants:", row[65])
            genders = row[63]

            #print("Sensitive data / ethical issues:", row[66])
            #print("Sensitive data(b):", row[67])
            #print("Sensitive data(c):", row[68])
            #print("Sensitive data(d):", row[69])

            #print("Existing metadata:", row[70])
            #print("Existing metadata(b):", row[71])
            #print("Existing metadata(c):", row[72])
            metadata = row[70]

            comments = row[95]

            #print("Annotation Type:", row[73])
            #print("Annotation Type(b):", row[74])
            annotation_types = row[73]

            #print("Resource Rights?:", row[75])
            #print("Resource Rights?(b):", row[76])
            #print("Rights Holder:", row[77])
            #print("Resource Rights(d):", row[78])
            #print("Resource Rights(e):", row[79])
            #print("Resource Rights(f):", row[80])
            #print("Resource Rights(g):", row[81])
            #print("Data provider / publisher:", row[82])
            #print("Resource rights(i?):", row[83])
            #print("Resource rights(j?):", row[84])

            #print("Access rights:", row[85])
            #print("Access rights(b):", row[86])
            availability = row[85]
            access_note = row[86]

            #print("Curation requirements:", row[87])
            #print("Curation requirements(b):", row[88])
            #print("Curation requirements(c):", row[89])

            #print("Resource History:", row[90])
            #print("Resource History(b):", row[91])

            #print("Date created:", row[92])
            years = row[92]

            #print("Transcription date:", row[93])

            #print("Access rights / consent:", row[94])

            #print("addl comments:", row[95])

            #print("topics?:", row[96])

            #print("placeholder?:", row[97])
            #print("placeholder?(b):", row[98])
            #print("placeholder?(c):", row[99])

            #print("Glottocodes:", row[100])
            glottocodes = row[100]

            #print("Title:", row[101])
            title = row[101]

            #print("YoutubeURL?:", row[102])
            #cmdi = row[102]
            cmdi = row[102]
            banklink = row[103]

            print("ingesting...")
            #dataset = Dataset(title=title, )
            dataset = Dataset(title=title,
                comments=comments,
                metadata=metadata,
                years=years, 
                contact=contact,
                software=software, 
                author=author,
                publisher=publisher,
                annotation_types=annotation_types,
                domains=domains,
                corpus_types=corpus_types,
                corpus_note=corpus_note,
                genders=genders, 
                modalities=modalities,
                sublocation=sublocation,
                location=location,
                description=description, 
                iso_language_code=iso_language_code, 
                languages=languages, 
                data_formats=data_formats,
                data_size=data_size, 
                data_types=data_types, 
                language_proficiencies=language_proficiencies, 
                cmdi=cmdi, 
                banklink=banklink, 
                glottocodes=glottocodes, 
                availability=availability,
                access_note=access_note)

            dataset.save() 

            #for column in row:
            #    #print(column)
            #    print(column, end='', flush=True)
            #print("\n")
            #time.sleep(0.1)
