class Recipe:
    def __init__(self) -> None:
        pass

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                       ingredients: list, description: str, recipe_type: str):
        if not name \
            or not isinstance(cooking_lvl, int) \
            or not isinstance(cooking_time, int) \
            or not isinstance(ingredients, list) \
            or len(ingredients) == 0 \
            or not all(isinstance(i, str) for i in ingredients) \
            or not all(len(i) for i in ingredients) \
            or not recipe_type:
            raise TypeError("Found empty string in Recipe initialization")
        
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description

        if recipe_type != "starter" \
            and recipe_type != "lunch" \
            and recipe_type != "dessert":
            raise ValueError("Found invalid recipe_type in Recipe initialization")
        
        self.recipe_type = recipe_type

    def __str__(self):
        return "Name: {0}\nCooking_lvl: {1}\nCooking_time: {2}min\nIngredients: {3}\nDescription: {4}\nRecipe_type: {5}".format(self.name, int(self.cooking_lvl), int(self.cooking_time),', '.join(self.ingredients), self.description, self.recipe_type)
