# Dashboard-Pagani-Car
Dashboard manage Car Pagani brand for the Shop

### Description
Dashboard allow management Car Pagani Brand in the Shop, modify his data or stated

### Features
- Create a new Car with model, brand, external and internal color, stated, price, etc
- Modify state of Car as price, stock and stated
- Delete a Car by Dashboard

### Structure Project
```
car_shop                    # Project of the Dashboard
|                           
|-- settings.py             # Setting by the Project
|-- urls.py                 # Connection of the Project with Apps
|-- views.py                # Render and display all Car in the Shop
|                               
car                         # App 1: Car Data e Information
|                           
|-- views.py                
|-- models.py               # Car Information and Functionabilitys for Manage
|-- urls.py                 
|                               
template                    # HTML show the car's, details every car and manage
|                           
|-- dashbboard/             # Show all car
|   |                       
|   |-- dashboard.html      # Home of Dashboard with all car availability
|                           
|-- car/                    # Show car
|   |                       
|   |...                    # Manage Car in the Shop
|                               
|-- .gitignore
|-- manage.py
```

### Technology

- Python and Django -> For data model and business logic manage Car
- HTML -> Create user interface in section List and Detail Car, Create, Update and Delete Car
- CSS -> Style to improving user interface

### Additionally
This project in development process, soon add JavaScript functionallitys to interactive interface
