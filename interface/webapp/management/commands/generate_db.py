import csv
import time
import io

from django.core.management.base import BaseCommand

from webapp.models import Dataset

from webapp.models import AnnotationType
from webapp.models import Gender
from webapp.models import Author
from webapp.models import LanguageProficiency
from webapp.models import CorpusType
from webapp.models import Language
from webapp.models import DataFormat
from webapp.models import Location
from webapp.models import DataType
from webapp.models import Modality
from webapp.models import Domain

class Command(BaseCommand):
    help = 'Generates DB choices for each field'

    def handle(self, *args, **options):

        ### import database here and generate datasets

        ###

        ### annotation types?
        ### authors
        ### corpustype?
        ### data format?
        ### locations?
        ### data type?
        ### modality?
        ### domains

        AnnotationType.objects.all().delete()

        annotation_type = AnnotationType(name="Cognates")
        annotation_type.save()

        annotation_type = AnnotationType(name="Dating")
        annotation_type.save()

        annotation_type = AnnotationType(name="Derivational History")
        annotation_type.save()

        annotation_type = AnnotationType(name="Explanation of a Journalist")
        annotation_type.save()

        annotation_type = AnnotationType(name="Historical Derivation")
        annotation_type.save()

        annotation_type = AnnotationType(name="Interpretation")
        annotation_type.save()

        annotation_type = AnnotationType(name="Kml")
        annotation_type.save()

        annotation_type = AnnotationType(name="Language Classification")
        annotation_type.save()

        annotation_type = AnnotationType(name="Lemma From Hittite Or Luwian")
        annotation_type.save()

        annotation_type = AnnotationType(name="Line- And Page Breaks")
        annotation_type.save()

        annotation_type = AnnotationType(name="Linear Order")
        annotation_type.save()

        annotation_type = AnnotationType(name="Linguistic Phenomena")
        annotation_type.save()

        annotation_type = AnnotationType(name="Linked Data Annotations")
        annotation_type.save()

        annotation_type = AnnotationType(name="Mark Up Of Words")
        annotation_type.save()

        annotation_type = AnnotationType(name="None")
        annotation_type.save()

        annotation_type = AnnotationType(name="Normalised Transcriptions")
        annotation_type.save()

        annotation_type = AnnotationType(name="Other")
        annotation_type.save()

        annotation_type = AnnotationType(name="Partial Glossing")
        annotation_type.save()

        annotation_type = AnnotationType(name="Pos-Tagging")
        annotation_type.save()

        annotation_type = AnnotationType(name="Praat")
        annotation_type.save()

        annotation_type = AnnotationType(name="Pronunciation Eligibility")
        annotation_type.save()

        annotation_type = AnnotationType(name="Reconstructed Forms")
        annotation_type.save()

        annotation_type = AnnotationType(name="Results")
        annotation_type.save()

        annotation_type = AnnotationType(name="Semantic Category")
        annotation_type.save()

        annotation_type = AnnotationType(name="Semantic Field")
        annotation_type.save()

        annotation_type = AnnotationType(name="Semantic Tags")
        annotation_type.save()

        annotation_type = AnnotationType(name="Semantics")
        annotation_type.save()

        annotation_type = AnnotationType(name="Source Text")
        annotation_type.save()

        annotation_type = AnnotationType(name="Speech Segments")
        annotation_type.save()

        annotation_type = AnnotationType(name="Syntactic Features")
        annotation_type.save()

        annotation_type = AnnotationType(name="Ta1/ta2")
        annotation_type.save()

        annotation_type = AnnotationType(name="Text Date")
        annotation_type.save()

        annotation_type = AnnotationType(name="Transcription")
        annotation_type.save()

        annotation_type = AnnotationType(name="Translation")
        annotation_type.save()

        annotation_type = AnnotationType(name="Treebanks")
        annotation_type.save()

        annotation_type = AnnotationType(name="Type of Spelling")
        annotation_type.save()

        annotation_type = AnnotationType(name="W3c")
        annotation_type.save()

        ###

        Gender.objects.all().delete()

        gender = Gender(name="male", weight="0")
        gender.save()

        gender = Gender(name="female", weight="1")
        gender.save()

        gender = Gender(name="unspecified", weight="2")
        gender.save()

        ###

        Author.objects.all().delete()
        # get from DB CSV

        author = Author(name="Albury N.")
        author.save()

        author = Author(name="Alem A.H.J.")
        author.save()

        author = Author(name="Alkhamees B.A.S.")
        author.save()

        author = Author(name="Ameka F.")
        author.save()

        author = Author(name="Amha A.")
        author.save()

        author = Author(name="Angoua T.")
        author.save()

        author = Author(name="Bellamy K.")
        author.save()

        author = Author(name="Bomsa E.")
        author.save()

        author = Author(name="Bruil M.")
        author.save()

        author = Author(name="Bylinina L.")
        author.save()

        author = Author(name="Carlin E.")
        author.save()

        author = Author(name="Caspers J.")
        author.save()

        author = Author(name="De Mulder H.N.M.")
        author.save()

        author = Author(name="Doetjes J.")
        author.save()

        author = Author(name="Dragoni F.")
        author.save()

        author = Author(name="Edwards O.")
        author.save()

        author = Author(name="Elenbaas M.")
        author.save()

        author = Author(name="Emlen N.Q.")
        author.save()

        author = Author(name="Fortuin E.")
        author.save()

        author = Author(name="Geambasu A.")
        author.save()

        author = Author(name="Glasbergen-Plas A.")
        author.save()

        author = Author(name="González González P.")
        author.save()

        author = Author(name="Hadjah T.")
        author.save()

        author = Author(name="Hansen R. P.")
        author.save()

        author = Author(name="Hansen R. P.")
        author.save()

        author = Author(name="Heeren W.F.L.")
        author.save()

        author = Author(name="Kaiping G.")
        author.save()

        author = Author(name="Klamer M.")
        author.save()

        author = Author(name="Kossmann M.G.")
        author.save()

        author = Author(name="Krogull A.")
        author.save()

        author = Author(name="Kroon M.S.")
        author.save()

        author = Author(name="Kroonen G.")
        author.save()

        author = Author(name="Liptak A.")
        author.save()

        author = Author(name="Moro F.R.")
        author.save()

        author = Author(name="Mous M.")
        author.save()

        author = Author(name="Mous M. and Petrollino S.")
        author.save()

        author = Author(name="Nielsen R.")
        author.save()

        author = Author(name="Nyst V.")
        author.save()

        author = Author(name="Okabe A.")
        author.save()

        author = Author(name="Pablos Robles L.")
        author.save()

        author = Author(name="Parafita Couto M.C.")
        author.save()

        author = Author(name="Pereira M.")
        author.save()

        author = Author(name="Petrollino S.")
        author.save()

        author = Author(name="Porck T.")
        author.save()

        author = Author(name="Puggaard R.")
        author.save()

        author = Author(name="Puggaard-Rode R. and Horslund C.S. and Jørgensen H. and Vet D.J.")
        author.save()

        author = Author(name="Reuneker A.")
        author.save()

        author = Author(name="Shi M.")
        author.save()

        author = Author(name="Smorenburg L.B.J.")
        author.save()

        author = Author(name="Sulistyono Y.")
        author.save()

        author = Author(name="Terkourafi M.")
        author.save()

        author = Author(name="Tieken-Boon van Ostade I.")
        author.save()

        author = Author(name="Van Baalen A.")
        author.save()

        author = Author(name="Van Doorn A.")
        author.save()

        author = Author(name="Van Hout T.")
        author.save()

        author = Author(name="Van der Wal G.J.")
        author.save()

        author = Author(name="Vertegaal X.")
        author.save()

        author = Author(name="Vieira E.A.")
        author.save()

        author = Author(name="Wichmann S.")
        author.save()

        author = Author(name="Wigman A.")
        author.save()

        author = Author(name="Wu J.")
        author.save()

        author = Author(name="Yannuar N.")
        author.save()

        ###

        LanguageProficiency.objects.all().delete()

        language_proficiency = LanguageProficiency(name="L1", weight="0")
        language_proficiency.save()

        language_proficiency = LanguageProficiency(name="L2", weight="1")
        language_proficiency.save()

        language_proficiency = LanguageProficiency(name="L3", weight="2")
        language_proficiency.save()

        language_proficiency = LanguageProficiency(name="Other", weight="3")
        language_proficiency.save()

        ###

        CorpusType.objects.all().delete()

        corpus_type = CorpusType(name="monolingual", weight="0")
        corpus_type.save()

        corpus_type = CorpusType(name="bilingual", weight="1")
        corpus_type.save()

        corpus_type = CorpusType(name="multilingual", weight="2")
        corpus_type.save()

        corpus_type = CorpusType(name="other", weight="3")
        corpus_type.save()

        ###

        Language.objects.all().delete()
        
        language = Language(name="Aari")
        language.save()
        
        language = Language(name="Aasax")
        language.save()
        
        language = Language(name="Adamorobe Sign Language")
        language.save()
        
        language = Language(name="Adang")
        language.save()
        
        language = Language(name="Akan")
        language.save()
        
        language = Language(name="Akiek")
        language.save()
        
        language = Language(name="Akileh")
        language.save()
        
        language = Language(name="Alagwa")
        language.save()
        
        language = Language(name="Alorese")
        language.save()
        
        language = Language(name="American Sign Language")
        language.save()
        
        language = Language(name="Arabic")
        language.save()
        
        language = Language(name="Arabic Dialects")
        language.save()
        
        language = Language(name="Armenian")
        language.save()
        
        language = Language(name="Artificial Language")
        language.save()
        
        language = Language(name="Austronesian Languages")
        language.save()
        
        language = Language(name="Awa Pit")
        language.save()
        
        language = Language(name="Aymara")
        language.save()
        
        language = Language(name="Bambara")
        language.save()
        
        language = Language(name="Berber")
        language.save()
        
        language = Language(name="Berbey Sign Language")
        language.save()
        
        language = Language(name="Biaks")
        language.save()
        
        language = Language(name="Bondei")
        language.save()
        
        language = Language(name="Bouakako Sign Language")
        language.save()
        
        language = Language(name="British English")
        language.save()
        
        language = Language(name="Bété")
        language.save()
        
        language = Language(name="Cantonese")
        language.save()
        
        language = Language(name="Catalan")
        language.save()
        
        language = Language(name="Chechen")
        language.save()
        
        language = Language(name="Chinese")
        language.save()
        
        language = Language(name="Classical Armenian")
        language.save()
        
        language = Language(name="Coastal Terengganu Malay")
        language.save()
        
        language = Language(name="Croatian")
        language.save()
        
        language = Language(name="Cuneiform Luwian")
        language.save()
        
        language = Language(name="Cypriot Greek")
        language.save()
        
        language = Language(name="Danish")
        language.save()
        
        language = Language(name="Datooga")
        language.save()
        
        language = Language(name="Dutch")
        language.save()
        
        language = Language(name="Dutch Dialects")
        language.save()
        
        language = Language(name="Early Modern Dutch")
        language.save()
        
        language = Language(name="East Rote Languages")
        language.save()
        
        language = Language(name="Ecuador Spanish")
        language.save()
        
        language = Language(name="English")
        language.save()
        
        language = Language(name="Ewe")
        language.save()
        
        language = Language(name="Ewondo")
        language.save()
        
        language = Language(name="Farsi")
        language.save()
        
        language = Language(name="Figuig Berber")
        language.save()
        
        language = Language(name="Finnish")
        language.save()
        
        language = Language(name="French")
        language.save()
        
        language = Language(name="Fries")
        language.save()
        
        language = Language(name="Fuchou")
        language.save()
        
        language = Language(name="Funai Helong")
        language.save()
        
        language = Language(name="Georgian")
        language.save()
        
        language = Language(name="German")
        language.save()
        
        language = Language(name="Germanic Languages")
        language.save()
        
        language = Language(name="Ghanaian Sign Language")
        language.save()
        
        language = Language(name="Greek")
        language.save()
        
        language = Language(name="Haags")
        language.save()
        
        language = Language(name="Hadza")
        language.save()
        
        language = Language(name="Hakka")
        language.save()
        
        language = Language(name="Hamar")
        language.save()
        
        language = Language(name="Hausa")
        language.save()
        
        language = Language(name="Hieroglyphic Luwian")
        language.save()
        
        language = Language(name="Hindi")
        language.save()
        
        language = Language(name="Hokkien")
        language.save()
        
        language = Language(name="Hungarian")
        language.save()
        
        language = Language(name="Icelandic")
        language.save()
        
        language = Language(name="Indo-european")
        language.save()
        
        language = Language(name="Inland Terengganu Malay")
        language.save()
        
        language = Language(name="Iraqw")
        language.save()
        
        language = Language(name="Italian")
        language.save()
        
        language = Language(name="Javanese")
        language.save()
        
        language = Language(name="Karo")
        language.save()
        
        language = Language(name="Kelantan Malay")
        language.save()
        
        language = Language(name="Kemak")
        language.save()
        
        language = Language(name="Kikuyu")
        language.save()
        
        language = Language(name="Konso")
        language.save()
        
        language = Language(name="Kopas")
        language.save()
        
        language = Language(name="Kotos Amarasi")
        language.save()
        
        language = Language(name="Kurdish")
        language.save()
        
        language = Language(name="Kusa Manea")
        language.save()
        
        language = Language(name="Latin")
        language.save()
        
        language = Language(name="Lili Wu")
        language.save()
        
        language = Language(name="Lingala Youth Language")
        language.save()
        
        language = Language(name="Luganda")
        language.save()
        
        language = Language(name="Maale")
        language.save()
        
        language = Language(name="Malay")
        language.save()
        
        language = Language(name="Malayalam")
        language.save()
        
        language = Language(name="Malaysia Chinese")
        language.save()
        
        language = Language(name="Malian Sign Language")
        language.save()
        
        language = Language(name="Mandarin")
        language.save()
        
        language = Language(name="Mapudungun")
        language.save()
        
        language = Language(name="Mawayana")
        language.save()
        
        language = Language(name="Mbugu")
        language.save()
        
        language = Language(name="Mexican Spanish")
        language.save()
        
        language = Language(name="Middle English")
        language.save()
        
        language = Language(name="Modern English And Present-day English")
        language.save()
        
        language = Language(name="Moluccan Malay")
        language.save()
        
        language = Language(name="Ngiemboon")
        language.save()
        
        language = Language(name="Nyoro")
        language.save()
        
        language = Language(name="Old English")
        language.save()
        
        language = Language(name="Old Khotanese")
        language.save()
        
        language = Language(name="Oyda")
        language.save()
        
        language = Language(name="Papiamento")
        language.save()
        
        language = Language(name="Papuan Languagues")
        language.save()
        
        language = Language(name="Polish")
        language.save()
        
        language = Language(name="Portuguese")
        language.save()
        
        language = Language(name="Proto-aymara")
        language.save()
        
        language = Language(name="Proto-quechua")
        language.save()
        
        language = Language(name="Punjabi")
        language.save()
        
        language = Language(name="Puquina")
        language.save()
        
        language = Language(name="Purepecha")
        language.save()
        
        language = Language(name="Ro'is Amarasi")
        language.save()
        
        language = Language(name="Romanian")
        language.save()
        
        language = Language(name="Rukiga")
        language.save()
        
        language = Language(name="Russian")
        language.save()
        
        language = Language(name="Sarnámi")
        language.save()
        
        language = Language(name="Sekpele")
        language.save()
        
        language = Language(name="Seme")
        language.save()
        
        language = Language(name="Serbian")
        language.save()
        
        language = Language(name="Sereer")
        language.save()
        
        language = Language(name="Shuangfeng Xiang")
        language.save()
        
        language = Language(name="Sign Languages")
        language.save()
        
        language = Language(name="Siona")
        language.save()
        
        language = Language(name="Somali")
        language.save()
        
        language = Language(name="South Amanuban")
        language.save()
        
        language = Language(name="Spanish")
        language.save()
        
        language = Language(name="Swahili")
        language.save()
        
        language = Language(name="Tamil")
        language.save()
        
        language = Language(name="Tarifyt Berber")
        language.save()
        
        language = Language(name="Tassawaq")
        language.save()
        
        language = Language(name="Telugu")
        language.save()
        
        language = Language(name="Teochew")
        language.save()
        
        language = Language(name="Timaus")
        language.save()
        
        language = Language(name="Toussian")
        language.save()
        
        language = Language(name="Tunen")
        language.save()
        
        language = Language(name="Turkish")
        language.save()
        
        language = Language(name="Various")
        language.save()
        
        language = Language(name="Walikan")
        language.save()
        
        language = Language(name="Wayana")
        language.save()
        
        language = Language(name="Welaun")
        language.save()
        
        language = Language(name="West Timor Languages")
        language.save()
        
        language = Language(name="Wolaytta")
        language.save()
        
        language = Language(name="Wolof")
        language.save()
        
        language = Language(name="Yaaku")
        language.save()
        
        language = Language(name="Zergulla")
        language.save()
        
        language = Language(name="Zigula")
        language.save()
        
        ###

        DataFormat.objects.all().delete()
        
        data_format = DataFormat(name="Analogue")
        data_format.save()
        
        data_format = DataFormat(name="Audio Cassettes")
        data_format.save()
        
        data_format = DataFormat(name="Bdf")
        data_format.save()
        
        data_format = DataFormat(name="Chat")
        data_format.save()
        
        data_format = DataFormat(name="Clan")
        data_format.save()
        
        data_format = DataFormat(name="Cldf")
        data_format.save()
        
        data_format = DataFormat(name="Css")
        data_format.save()
        
        data_format = DataFormat(name="Csv")
        data_format.save()
        
        data_format = DataFormat(name="Digital")
        data_format.save()
        
        data_format = DataFormat(name="Digitalized Cassettes")
        data_format.save()
        
        data_format = DataFormat(name="Doc")
        data_format.save()
        
        data_format = DataFormat(name="Edf")
        data_format.save()
        
        data_format = DataFormat(name="Elan")
        data_format.save()
        
        data_format = DataFormat(name="Excel")
        data_format.save()
        
        data_format = DataFormat(name="Flex")
        data_format.save()
        
        data_format = DataFormat(name="Html")
        data_format.save()
        
        data_format = DataFormat(name="Ipa Transcripts")
        data_format.save()
        
        data_format = DataFormat(name="Json")
        data_format.save()
        
        data_format = DataFormat(name="Kml")
        data_format.save()
        
        data_format = DataFormat(name="Letters")
        data_format.save()
        
        data_format = DataFormat(name="Mp3")
        data_format.save()
        
        data_format = DataFormat(name="Mp4")
        data_format.save()
        
        data_format = DataFormat(name="Mpeg")
        data_format.save()
        
        data_format = DataFormat(name="Mpeg-1")
        data_format.save()
        
        data_format = DataFormat(name="Mpeg-2")
        data_format.save()
        
        data_format = DataFormat(name="Ms Access")
        data_format.save()
        
        data_format = DataFormat(name="Mysql")
        data_format.save()
        
        data_format = DataFormat(name="Newspapers")
        data_format.save()
        
        data_format = DataFormat(name="Notebooks")
        data_format.save()
        
        data_format = DataFormat(name="Ocr-ed Scans")
        data_format.save()
        
        data_format = DataFormat(name="Orthographic Transcription")
        data_format.save()
        
        data_format = DataFormat(name="Pdf")
        data_format.save()
        
        data_format = DataFormat(name="Photocopies")
        data_format.save()
        
        data_format = DataFormat(name="Praat")
        data_format.save()
        
        data_format = DataFormat(name="Qualtrics")
        data_format.save()
        
        data_format = DataFormat(name="R")
        data_format.save()
        
        data_format = DataFormat(name="Rmd")
        data_format.save()
        
        data_format = DataFormat(name="Rtf")
        data_format.save()
        
        data_format = DataFormat(name="Scans")
        data_format.save()
        
        data_format = DataFormat(name="Spss")
        data_format.save()
        
        data_format = DataFormat(name="Starling Database")
        data_format.save()
        
        data_format = DataFormat(name="Ttl")
        data_format.save()
        
        data_format = DataFormat(name="Txt")
        data_format.save()
        
        data_format = DataFormat(name="Unicode")
        data_format.save()
        
        data_format = DataFormat(name="Vhs")
        data_format.save()
        
        data_format = DataFormat(name="Video Cassettes")
        data_format.save()
        
        data_format = DataFormat(name="Wav")
        data_format.save()
        
        data_format = DataFormat(name="Xls")
        data_format.save()
        
        data_format = DataFormat(name="Xml")
        data_format.save()

        ###

        Location.objects.all().delete()
        
        location = Location(name="Argentina, Peru, Spain")
        location.save()
        
        location = Location(name="Burkina Faso")
        location.save()
        
        location = Location(name="Cameroon")
        location.save()
        
        location = Location(name="Chile")
        location.save()
        
        location = Location(name="China")
        location.save()
        
        location = Location(name="Congo")
        location.save()
        
        location = Location(name="Cyprus")
        location.save()
        
        location = Location(name="Denmark")
        location.save()
        
        location = Location(name="Ecuador")
        location.save()
        
        location = Location(name="Ethiopia")
        location.save()
        
        location = Location(name="France")
        location.save()
        
        location = Location(name="Ghana")
        location.save()
        
        location = Location(name="Ghana, Ivory Coast")
        location.save()
        
        location = Location(name="Indonesia")
        location.save()
        
        location = Location(name="Ivory Coast")
        location.save()
        
        location = Location(name="Kenya")
        location.save()
        
        location = Location(name="Malaysia")
        location.save()
        
        location = Location(name="Mali")
        location.save()
        
        location = Location(name="Mexico")
        location.save()
        
        location = Location(name="Morocco")
        location.save()
        
        location = Location(name="Niger")
        location.save()
        
        location = Location(name="Nigeria")
        location.save()
        
        location = Location(name="Online")
        location.save()
        
        location = Location(name="Other")
        location.save()
        
        location = Location(name="Peru")
        location.save()
        
        location = Location(name="Russia")
        location.save()
        
        location = Location(name="Saudi Arabia")
        location.save()
        
        location = Location(name="Senegal")
        location.save()
        
        location = Location(name="Serbia, Online")
        location.save()
        
        location = Location(name="Somalia")
        location.save()
        
        location = Location(name="Suriname")
        location.save()
        
        location = Location(name="Tanzania")
        location.save()
        
        location = Location(name="The Netherlands")
        location.save()
        
        location = Location(name="The Netherlands, Belgium")
        location.save()
        
        location = Location(name="The Netherlands, UK, Germany")
        location.save()
        
        location = Location(name="UK")
        location.save()
        
        location = Location(name="UK and USA")
        location.save()
        
        location = Location(name="USA")
        location.save()
        
        location = Location(name="Uganda")
        location.save()

        ###

        DataType.objects.all().delete()
        
        data_type = DataType(name="audio", weight="0")
        data_type.save()
        
        data_type = DataType(name="audiovisual", weight="1")
        data_type.save()
        
        data_type = DataType(name="photo", weight="2")
        data_type.save()
        
        data_type = DataType(name="written", weight="3")
        data_type.save()
        
        data_type = DataType(name="other", weight="4")
        data_type.save()

        ###

        Modality.objects.all().delete()
        
        modality = Modality(name="signed", weight="0")
        modality.save() 

        modality = Modality(name="spoken", weight="1")
        modality.save() 
        
        modality = Modality(name="written", weight="2")
        modality.save() 

        modality = Modality(name="other", weight="3")
        modality.save() 

        ###

        Domain.objects.all().delete()
        
        domain = Domain(name="African Linguistics")
        domain.save() 
        
        domain = Domain(name="Anatolian Linguistics")
        domain.save() 
        
        domain = Domain(name="Anthropological Linguistics")
        domain.save() 
        
        domain = Domain(name="Artificial Language Learning")
        domain.save() 
        
        domain = Domain(name="Austronesian Linguistics")
        domain.save() 
        
        domain = Domain(name="Bilingual Acquisition")
        domain.save() 
        
        domain = Domain(name="Bilingualism")
        domain.save() 
        
        domain = Domain(name="Clause Type")
        domain.save() 
        
        domain = Domain(name="Code-switching")
        domain.save() 
        
        domain = Domain(name="Codicology")
        domain.save() 
        
        domain = Domain(name="Cognitive Control")
        domain.save() 
        
        domain = Domain(name="Comparative Syntax")
        domain.save() 
        
        domain = Domain(name="Computational Linguistics")
        domain.save() 
        
        domain = Domain(name="Consonants")
        domain.save() 
        
        domain = Domain(name="Contrastive Linguistics")
        domain.save() 
        
        domain = Domain(name="Conversational Data")
        domain.save() 
        
        domain = Domain(name="Correspondence Linguistic Analysis")
        domain.save() 
        
        domain = Domain(name="Crosslinguistics")
        domain.save() 
        
        domain = Domain(name="Descriptive Linguistics")
        domain.save() 
        
        domain = Domain(name="Dialectology")
        domain.save() 
        
        domain = Domain(name="Digital Humanities")
        domain.save() 
        
        domain = Domain(name="Eeg")
        domain.save() 
        
        domain = Domain(name="Elicitation")
        domain.save() 
        
        domain = Domain(name="Ellipsis")
        domain.save() 
        
        domain = Domain(name="Epistolary")
        domain.save() 
        
        domain = Domain(name="Erp")
        domain.save() 
        
        domain = Domain(name="Ethnicity")
        domain.save() 
        
        domain = Domain(name="Ethnolinguistics")
        domain.save() 
        
        domain = Domain(name="Etymology")
        domain.save() 
        
        domain = Domain(name="Forensic Linguistics")
        domain.save() 
        
        domain = Domain(name="Forensic Phonetics")
        domain.save() 
        
        domain = Domain(name="Fragments")
        domain.save() 
        
        domain = Domain(name="Gender Mismatch")
        domain.save() 
        
        domain = Domain(name="General Comparative Linguistics")
        domain.save() 
        
        domain = Domain(name="Germanic")
        domain.save() 
        
        domain = Domain(name="Gesture Studies")
        domain.save() 
        
        domain = Domain(name="Grammar")
        domain.save() 
        
        domain = Domain(name="Grammar,african Linguistics")
        domain.save() 
        
        domain = Domain(name="Grammar-writing")
        domain.save() 
        
        domain = Domain(name="Grammaticalization")
        domain.save() 
        
        domain = Domain(name="Head Subject")
        domain.save() 
        
        domain = Domain(name="Historical Linguistics")
        domain.save() 
        
        domain = Domain(name="Historical Sociolinguistics")
        domain.save() 
        
        domain = Domain(name="Historiography Of The Language")
        domain.save() 
        
        domain = Domain(name="In-situ Questions")
        domain.save() 
        
        domain = Domain(name="Indo-european Linguistics")
        domain.save() 
        
        domain = Domain(name="Information Structure")
        domain.save() 
        
        domain = Domain(name="Intercultural Bilingual Education")
        domain.save() 
        
        domain = Domain(name="Interlanguage")
        domain.save() 
        
        domain = Domain(name="Interviews")
        domain.save() 
        
        domain = Domain(name="Intraspeaker Variation")
        domain.save() 
        
        domain = Domain(name="Journalism")
        domain.save() 
        
        domain = Domain(name="Language Acquisition")
        domain.save() 
        
        domain = Domain(name="Language Acquisition")
        domain.save() 
        
        domain = Domain(name="Language And Cognition Interface")
        domain.save() 
        
        domain = Domain(name="Language Attitude")
        domain.save() 
        
        domain = Domain(name="Language Contact")
        domain.save() 
        
        domain = Domain(name="Language Description")
        domain.save() 
        
        domain = Domain(name="Language Documentation")
        domain.save() 
        
        domain = Domain(name="Language Evolution")
        domain.save() 
        
        domain = Domain(name="Language Identity")
        domain.save() 
        
        domain = Domain(name="Language Instructions")
        domain.save() 
        
        domain = Domain(name="Language Of Private Correspondence")
        domain.save() 
        
        domain = Domain(name="Language Policy")
        domain.save() 
        
        domain = Domain(name="Language Reversal")
        domain.save() 
        
        domain = Domain(name="Language Use")
        domain.save() 
        
        domain = Domain(name="Language Variation")
        domain.save() 
        
        domain = Domain(name="Languaging")
        domain.save() 
        
        domain = Domain(name="Learner Corpus")
        domain.save() 
        
        domain = Domain(name="Letters")
        domain.save() 
        
        domain = Domain(name="Lexical Typology")
        domain.save() 
        
        domain = Domain(name="Lexicography")
        domain.save() 
        
        domain = Domain(name="Lexis")
        domain.save() 
        
        domain = Domain(name="Light Verbs")
        domain.save() 
        
        domain = Domain(name="Linguistic Citizenship")
        domain.save() 
        
        domain = Domain(name="Linguistic Manipulation")
        domain.save() 
        
        domain = Domain(name="Linked Data")
        domain.save() 
        
        domain = Domain(name="Literacy")
        domain.save() 
        
        domain = Domain(name="Long Distance Dependencies")
        domain.save() 
        
        domain = Domain(name="Morpho-syntax")
        domain.save() 
        
        domain = Domain(name="Morphology")
        domain.save() 
        
        domain = Domain(name="Multilingualism")
        domain.save() 
        
        domain = Domain(name="Narratives")
        domain.save() 
        
        domain = Domain(name="Natural Speech")
        domain.save() 
        
        domain = Domain(name="Negative Polarity Items")
        domain.save() 
        
        domain = Domain(name="Neurolinguistics")
        domain.save() 
        
        domain = Domain(name="Old English")
        domain.save() 
        
        domain = Domain(name="Omotic Languages")
        domain.save() 
        
        domain = Domain(name="Oral Traditions")
        domain.save() 
        
        domain = Domain(name="Orthography")
        domain.save() 
        
        domain = Domain(name="Particle Verbs")
        domain.save() 
        
        domain = Domain(name="Philology")
        domain.save() 
        
        domain = Domain(name="Phonetics")
        domain.save() 
        
        domain = Domain(name="Phonology")
        domain.save() 
        
        domain = Domain(name="Phonotactics")
        domain.save() 
        
        domain = Domain(name="Pluractionals")
        domain.save() 
        
        domain = Domain(name="Prescriptivism")
        domain.save() 
        
        domain = Domain(name="Pronunciation")
        domain.save() 
        
        domain = Domain(name="Prosody")
        domain.save() 
        
        domain = Domain(name="Psycholinguistics")
        domain.save() 
        
        domain = Domain(name="Questions")
        domain.save() 
        
        domain = Domain(name="Rhetorics")
        domain.save() 
        
        domain = Domain(name="Rule Learning")
        domain.save() 
        
        domain = Domain(name="Second Language Acquisition")
        domain.save() 
        
        domain = Domain(name="Semantics")
        domain.save() 
        
        domain = Domain(name="Sign Linguistics")
        domain.save() 
        
        domain = Domain(name="Social Cognition")
        domain.save() 
        
        domain = Domain(name="Sociohistorical Linguistics")
        domain.save() 
        
        domain = Domain(name="Sociolinguistics")
        domain.save() 
        
        domain = Domain(name="Sociophonetics")
        domain.save() 
        
        domain = Domain(name="South East Asian Studies")
        domain.save() 
        
        domain = Domain(name="Speaker Characteristics")
        domain.save() 
        
        domain = Domain(name="Speech Acoustics")
        domain.save() 
        
        domain = Domain(name="Spelling")
        domain.save() 
        
        domain = Domain(name="Standaridization Process")
        domain.save() 
        
        domain = Domain(name="Syllable")
        domain.save() 
        
        domain = Domain(name="Syntax")
        domain.save() 
        
        domain = Domain(name="Tense & Aspect")
        domain.save() 
        
        domain = Domain(name="Tone")
        domain.save() 
        
        domain = Domain(name="Topological Relations")
        domain.save() 
        
        domain = Domain(name="Usage Guides")
        domain.save() 
        
        domain = Domain(name="Verbal Aspect")
        domain.save() 
        
        domain = Domain(name="Verlan")
        domain.save() 
        
        domain = Domain(name="Voice Comparison")
        domain.save() 
        
        domain = Domain(name="Youth Language")
        domain.save() 
        
