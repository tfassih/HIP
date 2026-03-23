from hmac import new
from db.loader import config
from flask import g
import webview
import psycopg2
from cfg.menu_items import newItem

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models.Item import Base, Item


class API:
    def __init__(self):
        self.connected = False

    def add_new_inv_item(self, data):
        item = data
        print(f"Received new inventory item data: {item}")
        inventory_controller.add_new_inventory_item(item)

    def check_db_connection(self):
        return self.connected
    
    def getNewItemTypes(self):
        print(f"Retrieving new item types: {newItem['primaryType']}")
        return newItem['primaryType']
    
    def getPhysicalItemTypes(self):
        print(f"Retrieving physical item types: {newItem['physicalType']}")
        return newItem['physicalType']
    
    def getPhysicalItemDimUnits(self):
        print(f"Retrieving physical item dimension units: {newItem['physicalTypeDimUnits']}")
        return newItem['physicalTypeDimUnits']
    
    def getPhysicalItemWeightUnits(self):
        print(f"Retrieving physical item weight units: {newItem['physicalTypeWeightUnits']}")
        return newItem['physicalTypeWeightUnits']
    
    def getActivityTypes(self):
        print(f"Retrieving activity item types: {newItem['activityType']}")
        return newItem['activityType']
    
    def getActivityLengthUnits(self):
        print(f"Retrieving activity length units: {newItem['activityLengthUnits']}")
        return newItem['activityLengthUnits']


class InventoryServerController:
    def __init__(self, init_tests=True):
        if init_tests:
            self.inventory_init_tests()

    def inventory_init_tests(self):
        test_item_data = {
            'name': 'Test Item',
            'quantity': 1,
            'price': 9.99,
            'location': 'Test Location',
            'description': 'This is a test item.',
            'primary_type': 'Physical',
            'physical_type': 'Tool',
            'physical_weight': 1.0,
            'physical_weight_unit': 'kg',
            'physical_length': 1.0,
            'physical_length_unit': 'cm',
            'physical_width': 1.0,
            'physical_width_unit': 'cm',
            'physical_height': 1.0,
            'physical_height_unit': 'cm',
            'item_type': 'Digital'

        }
        try:
            fail = 0
            self.get_inventory() 
            self.add_new_inventory_item(test_item_data)
            if self.validate_inventory_item():
                print("Test item successfully added and retrieved from database.")
            else:
                print("Failed to retrieve test item from database.")
                fail += 1
            if len(self.get_inventory()) > 0:
                print("Inventory retrieval test passed.")
            else:
                print("Inventory retrieval test failed: No items found in inventory.")
                fail += 1
            if fail == 0:
                print("Inventory initialization tests passed.")
                self.wipe_inventory()  # Clean up test data after successful tests
            else:
                raise Exception("One or more inventory initialization tests failed.")
        except Exception as e:
            print(f"Inventory initialization tests failed: {e}")

    def add_new_inventory_item(self, item_data):
        print(f"Item added to local memory: {item_data}")
        print(f"Session created: {session.is_active}")
        new_item = Item(**item_data)
        session.add(new_item)
        session.commit()
        if self.validate_inventory_item():
            print(f"Item successfully added to database: {new_item}")
        else:
            print(f"Failed to add item to database: {new_item}")

    def validate_inventory_item(self, **args):
        return session.query(Item).first() is not None

    def get_inventory(self):
        return session.query(Item).all()
    
    def get_inventory_item(self, item_id):
        return session.query(Item).filter(Item.id == item_id).first()
    
    def remove_inventory_item(self, item_id):
        item = self.get_inventory_item(item_id)
        if item:
            session.delete(item)
            session.commit()
            print(f"Item with ID {item_id} removed from inventory.")
        else:
            print(f"Item with ID {item_id} not found in inventory.")

    def wipe_inventory(self):
        try:
            num_deleted = session.query(Item).delete()
            session.commit()
            print(f"All inventory items wiped. Total items deleted: {num_deleted}")
        except Exception as e:
            print(f"Error wiping inventory: {e}")
    
    # TO ADD: Methods for editing and accessing inventory items, as well as syncing with the database

class DatabaseController:
    def __init__(self):
        self.connection = None
        self.connected = False

    def connect(self):
        try:
            self.connection = engine.connect()
            print("Database connection established.")
            self.connected = True
        except Exception as e:
            print(f"Error connecting to database: {e}")


db_params = config()
engine = create_engine(db_params['url'])
Session = sessionmaker(bind=engine)
session = Session()
add_new_inv_item = None
getNewItemTypes = newItem['primaryType']
print(f"New item types loaded: {getNewItemTypes}")
getPhysicalItemTypes = newItem['physicalType']
getPhysicalItemDimUnits = [newItem['physicalTypeDimUnits'], newItem['physicalTypeDimUnits'], newItem['physicalTypeDimUnits']]
getPhysicalItemWeightUnits = newItem['physicalTypeWeightUnits']
getActivityTypes = newItem['activityType']
getActivityLengthUnits = newItem['activityLengthUnits']

api = API()
inventory_init_tests = False
database_controller = DatabaseController()
database_controller.connect()
if database_controller.connected:
    api.connected = True
try:
    if not inspect(engine).has_table('items'):
        print("Creating database tables...")
        Base.metadata.create_all(engine)
        print("Database tables created successfully.")
        inventory_init_tests = True
    elif not session.query(Item).first():
        print("Database tables exist but are empty. Ready for inventory data.")
    elif session.query(Item).first():
        print("Database tables exist and contain inventory data.")
except Exception as e:
    print(f"Error creating or initializing database tables: {e}")

inventory_controller = InventoryServerController(inventory_init_tests)
webview.create_window('HIP', 'views/main-menu.html', js_api=api)
webview.start(debug=True, ssl=True)