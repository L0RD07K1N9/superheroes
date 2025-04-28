# Base class for superheroes
class Superhero:
    def __init__(self, name, power_level, secret_identity):
        self._name = name  # Protected attribute (encapsulation)
        self._power_level = power_level
        self.__secret_identity = secret_identity  # Private attribute
    
    # Getter for secret identity (encapsulation)
    def get_secret_identity(self):
        return self.__secret_identity
    
    # Method to display superhero info
    def display_info(self):
        return f"Superhero: {self._name}, Power Level: {self._power_level}"
    
    # Polymorphic method (to be overridden)
    def move(self):
        return "Moving at super speed!"

# Derived class: Flying superhero
class FlyingHero(Superhero):
    def __init__(self, name, power_level, secret_identity, flight_speed):
        super().__init__(name, power_level, secret_identity)
        self.flight_speed = flight_speed
    
    # Override move method (polymorphism)
    def move(self):
        return f"Flying at {self.flight_speed} mph! ✈️"
    
    # Additional method
    def soar(self):
        return f"{self._name} is soaring through the skies!"

# Derived class: Speedster superhero
class SpeedsterHero(Superhero):
    def __init__(self, name, power_level, secret_identity, run_speed):
        super().__init__(name, power_level, secret_identity)
        self.run_speed = run_speed
    
    # Override move method (polymorphism)
    def move(self):
        return f"Running at {self.run_speed} mph! 🏃‍♂️"
    
    # Additional method
    def dash(self):
        return f"{self._name} dashes in a blur!"

# Main program to demonstrate
def main():
    # Create superhero objects
    sky_striker = FlyingHero("Sky Striker", 90, "Alex Sky", 500)
    flash_bolt = SpeedsterHero("Flash Bolt", 85, "Sam Swift", 300)
    
    # Demonstrate polymorphism
    heroes = [sky_striker, flash_bolt]
    print("Polymorphic Moves:")
    for hero in heroes:
        print(f"{hero._name}: {hero.move()}")
    
    # Show encapsulation and other methods
    print("\nSuperhero Details:")
    print(sky_striker.display_info())
    print(f"Secret Identity: {sky_striker.get_secret_identity()}")
    print(sky_striker.soar())
    
    print("\n" + flash_bolt.display_info())
    print(f"Secret Identity: {flash_bolt.get_secret_identity()}")
    print(flash_bolt.dash())

# Run the program
if __name__ == "__main__":
    main()