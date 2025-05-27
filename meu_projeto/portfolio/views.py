from django.shortcuts import render

def post_view(request):
    # Aqui você pode buscar dados, preparar contexto, etc.
    context = {
        'title': 'Detalhes do Post',
        'content': 'Conteúdo do post vai aqui.',
    }
    return render(request, 'post_detail.html', context)
