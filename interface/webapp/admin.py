from django.contrib import admin

admin.site.site_header = "Leiland";
admin.site.site_title = "Leiland";

from .models import Dataset

from .models import Author
from .models import Language
from .models import Glottocode
from .models import ISO
from .models import AnnotationType
from .models import CorpusType
from .models import Location
from .models import Domain
from .models import DataType
from .models import Modality
from .models import DataFormat
from .models import LanguageProficiency
from .models import Gender
from .models import Access

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'comments', 'metadata',
        'years', 'contact', 'software',
        'author', 'rightsholder',
        #'get_author',
        'publisher',
        'annotation_types', 'domains', 'sublocation', 'location',
        'data_formats', 'data_size', 'collection_method',
        'languages', 'corpus_types', 'corpus_note', 'data_types',
        'genders', 'agegroup', 'demographics',
        'language_proficiencies', 'modalities',
        'availability', 'access_note',
        'iso_language_code', 'glottocodes', 'cmdi', 'banklink',)

    list_filter = ('title',)

    fields = ('title', 'description', 'comments', 'metadata',
        'years', 'contact', 'software',
        'author', 'rightsholder',
        #'get_author',
        'publisher',
        'annotation_types', 'domains', 'sublocation', 'location',
        'data_formats', 'data_size', 'collection_method',
        'languages', 'corpus_types', 'corpus_note', 'data_types',
        'genders', 'agegroup', 'demographics',
        'language_proficiencies', 'modalities',
        'availability', 'access_note',
        'iso_language_code', 'glottocodes', 'cmdi', 'banklink',)

    #def get_author(self, obj):
    #    return [author.name for author in obj.author.all()]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Glottocode)
class GlottocodeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(ISO)
class ISOAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(AnnotationType)
class AnnotationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(CorpusType)
class CorpusTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Domain)
class Domain(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Modality)
class ModalityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(DataFormat)
class DataFormatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(LanguageProficiency)
class LanguageProficiencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    fields = ('name',)

