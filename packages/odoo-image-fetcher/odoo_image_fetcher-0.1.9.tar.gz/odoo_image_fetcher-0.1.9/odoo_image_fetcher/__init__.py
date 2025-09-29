import os
import logging
import requests
from dotenv import load_dotenv
import urllib3
import xmlrpc.client
import base64
import ssl

# Suppress SSL warnings for this test
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ImageFetcher:
    _session = requests.Session()
    _base_url = os.getenv("ODOO_BASE_URL", "").rstrip("/")
    _username = os.getenv("ODOO_USERNAME")
    _password = os.getenv("ODOO_PASSWORD")
    _db = os.getenv("ODOO_DB")
    _odoo_url = os.getenv("ODOO_BASE_URL")

    @staticmethod
    def fetch_image(image_path, model="product.template"):
        logging.info("Starting image fetch process for: %s", image_path)
        
        try:
            # Create an unverified SSL context
            unverified_context = ssl._create_unverified_context()

            # Pass the unverified context to ServerProxy
            common = xmlrpc.client.ServerProxy(
                f'{ImageFetcher._odoo_url}/xmlrpc/2/common',
                context=unverified_context
            )
            uid = common.authenticate(ImageFetcher._db, ImageFetcher._username, ImageFetcher._password, {})

            if not uid:
                logging.error("Authentication failed.")
                exit()

            logging.info("Authentication successful. User ID: %s", uid)

            # Pass the unverified context to the models ServerProxy as well
            models = xmlrpc.client.ServerProxy(
                f'{ImageFetcher._odoo_url}/xmlrpc/2/object',
                context=unverified_context
            )
            
            url = image_path.strip()
            url_breaks = url.split('/')
            
            # Use a list to access the extracted image ID and name
            image_id = int(url_breaks[-2])  # Convert ID to integer
            image_name = url_breaks[-1].strip()
            logging.info("Extracted image name: %s", image_name)
            logging.info("Extracted image ID: %s", image_id)
            
            # Correctly handle the API response
            image_record = models.execute_kw(
                ImageFetcher._db, uid, ImageFetcher._password,
                model, 'read',
                [[image_id]],
                {'fields': [image_name]}  # Use the extracted image name here
            )

            if image_record and image_record[0].get(image_name):
                image_data_base64 = image_record[0][image_name]
                logging.info("Image data (Base64) fetched successfully for record %s.", image_id)
                image_bytes = base64.b64decode(image_data_base64)
                return image_bytes
            else:
                logging.info("No image data found for record %s.", image_id)
                
        except Exception as e:
            logging.error("An error occurred: %s", e)