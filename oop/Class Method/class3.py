class Counter:
    count = 0  # Class-level attribute to keep track of object creation

    @classmethod
    def increase_count(cls):
        """Increases the count of created Counter objects."""
        cls.count += 1
        return cls.count  # Return the updated count

    def __init__(self):
        self.id = Counter.increase_count()  # Call class method from constructor

# Create three Counter objects
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

print(f"Total objects created: {Counter.count}")  # Access class-level data

# Class method modifies the count attribute
total_count = Counter.increase_count()  # Call class method again
print(f"Updated total objects created: {total_count}")
