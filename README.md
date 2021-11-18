# PriceComparator
PriceComparator is a Django tool to compare prices from merchant API endpoints. The project was constructed in one week and represents my first experience with Django. This project uses a Merchants app that mocks the endpoints and a UPCs app that compares the prices and returns the first merchant URL with the lowest price.

## Installation and Usage
PriceComparator is not currently built into an executable. As such, The following command can be used to run the test environment:

`python manage.py runserver`

In a browser window, the following URL will run a price comparison on some of the mockup data:
- http://localhost:8000/price-comparator?upc=<upc>

Where `<upc>` is one of the following:
- 12345
- 56789
- 00000
- 11111

Each of these UPCs represents a manual test case that provides the calling function with a JsonResponse that is unique to each merchant and parsed by a merchant-specific parser.

## Features
- Easily add a merchant by adding the data to the Merchant model in the admin interface at http://localhost:8000/admin then implementing the appropriate parser in `upcs/parsers.py`
- The Merchant app simulates several vendor endpoints, as outlined above.
- The Upc app analyzes responses from the Merchant app and provides the first merchant URL with the lowest price and item in stock.
