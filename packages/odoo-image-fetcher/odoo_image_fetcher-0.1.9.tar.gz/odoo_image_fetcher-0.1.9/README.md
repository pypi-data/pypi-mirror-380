
# odoo-image-fetcher

Fetch product images from Odoo using session-based authentication.

## Installation

```bash
pip install odoo-image-fetcher
````

## Usage

```python
from odoo_image_fetcher import ImageFetcher

image_bytes = ImageFetcher.fetch_image("/web/image/product.template/17956/image_128")
if image_bytes:
    with open("product_image.png", "wb") as f:
        f.write(image_bytes)
    print("✅ Image saved.")
else:
    print("❌ Image fetch failed.")

```

## Environment Variables

Put these in a `.env` file or your environment:

```
ODOO_BASE_URL=https://your.odoo.instance
ODOO_USERNAME=your@email.com
ODOO_PASSWORD=yourpassword
ODOO_DB=your_db_name
```

Enjoy!
[![PyPI version](https://badge.fury.io/py/odoo-image-fetcher.svg)](https://pypi.org/project/odoo-image-fetcher/)
