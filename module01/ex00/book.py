from recipe import Recipe
from datetime import datetime

class Book:

    def __init__(self) -> None:
        pass

    def __init__(self, __name):
        self.name = __name
        self.last_update = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.creation_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        else:
            raise TypeError("not Recipe argument in Recipe.add_recipe")
    
    def get_recipes_by_types(self, type):
        if type != "starter" and type != "lunch" and type != "dessert":
            return []
        return [', '.join(str(k.name) for k in self.recipes_list[type])]
    
    def get_recipe_by_name(self, name):
        for key in self.recipes_list.keys():
            for recipe in self.recipes_list[key]:
                if name == recipe.name:
                    return recipe
        return Recipe
