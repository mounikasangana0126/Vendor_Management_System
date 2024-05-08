## Vendor Management System with Performance Metrics


### Objective

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

### Features
- **Vendor Management**: Manage vendor information including name, contact details, address, and vendor code.This model stores essential information about each vendor and their performance metrics.
- **Purchase Order Management**: Create, update, retrieve, and delete purchase orders with detailed information such as order date, delivery date, items, quantity, and status.This model captures the details of each purchase order and is used to calculate various
performance metrics.
- **Performance Metrics**: Compute vendor performance metrics including on-time delivery rate, quality rating average, average response time, and fulfillment rate.This model optionally stores historical data on vendor performance, enabling trend analysis.

### Performance Metrics
#### On-Time Delivery Rate: 
  Calculated each time a PO status changes to 'completed'
#### Quality Rating Average:
  Updated upon the completion of each PO where a quality_rating is provided.
#### Average Response Time:
  Calculated each time a PO is acknowledged by the vendor.
#### Fulfilment Rate:
  Calculated upon any change in PO status.
 
### Setup Instructions
1. Clone the repository:
2. Install dependencies:
3. Apply database migrations:
4. Run the development server:
5. Access the application at `http://localhost:8000/`.


### Setup In Detail
1. git clone https://github.com/mounikasangana0126/Vendor_Management_System.git
2. pip install Django
3. pip install djangorestframework
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver


## API Endpoints

### Secure API endpoints with token-based authentication

Create user through the admin panel and provide the same username and password for post api below to get authorization token. Use that authorization token in headers to secure the api end points. 

- **to get authorization token**: `POST /auth/` 

### Vendor Profile Management

- **List Vendors**: `GET /vendors/`
- **Create Vendor**: `POST /vendors/`
- **Retrieve Vendor**: `GET /vendors/<vendor_id>/`
- **Update Vendor**: `PUT /vendors/<vendor_id>/`
- **Delete Vendor**: `DELETE /vendors/<vendor_id>/`

### Purchase Orders Tracking

- **List Purchase Orders**: `GET /purchase-orders/`
- **Create Purchase Order**: `POST /purchase-orders/`
- **Retrieve Purchase Order**: `GET /purchase-orders/<order_id>/`
- **Update Purchase Order**: `PUT /purchase-orders/<order_id>/`
- **Delete Purchase Order**: `DELETE /purchase-orders/<order_id>/`

### Vendor Performance Evaluation:

- **Retrieve a vendor's performance metrics**: `GET /vendors/<vendor_id>/performance/`
- **vendors to acknowledge POs**: `POST /purchase_orders/<order_id>/acknowledge`

## Testing the API

You can run the test suite by executing: `python manage.py run test tests`


