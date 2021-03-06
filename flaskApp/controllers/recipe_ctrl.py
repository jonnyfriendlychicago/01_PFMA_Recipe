from flaskApp import app
from flask import Flask, render_template, redirect, session, request, flash
from flaskApp.models import user_mod 
from flaskApp.models import recipe_mod


# below existed originally, but we whacked it b/c now index is gonna be the register/login screen (right?)
# @app.route('/')
# def index():
#     return redirect ('/airlines')


@app.route('/recipe/add/')
def addRecipe():
    if 'user_id' not in session: 
        flash("You must be logged in to access this site.")
        return redirect('/')
    data = {
        "user_id": session['user_id']
    }
    return render_template(
        'recipeAdd.html' , 
        dsp_get_oneUser = user_mod.User_cls.get_oneUser(data) 
    )

@app.route('/recipe/create/', methods = ['POST'])
def createRecipe():
    data = {
        'user_id': session['user_id']
        , 'recipeName': request.form['recipeName']
        , 'recipeDesc': request.form['recipeDesc']
        , 'recipeInst': request.form['recipeInst']
        , 'under30min': request.form['under30min']
        , 'dateMade': request.form['dateMade']
    }
    recipe_mod.Recipe_cls.saveRecipe(data)
    return redirect('/dashboard/')


@app.route('/recipe/<int:recipe_id>/')
def viewRecipe(recipe_id): 
    if 'user_id' not in session: # this whole user_Id check needs to happen on every page that should be requiring a successful login
        flash("You must be logged in to access this site.")
        return redirect('/')
    data = {
        "user_id": session['user_id']
        , 'recipe_id': recipe_id
    }
    return render_template(
        'recipeView.html'
        , dsp_get_oneUser = user_mod.User_cls.get_oneUser(data) 
        , dsp_get_oneRecipe = recipe_mod.Recipe_cls.get_oneRecipe(data)   
    )

# @app.route('/recipe/<int:recipe_id>/edit/')
# def editRecipe(recipe_id): 
#     if 'user_id' not in session: 
#         flash("You must be logged in to access this site.")
#         return redirect('/')
#     data = {
#         'user_id': session['user_id']
#         , 'recipe_id': recipe_id
        
#     }
#     return render_template(
#         'recipeEdit.html' 
#         , dsp_get_oneUser = user_mod.User_cls.get_oneUser(data)
#         , dsp_get_oneRecipe = recipe_mod.Recipe_cls.get_oneRecipe(data)
#     )

@app.route('/recipe/<int:recipe_id>/edit/')
def editRecipe(recipe_id): 
    if 'user_id' not in session: 
        flash("You must be logged in to access this site.")
        return redirect('/')
    data = {
        'user_id': session['user_id']
        , 'recipe_id': recipe_id
        
    }
    get_oneRecipe = recipe_mod.Recipe_cls.get_oneRecipe(data)
    if session['user_id'] != get_oneRecipe.user_id:
        flash("You must be the creator of a recipe to edit the recipe.")
        return redirect('/')
    else: 
        return render_template(
        'recipeEdit.html' 
        , dsp_get_oneUser = user_mod.User_cls.get_oneUser(data)
        , dsp_get_oneRecipe = get_oneRecipe
    )

@app.route('/recipe/<int:recipe_id>/update/', methods=['POST'])
def updateRecipe(recipe_id): 
    data = {
        'user_id': session['user_id']
        , 'recipe_id': recipe_id
        , 'recipeName': request.form['recipeName']
        , 'recipeDesc': request.form['recipeDesc']
        , 'recipeInst': request.form['recipeInst']
        , 'under30min': request.form['under30min']
        , 'dateMade': request.form['dateMade']
    }
    print(request.form['recipeDesc'])
    updateRecipe = recipe_mod.Recipe_cls.updateRecipe(data)
    return redirect(f'/recipe/{recipe_id}/')

@app.route('/recipe/<int:recipe_id>/delete/')
def deleteRecipe(recipe_id): 
    if 'user_id' not in session: 
        flash("You must be logged in to access this site.")
        return redirect('/')
    data = {
        'user_id': session['user_id']
        , 'recipe_id': recipe_id
    }
    get_oneRecipe = recipe_mod.Recipe_cls.get_oneRecipe(data)
    if session['user_id'] != get_oneRecipe.user_id:
        flash("You must be the creator of a recipe to delete it.")
        return redirect('/dashboard/')
    else: 
        recipe_mod.Recipe_cls.deleteRecipe(data)
        flash("Recipe deleted.  POOF!  GONE!")
        return redirect ('/dashboard/')


"""
@app.route('/airlines/')
def airlineHome():
    if 'user_id' not in session: # this whole user_Id check needs to happen on every page that should be requiring a successful login
        flash("You must be logged in to view this page.")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template(
        'airlines.html'
        , display_get_allAirline = Airline_cls.get_allAirline()
        , display_get_oneUser = user_mod.User_cls.get_oneUser(data) 
    )












@app.route('/airlines/')
def airlineHome():
    if 'user_id' not in session: # this whole user_Id check needs to happen on every page that should be requiring a successful login
        flash("You must be logged in to view this page.")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template(
        'airlines.html'
        , display_get_allAirline = Airline_cls.get_allAirline()
        , display_get_oneUser = user_mod.User_cls.get_oneUser(data) 
    )







"""