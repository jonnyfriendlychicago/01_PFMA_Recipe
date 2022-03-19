from flaskApp import app

from flaskApp.controllers import recipe_ctrl, user_ctrl

if __name__ == "__main__": 
    app.run(debug = True)