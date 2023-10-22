from flask import request
from flask_restx import Namespace, Resource, fields
from models import db
from models.recipe import Recipe

from . import recipe_ns

recipe_ns = Namespace("recipe", description="A namespace for Recipes")

recipe_input_model = recipe_ns.model(
    "RecipeInput",
    {"title": fields.String(), "description": fields.String()},
)

recipe_model = recipe_ns.model(
    "Recipe",
    {"id": fields.Integer(), "title": fields.String(), "description": fields.String()},
)


@recipe_ns.route("/recipes")
class RecipesResource(Resource):
    @recipe_ns.marshal_list_with(recipe_model)
    def get(self):
        """Get all recipes"""
        recipes = Recipe.query.all()

        return recipes

    @recipe_ns.expect(recipe_input_model)
    @recipe_ns.marshal_with(recipe_model)
    def post(self):
        """Create new recipe"""
        data = request.get_json()
        new_recipe = Recipe(
            title=data.get("title"), description=data.get("description")
        )
        db.session.add(new_recipe)
        db.session.commit()
        return new_recipe, 201
