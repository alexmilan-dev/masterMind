import os # Para el clear de la consola y agarrar el nombre del usuario real 
import time # Para darle un toque mas dramatico poniendo esperas cortas
import random # Para generar valores aleatorios

opciones = ["s", "si", "sí", "y", "yes", "ja", "oui", "", "n", "no"] # Para las preguntas que requieren si o no

class colors: # Definim els colors 
    vermell = '\033[91m'
    blau = '\033[94m'
    verd = '\033[92m'
    groc = '\033[93m'
    rosa = '\033[95m'
    blanc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'
    invisible = '\33[8m'
    error = '\33[41m'
    alerta = '\33[103m'
    bgvermell = '\33[41m'
    bgblau = '\33[44m'
    bgverd = '\33[42m'
    bggroc = '\33[43m'
    bgrosa = '\33[45m'
    bgblanc = '\33[47m'
    a6 = f"\33[41m"
    a2 = f"\33[44m"
    a5 = f"\33[42m"
    a3 = f"\33[43m"
    a4 = f"\33[45m"
    a1 = f"\33[47m"

class piezas: # Creem peces per mostrar al tauler
    tvermell = f"{colors.vermell}███{colors.reset}"
    tblau = f"{colors.blau}███{colors.reset}"
    tverd = f"{colors.verd}███{colors.reset}"
    tgroc = f"{colors.groc}███{colors.reset}"
    trosa = f"{colors.rosa}███{colors.reset}"
    tblanc = f"{colors.blanc}███{colors.reset}"
    vermell = f"{colors.vermell} ██████ {colors.reset}"
    blau = f"{colors.blau} ██████ {colors.reset}"
    verd = f"{colors.verd} ██████ {colors.reset}"
    groc = f"{colors.groc} ██████ {colors.reset}"
    rosa = f"{colors.rosa} ██████ {colors.reset}"
    blanc = f"{colors.blanc} ██████ {colors.reset}"

    a6 = f"{colors.vermell} ██████ {colors.reset}"
    a2 = f"{colors.blau} ██████ {colors.reset}"
    a5 = f"{colors.verd} ██████ {colors.reset}"
    a3 = f"{colors.groc} ██████ {colors.reset}"
    a4 = f"{colors.rosa} ██████ {colors.reset}"
    a1 = f"{colors.blanc} ██████ {colors.reset}"

    nada = "        "
    nadac = "         "
    nada3 = "   "
    okficha = "@"
    okcolor = "&"

lat = "t" # Para seleccionar tvermell en vez de vermell pq es una fitxa més petita

class linea: # Inicialitzem la base per a cada linea del tauler
    comprobar = piezas.nadac
    color1 = piezas.nada # Totes les fitxes estaràn buides per a que no es vegi res en iniciar la taula
    color2 = piezas.nada
    color3 = piezas.nada
    color4 = piezas.nada



def printTaula(dif, llista):
    esborrarPantalla() # Esborrem primer la pantalla per a que tot es vegi més net
    print(f"{colors.reset}╔══════════════════════════════════════════════════════╗")
    print(f"║ {colors.underline}{colors.bold}LLEGENDA{colors.reset}                                             ║")
    print(f"║                                                      ║")
    print(f"║   {colors.bold}@{colors.reset} - Color correcte                                 ║")
    print(f"║   {colors.bold}&{colors.reset} - Color correcte, posició incorrecta             ║")
    print(f"║                                                      ║")
    print(f"║                                                      ║")
    print(f"║  {piezas.tblanc} - 1 / Blanc  {piezas.tblau} - 2 / Blau  {piezas.tgroc} - 3 / Groc     ║")
    print(f"║                                                      ║")
    print(f"║  {piezas.trosa} - 4 / Rosa   {piezas.tverd} - 5 / Verd  {piezas.tvermell} - 6 / Vermell  ║")
    print(f"║                                                      ║")
    print(f"╚══════════════════════════════════════════════════════╝")
    # I imprimim els taulers més grans o petits depenent de la dificultat de la partida
    if(dif == "facil"):
        print(f"╔════╦═══════════╦═════════╦════════╦════════╦═════════╗")
        print(f"║ {colors.bold}1{colors.reset}  ║ {llista[0]['comprobar']} ║ {llista[0]['color1']}║{llista[0]['color2']}║{llista[0]['color3']}║{llista[0]['color4']} ║")
        print(f"║ {colors.bold}2{colors.reset}  ║ {llista[1]['comprobar']} ║ {llista[1]['color1']}║{llista[1]['color2']}║{llista[1]['color3']}║{llista[1]['color4']} ║")
        print(f"║ {colors.bold}3{colors.reset}  ║ {llista[2]['comprobar']} ║ {llista[2]['color1']}║{llista[2]['color2']}║{llista[2]['color3']}║{llista[2]['color4']} ║")
        print(f"║ {colors.bold}4{colors.reset}  ║ {llista[3]['comprobar']} ║ {llista[3]['color1']}║{llista[3]['color2']}║{llista[3]['color3']}║{llista[3]['color4']} ║")
        print(f"║ {colors.bold}5{colors.reset}  ║ {llista[4]['comprobar']} ║ {llista[4]['color1']}║{llista[4]['color2']}║{llista[4]['color3']}║{llista[4]['color4']} ║")
        print(f"║ {colors.bold}6{colors.reset}  ║ {llista[5]['comprobar']} ║ {llista[5]['color1']}║{llista[5]['color2']}║{llista[5]['color3']}║{llista[5]['color4']} ║")
        print(f"║ {colors.bold}7{colors.reset}  ║ {llista[6]['comprobar']} ║ {llista[6]['color1']}║{llista[6]['color2']}║{llista[6]['color3']}║{llista[6]['color4']} ║")
        print(f"║ {colors.bold}8{colors.reset}  ║ {llista[7]['comprobar']} ║ {llista[7]['color1']}║{llista[7]['color2']}║{llista[7]['color3']}║{llista[7]['color4']} ║")
        print(f"║ {colors.bold}9{colors.reset}  ║ {llista[8]['comprobar']} ║ {llista[8]['color1']}║{llista[8]['color2']}║{llista[8]['color3']}║{llista[8]['color4']} ║")
        print(f"║ {colors.bold}10{colors.reset} ║ {llista[9]['comprobar']} ║ {llista[9]['color1']}║{llista[9]['color2']}║{llista[9]['color3']}║{llista[9]['color4']} ║")
        print(f"║ {colors.bold}11{colors.reset} ║ {llista[10]['comprobar']} ║ {llista[10]['color1']}║{llista[10]['color2']}║{llista[10]['color3']}║{llista[10]['color4']} ║")
        print(f"║ {colors.bold}12{colors.reset} ║ {llista[11]['comprobar']} ║ {llista[11]['color1']}║{llista[11]['color2']}║{llista[11]['color3']}║{llista[11]['color4']} ║")
        print(f"║ {colors.bold}13{colors.reset} ║ {llista[12]['comprobar']} ║ {llista[12]['color1']}║{llista[12]['color2']}║{llista[12]['color3']}║{llista[12]['color4']} ║")
        print(f"║ {colors.bold}14{colors.reset} ║ {llista[13]['comprobar']} ║ {llista[13]['color1']}║{llista[13]['color2']}║{llista[13]['color3']}║{llista[13]['color4']} ║")
        print(f"║ {colors.bold}15{colors.reset} ║ {llista[14]['comprobar']} ║ {llista[14]['color1']}║{llista[14]['color2']}║{llista[14]['color3']}║{llista[14]['color4']} ║")
        print(f"║ {colors.bold}16{colors.reset} ║ {llista[15]['comprobar']} ║ {llista[15]['color1']}║{llista[15]['color2']}║{llista[15]['color3']}║{llista[15]['color4']} ║")
        print(f"║ {colors.bold}17{colors.reset} ║ {llista[16]['comprobar']} ║ {llista[16]['color1']}║{llista[16]['color2']}║{llista[16]['color3']}║{llista[16]['color4']} ║")
        print(f"║ {colors.bold}18{colors.reset} ║ {llista[17]['comprobar']} ║ {llista[17]['color1']}║{llista[17]['color2']}║{llista[17]['color3']}║{llista[17]['color4']} ║")
        print(f"║ {colors.bold}19{colors.reset} ║ {llista[18]['comprobar']} ║ {llista[18]['color1']}║{llista[18]['color2']}║{llista[18]['color3']}║{llista[18]['color4']} ║")
        print(f"║ {colors.bold}20{colors.reset} ║ {llista[19]['comprobar']} ║ {llista[19]['color1']}║{llista[19]['color2']}║{llista[19]['color3']}║{llista[19]['color4']} ║")
        print(f"╚════╩═══════════╩═════════╩════════╩════════╩═════════╝")
        
        """ Este quedaba muy bien :,(
        print(f"╔════╦═══════════╦═════════╦════════╦════════╦═════════╗")
        print(f"║ {colors.bold}1{colors.reset}  ║ {llista[0]['comprobar']} ║ {llista[0]['color1']}║{llista[0]['color2']}║{llista[0]['color3']}║{llista[0]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}2{colors.reset}  ║ {llista[1]['comprobar']} ║ {llista[1]['color1']}║{llista[1]['color2']}║{llista[1]['color3']}║{llista[1]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}3{colors.reset}  ║ {llista[2]['comprobar']} ║ {llista[2]['color1']}║{llista[2]['color2']}║{llista[2]['color3']}║{llista[2]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}4{colors.reset}  ║ {llista[3]['comprobar']} ║ {llista[3]['color1']}║{llista[3]['color2']}║{llista[3]['color3']}║{llista[3]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}5{colors.reset}  ║ {llista[4]['comprobar']} ║ {llista[4]['color1']}║{llista[4]['color2']}║{llista[4]['color3']}║{llista[4]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}6{colors.reset}  ║ {llista[5]['comprobar']} ║ {llista[5]['color1']}║{llista[5]['color2']}║{llista[5]['color3']}║{llista[5]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}7{colors.reset}  ║ {llista[6]['comprobar']} ║ {llista[6]['color1']}║{llista[6]['color2']}║{llista[6]['color3']}║{llista[6]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}8{colors.reset}  ║ {llista[7]['comprobar']} ║ {llista[7]['color1']}║{llista[7]['color2']}║{llista[7]['color3']}║{llista[7]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}9{colors.reset}  ║ {llista[8]['comprobar']} ║ {llista[8]['color1']}║{llista[8]['color2']}║{llista[8]['color3']}║{llista[8]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}10{colors.reset} ║ {llista[9]['comprobar']} ║ {llista[9]['color1']}║{llista[9]['color2']}║{llista[9]['color3']}║{llista[9]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}11{colors.reset} ║ {llista[10]['comprobar']} ║ {llista[10]['color1']}║{llista[10]['color2']}║{llista[10]['color3']}║{llista[10]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}12{colors.reset} ║ {llista[11]['comprobar']} ║ {llista[11]['color1']}║{llista[11]['color2']}║{llista[11]['color3']}║{llista[11]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}13{colors.reset} ║ {llista[12]['comprobar']} ║ {llista[12]['color1']}║{llista[12]['color2']}║{llista[12]['color3']}║{llista[12]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}14{colors.reset} ║ {llista[13]['comprobar']} ║ {llista[13]['color1']}║{llista[13]['color2']}║{llista[13]['color3']}║{llista[13]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}15{colors.reset} ║ {llista[14]['comprobar']} ║ {llista[14]['color1']}║{llista[14]['color2']}║{llista[14]['color3']}║{llista[14]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}16{colors.reset} ║ {llista[15]['comprobar']} ║ {llista[15]['color1']}║{llista[15]['color2']}║{llista[15]['color3']}║{llista[15]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}17{colors.reset} ║ {llista[16]['comprobar']} ║ {llista[16]['color1']}║{llista[16]['color2']}║{llista[16]['color3']}║{llista[16]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}18{colors.reset} ║ {llista[17]['comprobar']} ║ {llista[17]['color1']}║{llista[17]['color2']}║{llista[17]['color3']}║{llista[17]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}19{colors.reset} ║ {llista[18]['comprobar']} ║ {llista[18]['color1']}║{llista[18]['color2']}║{llista[18]['color3']}║{llista[18]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}20{colors.reset} ║ {llista[19]['comprobar']} ║ {llista[19]['color1']}║{llista[19]['color2']}║{llista[19]['color3']}║{llista[19]['color4']} ║")
        print(f"╚════╩═══════════╩═════════╩════════╩════════╩═════════╝")
        """
    if(dif == "dificil"):
        print(f"╔════╦═══════════╦═════════╦════════╦════════╦═════════╗")
        print(f"║ {colors.bold}1{colors.reset}  ║ {llista[0]['comprobar']} ║ {llista[0]['color1']}║{llista[0]['color2']}║{llista[0]['color3']}║{llista[0]['color4']} ║")
        print(f"║ {colors.bold}2{colors.reset}  ║ {llista[1]['comprobar']} ║ {llista[1]['color1']}║{llista[1]['color2']}║{llista[1]['color3']}║{llista[1]['color4']} ║")
        print(f"║ {colors.bold}3{colors.reset}  ║ {llista[2]['comprobar']} ║ {llista[2]['color1']}║{llista[2]['color2']}║{llista[2]['color3']}║{llista[2]['color4']} ║")
        print(f"║ {colors.bold}4{colors.reset}  ║ {llista[3]['comprobar']} ║ {llista[3]['color1']}║{llista[3]['color2']}║{llista[3]['color3']}║{llista[3]['color4']} ║")
        print(f"║ {colors.bold}5{colors.reset}  ║ {llista[4]['comprobar']} ║ {llista[4]['color1']}║{llista[4]['color2']}║{llista[4]['color3']}║{llista[4]['color4']} ║")
        print(f"║ {colors.bold}6{colors.reset}  ║ {llista[5]['comprobar']} ║ {llista[5]['color1']}║{llista[5]['color2']}║{llista[5]['color3']}║{llista[5]['color4']} ║")
        print(f"║ {colors.bold}7{colors.reset}  ║ {llista[6]['comprobar']} ║ {llista[6]['color1']}║{llista[6]['color2']}║{llista[6]['color3']}║{llista[6]['color4']} ║")
        print(f"║ {colors.bold}8{colors.reset}  ║ {llista[7]['comprobar']} ║ {llista[7]['color1']}║{llista[7]['color2']}║{llista[7]['color3']}║{llista[7]['color4']} ║")
        print(f"║ {colors.bold}9{colors.reset}  ║ {llista[8]['comprobar']} ║ {llista[8]['color1']}║{llista[8]['color2']}║{llista[8]['color3']}║{llista[8]['color4']} ║")
        print(f"║ {colors.bold}10{colors.reset} ║ {llista[9]['comprobar']} ║ {llista[9]['color1']}║{llista[9]['color2']}║{llista[9]['color3']}║{llista[9]['color4']} ║")
        print(f"║ {colors.bold}11{colors.reset} ║ {llista[10]['comprobar']} ║ {llista[10]['color1']}║{llista[10]['color2']}║{llista[10]['color3']}║{llista[10]['color4']} ║")
        print(f"║ {colors.bold}12{colors.reset} ║ {llista[11]['comprobar']} ║ {llista[11]['color1']}║{llista[11]['color2']}║{llista[11]['color3']}║{llista[11]['color4']} ║")
        print(f"╚════╩═══════════╩═════════╩════════╩════════╩═════════╝")
        
        """
        print(f"╔════╦═══════════╦═════════╦════════╦════════╦═════════╗")
        print(f"║ {colors.bold}1{colors.reset}  ║ {llista[0]['comprobar']} ║ {llista[0]['color1']}║{llista[0]['color2']}║{llista[0]['color3']}║{llista[0]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}2{colors.reset}  ║ {llista[1]['comprobar']} ║ {llista[1]['color1']}║{llista[1]['color2']}║{llista[1]['color3']}║{llista[1]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}3{colors.reset}  ║ {llista[2]['comprobar']} ║ {llista[2]['color1']}║{llista[2]['color2']}║{llista[2]['color3']}║{llista[2]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}4{colors.reset}  ║ {llista[3]['comprobar']} ║ {llista[3]['color1']}║{llista[3]['color2']}║{llista[3]['color3']}║{llista[3]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}5{colors.reset}  ║ {llista[4]['comprobar']} ║ {llista[4]['color1']}║{llista[4]['color2']}║{llista[4]['color3']}║{llista[4]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}6{colors.reset}  ║ {llista[5]['comprobar']} ║ {llista[5]['color1']}║{llista[5]['color2']}║{llista[5]['color3']}║{llista[5]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}7{colors.reset}  ║ {llista[6]['comprobar']} ║ {llista[6]['color1']}║{llista[6]['color2']}║{llista[6]['color3']}║{llista[6]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}8{colors.reset}  ║ {llista[7]['comprobar']} ║ {llista[7]['color1']}║{llista[7]['color2']}║{llista[7]['color3']}║{llista[7]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}9{colors.reset}  ║ {llista[8]['comprobar']} ║ {llista[8]['color1']}║{llista[8]['color2']}║{llista[8]['color3']}║{llista[8]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}10{colors.reset} ║ {llista[9]['comprobar']} ║ {llista[9]['color1']}║{llista[9]['color2']}║{llista[9]['color3']}║{llista[9]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}11{colors.reset} ║ {llista[10]['comprobar']} ║ {llista[10]['color1']}║{llista[10]['color2']}║{llista[10]['color3']}║{llista[10]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}12{colors.reset} ║ {llista[11]['comprobar']} ║ {llista[11]['color1']}║{llista[11]['color2']}║{llista[11]['color3']}║{llista[11]['color4']} ║")
        print(f"╚════╩═══════════╩═════════╩════════╩════════╩═════════╝")"""
    if(dif == "extrem"):
        print(f"╔════╦═══════════╦═════════╦════════╦════════╦═════════╗")
        print(f"║ {colors.bold}1{colors.reset}  ║ {llista[0]['comprobar']} ║ {llista[0]['color1']}║{llista[0]['color2']}║{llista[0]['color3']}║{llista[0]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}2{colors.reset}  ║ {llista[1]['comprobar']} ║ {llista[1]['color1']}║{llista[1]['color2']}║{llista[1]['color3']}║{llista[1]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}3{colors.reset}  ║ {llista[2]['comprobar']} ║ {llista[2]['color1']}║{llista[2]['color2']}║{llista[2]['color3']}║{llista[2]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}4{colors.reset}  ║ {llista[3]['comprobar']} ║ {llista[3]['color1']}║{llista[3]['color2']}║{llista[3]['color3']}║{llista[3]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}5{colors.reset}  ║ {llista[4]['comprobar']} ║ {llista[4]['color1']}║{llista[4]['color2']}║{llista[4]['color3']}║{llista[4]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}6{colors.reset}  ║ {llista[5]['comprobar']} ║ {llista[5]['color1']}║{llista[5]['color2']}║{llista[5]['color3']}║{llista[5]['color4']} ║")
        print(f"╠════╬═══════════╬═════════╬════════╬════════╬═════════╣")
        print(f"║ {colors.bold}7{colors.reset}  ║ {llista[6]['comprobar']} ║ {llista[6]['color1']}║{llista[6]['color2']}║{llista[6]['color3']}║{llista[6]['color4']} ║")
        print(f"╚════╩═══════════╩═════════╩════════╩════════╩═════════╝")
        """ Y este como si que cabe pues dejo el bonio
        print(f"╔════╦═══════════╦═════════╦════════╦════════╦═════════╗")
        print(f"║ {colors.bold}1{colors.reset}  ║ {llista[0]['comprobar']} ║ {llista[0]['color1']}║{llista[0]['color2']}║{llista[0]['color3']}║{llista[0]['color4']} ║")
        print(f"║ {colors.bold}2{colors.reset}  ║ {llista[1]['comprobar']} ║ {llista[1]['color1']}║{llista[1]['color2']}║{llista[1]['color3']}║{llista[1]['color4']} ║")
        print(f"║ {colors.bold}3{colors.reset}  ║ {llista[2]['comprobar']} ║ {llista[2]['color1']}║{llista[2]['color2']}║{llista[2]['color3']}║{llista[2]['color4']} ║")
        print(f"║ {colors.bold}4{colors.reset}  ║ {llista[3]['comprobar']} ║ {llista[3]['color1']}║{llista[3]['color2']}║{llista[3]['color3']}║{llista[3]['color4']} ║")
        print(f"║ {colors.bold}5{colors.reset}  ║ {llista[4]['comprobar']} ║ {llista[4]['color1']}║{llista[4]['color2']}║{llista[4]['color3']}║{llista[4]['color4']} ║")
        print(f"║ {colors.bold}6{colors.reset}  ║ {llista[5]['comprobar']} ║ {llista[5]['color1']}║{llista[5]['color2']}║{llista[5]['color3']}║{llista[5]['color4']} ║")
        print(f"║ {colors.bold}7{colors.reset}  ║ {llista[6]['comprobar']} ║ {llista[6]['color1']}║{llista[6]['color2']}║{llista[6]['color3']}║{llista[6]['color4']} ║")
        print(f"╚════╩═══════════╩═════════╩════════╩════════╩═════════╝")"""


def esborrarPantalla(): # Una funció que depenent del sistema operatiu, executa una comanda o una altra depenent del sistema operatiu per a borrar 
    if os.name == "posix":
      os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
      os.system("cls")


def nombresAColors(num): # Creem una funció que pasa els numeros a colors
  if(num == "1"):
    num = "blanc"
  elif(num == "2"):
   num = "blau"
  elif(num == "3"):
    num = "groc"
  elif(num == "4"):
    num = "rosa"
  elif(num == "5"):
    num = "verd"
  elif(num == "6"):
    num = "vermell"
  return num
  

def comprovar(resultat, intent): # Aqui comprovem les fitxes introduides
    arrobas = 0
    yrara = 0

    codiRestant = []
    codiProvat = []
    arrayResultats = []

    for i in range(len(intent)): # Primer comprovem els valors que estàn ben colocats
      if resultat[i] != intent[i]:
        codiProvat.append(intent[i])
      else:
         arrobas += 1

    for i in range(len(resultat)): # I aqui els que no
      if intent[i] != resultat[i]:
        codiRestant.append(resultat[i])

    for color in set(codiProvat): # set() elimina els valors repetits de l'array. Aqui busquem els valors que estan en llocs incorrectes
        contadorCodiRestant = codiRestant.count(color)
        contadorCodiProvat = codiProvat.count(color)
        if contadorCodiRestant > 0:
            yrara += min(contadorCodiRestant, contadorCodiProvat)
            for i in range(min(contadorCodiRestant, contadorCodiProvat)):
                codiRestant.remove(color)

    for i in range(arrobas): # I afegim els valors als resultats
      arrayResultats.append("@")
    for i in range(yrara):
      arrayResultats.append("&")

    return arrayResultats


# me paso las pep8 por los huevos
def fiPartida(hasGuanyat: bool, moviments, resultat): # I aqui quan acabi la partida mostrem si has guanyat o perdut
  if hasGuanyat:
    print(f"{colors.reset}╔══════════════════════════════════════════════════════╗")
    print(f"{colors.reset}║{colors.bold}{colors.verd}    __     _____ ____ _____ ___  ____  ___    _       {colors.reset}║")
    print(f"{colors.reset}║{colors.bold}{colors.verd}    \ \   / /_ _/ ___|_   _/ _ \|  _ \|_ _|  / \      {colors.reset}║")
    print(f"{colors.reset}║{colors.bold}{colors.verd}     \ \ / / | | |     | || | | | |_) || |  / _ \\     {colors.reset}║")
    print(f"{colors.reset}║{colors.bold}{colors.verd}      \ V /  | | |___  | || |_| |  _ < | | / ___ \    {colors.reset}║")
    print(f"{colors.reset}║{colors.bold}{colors.verd}       \_/  |___\____| |_| \___/|_| \_\___/_/   \_\\   {colors.reset}║")
    print(f"{colors.reset}║                                                      ║")
    print(f"{colors.reset}╠══════════════════════════════════════════════════════╣")
    print(f"{colors.reset}║{colors.verd} FELICITATS!! {colors.reset}{colors.bold}Has guanyat amb {colors.underline}{moviments}{colors.reset}{colors.bold} {'moviment. ' if moviments == 1 else 'moviments.'}{colors.reset}          {'  ' if moviments < 10 else ' '}║")
    print(f"{colors.reset}╚══════════════════════════════════════════════════════╝")
  else:
    print(f"{colors.reset}╔══════════════════════════════════════════════════════╗")
    print(f"{colors.reset}║{colors.bold}{colors.vermell}       ____  _____ ____  ____   ___ _____  _    {colors.reset}      ║")
    print(f"{colors.reset}║{colors.bold}{colors.vermell}      |  _ \| ____|  _ \|  _ \ / _ \_   _|/ \   {colors.reset}      ║")
    print(f"{colors.reset}║{colors.bold}{colors.vermell}      | | | |  _| | |_) | |_) | | | || | / _ \  {colors.reset}      ║")
    print(f"{colors.reset}║{colors.bold}{colors.vermell}      | |_| | |___|  _ <|  _ <| |_| || |/ ___ \ {colors.reset}      ║")
    print(f"{colors.reset}║{colors.bold}{colors.vermell}      |____/|_____|_| \_\_| \_\\\\___/ |_/_/   \_\\{colors.reset}      ║")
    print(f"{colors.reset}║                                                      ║")
    print(f"{colors.reset}╠══════════════════════════════════════════════════════╣")
    print(f"{colors.reset}║{colors.vermell} Has perdut... {colors.reset}{colors.bold}No et servía amb {colors.underline}{moviments}{colors.reset}{colors.bold} moviments?{colors.reset}        {'  ' if moviments < 9 else ' '}║")
    print(f"{colors.reset}║ La combinació correcta era {colors.underline}{getattr(piezas, lat + resultat[0])} {getattr(piezas, lat + resultat[1])} {getattr(piezas, lat + resultat[2])} {getattr(piezas, lat + resultat[3])}{colors.reset}           ║")
    print(f"{colors.reset}╚══════════════════════════════════════════════════════╝")


def jugar(): # Fem una funció que sigui el joc en si

  # I creem un valor per cada linea del tauler
  llista = [{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  },{
    "comprobar": piezas.nadac,
    "color1": piezas.nada,
    "color2": piezas.nada,
    "color3": piezas.nada,
    "color4": piezas.nada
  }]

  resultat = ["nada3", "nada3", "nada3", "nada3"]
  
  esborrarPantalla()

  # Iniciem el joc
  print(f"{colors.reset}{colors.bold}╔══════════════════════════════════════════════════════╗")
  print(f"{colors.bold}║{colors.groc}  __  __           _            __  __ _           _  {colors.reset}║")
  print(f"{colors.bold}║{colors.groc} |  \/  | __ _ ___| |_ ___ _ __|  \/  (_)_ __   __| | {colors.reset}║")
  print(f"{colors.bold}║{colors.vermell} | |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` | {colors.reset}║")
  print(f"{colors.bold}║{colors.verd} | |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| | {colors.reset}║")
  print(f"{colors.bold}║{colors.blau} |_|  |_|\__,_|___/\__\___|_|  |_|  |_|_|_| |_|\__,_| {colors.reset}║")
  print(f"{colors.bold}║                                ╔═════════════════════╣")
  print(f"{colors.bold}║                                ║{colors.rosa}  -  Per {colors.underline}Marc Jaen{colors.reset}   ║")
  print(f"{colors.bold}╚════════════════════════════════╩═════════════════════╝{colors.reset}\n")

  # Demanem el nom d'usuari
  nom = input(f"Introdueix el teu nom de jugador: ")

  if(nom in ["", " ", "  ", "   "]): # Si no tenim nom introduit ho treiem del seu usuari 
    nom = os.popen("whoami").read().split('\n')[0]

  generacioAutomatica = input(f"\nVols que el programa et generi una combinació de colors? ({colors.verd}{colors.bold}Y{colors.reset}/{colors.vermell}n{colors.reset}): ")
  jugadordefecto = generacioAutomatica # jugador pero con mayusculas para que se vea igual en el while
  generacioAutomatica = generacioAutomatica.lower()
  while not generacioAutomatica in opciones:
      generacioAutomatica = input(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{jugadordefecto}{colors.reset} no és una resposta acceptada. Vols que el programa et generi una combinació de colors? ({colors.verd}{colors.bold}Y{colors.reset}/{colors.vermell}n{colors.reset}): ")
      jugadordefecto = generacioAutomatica
      generacioAutomatica = generacioAutomatica.lower()

  colorArray = ["blanc", "blau", "groc", "rosa", "verd", "vermell", "1", "2", "3", "4", "5", "6"]

  if(generacioAutomatica in ["s", "si", "sí", "y", "yes", "ja", "oui", ""]):
    resultat[0] = colorArray[random.randint(0, 5)]
    resultat[1] = colorArray[random.randint(0, 5)]
    resultat[2] = colorArray[random.randint(0, 5)]
    resultat[3] = colorArray[random.randint(0, 5)]
    mostrarResultat = input(f"\nVols que el programa et mostri la combinació de colors finals? ({colors.vermell}{colors.bold}N{colors.reset}/{colors.verd}y{colors.reset}): ")
    while mostrarResultat not in opciones:
      input(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{mostrarResultat}{colors.reset} no és una resposta acceptada. Vols que el programa et mostri la combinació de colors finals? ({colors.vermell}{colors.bold}N{colors.reset}/{colors.verd}y{colors.reset}): ")
    if mostrarResultat in ["s", "si", "sí", "y", "yes", "ja", "oui"]:
      print(f"La combinació generada és {getattr(piezas, lat + resultat[0])} {getattr(piezas, lat + resultat[1])} {getattr(piezas, lat + resultat[2])} {getattr(piezas, lat + resultat[3])}.") # getattr apaño para buscar atributos con la string
  else:
      random1 = colorArray[random.randint(0, 5)]
      random2 = colorArray[random.randint(0, 5)]
      random3 = colorArray[random.randint(0, 5)]
      random4 = colorArray[random.randint(0, 5)]
      resultat0 = input(f"Introdueix una sequencia dels següents nombres:\n1- {colors.blanc}Blanc{colors.reset}  2- {colors.blau}Blau{colors.reset}  3- {colors.groc}Groc{colors.reset}\n4- {colors.rosa}Rosa{colors.reset}   5- {colors.verd}Verd{colors.reset}  6- {colors.vermell}Vermell{colors.reset}\n"+
                        f"Per exemple {colors.bold}{getattr(colors, 'bg' + random1)}{random1}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random2)}{random2}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random3)}{random3}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random4)}{random4}{colors.reset}\n > ")
      resultat = resultat0.split()

      if(len(resultat) < 4):
        for j in range(4-len(resultat)):
          resultat.append("(no definit)")
      




      for num, i in enumerate(resultat):
        while not i in colorArray:
          i = input(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{i}{colors.reset} no és un valor acceptat.\nIntrodueix algun dels següents colors:\n1- {colors.blanc}Blanc{colors.reset}  2- {colors.blau}Blau{colors.reset}  3- {colors.groc}Groc{colors.reset}\n4- {colors.rosa}Rosa{colors.reset}   5- {colors.verd}Verd{colors.reset}  6- {colors.vermell}Vermell{colors.reset}\n > ")
        resultat[num] = nombresAColors(i)

      print(f"La combinació final és {getattr(piezas, lat + resultat[0])} {getattr(piezas, lat + resultat[1])} {getattr(piezas, lat + resultat[2])} {getattr(piezas, lat + resultat[3])}.") # getattr apaño para buscar atributos con la string
      resp = input(f"\nVols canviar els colors? ({colors.vermell}{colors.bold}N{colors.reset}/{colors.verd}y{colors.reset}) ")
      resp = resp.lower()

      while not resp in opciones:
          resp = input(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{resp}{colors.reset} no és una resposta acceptada.\nVols canviar els colors? ({colors.vermell}{colors.bold}N{colors.reset}/{colors.verd}y{colors.reset}) ")
          resp = resp.lower()
  

  difiArray = ["facil", "fàcil", "easy", "dificil", "difícil", "hard", "extrem", "extreme", "1", "2", "3", ""]
  dificultat = None

  print("\nDepenent de la dificultad que seleccionis, tindrás més o menys moviments disponibles.\n")
  print(f"\n1 - Fàcil, 20 moviments.\n2 - Difícil, 12 moviments.\n{colors.bold}{colors.underline}3 - Extrem, 7 moviments. {colors.underline}{colors.verd}(per defecte){colors.reset}")
  dificultat = input(f"\nSelecciona la dificultat: ").lower()

  while not dificultat in difiArray:
      print(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{resp}{colors.reset} no és una resposta acceptada.\nSelecciona alguna dificultat de les mostrades a continuació:")
      print(f"\n1 - Fàcil, 20 moviments.\n2 - Difícil, 12 moviments.\n{colors.bold}{colors.underline}3 - Extrem, 7 moviments.{colors.reset}{colors.underline} (per defecte)")
      dificultat = input(" > ")
      dificultat = dificultat.lower()

  if(dificultat in ["facil", "fàcil", "easy", "1"]):
      dificultat = "facil"
  elif(dificultat in ["dificil", "difícil", "hard", "2"]):
      dificultat = "dificil"
  elif(dificultat in ["extrem", "extreme", "3", ""]):
      dificultat = "extrem"

  torns = 0
  difiText = ""
  if (dificultat == "facil"):
      torns = 20
      difiText = "fàcil"
  elif (dificultat == "dificil"):
      torns = 12
      difiText = "difícil"
  elif (dificultat == "extrem"):
      torns = 7
      difiText = "extrema"


  print(f"\n{colors.bold}Benvingu(t/da), {colors.underline}{nom}{colors.reset}{colors.bold}, a una partida {difiText} de Mastermind. La partida comença en:")
  print("   3...")
  time.sleep(1)
  print("   2...")
  time.sleep(1)
  print("   1...")
  time.sleep(2)

  moviments = 0
  # Per cada torn fará lo de dins del for
  for i in range(torns):

    printTaula(dificultat, llista)

    random1 = colorArray[random.randint(0, 5)]
    random2 = colorArray[random.randint(0, 5)]
    random3 = colorArray[random.randint(0, 5)]
    random4 = colorArray[random.randint(0, 5)]
    randomc1 = str(random.randint(0, 5)+1)
    randomc2 = str(random.randint(0, 5)+1)
    randomc3 = str(random.randint(0, 5)+1)
    randomc4 = str(random.randint(0, 5)+1)
    introduit = input(f"Introdueix una sequencia de nombres, com, per exemple:\n - {colors.bold}{getattr(colors, 'bg' + random1)}{random1}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random2)}{random2}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random3)}{random3}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random4)}{random4}{colors.reset} o {colors.bold}{getattr(colors, 'a' + randomc1)}{randomc1}{colors.reset} {colors.bold}{getattr(colors, 'a' + randomc2)}{randomc2}{colors.reset} {colors.bold}{getattr(colors, 'a' + randomc3)}{randomc3}{colors.reset} {colors.bold}{getattr(colors, 'a' + randomc4)}{randomc4}{colors.reset}\n  > ")
    vintroduit = introduit.split()
    senseintroduir = vintroduit.copy()

    if(len(vintroduit) < 4):
      for j in range(4-len(vintroduit)):
        vintroduit.append("(no definit)")

    if len(vintroduit)-len(senseintroduir) == 1:
       avis = f"\nA més, t'has deixat {len(vintroduit)-len(senseintroduir)} valor sense introduir."
    elif len(vintroduit)-len(senseintroduir) == 0:
       avis = ""
    else:
       avis = f"\nA més, t'has deixat {len(vintroduit)-len(senseintroduir)} valors sense introduir."
    
    contadorparaloscoloresdelvalorincorrecto = 0
    for num, color in enumerate(vintroduit):
      if not color in colorArray and contadorparaloscoloresdelvalorincorrecto == 0:
        print(f"{colors.alerta}ALERTA!{colors.reset} Has introduit un o més valors incorrectes, així que haurás d'introduir-los correctament un a un.{avis}")
        contadorparaloscoloresdelvalorincorrecto = 1
        

    for num, color in enumerate(vintroduit):
      while not color in colorArray:
        color = input(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{color}{colors.reset} no és un valor acceptat.\nIntrodueix algun dels següents colors:\n1- {colors.blanc}Blanc{colors.reset}  2- {colors.blau}Blau{colors.reset}  3- {colors.groc}Groc{colors.reset}\n4- {colors.rosa}Rosa{colors.reset}   5- {colors.verd}Verd{colors.reset}  6- {colors.vermell}Vermell{colors.reset}\n > ")
      vintroduit[num] = nombresAColors(color)

    print(f"S'afegirà una línea amb els colors {getattr(piezas, vintroduit[0])} {getattr(piezas, vintroduit[1])} {getattr(piezas, vintroduit[2])} {getattr(piezas, vintroduit[3])}.\nD'acord? ({colors.verd}{colors.bold}Y{colors.reset}/{colors.vermell}n{colors.reset})") # getattr apaño para buscar atributos con la string
    confirmarAfegir = input(" > ")

    canvi2 = 0
    while canvi2 == 0:
      if(confirmarAfegir in ["s", "si", "sí", "y", "yes", "ja", "oui", ""]):
        canvi2 = 1
      else:
        introduit = input(f"Introdueix una sequencia de nombres, com, per exemple:\n - {colors.bold}{getattr(colors, 'bg' + random1)}{random1}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random2)}{random2}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random3)}{random3}{colors.reset} {colors.bold}{getattr(colors, 'bg' + random4)}{random4}{colors.reset}\n"+
    f" - o {colors.bold}{getattr(colors, 'a' + randomc1)}{randomc1}{colors.reset} {colors.bold}{getattr(colors, 'a' + randomc2)}{randomc2}{colors.reset} {colors.bold}{getattr(colors, 'a' + randomc3)}{randomc3}{colors.reset} {colors.bold}{getattr(colors, 'a' + randomc4)}{randomc4}{colors.reset}\n  > ")
        vintroduit = introduit.split()
        
        if(len(vintroduit) < 4):
          for j in range(4-len(vintroduit)):
            vintroduit.append("(no definit)")


        for num, color in enumerate(vintroduit):
          while (not color in colorArray):
            color = input(f"{colors.error}ERROR!{colors.reset} {colors.underline}{colors.bold}{color}{colors.reset} no és un valor acceptat.\nIntrodueix algun dels següents colors:\n1- {colors.blanc}Blanc{colors.reset}  2- {colors.blau}Blau{colors.reset}  3- {colors.groc}Groc{colors.reset}\n4- {colors.rosa}Rosa{colors.reset}   5- {colors.verd}Verd{colors.reset}  6- {colors.vermell}Vermell{colors.reset}\n > ")
          vintroduit[num] = nombresAColors(color)
        print(f"S'afegirà una línea amb els colors {getattr(piezas, vintroduit[0])} {getattr(piezas, vintroduit[1])} {getattr(piezas, vintroduit[2])} {getattr(piezas, vintroduit[3])}.\nD'acord? ({colors.verd}{colors.bold}Y{colors.reset}/{colors.vermell}n{colors.reset})") # getattr apaño para buscar atributos con la string
        
        confirmarAfegir = input(" > ")

    llista[i]["color1"] = getattr(piezas, vintroduit[0])
    llista[i]["color2"] = getattr(piezas, vintroduit[1])
    llista[i]["color3"] = getattr(piezas, vintroduit[2])
    llista[i]["color4"] = getattr(piezas, vintroduit[3])

    valorsArray = []

    valorsArray = comprovar(resultat, vintroduit)

    for arroba in valorsArray:
      if arroba != '':
        None
      else:
        arroba
    
    for j in range(4-len(valorsArray)):
      valorsArray.append(f"{colors.invisible}@{colors.reset}")

    valors = " ".join(valorsArray)
    llista[i]["comprobar"] = colors.bold + " " + valors + " " + colors.reset
    moviments += 1

    if(resultat[0] == vintroduit[0] and resultat[1] == vintroduit[1] and resultat[2] == vintroduit[2] and resultat[3] == vintroduit[3]):
      printTaula(dificultat, llista)
      fiPartida(True, moviments, resultat)
      break
    if(torns == moviments):
      printTaula(dificultat, llista)
      fiPartida(False, moviments, resultat)


  restart = input(f"Vols jugar una altra partida? ({colors.vermell}{colors.bold}N{colors.reset}/{colors.verd}y{colors.reset})\n > ")
  while not restart in opciones:
    restart = input(f"{colors.bold}{colors.underline}{str(restart)}{colors.reset} no es una repsosta correcta. Respon amb ({colors.vermell}{colors.bold}N{colors.reset}/{colors.verd}y{colors.reset})\n > ")

  if restart.lower() in ["", "n", "no"]:
    quit()
  else:
    jugar()
  jugar()
jugar()
