# Installation

- Installer python3.11
- installer les packages python avec la commande suivante : 

```
pip install -r requirements.txt
```
*sur certaines machines, vous devrez peut etre lancer le programme en mode administrateur.*

# A faire 

- AJOUTER UN MENU 
    - création de la possibilité de donner un offset à la grille : done
    - création de la possibilité de travailler avec différentes grilles : en cour
    - possibilité d'ouvrir le menu puis de séléctionner une option qui te fait revenir a la liste principale.

- FAIRE ROULER LA LISTE DE CALCULS  : fait
    - la liste s'étend automatiquement : fait
    - plus que 26 variables serait bien. 
    - petit bug : la couleur reste en focus quand on fait monter la liste
- CREER UN MODE TEXTE AVEC UN ECHAP ( LES ARROW KEYS verticales ) 
    - créer text mode basique : fait
    - créer un curseur pour la navigation

- CREER LA CALCULATRICE
    - Creer les objets flouss (IFT, NTF, Intervalles, etc..0)
    - intégrer les calculs avec l'interface

# Attention

python sur nomworks ne supporte pas les décorateurs comme ```@property```. Merci de ne pas les utiliser ainsi que des package autres que maths, time et ceux dans le requirement.txt. Les autres packages ne sont pas présent sur la numworks a priori. Il faut également que les noms de variables soient en minuscule et sans accent. Les f string ne sont pas supportées. On ne peut pas non plus utiliser *variable_liste pour passer les éléments d'une liste d'un coup.


