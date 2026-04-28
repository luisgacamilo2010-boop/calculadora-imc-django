from django.shortcuts import render

def calcular_imc(request):
    resultado = None
    classificacao = ""
    imc = None
    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        
        try:
            imc = peso / (altura ** 2)
        #resultado = round(imc, 2)
        except ZeroDivisionError:
            return render (request, 'calculadora/index.html', 
                {
                'resultado': f'Erro!!! \U000026A0',
                'classificacao': 'A altura não pode ser zero!!!\nInsira novamente as informações e tente novamente.'
                }
                )
        # resultado_formatado = f"{imc:.2f}".replace('.', ',')
        
        # Lógica de Classificação
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc >= 18.5 and imc < 24.9:
            classificacao = "Peso normal"
        elif imc >= 25.0 and imc < 29.9:
            classificacao = "Sobrepeso"
        elif imc >= 30.0 and imc < 34.9:
            classificacao = "Obesidade Grau I"
        elif imc >= 35.0 and imc < 39.9:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"
    
    return render(request, 'calculadora/index.html', 
	    {
        # 'resultado': resultado_formatado, 
        'resultado': imc, 
        'classificacao': classificacao
	    }
    )

def texto01 (valor = None):
    return render(valor, 'calculadora/pag1.html')

def texto02 (valor = None):
    return render(valor, 'calculadora/pag2.html')

def texto03 (valor = None):
    return render(valor, 'calculadora/pag3.html')

def texto04 (valor = None):
    return render(valor, 'calculadora/pag4.html')