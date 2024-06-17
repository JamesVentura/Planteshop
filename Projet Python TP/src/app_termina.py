
import os,sys

class Plantes :
    def __init__(self, name: str, Type: str, description: str):
        self.name = name
        self.type = Type
        self.description = description

    #Getters & Setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value 
    
    @name.deleter
    def name(self):
        raise Exception("tu ne peux suprimer le nom d'une plantes !")
    
    @property 
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
    


class Plantes_exterieur (Plantes):

    Plantes_exterieur_instances = 0
    def __init__(self, name: str, Type: str, description: str):
        Plantes.__init__(self, name, Type, description)
        Plantes_exterieur.Plantes_exterieur_instances += 1


class Plantes_interieur (Plantes):
    Plantes_interieur_instances = 0

    def __init__(self, name: str, Type: str, description: str):
        Plantes.__init__(self, name, Type, description)
        Plantes_interieur.Plantes_interieur_instances += 1

class Terminal: 

    def __init__(self):
        pass

    def app_initialize (self):
        pass

        #Clearing Terminal
        os.system('cls')

    def app_launch (self):
        print ("Welcome to the Plantshop")

    def app_menu (self):
        
        print ("Main menu: \n\n1) Display plants info \n2) Quit")

        user_choice = int(input())

        match(user_choice):
            case 1:
                print ("Loading Plante Data")
                self.app_plantes_info()
            case 2:
                self.app_quit()

    def app_plantes_info (self):
        print (f"Nombre de Plantes d'exterieur : {Plantes_exterieur.Plantes_exterieur_instances}")
        print (f"Nombre de Plantes d'interieur : {Plantes_interieur.Plantes_interieur_instances}")


    def app_quit (self):
        sys.exit()

#Main Guard 
def main():

    new_plantes = Plantes("test", "test", "test")


    Monstera = Plantes_interieur("Monstera", "Gras", "Plante vert à feuilles trouées" )
    Ficus = Plantes_interieur("Ficus", "Arbre", "Arbuste à feuilles irisées")
    Gui = Plantes_exterieur("Gui","Abres", "Arbuste touffu")
    Laurier = Plantes_exterieur("Laurier", "Arbre", "Arbre a feuilles odorantes")

    app_instance = Terminal ()
    app_instance.app_initialize ()
    app_instance.app_launch ()
    app_instance.app_menu ()

    print(new_plantes.name)
    new_plantes.name = "un autre nom"
    print(new_plantes.name)

if __name__ == "__main__":
    main()

# DATA 


