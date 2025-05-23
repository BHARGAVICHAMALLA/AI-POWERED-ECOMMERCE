from django import template
from django.conf import settings

register = template.Library()

PRODUCT_PLACEHOLDER_IMAGES = [
    'https://images.unsplash.com/photo-1572635196237-14b3f281503f',  # Sunglasses
    'https://images.unsplash.com/photo-1542291026-7eec264c27ff',  # Red Nike
    'https://images.unsplash.com/photo-1523275335684-37898b6baf30',  # Watch
    'https://images.unsplash.com/photo-1505740420928-5e560c06d30e',  # Headphones
    'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f',  # Camera
    'https://images.unsplash.com/photo-1585386959984-a4155224a1ad',  # Perfume
    'https://images.unsplash.com/photo-1591337676887-a217a6970a8a',  # Laptop
    'https://images.unsplash.com/photo-1600080972464-8e5f35f63d08',  # Smartphone
]

CATEGORY_IMAGES = {
    'electronics': 'https://images.unsplash.com/photo-1526738549149-8e07eca6c147',
    'clothing': 'https://images.unsplash.com/photo-1489987707025-afc232f7ea0f',
    'books': 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f',
    'home': 'https://images.unsplash.com/photo-1556228453-efd6c1ff04f6',
    'sports': 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211',
    'beauty': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348',
    'food': 'https://images.unsplash.com/photo-1606787366850-de6330128bfc',
    'toys': 'https://images.unsplash.com/photo-1558877385-81a1c7e67d72',
}

@register.filter
def get_placeholder_image(product, index=0):
    """
    Returns a placeholder image URL based on product category or index
    """
    if product.category:
        category_name = product.category.name.lower()
        if category_name in CATEGORY_IMAGES:
            return CATEGORY_IMAGES[category_name]
    
    return PRODUCT_PLACEHOLDER_IMAGES[index % len(PRODUCT_PLACEHOLDER_IMAGES)]

@register.filter
def get_empty_state_image(index=0):
    """
    Returns a placeholder image for empty states
    """
    return PRODUCT_PLACEHOLDER_IMAGES[0] 