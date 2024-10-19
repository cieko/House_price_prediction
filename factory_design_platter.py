from abc import ABC, abstractmethod

# The abc module in Python provides the Abstract Base Class (ABC) infrastructure.
# It allows us to define abstract classes and methods which must be implemented in derived classes.
# The ABC class is used to mark a class as abstract, meaning it cannot be instantiated directly.
# Instead, it acts as a blueprint for other classes.
# Abstract methods are methods defined in an abstract class that do not contain any implementation.
# Any subclass inheriting from an abstract class must implement these abstract methods,
# otherwise, it too will be considered abstract and cannot be instantiated.

# Step 1: Define the Product interface (Abstract Base Class)
class Coffee(ABC):
    """
    Coffee class is an abstract base class (ABC) which defines an abstract method 'prepare'.
    All subclasses of Coffee must implement the 'prepare' method, ensuring a consistent interface.
    """
    
    @abstractmethod
    def prepare(self):
        """
        Abstract method 'prepare' which needs to be implemented by all concrete subclasses.
        This method defines the behavior that must be provided by specific coffee types.
        """
        pass

# Step 2: Implement Concrete Products
# These concrete classes (Expresso, Latte, Cappuccino) inherit from the abstract Coffee class
# and provide specific implementations of the 'prepare' method.

class Expresso(Coffee):
    """Concrete class representing Expresso coffee."""
    
    def prepare(self):
        """Implements the abstract 'prepare' method to create an Expresso."""
        return "Preparing a rich and strong Expresso."

class Latte(Coffee):
    """Concrete class representing Latte coffee."""
    
    def prepare(self):
        """Implements the abstract 'prepare' method to create a Latte."""
        return "Preparing a smooth and creamy Latte."

class Cappuccino(Coffee):
    """Concrete class representing Cappuccino coffee."""
    
    def prepare(self):
        """Implements the abstract 'prepare' method to create a Cappuccino."""
        return "Preparing a frothy Cappuccino."


# Step 3: Implement the Factory (CoffeeMachine)
# The CoffeeMachine class acts as a factory that dynamically creates different Coffee objects
# depending on the type of coffee requested. The factory pattern allows us to abstract the
# creation process, so the client code doesn't need to know about the specific classes.

class CoffeeMachine:
    """
    Factory class to create different types of Coffee based on the coffee_type input.
    It hides the object creation details and provides a simple interface to the user.
    """
    
    def make_coffee(self, coffee_type):
        """
        Creates a Coffee object based on the input coffee_type.
        
        Args:
            coffee_type (str): The type of coffee requested (Expresso, Latte, Cappuccino).
        
        Returns:
            str: The preparation message for the chosen coffee type, or an error message for unknown types.
        """
        if coffee_type == "Expresso":
            return Expresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        else:
            return "Unknown Coffee type!"


# Step 4: Use the factory to create products
# In this section, we use the CoffeeMachine to produce different types of coffee without
# needing to know the internal details of how each type is prepared.

if __name__ == "__main__":
    # Instantiate the CoffeeMachine (Factory)
    machine = CoffeeMachine()

    # Make an Expresso
    coffee = machine.make_coffee("Expresso")
    print(coffee)

    # Make a Latte
    coffee = machine.make_coffee("Latte")
    print(coffee)

    # Make a Cappuccino
    coffee = machine.make_coffee("Cappuccino")
    print(coffee)
