# Gestion d'Inventaire

Ce programme permet de gérer facilement des fichiers CSV contenant des informations sur des stocks. Il offre plusieurs fonctionnalités pour fusionner les fichiers, rechercher des informations, et générer un rapport récapitulatif.

## Fonctionnalités

### Fusion des fichiers CSV :

- Regroupe plusieurs fichiers CSV en une base de données centralisée.
- Par exemple, agréger des fichiers provenant de différentes divisions ou sections.

### Génération de rapport :

- Regroupe les données par catégorie.
- Calcule la somme des quantités.
- Calcule la valeur total. 
- Sauvegarde le rapport dans un fichier CSV.  

## Installation

1. Prérequis :

- Python 3.x installé.
- La librairie pandas (si non installée, utilisez la commande suivante) :
```pip install pandas```

2. Cloner le dépôt GitHub :

- Téléchargez ou clonez ce projet depuis GitHub :
```git clone <URL_DU_DEPOT>```
```cd scriptPerso```

## Utilisation
### Commandes principales

Lancement de l'interface : python main.py

## Exemple d'utilisation
### Fichiers CSV initiaux
- inventory.csv :
```text 
product_name,category,price,quantity
Smartphone,Electronics,299.99,50
Laptop,Electronics,899.99,30
Headphones,Electronics,79.99,100
Keyboard,Accessories,49.99,150
Mouse,Accessories,29.99,200
Desk Lamp,Furniture,39.99,80
Office Chair,Furniture,129.99,45
Wrench,Tools,19.99,70
Hammer,Tools,15.99,60
Drill,Tools,149.99,25
```
- inventory2.csv :
```text 
product_name,category,price,quantity
Tablet,Electronics,399.99,40
Smartwatch,Electronics,199.99,60
Bluetooth Speaker,Electronics,129.99,90
Gaming Headset,Accessories,99.99,120
Laptop Stand,Accessories,34.99,180
Floor Lamp,Furniture,79.99,50
Bookshelf,Furniture,149.99,30
Screwdriver Set,Tools,24.99,100
Pliers,Tools,17.99,80
Chainsaw,Tools,249.99,15

```
- empty.csv :
Un fichier csv vide pour tester

- Commande :

- Terminal :
```text 
1. Consolider les fichiers CSV
2. Rechercher un produit
3. Générer un rapport
4. Quitter
```
### Résultat après fusion et génération de rapport
- Contenu de inventory_report.csv :
```text 
category,total_quantity,total_value
Accessories,650.0,31793.5
Electronics,370.0,89696.3
Furniture,205.0,17547.95
Tools,350.0,13796.5
```

## Organisation du projet
- main.py : Point d'entrée du programme
- inventory.py : Contient les fonctions pour fusionner les fichiers CSV et rechercher des informations.
- report.py : Contient la fonction pour générer des rapports.
- tests/ : Dossier contenant les tests unitaires pour valider le programme.

## Tests unitaires
Les tests unitaires sont disponibles dans le dossier tests. Pour les exécuter, utilisez la commande suivante :  
python -m unittest discover -s tests -p "test_*.py"
