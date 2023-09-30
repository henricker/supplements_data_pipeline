from ..abstract_transform_data import AbstractTransformData
from typing import Dict, Any

class GrowthTransformData(AbstractTransformData):
    def transform(self, product: Dict[str, Any]) -> Dict[str, Any]:
        keys_to_convert = ['cash_payment', 'min_price_installments', 'cash_payment_credit_card']
        product_parsed = {
            'company_name': product['company_name'],
            'product_name': product['product_name'],
        }
        
        for key in keys_to_convert:
            value = product.get(key)
            if value is not None:
                product_parsed[key] = float(value.replace(',', '.'))
        
        max_installments = product.get('max_installments')

        if max_installments is not None:
            product_parsed['max_installments'] = int(max_installments)
        
        return product_parsed