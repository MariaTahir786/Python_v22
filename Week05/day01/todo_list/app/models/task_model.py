from app.config.mysqlconnection import connectToMySQL

class TaskModel:
    
    dB = 'registeration_db_cls'
    def __init__(self, data):
        self.id=data['id']
        self.description=data['description']
        
    @classmethod
    def create_task(cls,description,todo_id):
        query="""
            insert into 
            tasks
            (description,todo_id)
            values
            (%(description)s,%(todo_id)s)
        """
        data={'description': description,'todo_id':todo_id}
        return connectToMySQL(cls.dB).query_db(query, data)
        