
def get_data():
    data = []

    data_file = open("data.txt")

    for val in data_file:
        ingredients, allergens = val.split("(")
        ingredients = ingredients.strip().split(" ")
        allergens = allergens.strip()[9:-1].split(', ')
        data.append((ingredients, allergens))
    data_file.close()

    print(f"read {len(data)} lines\n")

    return data


def check_data(data):

    # loop over all items, track all the individual ingredents and
    # their potetial allergens
    ingredients_xref = {}
    ingredient_count = {}
    allergiens_xref = {}
    for item in data:
        for ingredient in item[0]:
            if ingredient in ingredient_count:
                ingredient_count[ingredient] += 1
            else:
                ingredient_count[ingredient] = 1

        for allergen in item[1]:
            if allergen not in allergiens_xref:
                allergiens_xref[allergen] = set(item[0])
                # add potential allergen to each item
                for ing in item[0]:
                    if ing in ingredients_xref:
                        ingredients_xref[ing].append(allergen)
                    else:
                        ingredients_xref[ing] = [allergen]
            else:
                # try to solve.
                for ingredient in item[0]:
                    if ingredient in allergiens_xref[allergen] and allergen in ingredients_xref[ingredient]:
                        # found match
                        ingredients_xref[ingredient] = [allergen]
                        print(ingredient, "has alergen ", allergen)
                        # prune this allergen off the rest.
                        for ing in allergiens_xref[allergen]:
                            if ing != ingredient and allergen in ingredients_xref[ing]:
                                ingredients_xref[ing].remove(allergen)
                    else:
                        if ingredient not in ingredients_xref:
                            ingredients_xref[ingredient] = []
                # allergiens_xref[allergen].update(item[0])

        # print(ingredients_xref)

    final_count = 0
    for ingredient in ingredients_xref:
        if len(ingredients_xref[ingredient]) == 0:
            print("ING: ", ingredient, " COUNT: ",
                  ingredient_count[ingredient])
            final_count += ingredient_count[ingredient]

    print(final_count)

    return None


def main():
    data = get_data()
    check_data(data)


main()
