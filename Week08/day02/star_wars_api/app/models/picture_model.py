from app.config.mysqlconnection import connectToMySQL


class Picture:
    db = "star_wars_cls"
    
    def __init__(self, data):
        self.id = data['id']
        self.image_name = data.get('image_name',None)
    
    @classmethod
    def upload_image(cls,image_name):
        query="""
            insert into
            pictures
            (image_name)
            values
            (%(image_name)s)
        
        
        """
        return connectToMySQL(cls.db).query_db(query,image_name)
    
    @classmethod
    def get_all_images(cls):
        query="""
            select image_name
            from pictures
        """
        return connectToMySQL(cls.db).query_db(query)