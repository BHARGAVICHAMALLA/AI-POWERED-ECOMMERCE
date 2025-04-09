# AI-Powered E-Commerce Website

This is a feature-rich e-commerce platform with an AI-powered recommendation system that personalizes shopping experiences based on user behavior, purchase history, and browsing patterns.

## Features

- **User Management & Authentication**
  - User registration and login
  - JWT-based authentication
  - Profile management

- **Product Management & Smart Search**
  - Well-structured product catalog with categories and brands
  - Advanced product filtering and sorting
  - Smart search with keyword matching

- **AI-Based Recommendation System**
  - Content-Based Filtering: Suggests similar products based on product attributes
  - Collaborative Filtering: Suggests products based on similar user preferences
  - Hybrid Recommendation Model: Combines multiple approaches for accurate predictions

- **Shopping Cart & Wishlist**
  - Add/remove products to cart and wishlist
  - Dynamic cart updates with price calculations

- **Secure Payment Integration**
  - Multiple payment options
  - Secure checkout process

- **Order Management & Tracking**
  - Order history and tracking
  - Order status updates

- **Product Reviews & Ratings**
  - User reviews and ratings for products
  - Average rating calculation

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (development), PostgreSQL (production)
- **AI & Machine Learning**: scikit-learn, pandas, numpy
- **Authentication**: JWT (JSON Web Tokens)

## API Endpoints

### Authentication
- `POST /api/token/`: Get JWT token
- `POST /api/token/refresh/`: Refresh JWT token

### Products
- `GET /api/products/`: List all products
- `GET /api/products/{id}/`: Get product details
- `GET /api/products/featured/`: Get featured products
- `GET /api/products/new_arrivals/`: Get new arrivals
- `GET /api/products/top_rated/`: Get top-rated products
- `GET /api/categories/`: List all categories
- `GET /api/brands/`: List all brands
- `POST /api/products/{id}/reviews/`: Add a product review
- `GET /api/search/?q={query}`: Search products

### Recommendations
- `GET /api/recommendations/`: Get personalized recommendations
- `GET /api/recommendations/preferences/`: Get user preferences
- `POST /api/recommendations/preferences/`: Update user preferences

## Installation

1. Clone the repository
```
git clone https://github.com/yourusername/ai-ecommerce.git
cd ai-ecommerce
```

2. Create a virtual environment and install dependencies
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run migrations
```
python manage.py migrate
```

4. Create a superuser
```
python manage.py createsuperuser
```

5. Run the development server
```
python manage.py runserver
```

6. Access the admin interface at http://127.0.0.1:8000/admin/

## AI Recommendation System

The recommendation system uses multiple approaches:

1. **Content-Based Filtering**: Recommends products similar to what the user has liked before, based on product attributes.

2. **Collaborative Filtering**: Recommends products based on what similar users have liked.

3. **Hybrid Approach**: Combines both methods for better recommendations.

4. **Trending Recommendations**: Shows popular products based on recent activity.

5. **Recent Activity Based**: Recommends products based on the user's recent browsing history.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 