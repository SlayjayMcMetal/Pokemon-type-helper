
def get_not_very_effective_types(t):
    not_very_effective_types = []
    if t == "steel":
        not_very_effective_types.append("ice")
        not_very_effective_types.append("steel")
        not_very_effective_types.append("rock")
        not_very_effective_types.append("electric")
        not_very_effective_types.append("poison")
        not_very_effective_types.append("grass")
        not_very_effective_types.append("bug")
        not_very_effective_types.append("normal")
        not_very_effective_types.append("psychic")
        not_very_effective_types.append("flying")
        not_very_effective_types.append("dragon")
    elif t == "flying":
        not_very_effective_types.append("fighting")
        not_very_effective_types.append("grass")
        not_very_effective_types.append("bug")

    return not_very_effective_types

def get_super_effective_types(t):
    super_effective_types = []
    if t == "fire":
        super_effective_types.append("water")
        super_effective_types.append("ground")
        super_effective_types.append("rock")
    elif t == "water":
        super_effective_types.append("electric")
        super_effective_types.append("grass")
    elif t == "grass":
        super_effective_types.append("fire")
        super_effective_types.append("bug")
        super_effective_types.append("flying")
    elif t == "flying":
        super_effective_types.append("rock")
        super_effective_types.append("electric")
        super_effective_types.append("ice")
    elif t == "fighting":
        super_effective_types.append("flying")
        super_effective_types.append("psychic")
    elif t == "normal":
        super_effective_types.append("fighting")
    elif t == "poison":
        super_effective_types.append("ground")
        super_effective_types.append("psychic")
    elif t == "electric":
        super_effective_types.append("ground")
    elif t == "ground":
        super_effective_types.append("water")
        super_effective_types.append("ice")
        super_effective_types.append("grass")
    elif t == "psychic":
        super_effective_types.append("dark")
        super_effective_types.append("bug")
        super_effective_types.append("ghost")
    elif t == "rock":
        super_effective_types.append("water")
        super_effective_types.append("fighting")
        super_effective_types.append("grass")
        super_effective_types.append("ground")
        super_effective_types.append("steel")
    elif t == "ice":
        super_effective_types.append("fire")
        super_effective_types.append("fighting")
        super_effective_types.append("rock")
        super_effective_types.append("steel")
    elif t == "bug":
        super_effective_types.append("fire")
        super_effective_types.append("rock")
        super_effective_types.append("flying")
    elif t == "dragon":
        super_effective_types.append("dragon")
        super_effective_types.append("ice")
    elif t == "ghost":
        super_effective_types.append("ghost")
        super_effective_types.append("dark")
    elif t == "dark":
        super_effective_types.append("fighting")
    elif t == "steel":
        super_effective_types.append("fighting")
        super_effective_types.append("fire")
        super_effective_types.append("ground")


#to do: finish all this

    return super_effective_types

user_exit = False
while not user_exit:
    print ("What type is the enemy Pokemon?")
    enemy_type = input("")
    first_type_super_effective_types = get_super_effective_types(enemy_type)
    print ("Does the enemy Pokemon have second type?")
    yes_no = input("")
    if yes_no == "yes":
        print ("What is the second type?")
        second_type = input("")
        second_type_super_effective_types = get_super_effective_types(second_type)

        first_type_resists = get_not_very_effective_types(enemy_type)
        second_type_resists = get_not_very_effective_types(second_type)


        super_effective_types = []
        quad_effective_types = []
        for t in first_type_super_effective_types:
            if t in second_type_super_effective_types:
                quad_effective_types.append(t)
            elif t not in second_type_resists:
                super_effective_types.append(t)
        for t in second_type_super_effective_types:
            if t not in super_effective_types and t not in quad_effective_types and t not in first_type_resists:
                super_effective_types.append(t)



        print("These types are super effective")
        for t in super_effective_types:
            print(t)
        print("These types are quad effective")
        for t in quad_effective_types:
            print(t)



    else:
        print("You should use one of the following types")
        for t in first_type_super_effective_types:
            print (t)


    print("Would you like to exit the program?")
    yes_no = input("")
    if yes_no == "yes":
        user_exit = True
print("Bye Felicia!")
