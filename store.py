from typing import List
import products


class Store:
    """Ein Geschäft, das eine Liste von Produkten verwaltet."""

    def __init__(self, product_list):
        """Erstellt den Store mit einer Liste von Produkten."""
        self.products = list(product_list)

    def add_product(self, product):
        """Fügt ein Produkt zum Store hinzu."""
        self.products.append(product)

    def remove_product(self, product):
        """Entfernt ein Produkt aus dem Store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Gibt die Gesamtmenge aller Produkte im Store zurück."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[products.Product]:
        """Gibt alle aktiven Produkte im Store zurück."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:  # pylint: disable=no-self-use
        """Kauft alle Produkte der Liste und gibt den Gesamtpreis zurück."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    """Testet die Klasse Store mit einigen Beispielprodukten."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()
