from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, "home.html", {"notes": notes})

def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            Note.objects.create(title=title, content=content)
        return redirect("home")
    return render(request, "add_note.html")

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect("home")
    return render(request, "delete_note.html", {"note": note})
