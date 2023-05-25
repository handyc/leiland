from django import forms
#from django_select2 import forms
from django_select2 import forms as s2forms
from django_select2.forms import Select2MultipleWidget

from .models import Author
from .models import Language
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

#from core.models import Member

class SearchForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = []
    #name = forms.CharField()
    #date = forms.DateInput()
    languages = forms.ModelMultipleChoiceField(
        queryset = Language.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        #widget = forms.SelectMultiple,
        #widget = forms.Select2MultipleWidget(attrs={'data-width': '100%'}),
        widget = s2forms.Select2MultipleWidget(attrs={'data-width': '100%'}),
        required = False
    )

    modalities = forms.ModelMultipleChoiceField(
        queryset = Modality.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        #widget = forms.SelectMultiple,
        widget = s2forms.Select2MultipleWidget(attrs={'data-width': '100%'}),

        required = False
    )

    annotations = forms.ModelMultipleChoiceField(
        queryset = AnnotationType.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    datatypes = forms.ModelMultipleChoiceField(
        queryset = DataType.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    dataformats = forms.ModelMultipleChoiceField(
        queryset = DataFormat.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    corpustypes = forms.ModelMultipleChoiceField(
        queryset = CorpusType.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    proficiencies = forms.ModelMultipleChoiceField(
        queryset = LanguageProficiency.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    genders = forms.ModelMultipleChoiceField(
        queryset = Gender.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    locations = forms.ModelMultipleChoiceField(
        queryset = Location.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    authors = forms.ModelMultipleChoiceField(
        queryset = Author.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )
    
    domains = forms.ModelMultipleChoiceField(
        queryset = Domain.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )

    access = forms.ModelMultipleChoiceField(
        queryset = Access.objects.all(),
        #widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
        required = False
    )
