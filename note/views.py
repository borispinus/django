import json
from django.shortcuts import render_to_response, redirect
from note.models import Note
from django.http.response import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from note.forms import NoteForm
from django.core.context_processors import csrf
from datetime import datetime
from django.core import serializers
from django.utils.functional import Promise
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super(LazyEncoder, self).default(obj)


def all(request):
    args = {}
    args.update(csrf(request))
    args['notes'] = Note.objects.all
    return render_to_response('all.html', args)


def get(request, note_id):
    try:
        return render_to_response('note.html', {'note': Note.objects.get(id=note_id)})
    except ObjectDoesNotExist:
        raise Http404


def new(request):
    args = {}
    form = NoteForm
    args.update(csrf(request))
    args['form'] = form
    if (request.method == 'GET'):
        return render_to_response('new.html',args)
    else:
        if (request.POST):
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.date = datetime.now()
                note.save()
                return redirect('/note/all')
        return render_to_response('new.html',args)


def delete(request, note_id):
    if (request.POST and  request.is_ajax()):
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return HttpResponse()
        except ObjectDoesNotExist:
            raise Http404


def filter_category(request):
    if (request.is_ajax() and request.POST):
        notes = Note.objects.filter(category=request.POST.get('category'))
        list= []
        for note in notes:
           list.append(note.to_string())
        data = json.dumps(list)
        return HttpResponse({'notes': notes})
    else:
        raise Http404


def favorite(request, note_id):
     if (request.is_ajax() and request.method == 'POST'):
         note =Note.objects.get(id=note_id)
         note.isFavorite = not note.isFavorite
         note.save()
         return HttpResponse(note.isFavorite)
     else:
         raise Http404
