from django.shortcuts import render

# Create your views here.
def contar_as_letras(request):
    letras = str(input('Seu texto: \n -> '))
    quantidade = 0 

    for i in letras:
        if i != ' ':
            quantidade += 1

    return render(request, 'contar.letras/index.html', 
            {
            # 'resultado': resultado_formatado, 
            'numero_letras': quantidade,
            }
        )