from app.config.mysqlconnection import connectToMySQL
from  app.models.user_model import User

class Recipies:
    
    dB = 'recipies_exam'
    
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instruction=data['instruction']
        # self.likes=[]
        # self.num_likes = data['num_likes']
        self.poster=None
        
        if'users.id' in data:
            self.poster= User({
                'id':data['users.id'],
                'first_name':data['first_name'],
                'last_name':data['last_name'],
                'email_address':data['email_address'],
                'password':data['password']
            })
        
    @classmethod
    def create_recipie(cls, data):
        query = """
        INSERT INTO recipies (name, description, instruction, user_id)
        VALUES (%(name)s, %(description)s, %(instruction)s, %(user_id)s)
        """
        return connectToMySQL(cls.dB).query_db(query, data)

    @classmethod
    def update_recipie(cls, data):
        query = """
        UPDATE recipies
        SET name = %(name)s, description = %(description)s, instruction = %(instruction)s
        WHERE id = %(id)s
        """
        return connectToMySQL(cls.dB).query_db(query, data)

    @classmethod
    def delete_recipie(cls, id):
        query = "DELETE FROM recipies WHERE id = %(id)s"
        return connectToMySQL(cls.dB).query_db(query, {'id': id})

    @classmethod
    def get_one_recipie(cls, id):
        query = "SELECT * FROM recipies WHERE id = %(id)s"
        results = connectToMySQL(cls.dB).query_db(query, {'id': id})
        if not results:
            return None
        return cls(results[0])

    @classmethod
    def get_all_recipies(cls):
        query = "SELECT * FROM recipies"
        try:
            results = connectToMySQL(cls.dB).query_db(query)
            if results is False:  # If the query fails, results will be False
                return []
            recipies = []
            for row in results:
                recipies.append(cls(row))
            return recipies
        except Exception as e:
            print(f"!!!!!!!!!!!!!Something went wrong!!!!!!!!!!!!!!!!!!!!!! {str(e)}")
            return []