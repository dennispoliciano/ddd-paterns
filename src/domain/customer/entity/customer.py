from ..value_object.address import Address


class Customer:
    # Constructor of the class
    def __init__(self, id: str, name: str):
        # Initialization of class attributes
        self._id = id
        self._name = name
        self._address = None
        self._active = False
        self._reward_points = 0
        # Validation of attributes
        self.validate()

    # Properties of the class
    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def reward_points(self) -> int:
        return self._reward_points

    # Method to validate the attributes
    def validate(self):
        if len(self._id) == 0:
            raise ValueError("Id is required")
        if len(self._name) == 0:
            raise ValueError("Name is required")

    # Method to change the customer's name
    def change_name(self, name: str):
        self._name = name
        self.validate()

    # Method to check if the customer is active
    def is_active(self) -> bool:
        return self._active

    # Method to activate the customer
    def activate(self):
        if self._address is None:
            raise ValueError("Address is mandatory to activate a customer")
        self._active = True
    
    # Method to deactivate the customer
    def deactivate(self):
        self._active = False
        
    # Property to access the customer's address
    @property
    def address(self) -> Address:
        return self._address

    # Method to change the customer's address
    def change_address(self, address: Address):
        self._address = address


    # Method to add reward points to the customer
    def add_reward_points(self, points: int):
        self._reward_points += points

    # Property to set the customer's address
    @address.setter
    def address(self, address: Address):
        self._address = address
