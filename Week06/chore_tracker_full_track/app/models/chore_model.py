from app.config.mysqlconnection import connectToMySQL
from  app.models.user_model import User

class Chores:
    
    dB = 'chore_track'
    
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.description=data['description']
        self.location=data['location']
        
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
    def get_one_chore(cls,id):
        query ="""
                select *
                from chores
                where chores.id=%(id)s
        
        """
        
        results =connectToMySQL(cls.dB).query_db(query,{'id':id})
        
        #checking to make sure something was loaded
        # if not results:
        #     return None
        return cls(results[0]) if results else None
    
    @classmethod
    def get_all_chores(cls):
        query="""
        select * 
        from chores
        left join users on users.id=chores.user_id
        """
        # results =connectToMySQL(cls.dB).query_db(query)
        
        # chores=[]
        # for result in results:
        #     chores.append(cls(results))
        
        return [cls(data) for data in connectToMySQL(cls.dB).query_db(query)]
        
    @classmethod
    def create_chore(cls,data):
        query="""
        insert into chores
        (title,description,location,user_id)
        values
        (%(title)s,%(description)s,%(location)s,%(user_id)s)
            """
        return connectToMySQL(cls.dB).query_db(query,data)
    
    @classmethod
    def update_chore(cls,data):
        query="""
        update chores
        set title=%(title)s, description=%(description)s, location=%(location)s
        Where id=%(id)s
        """
        return connectToMySQL(cls.dB).query_db(query,data)
    
    @classmethod
    def delete_chore(cls,id):
        query="""
        
        delete 
        from chores
        where id=%(id)s
        """
        return connectToMySQL(cls.dB).query_db(query,{'id':id})