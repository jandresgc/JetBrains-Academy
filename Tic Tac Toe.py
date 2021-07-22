def imprimir(cells):
    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")


def validar(cells, f, serie):
    var = 3
    for i in range(f, f + var):
        if "".join(cells[f:f + var]) == serie or \
            "".join(cells[f+var:f+(var*2)]) == serie or \
            "".join(cells[f+(var*2):f+(var*3)]) == serie or \
            "".join(cells[::var]) == serie or \
            "".join(cells[1::var]) == serie or \
            "".join(cells[2::var]) == serie or \
            "".join(cells[::var+1]) == serie or \
            "".join(cells[2:8:2]) == serie:
            return True
        else:
            return False

lista = list(" " * 9)
lista2 = [11, 12, 13, 21, 22, 23, 31, 32, 33]
imprimir(lista)

while True:
    try:
        f, c = input("Enter the coordinates:").split()
        fc = int(f.strip() + c.strip())
        pos = lista2.index(fc)
        if pos >= 0:
            if lista[pos] == " ":
                lista[pos] = "X"
                imprimir(lista)
                if validar(lista, 0, "XXX"):
                    print("X Wins")
                    break
                elif validar(lista, 0, "OOO"):
                    print("O Wins")
                    break
                else:
                    print("Draw")
            else:
                print("This cell is occupied! Choose another one!")
    except ValueError:
        print("Error - Input a valid value!")
