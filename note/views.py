from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from note.models import Note
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from note.forms import NoteForm
from django.core.context_processors import csrf
from datetime import datetime

# Create your views here.


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
    if (request.method == 'GET'):
        form = NoteForm
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('new.html',args)
    else:
        if (request.POST):
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.date = datetime.now()
                note.save()
    return redirect('/note/all')


def delete(request, note_id):
    if (request.POST):
        try:
            note = Note.objects.get(id = note_id)
            note.delete()
            return redirect('/note/all')
        except ObjectDoesNotExist:
            raise Http404




