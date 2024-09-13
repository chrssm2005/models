import unittest
from models import Product

class TestProductModel(unittest.TestCase):
    
    def test_create_product(self):
        product = Product(name='Test Product', category='Test Category', availability='in_stock', price=29.99)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.category, 'Test Category')
        self.assertEqual(product.availability, 'in_stock')
        self.assertEqual(product.price, 29.99)
    
    def test_update_product(self):
        product = Product(name='Old Name', category='Old Category', availability='out_of_stock', price=10.00)
        product.update(name='New Name', price=20.00)
        self.assertEqual(product.name, 'New Name')
        self.assertEqual(product.price, 20.00)
    
    def test_delete_product(self):
        product = Product(name='Delete Me', category='Category', availability='in_stock', price=15.00)
        product.delete()
        self.assertIsNone(Product.find_by_name('Delete Me'))
    
    def test_list_all_products(self):
        products = Product.list_all()
        self.assertGreater(len(products), 0)
    
    def test_find_by_name(self):
        product = Product.find_by_name('Some Product')
        self.assertIsNotNone(product)
    
    def test_find_by_category(self):
        products = Product.find_by_category('Some Category')
        self.assertGreater(len(products), 0)
    
    def test_find_by_availability(self):
        products = Product.find_by_availability('in_stock')
        self.assertGreater(len(products), 0)
