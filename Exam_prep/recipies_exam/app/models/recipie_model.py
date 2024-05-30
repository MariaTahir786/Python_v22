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
    def get_one_recipie(cls,id):
        query ="""
                SELECT *
                # , 
                    # (
                    #     SELECT count(*) 
                    #     FROM recipies_exam.recipies_has_likes
                    #     WHERE recipie_id = recipies.id
                    # ) as num_likes
                from recipies
                where recipies.id=%(id)s
        
            """
        
        results =connectToMySQL(cls.dB).query_db(query,{'id':id})
        
        #checking to make sure something was loaded
        # if not results:
        #     return None
        return cls(results[0]) if results else None
    
    @classmethod
    def get_all_recipies(cls):
        query="""
                SELECT *
                from recipies
                left join users on users.id=recipies.user_id
            """
        # results =connectToMySQL(cls.dB).query_db(query)
        
        # chores=[]
        # for result in results:
        #     chores.append(cls(results))
        
        return [cls(data) for data in connectToMySQL(cls.dB).query_db(query)]
        
    @classmethod
    def create_recipie(cls,data):
        query="""
        insert into recipies
        (name,description,instruction,user_id)
        values
        (%(name)s,%(description)s,%(instruction)s,%(user_id)s)
            """
        return connectToMySQL(cls.dB).query_db(query,data)
    
    @classmethod
    def update_recipie(cls,data):
        query="""
        update recipies
        set name=%(name)s, description=%(description)s, instruction=%(instruction)s
        Where id=%(id)s
        """
        return connectToMySQL(cls.dB).query_db(query,data)
    
    @classmethod
    def delete_recipie(cls,id):
        query="""
        
        delete 
        from recipies
        where id=%(id)s
        """
        return connectToMySQL(cls.dB).query_db(query,{'id':id})
    
    
# many to many 
    # # @classmethod
    # # def get_one_with_likes(cls,id):
    #     query="""
    #         SELECT *, 
    #                 (
    #                     SELECT count(*) 
    #                     FROM recipie_track.recipies_has_likes
    #                     WHERE recipie_id = recipies.id
    #                 ) as num_likes
    #         FROM recipies   
    #         left join recipies_has_likes on recipies.id=recipies_has_likes.recipie_id
    #         left join users on recipies_has_likes.user_id=users.id
    #         where recipies.id=%(id)s
    #     """
    #     results =connectToMySQL(cls.dB).query_db(query,{'id':id})
    #     if not results:
    #         return None
            
    #     recipie=cls(results[0])
            
    #     for row in results:
    #         if row['users.id']:
    #             recipie.likes.append(User({
    #                 'id':row['users.id'],
    #                 'first_name':row['first_name'],
    #                 'last_name':row['last_name'],
    #                 'email_address':row['email_address'],
    #                 'password':row['password']
                    
    #             }))
    #         return recipie
            
    # @classmethod
    # def add_like(cls, recipie_id, user_id):
    #     query = """
    #         INSERT INTO recipies_has_likes
    #         (recipie_id, user_id)
    #         VALUES
    #         (%(recipie_id)s, %(user_id)s)
    #     """
    #     return  connectToMySQL(cls.dB).query_db(query, {"recipie_id": recipie_id, "user_id": user_id})