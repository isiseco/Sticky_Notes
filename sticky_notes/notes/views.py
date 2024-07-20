from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Bulletin
from .forms import NoteForm, BulletinForm

def note_list(request):
    """View function for listing all notes."""
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    """View function for displaying a single note."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    """View function for creating a new note."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_edit(request, pk):
    """View function for editing an existing note."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk):
    """View function for deleting a note."""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')

def bulletin_list(request):
    """View function for listing all bulletins."""
    bulletins = Bulletin.objects.all()
    return render(request, 'notes/bulletin_list.html', {'bulletins': bulletins})

def bulletin_detail(request, pk):
    """View function for displaying a single bulletin."""
    bulletin = get_object_or_404(Bulletin, pk=pk)
    return render(request, 'notes/bulletin_detail.html', {'bulletin': bulletin})

def bulletin_create(request):
    """View function for creating a new bulletin."""
    if request.method == "POST":
        form = BulletinForm(request.POST)
        if form.is_valid():
            bulletin = form.save(commit=False)
            bulletin.save()
            return redirect('bulletin_detail', pk=bulletin.pk)
    else:
        form = BulletinForm()
    return render(request, 'notes/bulletin_form.html', {'form': form})

def bulletin_edit(request, pk):
    """View function for editing an existing bulletin."""
    bulletin = get_object_or_404(Bulletin, pk=pk)
    if request.method == "POST":
        form = BulletinForm(request.POST, instance=bulletin)
        if form.is_valid():
            bulletin = form.save(commit=False)
            bulletin.save()
            return redirect('bulletin_detail', pk=bulletin.pk)
    else:
        form = BulletinForm(instance=bulletin)
    return render(request, 'notes/bulletin_form.html', {'form': form})

def bulletin_delete(request, pk):
    """View function for deleting a bulletin."""
    bulletin = get_object_or_404(Bulletin, pk=pk)
    bulletin.delete()
    return redirect('bulletin_list')
