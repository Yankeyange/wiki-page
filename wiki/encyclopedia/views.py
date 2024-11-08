from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# pour permettre à l'utilisateur de créer une nouvelle page
def newpage(request):
    # si la méthode est post
    if request.method != 'POST':
    # form va iriter de TopicForm
     form = TopicForm()
    # le sinon au cas où
    else:
        form = TopicForm(data=request.POST)

    # maintenat si le formulaire est valide
    if form.is_valid():
      # si le formulaire est valide on sauvegarde
      form.save()
      # et on retourne à topics
      return redirect('topics')
    context = {'form':form}
    return render(request, 'newpage.html', context)
