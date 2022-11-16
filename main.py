from crudmysql import MySQL
from env import variables
import json

def reporte(numero_control):
    db = MySQL(variables)
    db.conectar_mysql()
    estudiante = db.consulta_sql('SELECT estudiantes.nombre FROM estudiantes where estudiantes.control = {};'.format(numero_control))
    materias = db.consulta_sql('SELECT kardex.materia, kardex.calificacion FROM kardex WHERE kardex.control = {};'.format(numero_control))
    db.desconectar_mysql()

    arr_materias = []
    for i in range(len(materias)):
        materia, calificacion = materias[i]
        materia = {'materia': materia, 'calificacion': float(calificacion)}
        arr_materias.append(materia)

    return {'estudiante': estudiante[0][0], 'materias': arr_materias}

def promedio(numero_control):
    db = MySQL(variables)
    db.conectar_mysql()
    estudiante = db.consulta_sql('SELECT estudiantes.nombre FROM estudiantes where estudiantes.control = {};'.format(numero_control))
    promedio = db.consulta_sql('SELECT AVG(kardex.calificacion) AS PROMEDIO FROM kardex WHERE kardex.control = {};'.format(numero_control))
    db.desconectar_mysql()
    return {'estudiante': estudiante[0][0], 'promedio': float(promedio[0][0])}

if __name__ == '__main__':
    while True:
        numero_control = input('Numero de control: ')
        print(json.dumps(reporte(numero_control)))
        print("")
        print(json.dumps(promedio(numero_control)))