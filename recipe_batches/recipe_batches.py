#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches_per = []
    for item in recipe:
        batches_per.append(int(ingredients.get(item, 0)/recipe[item]))
    return min(batches_per)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))