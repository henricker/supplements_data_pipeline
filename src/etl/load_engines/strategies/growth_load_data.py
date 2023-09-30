from ..abstract_load_data import AbstractLoadData
from typing import Dict, Any
import csv
import os

class GrowthLoadData(AbstractLoadData):
    def load(self, product: Dict[str, Any]) -> None:
        file_path = './src/etl/products.csv'
        field_names = ['company_name', 'product_name', 'cash_payment', 'max_installments', 'min_price_installments', 'cash_payment_credit_card']
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
        with open(file_path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writerow({
                'company_name': product.get('company_name'),
                'product_name': product.get('product_name'),
                'cash_payment': product.get('cash_payment'),
                'max_installments': product.get('max_installments'),
                'min_price_installments': product.get('min_price_installments'),
                'cash_payment_credit_card': product.get('cash_payment_credit_card')
            })
        