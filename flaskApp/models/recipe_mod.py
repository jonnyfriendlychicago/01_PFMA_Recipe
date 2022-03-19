from flaskApp.config.mysqlconnection import connectToMySQL

class Recipe_cls: 
    db = 'recipe_sch' # here, we are creating a reliable variable 'db' so that when we inevitably change the name of the db we are referencing, we only need to change this line to reflect that. 

    def __init__(self, data): 
        self.id = data['id']
        self.recipeName = data['recipeName']
        self.under30min = data['under30min']
        self.recipeDesc = data['recipeDesc']
        self.recipeInst = data['recipeInst']
        self.dateMade = data['dateMade']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
        self.user_id = data['user_id']

    @classmethod
    def get_allRecipe(cls):
        q = 'select * from recipe;'
        result = connectToMySQL(cls.db).query_db(q)
        recipeList = []
        for row in result: 
            recipeList.append(cls(row))
        return recipeList

    @classmethod
    def saveRecipe(cls, data):
        q = 'insert into recipe (recipeName, recipeDesc, recipeInst, under30min, user_id, dateMade, createdAt, updatedAt) values ( %(recipeName)s, %(recipeDesc)s, %(recipeInst)s, %(under30min)s , %(user_id)s, %(dateMade)s, NOW(), NOW() );'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def get_oneRecipe(cls, data):
        q = 'select * from recipe where id = %(recipe_id)s;'
        result = connectToMySQL(cls.db).query_db(q, data)
        if len(result) <1:
            return False
        return cls(result[0])

    @classmethod
    def updateRecipe (cls, data):
        q = 'update recipe set recipeName = %(recipeName)s, recipeDesc = %(recipeDesc)s, recipeInst = %(recipeInst)s, under30min = %(under30min)s, updatedAt = NOW() where id = %(recipe_id)s;'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def deleteRecipe (cls, data):
        q = 'delete from recipe where id = %(recipe_id)s;'
        return connectToMySQL(cls.db).query_db(q, data)

"""





    

    @classmethod
    def get_oneAirlineAllFlight(cls, data):
        q = 'select * from airline a left join flight f on a.id = f.airline_id where a.id = %(id)s;'
        result = connectToMySQL(cls.db).query_db(q, data)
        # print('something??')
        airlineX = cls(result[0])
        for row in result: 
            airlineFlightDataDict = {
                'id': row['flight.id'],
                'flightNumber': row['flightNumber'],
                'departureAirport': row['departureAirport'],
                'arrivalAirport': row['arrivalAirport'],
                'createdAt': row['createdAt'],
                'updatedAt': row['updatedAt'],
                'airline_id': row['airline_id']
            }
            
            airlineX.airlineAllFlightList.append(flight_mod.Flight_cls(airlineFlightDataDict))
            # print("printing the lst form models: ", Airline_cls.flight)
        return airlineX

"""