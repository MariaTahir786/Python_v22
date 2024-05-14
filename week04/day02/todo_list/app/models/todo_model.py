from app.config.mysqlconnection import connectToMySQL


class Todo:
    dB = 'todos_app'

    #constructor
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
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
            (text, description)
            VALUES
            (%(text)s, %(description)s)
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