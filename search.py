import pandas as pd


class Search:
    def __init__(self):
        # Chargement du fichier d'inventaire
        self.inventory = pd.read_csv('consolidated_inventory.csv')

    def run_search(self):
        """Permet de lancer la recherche par produit, catégorie ou prix"""
        print("Recherche par:")
        print("1. Nom du produit")
        print("2. Catégorie")
        print("3. Plage de prix")
        choice = input("Entrez un choix: ")

        results = None

        if choice == '1':
            product_name = input("Entrez le nom du produit à rechercher: ")
            results = self.search_by_product(product_name)
        elif choice == '2':
            category = input("Entrez la catégorie à rechercher: ")
            results = self.search_by_category(category)
        elif choice == '3':
            min_price = float(input("Entrez le prix minimum: "))
            max_price = float(input("Entrez le prix maximum: "))
            results = self.search_by_price(min_price, max_price)
        else:
            print("Choix invalide!")
            return

        if results is not None and not results.empty:
            print("\nRésultats de recherche:")
            print(results)
        else:
            print("Aucun résultat trouvé.")

    def search_by_product(self, name):
        """Recherche par nom de produit"""
        # Message de vérification
        print(f"\nRecherche de produits contenant '{name}'...")
        results = self.inventory[self.inventory['product_name']
                                 .str.contains(name, case=False, na=False)]
        # Affichage du nombre de résultats
        print(f"Nombre de résultats pour '{name}': {len(results)}")
        return results

    def search_by_category(self, category):
        """Recherche par catégorie"""
        # Message de vérification
        print(f"\nRecherche de produits dans la catégorie '{category}'...")
        results = self.inventory[self.inventory['category']
                                 .str.contains(category, case=False, na=False)]
        # Affichage du nombre de résultats
        print(f"Nombre de résultats pour la catégorie '{category}': "
              f"{len(results)}")
        return results

    def search_by_price(self, min_price, max_price):
        """Recherche par plage de prix"""
        # Message de vérification
        print(f"\nRecherche de produits avec un prix entre "
              f"{min_price} et {max_price}...")
        results = self.inventory[(self.inventory['price'] >= min_price) &
                                 (self.inventory['price'] <= max_price)]
        # Affichage du nombre de résultats
        print(
        f"Nombre de résultats pour le prix entre {min_price} et {max_price}: "
        f"{len(results)}")
        return results
