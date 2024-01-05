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

- Ne pas utiliser les décorateurs comme ```@property```
- Ne pas utiliser d'autres packages que maths, time et ceux dans le requirement.txt
- Les noms de variables doivent être en minuscule et sans accent
- Les f string ne sont pas supportées
- On ne peut pas utiliser *variable_liste pour passer les éléments d'une liste d'un coup
- Les ```raise error``` ne fonctionnent pas
- Les variables ne doivent pas avoir de majuscule.

Tout cela n'est pas permis par la numworks qui ne supporte pas ces feature de python. 

# Structure de l'interface 
**la class bouton** : il fit dans la grid, il contient des infos sur ou il est dans la grid. De la, c'est la grid qui lui donne sa position sur l'écran, et sa taille pour qu'il puisse etre déssiné


**la class textinput**

**la class grid** : Elle a une hauteur et une largeur. Elle divise l'écran et contient les boutons. Elle contient également l'information de la cellule sur la quelle on est focus. C'est aussi elle qui gère le fait de focuser une de ses cell, et de déplacer le focus vers le haut ou le bas. on y ajoute des boutons via add bouton. 

**la class liste_principale** : elle est une grid spéciale : elle contient des éléments bien définis, en colonne. elle se charge de déplacer les éléments qu'elle contient vers le haut, ou vers le bas quand on arrive en haut ou en bas de la liste. son self.rows contient tout les boutons, meme ceux en dehors de l'écran


**la classe Interface**
C'est elle qui récolte les inputs. Elle controle les deux grid (bientot deux) qui composent l'interface. C'est aussi elle qui gère le text mode et donc l'envoi du caractère au text input


