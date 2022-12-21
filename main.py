class Game:
    def __init__(self, maxJugades, colors):

        if isinstance(maxJugades, int):
            if maxJugades > 0:
                self.maxJugades = maxJugades
            else:
                raise TypeError("El màxim de jugades ha de ser superior a 0")
        else:
            raise TypeError("El màxim de jugades ha de ser enter")

        if len(colors) > 0:
            self.colors = colors
            self.numColors = len(colors)
        else:
            raise TypeError("Nombre de colors ha de ser 6")


def validaColor(color, index, solucion, resposta):
    if color in solucion and solucion.count(color) > resposta.count(color):
        resposta.append(color)
    res = {"resposta": resposta}
    return res

def validaExactos(solucion, jugada):
    x=0
    sol_sal = solucion
    resp=[]
    for j in jugada:
        if sol_sal.index(j) == x:
            resposta.append('@')
            sol_sal[x] = ''
            resp.append(j)
        x+=1
    return {"sol_sal":sol_sal, "resp":resp}



g = Game(-1)
print(g)

"""
solucion = ['A','B','C','D']
jugada= ['C','B','A','D']
resposta = []
sol = validaExactos(solucion,jugada)
print(sol["sol_sal"])
print(sol["resp"])
sol = sol["sol_sal"]
x=0
for j in jugada:
    res=validaColor(j,x,sol,resposta)
    #sol = res["sol"]
    resposta = res ["resposta"]
    x+=1
"""
