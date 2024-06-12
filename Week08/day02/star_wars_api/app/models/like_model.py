
from app.config.mysqlconnection import connectToMySQL


class Like:
    db = "star_wars_cls"
    
    def __init__(self, data):
        self.id = data['id']
        self.people_id = data['people_id']
        self.user_id = data['user_id']

    
    @classmethod
    def add_like(cls, user_id, people_id):
        query = """
            INSERT INTO
                likes
                (people_id, user_id)
            VALUES
                (%(people_id)s, %(user_id)s)
        """
        
        result = connectToMySQL(cls.db).query_db(query, {
            "user_id": user_id,
            "people_id": people_id
        })
        return result
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT *
            FROM likes
        """

        return connectToMySQL(cls.db).query_db(query)
    
    @classmethod
    def get_likes_for_character(cls, people_id):
        query = """
            SELECT *
            FROM likes
            WHERE people_id = %(people_id)s
        """
        return connectToMySQL(cls.db).query_db(query, {"people_id": people_id})
        
