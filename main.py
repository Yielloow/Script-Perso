import os
import pandas as pd
import argparse
from inventory_manager import InventoryManager
from search import Search
from report import Report

def create_csv(file_name):
    """Permet à l'utilisateur de créer un fichier CSV."""
    # Liste pour stocker les produits
    products = []

    # Demander à l'utilisateur d'ajouter des produits
    while True:
        product_name = input("Entrez le nom du produit : ")
        category = input("Entrez la catégorie : ")
        price = float(input("Entrez le prix : "))
        quantity = int(input("Entrez la quantité : "))

        # Ajouter le produit à la liste
        products.append({
            "product_name": product_name,
            "category": category,
            "price": price,
            "quantity": quantity
        })

        # Demander si l'utilisateur veut ajouter un autre produit
        another = input("Voulez-vous ajouter un autre produit ? (o/n) : ").lower()
        if another != 'o':
            break

    # Créer un DataFrame et sauvegarder dans un fichier CSV
    df = pd.DataFrame(products)
    df.to_csv(file_name, index=False)
    print(f"Fichier '{file_name}' créé avec succès.")

def menu():
    """Affiche le menu principal."""
    print("1. Consolider les fichiers CSV")
    print("2. Rechercher un produit")
    print("3. Générer un rapport")
    print("4. Quitter")
    choice = input("Choisissez une option: ")
    if choice == '1':
        inventory_manager = InventoryManager()
        inventory_manager.consolidate_files()
    elif choice == '2':
        search = Search()
        search.run_search()
    elif choice == '3':
        report = Report()
        report.generate_report()
    elif choice == '4':
        print("Au revoir!")
        exit()
    else:
        print("Choix invalide, essayez encore.")
        menu()

if __name__ == "__main__":
    # Configurer argparse pour gérer les options en ligne de commande
    parser = argparse.ArgumentParser(description="Gestion des fichiers CSV pour l'inventaire.")
    parser.add_argument("--create", help="Créer un nouveau fichier CSV.", action="store_true")
    parser.add_argument("--menu", help="Afficher le menu principal.", action="store_true")

    # Analyser les arguments
    args = parser.parse_args()

    # Si l'utilisateur veut créer un fichier CSV
    if args.create:
        file_name = input("Entrez le nom du fichier CSV (avec .csv à la fin) : ")
        create_csv(file_name)

    # Si l'utilisateur veut afficher le menu
    if args.menu:
        while True:
            menu()

