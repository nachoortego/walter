print("Nombre del curso: ")
curso = input()

print("Cantidad de materias (si hay una 2 dias distintos cuenta como 2): ")
cant = int(input())

dicc = {
    'nombre': '',
    'dia': 0,
    'link': '',
    'hora': ''
}

lista = []


def ingresar(i):
    dic = {}
    print(f'Nombre de la materia {i+1}: ')
    dic['nombre'] = input()
    print(f'Dia de {dicc["nombre"]} (lunes 0, martes 1...):')
    dic['dia'] = int(input())
    print(f'Link de {dicc["nombre"]}:')
    dic['link'] = input()
    print('Hora (2min antes de la clase, formato:07:58:00):')
    dic['hora'] = input()
    return dic


for i in range(cant):
    lista.append(ingresar(i))

f = open('clases.py', 'a')
f.write(curso+'='+str(lista))
f.close()
print(lista)
