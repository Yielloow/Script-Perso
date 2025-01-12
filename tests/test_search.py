import unittest
import os
import sys
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from search import Search

# Ajout du répertoire parent pour accéder à search.py


class TestSearch(unittest.TestCase):

    def setUp(self):
        """Configuration des fichiers nécessaires aux tests."""
        # Utilisation du fichier existant inventory.csv
        self.test_file = "inventory.csv"
        # Exemple pour que le test puisse fonctionner
        if not os.path.exists(self.test_file):
            pd.DataFrame({
                "product_name": ["Item1", "Item2", "Item3", "Item4"],
                "quantity": [10, 20, 30, 40],
                "price": [5.0, 15.0, 25.0, 10.0],
                "category": ["Electronics", "Clothing", "Electronics", "Furniture"]
            }).to_csv(self.test_file, index=False)

        # Initialisation de l'instance de recherche
        self.search = Search()

    def tearDown(self):

        """Nettoyage après chaque test."""
        pass  # Aucun fichier à supprimer car on utilise le fichier existant

    def test_search_by_product(self):
        """Test de la fonction de recherche par nom de produit."""
        product_name = "Smartphone"
        results = self.search.search_by_product(product_name)
        expected_result = 1  # Un seul résultat pour 'Smartphone'
        self.assertEqual(len(results), expected_result,
                         f"La recherche par produit '{product_name}' "
                         f"doit retourner un seul résultat.")
        self.assertTrue(results['product_name'].str.contains(product_name).any(),
                        f"Le produit '{product_name}' "
                        f"doit être dans les résultats.")

    def test_search_by_category(self):
        """Test de la fonction de recherche par catégorie."""
        category = "Electronics"
        results = self.search.search_by_category(category)
        # Trois résultats dans la catégorie 'Electronics'
        expected_result = 3
        self.assertEqual(len(results), expected_result,
                         f"La recherche par catégorie '{category}' "
                         f"doit retourner {expected_result} résultats.")
        self.assertTrue("Smartphone" in results['product_name'].values,
                        "Le produit 'Smartphone' doit être dans les résultats.")
        self.assertTrue("Laptop" in results['product_name'].values,
                        "Le produit 'Laptop' doit être dans les résultats.")
        self.assertTrue("Headphones" in results['product_name'].values,
                        "Le produit 'Headphones' doit être dans les résultats.")

    def test_search_by_price(self):
        """Test de la fonction de recherche par prix."""
        min_price = 30
        max_price = 100
        results = self.search.search_by_price(min_price, max_price)
        # Attendu : 3 produits dans cette gamme de prix
        expected_result = 3
        self.assertEqual(len(results), expected_result,
                         f"La recherche par prix entre {min_price} et "
                         f"{max_price} doit retourner {expected_result} résultats.")
        self.assertTrue((results['price'] >= min_price).all() and (results['price'] <= max_price).all(),
                        f"Les prix doivent être entre {min_price} et {max_price}.")


if __name__ == "__main__":
    unittest.main()
