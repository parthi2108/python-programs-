class IceCream:
    def __init__(self, ingredients, flavours):
        # Store the ingredients and flavours in the instance
        self.ingredients = ingredients
        self.flavours = flavours

    def scoops(self):
        # If either ingredients or flavours is empty, return an empty list
        if not self.ingredients or not self.flavours:
            return []
        
        # Generate combinations of ingredients and flavours
        return [[ingredient, flavour] for ingredient in self.ingredients for flavour in self.flavours]


if __name__ == "__main__":
    # Create an IceCream instance with ingredients and flavours
    vending = IceCream(["vanilla", "milkshake"], ["just_shake"])

    # Call the scoops method and print the output
    print(vending.scoops())  # Ensure the parentheses () are added






     

