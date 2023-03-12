class Recipe:

    def __init__(self, name, ingredients, meal, prep_time):
        self.recipe_name = name
        self.ingredients = ingredients
        self.meal = meal
        self.prep_time = prep_time

    def get_recipe(self):
        return {
            "ingredients" : self.ingredients,
            "meal" : self.meal,
            "prep_time" : self.prep_time
        }

    def get_name(self):
        return self.recipe_name
    
sandwich = Recipe("Sandwich", ["ham", "bread", "cheese", "tomatoes"], "lunch", 10)
cake = Recipe("Cake", ["flour", "sugar", "eggs"], "dessert", 60)
salad = Recipe("Salad", ["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15)

cookbook = {sandwich.get_name() : sandwich.get_recipe(),
            cake.get_name() : cake.get_recipe(),
            salad.get_name() : salad.get_recipe()}
