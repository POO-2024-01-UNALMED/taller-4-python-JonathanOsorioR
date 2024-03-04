from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = [] if asignaturas is None else asignaturas
        self.listadoAlumnos = [] if estudiantes is None else estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno=None, lista=None):

        if lista is not None:
            self.listadoAlumnos.extend(lista)
            
        if alumno is not None:
            self.listadoAlumnos.append(alumno)
          

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
