from app.config.mysqlconnection import connectToMySQL

class Chores:
    
    dB = 'chore_track'
    
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.description=data['description']
        self.location=data['location']
        
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