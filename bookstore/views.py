from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git


@csrf_exempt
def update(request):
    if request.method == "POST":
        # Use o caminho correto do diretório onde o repositório Git está localizado
        repo = git.Repo('/mnt/c/Users/Glaucco/Documents/EBAC/bookstore')
        origin = repo.remotes.origin

        # Realiza o pull para atualizar o código do repositório remoto
        origin.pull()
        return HttpResponse("Updated code on local environment")
    else:
        return HttpResponse("Couldn't update the code on local environment")


def hello_world(request):
    # Carrega o template hello_world.html
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())


# Nova view para a página inicial
def home(request):
    return HttpResponse("Página inicial da Bookstore!")
