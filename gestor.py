class Personaje:
    def __init__(self,nombre:str,vida:int,daño:int,defensa:int,alcanze:int):
        if(type(nombre)!=str):
            raise TypeError('El nombre debe ser un string')
        else:
            self.nombre=nombre
        if(type(vida)!=int):
            raise TypeError('La vida debe ser un entero')
        else:
            self.vida=vida
        if(type(daño)!=int):
            raise TypeError('El daño debe ser un entero')
        else:
            self.daño=daño
        if(type(defensa)!=int):
            raise TypeError('La defensa debe ser un entero')
        else:
            self.defensa=defensa
        if(type(alcanze)!=int):
            raise TypeError('El alcanze debe ser un entero')
        else:
            self.alcanze=alcanze


class Gestor:
    pass

def main_gestor():
    p=Personaje('Juan',100,10,5,0)
    print(p)