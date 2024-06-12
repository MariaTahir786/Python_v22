from app.config.mysqlconnection import connectToMySQL
from  app.models.user_model import User

class Sightings:
    
    dB = 'sas_sighting'
    
    def __init__(self,data):
        self.id=data['id']
        self.location=data['location']
        self.what_happened=data['what_happened']
        self.num_sasquatches = data['num_sasquatches']
        self.user_id = data.get('user_id')
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
        self.created_at=data.get('created_at','')
        self.sasquatches=[]
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
    def get_one_sighting(cls, id):
        query = """
        SELECT sightings.*, users.first_name, users.last_name,users.created_at,
            (
                SELECT count(*) 
                FROM sas_sighting.sightings_has_users 
                WHERE sighting_id = sightings.id
            ) as num_sasquatches
        FROM sightings
        LEFT JOIN users ON sightings.user_id = users.id
        WHERE sightings.id = %(id)s
        """
        results = connectToMySQL(cls.dB).query_db(query, {'id': id})
        return cls(results[0]) if results else None
    
    @classmethod
    def get_all_sightings(cls):
        query = """
            SELECT sightings.*, users.first_name, users.last_name,users.created_at,
                (
                    SELECT count(*) 
                    FROM sas_sighting.sightings_has_users 
                    WHERE sighting_id = sightings.id
                ) as num_sasquatches
            FROM sightings
            LEFT JOIN users ON sightings.user_id = users.id
    """
        return [cls(data) for data in connectToMySQL(cls.dB).query_db(query)]

    
    # @classmethod
    # def get_all_sightings(cls):
    #     query="""
    #             SELECT *, 
    #                 (
    #                     SELECT count(*) 
    #                     FROM sas_sighting.sightings_has_users
    #                     WHERE sighting_id = sightings.id
    #                 ) as num_sasquatches
    #             from sightings
    #             left join users on users.id=sightings.user_id
    #         """
    #     # results =connectToMySQL(cls.dB).query_db(query)
        
    #     # chores=[]
    #     # for result in results:
    #     #     chores.append(cls(results))
        
    #     return [cls(data) for data in connectToMySQL(cls.dB).query_db(query)]
        # =============================================================
        # start from here Maria
        # =========================================
    @classmethod
    def create_sighting(cls, data):
        query = """
        INSERT INTO sightings
        (location, what_happened, user_id)
        VALUES
        (%(location)s, %(what_happened)s, %(user_id)s)
        """
        return connectToMySQL(cls.dB).query_db(query, data)

    
    @classmethod
    def update_sighting(cls,data):
        query="""
        update sightings
        set location=%(location)s, what_happened=%(what_happened)s
        Where id=%(id)s
        """
        return connectToMySQL(cls.dB).query_db(query,data)
    
    @classmethod
    def delete_sighting(cls,id):
        query="""
        
        delete 
        from sightings
        where id=%(id)s
        """
        return connectToMySQL(cls.dB).query_db(query,{'id':id})
    
    
# many to many 
    @classmethod
    def get_one_with_sasquatch(cls, id):
        query = """
        SELECT sightings.*, users.first_name, users.last_name,users.created_at,
            (
                SELECT count(*) 
                FROM sas_sighting.sightings_has_users 
                WHERE sighting_id = sightings.id
            ) as num_sasquatches
        FROM sightings
        LEFT JOIN sightings_has_users ON sightings.id = sightings_has_users.sighting_id
        LEFT JOIN users ON sightings_has_users.user_id = users.id
        WHERE sightings.id = %(id)s
        """
        results = connectToMySQL(cls.dB).query_db(query, {'id': id})
        if not results:
            return None
        
        sighting = cls(results[0])
        
        for row in results:
            if row['users.id']:
                sighting.sasquatches.append(User({
                    'id': row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email_address': row['email_address'],
                    'password': row['password']
                }))
        return sighting
    # @classmethod
    # def get_one_with_sasquatch(cls,id):
    #     query="""
    #         SELECT *, 
    #                 (
    #                     SELECT count(*) 
    #                     FROM sas_sighting.sightings_has_users
    #                     WHERE sighting_id = sightings.id
    #                 ) as num_sasquatches
    #         FROM sightings   
    #         left join sightings_has_users on sightings.id=sightings_has_users.sighting_id
    #         left join users on sightings_has_users.user_id=users.id
    #         where sightings.id=%(id)s
    #     """
    #     results =connectToMySQL(cls.dB).query_db(query,{'id':id})
    #     if not results:
    #         return None
            
    #     sighting=cls(results[0])
            
    #     for row in results:
    #         if row['users.id']:
    #             sighting.sasquatches.append(User({
    #                 'id':row['users.id'],
    #                 'first_name':row['first_name'],
    #                 'last_name':row['last_name'],
    #                 'email_address':row['email_address'],
    #                 'password':row['password']
                    
    #             }))
    #         return sighting
            
    @classmethod
    def add_saquatch(cls, sighting_id, user_id):
        query = """
            INSERT INTO sightings_has_users
            (sighting_id, user_id)
            VALUES
            (%(sighting_id)s, %(user_id)s)
        """
        return  connectToMySQL(cls.dB).query_db(query, {"sighting_id": sighting_id, "user_id": user_id})