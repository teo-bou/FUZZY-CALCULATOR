from  ion import get_keys, is_pressed
from kandinsky import *
import time
# Set the screen size
WIDTH = 320
HEIGHT = 240



# Set the box dimensions
            
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
g = green
class Caclul : 
    def __init__() : 
        # Une varaible qui prend le résultat
        # Une variable qui prend ce qu'on ecrit
        # Les deux boutons 
        pass

    def go_up() : 
        # Methode pour faire monter le calcul dans l'UI
        pass
    
    def go_down() :
        # Methode pour faire descendre le calcul dans l'UI
        pass


class Bouton : 
    """
    Cette classe permet d'initialiser ce qui se rapproche le plus d'un bouton (le bouton est toujours rectangulaire ): 
    Il a les propriété suivante : 
    - x : l'ensemble des cellules sur les quelles il s'étend horizontalement
    - y : l'ensemble des cellules sur les quelles il s'étend verticalement
    - color : la couleur du bouton
    - focused_color : la couleur du bouton quand il est focus, pour avoir un retour visuel
    - action : une fonction qui sera appelée lorsqu'on appuie sur le bouton
    - text : le texte qui sera affiché sur le bouton
    - focused : un booleen qui permet de savoir si le bouton est focus ou non
    - cordinates : les coordonnées du bouton sur l'écran (les vraie, pas dans la grille)
    - grid_coordinates : les coordonnées du bouton dans la grille (coin supérieur gauche)
    """
    def __init__(self, text, color, x:list[int], y : list[int], focused = False, action = lambda : None) :
        """
        les x sont les colonnes ou le bouton s'étend dans la grid
        les y sont les lignes ou le bouton s'étend dans la grid
        x et y doivent etre des listes

        """
        self.text = text
        self.color = color
        self.focused_color = (color[0]+40, color[1]+40, color[2]+40)
        self.focused = focused
        self.action = action

        for i in x : 
            if i < 0 or i > grid.width - 1 : 
                raise ValueError("x not inside Grid")
        i = 0
        for i in y : 
            if i < 0 or i > grid.height -1 : 
                raise ValueError("y ({y[i]}) not inside Grid")

        self.x = x
        self.y = y
        
        # SONT SET PAR LA GRID QUAND ILS Y SONT AJOUTES
        self.height = None
        self.width = None
        self.cordinates = None  #   (self.x[0] * grid.cell_w, self.y[0] * grid.cell_h)


        self.grid_coordinates = [self.x[0], self.y[0]]

    def draw(self) : 
        if self.height is None or self.width is None or self.cordinates is None : 
            raise ValueError("height, width, cordinates not set, button {self.text} must not be in grid yet")
        color = self.color if not self.focused else self.focused_color
        left_top = (self.cordinates[0], self.cordinates[1]) 
        fill_rect(left_top[0], left_top[1], self.width, self.height, color)
        draw_string(self.text, left_top[0], left_top[1], (0, 0, 0))
    
    def put_in_grid(self) :
        grid[self.grid_coordinates[1]][self.grid_coordinates[0]] = self
        for i in self.x :
            for j in self.y :
                if i == self.x[0] and j == self.y[0] :
                    continue
                grid[j][i] = None  
    
    def focus(self) : 
        print(f"{self.text} at {self.grid_coordinates} is focused")
        self.focused = True
        self.draw()
    
    def unfocus(self) : 
        self.focused = False
        self.draw()
    
    def __str__(self) -> str:
        return self.text
        

class TextInput(Bouton) :
    def __init__(self, text, color, x:list[int], y : list[int], focused = False, action = lambda : None) :
        action = lambda : self.text_mode()
        action()
        super().__init__(text, color, x, y, focused, action)


    def text_mode(self) : 
        print("TEXT MODE")
        return "TEXT MODE"

    def add_char(self, char) :
        self.text += char
        draw_string(self.text, self.cordinates[0], self.cordinates[1], (0, 0, 0))

    def del_char(self) : 
        self.text = self.text[:-1]
        self.draw()
    
    ## AJOUTER UN COURSEUR ET DES M2THODE POUR TRAVAILLER AVEC DU TEXTE
    

        



#         SHEMA DE LA GRILLE
#                        x
# 
#       ───────────────────────────────────►
# 
#   │   ┌────────┬────────┬────────┬────────┐
#   │   │        │        │        │        │
#   │   │        │        │        │        │
#   │   │        │        │        │        │
#   │   ├────────┼────────┼────────┼────────┤
# y │   │        │        │        │        │
#   │   │        │        │        │        │
#   │   │        │        │        │        │
#   │   ├────────┼────────┼────────┼────────┤
#   │   │        │        │        │        │
#   │   │        │        │        │        │
#   │   │        │        │        │        │
#   │   ├────────┼────────┼────────┼────────┤
#   │   │        │        │        │        │
#   │   │        │        │        │        │
#   ▼   │        │        │        │        │
#       └────────┴────────┴────────┴────────┘


class Grid:
    """
    La grille contient l'ensemble des boutons. Ici, chaque élément est appellé une "cell".
    On accède au contenu de la grille avec la methode get_cell(x, y)
    ATTENTION : pour accéder au contenu des cell avec la propriété __grid, il faudra utiliser :  self.__grid[y][x]
    Les méthode suivantes sont aussi disponibles : 
    - get_focused_cell() : renvoie le contenu de la cellule en cours de selection
    - focus_cell(button : Bouton) : déselectionne la cellule en cours de selection, puis selectionne le bouton qu'on vien de lui passer.
    - __getitem__ permet de récupérer les contenus des cellules avec grid[y][x] ou grid est l'objet grid et non la propriété __grid. Cela permet une interface plus simple
    - __setitem__ permet de modifier les contenus des cellules avec grid[y][x] 
    - travel_x() permet de focus la cellule directement a droite ou a gauche de la cellule en cours de selection
    - travel_y() permet de focus la cellule directement en haut ou en bas de la cellule en cours de selection

    Les paramètre suivants sont disponibles lors de la création de la grille 
    - offset_x : position de la grille sur l'axe x (coin supérieur gauche)
    - offset_y : position de la grille sur l'axe y (coin supérieur gauche)
    - width : largeur de la grille
    - height : hauteur de la grille
    - x_div : nb de divisions sur l'axe x
    - y_div : nb de divisions sur l'axe y

    Les valeurs par défaut sont celles de la grille principale

    """
    def __init__(self, offset_x = 0, offset_y = 0, width = WIDTH, height = HEIGHT, x_div = 4, y_div = 5) :   
        """
        On initialise la grille avec sa hauteur et sa largeur
        """
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.n = x_div # division on x
        self.m = y_div # division on y

        self.width = self.n
        self.height = self.m

        self.cell_w = width//self.n
        self.cell_h = height//self.m
        self.__focused = [0, 0]

        # Contient tout les boutons.
        self.__grid = [[None for j in range(self.width)] for i in range(self.height)]
    
    def get_cell(self, x, y) : 
        """
        retourne la cellule
        """
        if x < 0 or x > self.width - 1 : 
            raise ValueError("x not inside Grid")
        if y < 0 or y > self.height -1 : 
            raise ValueError("y not inside Grid")
        return self.__grid[y][x]

    
    
    def get_focused_cell(self) :
        """
        retourne la cellule focused. Celle ci ne devrait pas etre nulle. 
        """
        cell_content = self.__grid[self.__focused[1]][self.__focused[0]]
        if cell_content is None : 
            print(f"Cell {self.__focused} is empty")
            print(self.__grid)
            return None
        return cell_content
    
    def focus_cell(self, cell : Bouton) :
        if cell is None : 
            raise Exception("Can't focus an empty cell")
        
        button_to_unfocus = self.get_cell(self.__focused[0],self.__focused[1])
        if button_to_unfocus is  None : 
            raise Exception("Can't unfocus an empty cell")
        
        button_to_unfocus.unfocus()
        cell.focus()
        self.__focused = [*cell.grid_coordinates]
    
    def __getitem__(self, index) :
        try : 
            return self.__grid[index]
        except IndexError :
            raise IndexError(f"Index out of range : {index} not in range of {self.__grid}")
        except Exception as e:
            raise e
        
    def __setitem__(self,  index, value) :
        self.__grid[index] = value
    
    def travel_x(self, i) :
        x, y = self.__focused
        if i != 1 and i != -1 : 
            raise ValueError("This function only allows to travel of 1 or -1") 
        if i == 1  :  # GO RIGHT
            for cell in self.__grid[y][x+1:] : 
                if cell is not None :
                    self.focus_cell(cell)
                    return
        elif i == -1 : # Go LEFT
            for cell in self.__grid[y][:x][::-1]: # On part notre cell et on va vers la gauche et focus le premier bouton. 
                if cell is not None : 
                    self.focus_cell(cell)
                    return
            return
    def travel_y(self, i) : 
        """
        On parcour les lignes pour trouver la ligne au dessus ou au dessou qui renvoie 
        """
        x, y = self.__focused
        if i != 1 and i != -1 : 
            raise ValueError("This function only allows to travel of 1 or -1") 
        if i == 1  :  # GO DOWN
            for list in self.__grid[y+1:] : 
                if list[x] is not None :
                    self.focus_cell(list[x])
                    return
            print("EDGE")
            return
        if i == -1 : # Go UP
            for list in self.__grid[:y][::-1] : # On part notre cell et on va vers le haut et focus le premier bouton. 
                if list[x] is not None : 
                    self.focus_cell(list[x])
                    return
            print("EDGE")
            return
    def add_button(self, button : Bouton) :
        print(f"ADD TO GRID {button.text}")
        x, y = button.grid_coordinates
        self.__grid[button.grid_coordinates[1]][button.grid_coordinates[0]] = button
        for i in button.x :
            for j in button.y :
                if i == button.grid_coordinates[0] and j == button.grid_coordinates[1] :
                    continue
                grid[j][i] = None 
        self.__grid[y][x].height = self.cell_h * len(button.y)
        self.__grid[y][x].width = self.cell_w * len(button.x)
        self.__grid[y][x].cordinates = (button.x[0] * self.cell_w + self.offset_x, button.y[0] * self.cell_h + self.offset_y)

    def draw(self) : 
        for i in self.__grid : 
            for j in i : 
                if j is not None : 
                    j.draw()

    def __str__(self) : 
        st = ""
        for y in range(self.m) : 
            for x in range(self.n) : 
                
                st += str(type(self.get_cell(x, y)))
                st += " "
            st += "\n"
        return st


class Interface() : 
    def __init__(self, grid : Grid, menu = Grid) : 
        self.main_grid = grid
        self.menu = menu
        self.text_mode = False
        self.grid_focused = self.main_grid
        self.focused_button : TextInput = self.grid_focused.get_focused_cell()

        self.actions = {   # Actions de navigation
            "up" : lambda :  self.grid_focused.travel_y(-1),
            "down" : lambda : self.grid_focused.travel_y(1),
            "left" : lambda : self.grid_focused.travel_x(-1),
            "right" :lambda : self.grid_focused.travel_x(1),
            "enter" : lambda : self.grid_focused.get_focused_cell().action()
        }

        self.text_mode_actions = {
            "del" : lambda : self.focused_button.del_char() ,
            "lettres" : "/1234567895+-0,; "
        }

        self.ACTION_RATE = 0.15
    def main_loop(self) : 
        
        self.grid_focused.draw()
        while True :
            if is_pressed("/") : 
                # DEBUG ACTIONS
                print(self.grid_focused)
                print(self.focused_button)
            self.scan_actions()                
            if self.text_mode : 
                self.scan_text_mode_actions()
            time.sleep(0.01)    
    
    def scan_actions(self) : 
        for i in self.actions.keys() : 
                if is_pressed(i) : 
                    if self.text_mode : 
                        print("STOP text mode")
                        self.text_mode = False
                    result = self.actions[i]()

                    if result == "TEXT MODE"  :
                        print("Text mode in interface") 
                        self.text_mode = True
                    self.focused_button = self.grid_focused.get_focused_cell()
                    
                    time.sleep(self.ACTION_RATE)
                    continue
    
    def scan_text_mode_actions(self) : 
        if is_pressed("del") : 
            self.text_mode_actions["del"]()
            time.sleep(self.ACTION_RATE)
        else : 
            for j in self.text_mode_actions["lettres"] : 
                if is_pressed(j) : 
                    self.focused_button.add_char(j)
                    time.sleep(self.ACTION_RATE)
                    break
            
        
                
            
            
    
    

#grid = Grid(offset_x=30, offset_y=30, width=WIDTH - 30, height=HEIGHT - 30)
grid = Grid()
# Set the box names
BOX_NAMES = ["NFT", "IFT", "INT", "VAR"]
colors = [red, g, blue, black]
bottom_menue = [
    {"text" : "NFT", "color" : red},
    {"text" : "IFT", "color" : g},
    {"text" : "INT", "color" : blue},
    {"text" : "VAR", "color" : black},
]
BOX_WIDTH = WIDTH // len(bottom_menue)
BOX_HEIGHT = 50


### Bottom bar with buttons
button = Bouton("NFT", red, [0], [grid.m-1])
button2 = Bouton("IFT", g, [1], [grid.m-1])
button3 = Bouton("INT", blue, [2], [grid.m-1])
button4 = Bouton("VAR", black, [3], [grid.m-1])


grid.add_button(button)
grid.add_button(button2)
grid.add_button(button3)
grid.add_button(button4)


for i in range(grid.height - 1) :
    print("row created")
    button_calcul = TextInput("CALC", black, [1, 2, 3], [i])
    bouton_valeur = Bouton("A = ", white,[0], [i], action = lambda : print("test"))
    grid.add_button(button_calcul)
    grid.add_button(bouton_valeur)


interface = Interface(grid, None)
interface.main_loop()