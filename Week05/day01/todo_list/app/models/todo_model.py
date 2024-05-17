from app.config.mysqlconnection import connectToMySQL
from app.models.task_model import TaskModel

class Todo:
    dB = 'registeration_db_cls'

    #constructor
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
        self.tasks=[]
        
    #! Read all 
    @classmethod
    def get_all_todos(cls):
        query = """
            SELECT
                *
            FROM
                todos
        """
        results = connectToMySQL(cls.dB).query_db(query)
        rows = []
        # each result is dictionary
        for result in results:
            rows.append(cls(result)) # instantiate Todo dictionary
            
        return rows
    
    #! Read single todo
    @classmethod
    def get_one_by_id(cls, id):
        query = """
            SELECT
                *
            FROM 
                todos
            WHERE
                id = %(id)s
        """
        
        return cls(connectToMySQL(cls.dB).query_db(query, {'id':id})[0])
    
    #! Read single todo
    @classmethod
    def get_one_by_id_1_to_many(cls,id):
        query="""
        select * 
        from todos
        left join tasks on tasks.todo_id= todos.id
        where todos.id= %(id)s
        """
        results= connectToMySQL(cls.dB).query_db(query, {'id':id})
        if results:
            #create instance of to do that we want to populate grabbing first line from results
            todo=cls(results[0])
            
            for result in results:
                #create instanec of task
                task=TaskModel({
                    'id':result['tasks.id'],
                    'description':result['tasks.description']
                })
                print(task)
                todo.tasks.append(task)
            return todo
        return False
    
    
    #! Update
    @classmethod
    def update_todo(cls, data):
        query = """
            UPDATE
                todos
            SET
                text = %(text)s,
                description= %(description)s
            WHERE
                id = %(id)s
        """
        
        return connectToMySQL(cls.dB).query_db(query, data)
    
    #! Create
    @classmethod
    def create_todo(cls, data):
        query = """
            INSERT INTO
                    todos
            (text, description,user_id)
            VALUES
            (%(text)s, %(description)s ,5)
        """
        return connectToMySQL(cls.dB).query_db(query, data)
    
    #! Delete
    @classmethod
    def delete_todo(cls, id):
        query = """
            DELETE 
            FROM
                todos
            WHERE 
                id = %(id)s
        """
        return connectToMySQL(cls.dB).query_db(query, {'id': id})