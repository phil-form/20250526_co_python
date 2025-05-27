def get_int(text):
    val = None
    while val is None:
        try:
            val = int(input(text))
        except ValueError as e:
            print("You must enter an integer !")
            
    return val