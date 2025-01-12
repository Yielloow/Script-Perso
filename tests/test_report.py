import unittest
import os
import sys
import pandas as pd
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from report import Report


class TestReport(unittest.TestCase):

    @patch('builtins.print')
    def test_generate_report(self, mock_print):
        report = Report()
        # Appeler la méthode generate_report
        report.generate_report()
        # Vérifier si le fichier a été créé
        self.assertTrue(os.path.exists('inventory_report.csv'))
        # Lire le fichier et vérifier le contenu
        result_df = pd.read_csv('inventory_report.csv')
        # Vérifier que les colonnes attendues sont présentes
        self.assertIn('category', result_df.columns)
        self.assertIn('total_quantity', result_df.columns)
        self.assertIn('total_value', result_df.columns)
        # Vérifier si le fichier contient des données
        self.assertGreater(len(result_df), 0)
        # Vérifier l'appel du print
        mock_print.assert_called_with(
            "Rapport généré et sauvegardé sous 'inventory_report.csv'."
        )
        # Nettoyer après le test
        # os.remove('inventory_report.csv')


if __name__ == '__main__':
    unittest.main()
