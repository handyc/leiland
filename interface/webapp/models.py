from django.db import models

#from django.contrib.auth import get_user_model

class Dataset(models.Model):
    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Datasets"

    #availability = models.CharField(max_length=30, null=True, blank=True)
    # .startYear(dto.getStartYear())
    # .endYear(dto.getEndYear())
    # .accessRightsDescription(dto.getAccessRightsComments())
    # .cmdiPersistentIdentifier(dto.getCmdiPersistentIdentifier())
    # .comments(dto.getComments())
    # .contactPerson(dto.getContactPerson())
    # .corpusTypeDescription(dto.getCorpusTypeDescription())
    # .dataFormatsDescription(dto.getDataFormatsDescription())
    # .dataTypesDescription(dto.getDataTypesDescription())
    # .description(dto.getDescription())
    # .isoCode(dto.getIsoCode())
    # .glottoCode(dto.getGlottoCode())
    # .metadata(dto.getMetadata())
    # .participants(dto.getParticipants())
    # .publisher(dto.getPublisher())
    # .title(dto.getTitle())
    # .author(author)
    # .location(location)
    # .annotationTypes(annotationTypes)
    # .dataFormats(dataFormats)
    # .domains(domains)
    # .languages(languages)
    # .corpusTypes(dto.getCorpusTypes())
    # .dataTypes(dto.getDataTypes())
    # .genders(dto.getGenders())
    # .languageProficiencies(dto.getLanguageProficiencies())
    # .modalities(dto.getModalities())

    description = models.CharField(max_length=300, null=True, blank=True)
    comments = models.CharField(max_length=300, null=True, blank=True)
    years = models.CharField(max_length=300, null=True, blank=True)
    contact = models.CharField(max_length=300, null=True, blank=True)
    software = models.CharField(max_length=300, null=True, blank=True)

    publisher = models.CharField(max_length=300, null=True, blank=True)

    cmdi = models.CharField(max_length=300, null=True, blank=True)
    banklink = models.CharField(max_length=300, null=True, blank=True)

    title = models.CharField(max_length=300, null=True, blank=True)

    author = models.CharField(max_length=300, null=True, blank=True)
    authorlink = models.ManyToManyField('Author', blank=True)
    
    rightsholder = models.CharField(max_length=300, null=True, blank=True)

    ###

    sublocation = models.CharField(max_length=300, null=True, blank=True)

    location = models.CharField(max_length=300, null=True, blank=True)
    location_link = models.ManyToManyField('Location', blank=True)

    annotation_types = models.CharField(max_length=300, null=True, blank=True)
    annotation_link = models.ManyToManyField('AnnotationType', blank=True)

    data_formats = models.CharField(max_length=300, null=True, blank=True)
    data_formats_link = models.ManyToManyField('DataFormat', blank=True)

    data_size = models.CharField(max_length=300, null=True, blank=True)

    domains = models.CharField(max_length=300, null=True, blank=True)
    domain_link = models.ManyToManyField('Domain', blank=True)

    ###
    languages = models.CharField(max_length=300, null=True, blank=True)
    languages_link = models.ManyToManyField('Language', blank=True)

    glotto_link = models.ManyToManyField('Glottocode', blank=True)
    iso_link = models.ManyToManyField('ISO', blank=True)

    iso_language_code = models.CharField(max_length=300, null=True, blank=True)
    glottocodes = models.CharField(max_length=300, null=True, blank=True)
    ###

    corpus_types = models.CharField(max_length=300, null=True, blank=True)
    corpus_types_link = models.ManyToManyField('CorpusType', blank=True)

    corpus_note = models.CharField(max_length=300, null=True, blank=True)
    collection_method = models.CharField(max_length=300, null=True, blank=True)

    data_types = models.CharField(max_length=300, null=True, blank=True)
    data_types_link = models.ManyToManyField('DataType', blank=True)

    agegroup = models.CharField(max_length=300, null=True, blank=True)
    demographics = models.CharField(max_length=300, null=True, blank=True)

    genders = models.CharField(max_length=300, null=True, blank=True)
    gender_link = models.ManyToManyField('Gender', blank=True)


    language_proficiencies = models.CharField(max_length=300, null=True,
        blank=True)
    language_proficiencies_link = models.ManyToManyField('LanguageProficiency', blank=True)

    modalities = models.CharField(max_length=300, null=True, blank=True)
    modalities_link = models.ManyToManyField('Modality', blank=True)

    availability = models.CharField(max_length=300, null=True, blank=True)
    availability_link = models.ManyToManyField('Access', blank=True)

    access_note = models.CharField(max_length=300, null=True, blank=True)
    metadata = models.CharField(max_length=300, null=True, blank=True)

    # move to Language -- this is a temporary fix
    #glottocode = models.CharField(max_length=10, null=True, blank=True)
    #iso = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title

####

class Author(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Authors"

    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Languages"

    name = models.CharField(max_length=300, null=True, blank=True)
    #glottocode = models.CharField(max_length=10, null=True, blank=True)
    #iso = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Glottocode(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Glottocodes"

    name = models.CharField(max_length=10, null=True, blank=True)
    #glottocode = models.CharField(max_length=10, null=True, blank=True)
    #iso = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class ISO(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "ISOcodes"

    name = models.CharField(max_length=10, null=True, blank=True)
    #glottocode = models.CharField(max_length=10, null=True, blank=True)
    #iso = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class AnnotationType(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Annotation Types"

    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class CorpusType(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Corpus Types"

    name = models.CharField(max_length=300, null=True, blank=True)
    weight = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Locations"

    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class Domain(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Domains"

    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class DataType(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Data Types"

    name = models.CharField(max_length=300, null=True, blank=True)
    weight = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Modality(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Modalities"

    name = models.CharField(max_length=300, null=True, blank=True)
    weight = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class DataFormat(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Data Formats"

    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class LanguageProficiency(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Language Proficiencies"

    name = models.CharField(max_length=300, null=True, blank=True)
    weight = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Genders"

    name = models.CharField(max_length=300, null=True, blank=True)
    weight = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Access(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Access"

    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

