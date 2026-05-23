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

### Additionally
This project in development process, soon improving User Interface and create connection with MySQL o PostgreSQL
DataBase, sqlite.db is temporall database
