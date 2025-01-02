import pandas as pd


class Report:
    def __init__(self):
        self.inventory = pd.read_csv('consolidated_inventory.csv')

    def generate_report(self):
        total_value = self.inventory['quantity'] * self.inventory['price']
        self.inventory['total_value'] = total_value
        report = self.inventory.groupby('category').agg(
            total_quantity=('quantity', 'sum'),
            total_value=('total_value', 'sum')
        ).reset_index()

        report.to_csv('inventory_report.csv', index=False)
        print("Rapport généré et sauvegardé sous 'inventory_report.csv'.")
