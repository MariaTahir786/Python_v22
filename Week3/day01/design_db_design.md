#Users
    columns
        id
        first_name -->varchar
        last_name   -->varchar
        email_address -->varchar
        Address     -->mediumint
        city  -->varchar
        State -->varchar
        password --> password
        created_at
        updated_at

 #Orders

    columns
        id
        size
        crust
        created_at
        updated_at
        -user_id(1:many users:orders FK=foreign key)

#pizzas
    columns
        id
        method -->varchar
        size -->int
        crust  -->varchar
        quantity -->int
        toppings(many to many)
        created_at
        updated_at

#toppings
    _id
    _name: varchar
    _blah bla_
pizza_topping
        _pizza_id
        _topping_id