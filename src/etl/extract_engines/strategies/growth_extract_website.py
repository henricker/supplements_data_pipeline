from ..abstract_extract_website import AbstractExtractWebsite
import requests
from bs4 import BeautifulSoup
import re

class GrowthExtractWebsite(AbstractExtractWebsite):
    def __init__(self):
        self.base_url = 'https://www.gsuplementos.com.br'
        self.product_categories = [
            'proteina', 
            'aminoacidos', 
            'carboidratos', 
            'vegetariano', 
            'vegano',
            'vitaminas',
            'termogenico',
            'acessorios',
            'roupas-de-treino',
            'clinical'
        ]

    def __get_product_details(self, item):
        text_item = item.text.replace('\n', '')
        product_name = text_item.lower().split('- growth supplements')[0].strip()
        
        if 'r$' in product_name:
            product_name = product_name.split('r$')[0]
        
        price_matches = re.findall(r'R\$(\d+\,\d{2})',  text_item)
        max_installments_data = re.findall(r'(\d+)x', text_item)

        cash_payment = None
        max_installments = None
        min_price_installments = None
        cash_payment_credit_card = None
        
        if len(price_matches) != 0:
            cash_payment = price_matches[0]
            max_installments = max_installments_data[0]
            min_price_installments = price_matches[2]
            cash_payment_credit_card = price_matches[1] 

        product_info = {
            'company_name': 'Growth Supplements',
            'product_name': product_name, 
            'cash_payment': cash_payment,
            'max_installments': max_installments,
            'min_price_installments': min_price_installments,
            'cash_payment_credit_card': cash_payment_credit_card
        }
        return product_info
    
    def __extract_items_from_request(self, category, page):
        print("----------: ", page)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get('{}/{}/{}'.format(self.base_url, category, page), headers=headers)
        if response.status_code != 200:
            raise RuntimeError('Request failed')
        soup = BeautifulSoup(response.content, 'html.parser')
        product_items = [prod for prod in soup.find_all('div', class_='vitrine-precos')]
        has_next = False
        try:
            has_next = 'disabled' not in soup.find('button', class_="proxima").attrs['class']
        except (AttributeError, KeyError):
            has_next = False
        
        return { 'product_items': product_items, 'has_next': has_next }
        
    def __extract_products_by_category(self, category):
        print("----------: ", category)
        has_next_page = True
        current_page = 1
        while has_next_page:
            result = self.__extract_items_from_request(category, page=current_page)
            data = [self.__get_product_details(item) for item in result['product_items']]
            for item in data:
                yield item
            current_page += 1
            if not result['has_next']:
                has_next_page = False

    
    def extract(self):
       for category in self.product_categories:
           yield from self.__extract_products_by_category(category)