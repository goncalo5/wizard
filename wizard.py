animals = {
    "bird": {"fly", "vertebrate"},
    "ant": {},
    "leon": {"vertebrate", "carnivorous"},
    "elephant": {"vertebrate"},
    "fly": {"fly"}
    }

# print animals


def make_new_dict(animal_dict, characteristic, positve=True):
    new_dict = {}
    for animal in animal_dict:
        # print animal
        if characteristic in animal_dict[animal] and positve:
            new_dict[animal] = animal_dict[animal]
        elif characteristic not in animal_dict[animal] and not positve:
            new_dict[animal] = animal_dict[animal]
    return new_dict


def fetch_all_characteristic():
    all_characteristic = set()
    for animal_characteristic in animals.values():
        # print animal_characteristic
        all_characteristic = all_characteristic.union(animal_characteristic)
    return all_characteristic


def convert_answer_to_bolean(answer):
    if answer == "y":
        return True
    elif answer == "n":
        return False


def run():
    global animals
    all_characteristic = fetch_all_characteristic()
    for characteristic in all_characteristic:
        question = "{} ? ".format(characteristic)
        answer = raw_input(question).lower()
        while answer not in ["y", "n"]:
            print "\nplease insert [y]es or [n]o"
            answer = raw_input(question)
        animals = make_new_dict(animals, characteristic, convert_answer_to_bolean(answer))
        # print animals
        if len(animals) < 2:
            break
    print animals.keys()
# print make_new_dict("fly", False)

run()
