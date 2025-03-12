def greet(name): 
    capitalized_name = name[0].upper() + name[1:].lower()
    text = "Hello " + capitalized_name + "!"
    return text