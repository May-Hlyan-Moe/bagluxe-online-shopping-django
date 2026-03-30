import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bagluxe.settings')
django.setup()

from django.core.files.base import ContentFile
from shop.models import Product

BRAND_COLORS = {
    'chanel':        ('#1a1a1a', '#3d3d3d', '#e8a0b4'),
    'dior':          ('#2d1b4e', '#4a2d7a', '#f8bbd0'),
    'hermes':        ('#b85c00', '#d4720a', '#ffffff'),
    'louis-vuitton': ('#6b3a1f', '#8b4513', '#f8bbd0'),
    'gucci':         ('#1a3a1a', '#2d5a2d', '#f8bbd0'),
    'prada':         ('#1a1a2e', '#16213e', '#e8a0b4'),
    'balenciaga':    ('#0d0d0d', '#1a1a1a', '#e8a0b4'),
    'fendi':         ('#8b6914', '#c9a96e', '#ffffff'),
}

SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="bg{idx}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1}"/>
      <stop offset="100%" style="stop-color:{c2}"/>
    </linearGradient>
  </defs>
  <rect width="600" height="600" fill="url(#bg{idx})"/>
  <circle cx="500" cy="80" r="130" fill="rgba(255,255,255,0.07)"/>
  <circle cx="80" cy="520" r="110" fill="rgba(255,255,255,0.05)"/>
  <g transform="translate(210,110)">
    <rect x="10" y="45" width="160" height="125" rx="14" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.45)" stroke-width="2.5"/>
    <path d="M38 45 Q38 8 90 8 Q142 8 142 45" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="3" stroke-linecap="round"/>
    <rect x="62" y="62" width="56" height="9" rx="4.5" fill="rgba(255,255,255,0.35)"/>
    <circle cx="90" cy="108" r="14" fill="rgba(255,255,255,0.25)" stroke="rgba(255,255,255,0.45)" stroke-width="2"/>
    <line x1="90" y1="94" x2="90" y2="122" stroke="rgba(255,255,255,0.45)" stroke-width="2"/>
    <line x1="76" y1="108" x2="104" y2="108" stroke="rgba(255,255,255,0.45)" stroke-width="2"/>
  </g>
  <rect x="50" y="305" width="500" height="240" rx="22" fill="rgba(255,255,255,0.96)"/>
  <text x="300" y="352" font-family="Georgia,serif" font-size="12" font-weight="700"
    fill="{accent}" text-anchor="middle" letter-spacing="5">{brand}</text>
  <line x1="190" y1="366" x2="410" y2="366" stroke="{accent}" stroke-width="1" opacity="0.35"/>
  <text x="300" y="408" font-family="Georgia,serif" font-size="{fs}" font-weight="600"
    fill="#2c2c2c" text-anchor="middle">{line1}</text>
  <text x="300" y="442" font-family="Georgia,serif" font-size="{fs}" font-weight="600"
    fill="#2c2c2c" text-anchor="middle">{line2}</text>
  <text x="300" y="488" font-family="Georgia,serif" font-size="24" font-weight="700"
    fill="{accent}" text-anchor="middle">${price}</text>
  <text x="300" y="522" font-family="Arial,sans-serif" font-size="13"
    fill="{accent}" text-anchor="middle" opacity="0.55">&#9825; Authentic Luxury &#9825;</text>
</svg>"""


def split_name(name):
    if len(name) <= 14:
        return name, ''
    words = name.split()
    mid = len(words) // 2
    return ' '.join(words[:mid]), ' '.join(words[mid:])


os.makedirs('media/products', exist_ok=True)
products = Product.objects.all()

for idx, product in enumerate(products):
    slug = product.brand.slug
    c1, c2, accent = BRAND_COLORS.get(slug, ('#c2185b', '#880e4f', '#ffffff'))
    line1, line2 = split_name(product.name)
    fs = '26' if len(product.name) <= 16 else '20'
    svg = SVG.format(
        idx=idx, c1=c1, c2=c2, accent=accent,
        brand=product.brand.name.upper(),
        line1=line1, line2=line2, fs=fs,
        price=int(product.price),
    )
    filename = f"{product.slug}.svg"
    product.image.save(filename, ContentFile(svg.encode('utf-8')), save=True)
    print(f"  OK: {product.brand.name} - {product.name}")

print(f"\nDone! {products.count()} images generated.")
