from django.shortcuts import render,redirect
from datetime import date

from app.models import Note

# Create your views here.

def indexpage(request):
    all = Note.objects.all()
    data = {'data':all}
    return render(request,'app/list.html',data)

def notes(request):
    if request.POST:
        today = date.today()
        note = request.POST['notes']
        title = request.POST['title']
        new_note = Note.objects.create(
            notes = note,
            title = title,
            created_at = today   
        )
        return redirect('indexpage')
    else:
        return render(request,'app/notes.html')
    
def edit(request,pk):
    if request.POST:
        note = Note.objects.get(id=pk)
        note.title = request.POST['title']
        note.notes = request.POST['notes']
        note.save()
        url = f"/up_note/{pk}"
        
        return redirect(url)
    else:
        note = Note.objects.get(id=pk)
        request.session['id']=note.id
        return render(request,'app/up_note.html',{'data':note})
