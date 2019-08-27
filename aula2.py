tabela = {
    0: {"digito": 1, 'other': 'qrej', "e": "qrej"},
    1: {"digito": 1, '.': 2, "e": 2},
    2: {"other": "qrej", "digito": 3, "e": 4},
    3: {"digito": 3, "e": 4, "other": "qf1"},
    4: {"other": "qrej", "+": 5, "-": 5},
    5: {"other": "qrej", "digito": 6},
    6: {"digito": 6, "other": "qrej"},
    "qrej": "qrej",
    "qf1": "qf1"
}


def validar(transicoes, string, aceitacao=None, estado_inicial=0):
    estado = estado_inicial
    palavra = []
    sentenca = ""

    for caractere in string:
        try:
            sentenca = int(caractere.lower())
            if isinstance(sentenca, int):
                print("sou um digito")
                estado = transicoes[estado]["digito"]
                palavra.append(sentenca)
        except ValueError:
            print("n sou um digito")
            if caractere == "e":
                print(
                    f"Estou no 'e' estado = {estado} caractere = {caractere}")
                estado = transicoes[estado][caractere]
                if estado is not "qrej":
                    palavra.append(caractere)
            elif caractere is not "e":
                estado = transicoes[estado]["other"]
            elif caractere in ["+", "-"]:
                estado = transicoes[estado][caractere]
                palavra.append(caractere)
            if estado == "qrej" or estado == "qf1":
                estado = 0

    return palavra
