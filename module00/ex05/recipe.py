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

    def __str__(self):
        return "Ingredients: {0}\nMeal: {1}\nPrep_time: {2}".format(', '.join(self.ingredients), self.meal, self.prep_time)

class CookBook:

    def __init__(self):
        self.recipes = {
            "Sandwich" : Recipe("Sandwich", ["ham", "bread", "cheese", "tomatoes"], "lunch", 10),
            "Cake" : Recipe("Cake", ["flour", "sugar", "eggs"], "dessert", 60),
            "Salad" : Recipe("Salad", ["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15)
            }
    
    def print_cookbook(self):
        [print(f' {r} : {self.recipes[r]}') for r in self.recipes]

    def add_recipe(self, recipe_name, recipe):
        self.recipes[recipe_name] = recipe
    
    def print_recipe(self, recipe_name):
        if recipe_name in self.recipes.keys():
            print(self.recipes[recipe_name])

    def del_recipe(self, recipe_name):
        if recipe_name in self.recipes.keys():
            del self.recipes[recipe_name]
    
    def input_recipe(self):
        
        ingredients = []
        recipe_name = input("Enter a recipe name: ")
        while True:
            ing_input = input("Enter ingredients: ")
            if not ing_input:
                break
            else:
                ingredients.append(ing_input)
        meal = input("Enter a meal type: ")
        prep_time = input("Enter a preparation time: ")

        self.add_recipe(recipe_name, Recipe(recipe_name, ingredients, meal, prep_time))

if __name__ == "__main__":
    
    options = "List of available option\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n"

    print("Welcome to the Python Cookbook !")
    print(options)
    cookbook = CookBook()

    while True:
        try:
            inp = int(input("Please select an option: "))
            if inp == 1:
                cookbook.input_recipe()
            elif inp == 2:
                del_entry = input("Enter a recipe name to delete: ")
                cookbook.del_recipe(del_entry)
            elif inp == 3:
                print_entry = input("Enter a recipe name to print: ")
                cookbook.print_recipe(print_entry)
            elif inp == 4:
                cookbook.print_cookbook()
            elif inp == 5:
                print("Cookbook closed. Goodbye !")
                break
            else:
                print("Sorry, this option does not exist.")
                print(options)

            print()

        except ValueError:
            print("Sorry, this option does not exist.")
            print(options)
        except:
            break