from django.core.management.base import BaseCommand
from shop.models import Brand, Category, Product


class Command(BaseCommand):
    help = 'Seed sample luxury brands and products'

    def handle(self, *args, **kwargs):
        cats = ['Tote Bag', 'Shoulder Bag', 'Clutch', 'Crossbody', 'Mini Bag', 'Backpack']
        cat_objs = {}
        for c in cats:
            obj, _ = Category.objects.get_or_create(name=c, slug=c.lower().replace(' ', '-'))
            cat_objs[c] = obj

        brands_data = [
            ('Chanel', 'chanel', 'Iconic French fashion house known for timeless elegance.'),
            ('Dior', 'dior', 'Parisian luxury house celebrated for feminine sophistication.'),
            ('Hermes', 'hermes', 'French luxury goods manufacturer known for the Birkin bag.'),
            ('Louis Vuitton', 'louis-vuitton', 'The world\'s most valuable luxury brand.'),
            ('Gucci', 'gucci', 'Italian fashion house with bold, eclectic designs.'),
            ('Prada', 'prada', 'Italian luxury brand known for minimalist elegance.'),
            ('Balenciaga', 'balenciaga', 'Avant-garde Spanish fashion house.'),
            ('Fendi', 'fendi', 'Italian luxury house famous for the Baguette bag.'),
        ]

        brand_objs = {}
        for name, slug, desc in brands_data:
            obj, _ = Brand.objects.get_or_create(name=name, slug=slug, defaults={'description': desc})
            brand_objs[slug] = obj

        products = [
            ('Classic Flap Bag', 'chanel-classic-flap', 'chanel', 'Shoulder Bag', 8500.00, 3, True),
            ('2.55 Reissue', 'chanel-255-reissue', 'chanel', 'Shoulder Bag', 9200.00, 2, False),
            ('Boy Bag', 'chanel-boy-bag', 'chanel', 'Crossbody', 7800.00, 4, True),
            ('Lady Dior', 'dior-lady-dior', 'dior', 'Shoulder Bag', 5500.00, 5, True),
            ('Saddle Bag', 'dior-saddle-bag', 'dior', 'Crossbody', 4200.00, 3, False),
            ('Book Tote', 'dior-book-tote', 'dior', 'Tote Bag', 3100.00, 6, True),
            ('Birkin 25', 'hermes-birkin-25', 'hermes', 'Tote Bag', 18000.00, 1, True),
            ('Kelly 28', 'hermes-kelly-28', 'hermes', 'Shoulder Bag', 15000.00, 1, True),
            ('Constance 18', 'hermes-constance-18', 'hermes', 'Crossbody', 12000.00, 2, False),
            ('Neverfull MM', 'lv-neverfull-mm', 'louis-vuitton', 'Tote Bag', 2100.00, 8, True),
            ('Speedy 30', 'lv-speedy-30', 'louis-vuitton', 'Tote Bag', 1800.00, 7, False),
            ('Pochette Metis', 'lv-pochette-metis', 'louis-vuitton', 'Crossbody', 2400.00, 4, True),
            ('GG Marmont', 'gucci-gg-marmont', 'gucci', 'Shoulder Bag', 1650.00, 6, True),
            ('Dionysus', 'gucci-dionysus', 'gucci', 'Shoulder Bag', 2200.00, 3, False),
            ('Galleria Bag', 'prada-galleria', 'prada', 'Tote Bag', 2800.00, 4, True),
            ('Re-Edition 2005', 'prada-re-edition-2005', 'prada', 'Shoulder Bag', 1450.00, 5, False),
            ('Cleo Bag', 'prada-cleo', 'prada', 'Clutch', 1750.00, 3, True),
            ('City Bag', 'balenciaga-city', 'balenciaga', 'Shoulder Bag', 2100.00, 4, False),
            ('Hourglass Bag', 'balenciaga-hourglass', 'balenciaga', 'Shoulder Bag', 2400.00, 3, True),
            ('Baguette', 'fendi-baguette', 'fendi', 'Shoulder Bag', 3200.00, 4, True),
            ('Peekaboo', 'fendi-peekaboo', 'fendi', 'Tote Bag', 4500.00, 2, False),
        ]

        for name, slug, brand_slug, cat_name, price, stock, featured in products:
            brand = brand_objs.get(brand_slug)
            cat = cat_objs.get(cat_name)
            desc = (
                f"The {name} by {brand.name} is a masterpiece of luxury craftsmanship. "
                f"Featuring premium materials and exquisite detailing, this iconic piece "
                f"is a timeless addition to any collection."
            )
            Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'brand': brand,
                    'category': cat,
                    'name': name,
                    'description': desc,
                    'price': price,
                    'stock': stock,
                    'is_featured': featured,
                    'is_active': True,
                }
            )

        self.stdout.write(self.style.SUCCESS('Sample data seeded successfully!'))
        self.stdout.write(self.style.SUCCESS(
            f'{Brand.objects.count()} brands, {Product.objects.count()} products created.'
        ))
