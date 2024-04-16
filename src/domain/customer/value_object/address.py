class Address:
    # Constructor of the class
    def __init__(self, street: str, number: int, zip_code: str, city: str):
        # Initialization of class attributes
        self._street = street
        self._number = number
        self._zip_code = zip_code
        self._city = city
        # Validation of attributes
        self.validate()

    # Properties of the class
    @property
    def street(self) -> str:
        return self._street

    @property
    def number(self) -> int:
        return self._number

    @property
    def zip_code(self) -> str:
        return self._zip_code

    @property
    def city(self) -> str:
        return self._city

    # Method to validate the attributes
    def validate(self):
        if len(self._street) == 0:
            raise ValueError("Street is required")
        if self._number == 0:
            raise ValueError("Number is required")
        if len(self._zip_code) == 0:
            raise ValueError("Zip is required")
        if len(self._city) == 0:
            raise ValueError("City is required")

    # Method to get the full address
    def __str__(self):
        return f"{self._street}, {self._number}, {self._zip_code} {self._city}"
