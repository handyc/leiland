from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404, HttpResponseServerError

from django.shortcuts import render
from django.template import loader
from django.utils import timezone

from itertools import chain
# needed for query concatenation?

from django.db.models import Q

#from subprocess import Popen, PIPE, STDOUT

#import json
#import datetime

import operator
from functools import reduce

from .forms import SearchForm

from .models import Dataset

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

index_template="webapp/index.html"
search_template="webapp/search.html"
testsearch_template="webapp/testsearch.html"
about_template="webapp/about.html"
results_template="webapp/results.html"
dataset_template="webapp/dataset.html"
cmdi_template="webapp/cmdi.html"
#index_template="webapp/index.html"
#index_template="webapp/index.html"
#index_template="webapp/index.html"

def index(request):
    template = loader.get_template(index_template)
    datasets = Dataset.objects.all()
    context = {
        'datasets': datasets,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template(search_template)

    annotation_types = AnnotationType.objects.all()
    authors = Author.objects.all()
    corpus_types = CorpusType.objects.all().order_by('weight')
    data_formats = DataFormat.objects.all()
    data_types = DataType.objects.all().order_by('weight')
    domains = Domain.objects.all()
    genders = Gender.objects.all().order_by('weight')
    language_proficiencies = LanguageProficiency.objects.all().order_by('weight')
    languages = Language.objects.all()
    locations = Location.objects.all()
    modalities = Modality.objects.all().order_by('weight')
    access = Access.objects.all()

    context = {
        'annotation_types': annotation_types,
        'authors': authors,
        'corpus_types': corpus_types,
        'data_formats': data_formats,
        'data_types': data_types,
        'domains': domains,
        'genders': genders,
        'language_proficiencies': language_proficiencies,
        'languages': languages,
        'locations': locations,
        'modalities': modalities,
        'access': access,
    }
    return HttpResponse(template.render(context, request))

def testsearch(request):
    #template = loader.get_template(testsearch_template)
    template = testsearch_template

    annotation_types = AnnotationType.objects.all()
    authors = Author.objects.all()
    corpus_types = CorpusType.objects.all().order_by('weight')
    data_formats = DataFormat.objects.all()
    data_types = DataType.objects.all().order_by('weight')
    domains = Domain.objects.all()
    genders = Gender.objects.all().order_by('weight')
    language_proficiencies = LanguageProficiency.objects.all().order_by('weight')
    languages = Language.objects.all()
    locations = Location.objects.all()
    modalities = Modality.objects.all().order_by('weight')

    #model = Author
    #form = SearchForm()

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    context = {
        'annotation_types': annotation_types,
        'authors': authors,
        'corpus_types': corpus_types,
        'data_formats': data_formats,
        'data_types': data_types,
        'domains': domains,
        'genders': genders,
        'language_proficiencies': language_proficiencies,
        'languages': languages,
        'locations': locations,
        'modalities': modalities,
        'form': form,
    }
    return render(request, template, context)



    #success_url = reverse_lazy(‘testresults’)



    #return HttpResponse(template.render(context, request))
    #return HttpResponse(template.render(context, request))
    
    return render(request, template, {"form": form})


def about(request):
    template = loader.get_template(about_template)
    #datasets = Dataset.objects.all()
    context = {
        #'datasets': datasets,
    }
    return HttpResponse(template.render(context, request))

def cmdi(request):
    template = loader.get_template(cmdi_template)
    #datasets = Dataset.objects.all()
    context = {
        #'datasets': datasets,
    }
    return HttpResponse(template.render(context, request))

#qs1.intersection(qs2, qs3) -- simple queryset intersection
def testresults(request):
    template = loader.get_template(results_template)

    #https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
    context = {}
    form = SearchForm(request.POST or None)
    #form = GeeksForm(request.POST or None)
    context['form']= form
    if request.POST:
        if form.is_valid():
            datasets = Dataset.objects.none()

            temp = form.cleaned_data.get("languages")
            

            #ds = Dataset.objects.filter(languages_link=temp)
            #datasets = list(chain(datasets, ds,))

            """
            #print(temp)
            if temp:
                for e in temp:
                    ds = Dataset.objects.filter(languages_link=e)
                    #try:
                    #    #datasets
                    #    datasets = datasets & ds
                    #except NameError:
                    #datasets = ds
                    datasets = list(chain(datasets, ds,))
            """
            temp = form.cleaned_data.get("modalities")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(modalities_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds
            
            temp = form.cleaned_data.get("annotations")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(annotation_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("datatypes")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(data_types_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("dataformats")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(data_formats_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("corpustypes")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(corpus_types_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds
            
            temp = form.cleaned_data.get("proficiencies")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(language_proficiencies_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("genders")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(gender_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try: 
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("locations")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(location_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("authors")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(authorlink=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("domains")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(domain_link=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds

            temp = form.cleaned_data.get("access")
            #print(temp)
            if temp:     
                for e in temp:
                    ds = Dataset.objects.filter(availability=e)
                    #datasets = list(chain(datasets, ds,))
                    try:
                        #datasets
                        #datasets = datasets & ds
                        datasets = list(chain(datasets, ds,))
                    except NameError:
                        datasets = ds
                    #datasets = datasets | ds
                    #datasets = datasets & ds

            try:
                datasets
            except NameError: 
                datasets = None
            
            context = {"error_message": temp, 'datasets': datasets,}
            return render(request, results_template, context)
    #return render(request, "home.html", context)
    return render(request, results_template, context)

    #datasets = Dataset.objects.all()

    context = {
        'datasets': datasets,
    }
    return HttpResponse(template.render(context, request))

def results(request):
    template = loader.get_template(results_template)

    datasets = Dataset.objects.all()
    form = SearchForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            datasets = Dataset.objects.none()
            #datasets = Dataset.objects.all()
            #temp = form.cleaned_data.get("language")
            templ = request.POST.getlist("language")
            tempm = request.POST.getlist("modality")
            tempan = request.POST.getlist("annotation_type")
            tempdt = request.POST.getlist("data_type")
            tempda = request.POST.getlist("data_format")
            tempct = request.POST.getlist("corpus_type")
            temppr = request.POST.getlist("language_proficiency")
            tempge = request.POST.getlist("gender")
            templo = request.POST.getlist("location")
            tempau = request.POST.getlist("author")
            tempdo = request.POST.getlist("domain")
            tempac = request.POST.getlist("accessfield")

            lookups = {}
            #lookups = []

            templ_string = "languages_link__in=templ"
            tempm_string = "modalities_link__in=tempm"
            tempan_string = "annotation_link__in=tempan"
            tempdt_string = "data_types_link__in=tempdt"
            tempda_string = "data_formats_link__in=tempda"
            tempct_string = "corpus_types_link__in=tempct"
            temppr_string = "language_proficiencies_link__in=temppr"
            tempge_string = "gender_link__in=tempge"
            templo_string = "location_link__in=templo"
            tempau_string = "authorlink__in=tempau"
            tempdo_string = "domain_link__in=tempdo"
            tempac_string = "availability_link__in=tempac"
                        
            #if lookups:
            #    qs = qs.filter(reduce(operator.or_, [Q(f) for f in lookups.items()]))
            
            #if lookups:
            #    datasets = Dataset.objects.filter(reduce(operator.or_, [Q(f) for f in lookups.items()]))

            #datasets = Dataset.objects.filter(Q(languages_link__in=templ)).order_by('title').distinct()

            # a very basic search on languages with distinct return

            #datasets = Dataset.objects.filter(Q(languages_link__in=templ) & Q(domain_link__in=tempdo)).distinct()
            #datasets = Dataset.objects.filter(Q(languages_link__in=templ) & Q(domain_link__in=tempdo) & Q(modalities_link__in=tempm)).distinct()
            datasets = Dataset.objects.all()

            if templ:
                datasets = datasets.filter(languages_link__in=templ)
            if tempm:
                datasets = datasets.filter(modalities_link__in=tempm)
            if tempan:
                datasets = datasets.filter(annotation_link__in=tempan)
            if tempdt:
                datasets = datasets.filter(data_types_link__in=tempdt)
            if tempda:
               datasets = datasets.filter(data_formats_link__in=tempda)
            if tempct:
                datasets = datasets.filter(corpus_types_link__in=tempct)
            if temppr:
                datasets = datasets.filter(language_proficiencies_link__in=temppr)
            if tempge:
                datasets = datasets.filter(gender_link__in=tempge)
            if templo:
                datasets = datasets.filter(location_link__in=templo)
            if tempau:
                datasets = datasets.filter(authorlink__in=tempau)
            if tempdo:
                datasets = datasets.filter(domain_link__in=tempdo)
            if tempac:
                datasets = datasets.filter(availability_link__in=tempac)
            
            datasets = datasets.distinct()

            if not templ and not tempm and not tempan and not tempdt and not tempda and not tempct and not temppr and not tempge and not templo and not tempau and not tempdo and not tempac:
                datasets = None
            
            #datasets = datasets.filter(domain_link__in=tempdo)
            #datasets = datasets.filter(modalities_link__in=tempm)


            #datasets = Dataset.objects.filter(Q(domain_link__in=tempdo))
            #datasets = Dataset.objects.filter(Q(languages_link__in=templ))

            #datasets = Dataset.objects.filter(languages_link__in=templ).filter(modalities_link__in=tempm)
            #datasets = Dataset.objects.filter(Q(languages_link__in=templ) & Q(data_formats_link__in=tempf))
            
            #datasets = Dataset.objects.filter(Q(languages_link__in=templ)).order_by('title').distinct()
            #datasets = Dataset.objects.filter(Q(modalities_link__in=tempf)).order_by('title').distinct()

            #datasets = Dataset.objects.filter(languages_link__in=templ)
            #datasets = Dataset.objects.filter(Q(modalities_link__in=tempm))

            #datasets = Dataset.objects.filter(Q(annotation_link__in=tempan))
            #datasets = Dataset.objects.all()
            
            #datasets = Dataset.objects.filter(Q(data_types_link__in=tempdt))
            
            #datasets = Dataset.objects.filter(Q(data_formats_link__in=tempda))

            #datasets = Dataset.objects.filter(Q(corpus_types_link__in=tempct))

            #datasets = Dataset.objects.filter(Q(language_proficiencies_link__in=temppr))
            #datasets = Dataset.objects.filter(Q(gender_link__in=tempge))

            #datasets = Dataset.objects.filter(Q(location_link__in=templo))
            #datasets = Dataset.objects.filter(Q(authorlink__in=tempau))
            
            #datasets = Dataset.objects.filter(Q(domain_link__in=tempdo))

            #datasets = Dataset.objects.filter(Q(availability_link__in=tempac))

            
            templ = request.POST.getlist("language")
            tempm = request.POST.getlist("modalities")
            tempf = request.POST.getlist("dataformats")
            tempan = request.POST.getlist("annotations")
            tempdt = request.POST.getlist("datatypes")
            tempda = request.POST.getlist("dataformats")
            tempct = request.POST.getlist("corpustypes")
            temppr = request.POST.getlist("proficiencies")
            tempge = request.POST.getlist("genders")
            templo = request.POST.getlist("locations")
            tempau = request.POST.getlist("authors")
            tempdo = request.POST.getlist("domains")
            tempac = request.POST.getlist("accessfield")
            


            errormsg = tempdo

            #datasets = Dataset.objects.filter(Q(languages_link__in=templ)).order_by('title').distinct()
            
            #datasets = set(datasets)

            #datasets = list(chain(datasets, ds,))
            
            """
            if temp:
                for e in temp:
                    ds = Dataset.objects.filter(languages_link=e)
                    #ds = Dataset.objects.filter(name=e)
                    #try:
                    #    #datasets
                    #    datasets = datasets & ds
                    #except NameError:
                    #datasets = ds
                    datasets = list(chain(datasets, ds,))
            #print(temp)
            """

    context = {
        'datasets': datasets,
        'error_message': errormsg,
    }
    return HttpResponse(template.render(context, request))


def dataset(request, dataset_id):
    template = loader.get_template(dataset_template)
    #datasets = Dataset.objects.all()
    dataset = Dataset.objects.get(pk=dataset_id)

    authors = dataset.authorlink.all()
    languages = dataset.languages_link.all()
    isos = dataset.iso_link.all()
    glottos = dataset.glotto_link.all()

    context = {
        'dataset': dataset,
        'authors': authors,
        'languages': languages,
        'glottos': glottos,
        'isos': isos,
    }
    return HttpResponse(template.render(context, request))


