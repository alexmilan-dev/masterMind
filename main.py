import random
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

        self.solucio = self.creaSolucio()

        self.torn = 0

        self.jugades = 0

    def creaSolucio(self):
        sol = []
        for i in range(self.numColors):
            sol.append(random.choice(self.colors))
        return sol

    def getSolucio(self):
        return self.solucio

    def getMaxJugades(self):
        return self.maxJugades

    def getJugades(self):
        return self.jugades

    def juegoAcabado(self):
        if self.jugades >= self.maxJugades:
            return True
        else:
            return False

    def jugaTorn(self, jugada):
        if self.maxJugades == self.jugades:
            return {"error":1,"errMsg":"Nombre màxim de jugades superat"}

        if len(jugada) != self.numColors:
            return {"error":1,"errMsg":"La jugada no té el nombre de colors del joc"}

        for j in jugada:
            if j in self.colors:
                None
            else:
                return {"error":1,"errMsg":"Algun/s colors de jugada no coincideixen amb els colors del joc"}


        resposta = validaExactos(self.solucio, jugada)

        ## contiene los índices exactos de la entrada
        usados = resposta["usados"]

        ## contiene sólo las letras de la solución que no han sido exactas
        sol_sal = resposta["sol_sal"]

        ## contiene la respues que se le va a dar al usuario, sólo con las coincidentes
        res = resposta["res"]

        x=0
        for j in jugada:
            if x in usados:
                None
            else:
                if j in sol_sal:
                    index = sol_sal.index(j)
                    sol_sal[index] = ''
                    usados.append(x)
                    res.append('&')
            x += 1

        self.jugades += 1
        return {"error":0, "res":res}

def validaExactos(solucion, jugada):
    x=0
    sol_sal = solucion.copy()
    res=[]
    usados=[]
    for j in jugada:
        if sol_sal[x] == j:
            res.append('@')
            usados.append(x)
            sol_sal[x] = ''
        x+=1
    return {"usados":usados, "res":res, "sol_sal":sol_sal}



g = Game(7,['V','R','A','M','N','L'])
print(g.getSolucio())
print(g.getMaxJugades())
print(g.getJugades())

while(not g.juegoAcabado()):
    res = g.jugaTorn(['A','R','A','R','A','R'])
    if res["error"] == 0:
        print(g.getJugades())
        print("resultado:",res["res"])
    else:
        print(res["errMsg"])
        exit(1)


"""
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
