import json
from django.shortcuts import render_to_response, redirect
from note.models import Note
from django.http.response import Http404, HttpResponse, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from note.forms import NoteForm
from django.core.context_processors import csrf
from datetime import datetime
from django.contrib import auth
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.


def all(request):
    args = {}
    args.update(csrf(request))
    if (request.user.is_authenticated()):
        args['notes'] = Note.objects.filter(user=request.user)
    else:
        return redirect('/auth/login')
    args['username'] = auth.get_user(request).username
    return render_to_response('all.html', args)


def get(request, note_id):
    if (request.user.is_anonymous() or not Note.objects.filter(user=request.user, id = note_id)):
       return redirect('/auth/login')
    try:
        return render_to_response('note.html', {'note': Note.objects.get(id=note_id), 'username': auth.get_user(request).username})
    except ObjectDoesNotExist:
        raise Http404


def new(request):
    if (not request.user.is_authenticated()):
         return redirect('/auth/login')
    else:
        args = {}
        form = NoteForm
        args.update(csrf(request))
        args['form'] = form
        args['username'] = auth.get_user(request).username
        if (request.method == 'GET'):
            return render_to_response('new.html',args)
        else:
            if (request.POST):
                form = NoteForm(request.POST)
                if form.is_valid():
                    note = form.save(commit=False)
                    note.date = datetime.now()
                    note.user = request.user
                    note.save()
                    return redirect('/note/all')
                else:
                    args['errors'] = form.errors
                return render_to_response('new.html',args)


def delete(request, note_id):
    if (request.POST and  request.is_ajax()):
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return HttpResponse()
        except ObjectDoesNotExist:
            raise Http404


def favorite(request, note_id):
     if (request.is_ajax() and request.method == 'POST'):
         note =Note.objects.get(id=note_id)
         note.isFavorite = not note.isFavorite
         note.save()
         return HttpResponse(note.isFavorite)
     else:
         raise Http404


def edit(request, note_id):
    if (not request.user.is_authenticated()):
         return redirect('/auth/login')
    else:
        args = {}
        form = NoteForm(instance=Note.objects.get(id = note_id))
        args.update(csrf(request))
        args['form'] = form
        args['username'] = auth.get_user(request).username
        if (request.method == 'GET'):
            return render_to_response('edit.html',args)
        else:
            if (request.POST):
                form = NoteForm(request.POST)
                if form.is_valid():
                    note = form.save(commit=False)
                    note.date = datetime.now()
                    note.user = request.user
                    note.save()
                    return redirect('/note/all')
                else:
                    args['errors'] = form.errors
                return render_to_response('edit.html',args)

