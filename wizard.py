#!/usr/bin/env python
import json


SETTING_FILE_NAME = "settings.json"
ANIMALS_FILE_NAME = "animals.json"

ANSWERS = {
    "en": {"yes": 1, "y": 1, "no": 0, "n": 0, "pass": 2, "p": 2},
    "pt": {"sim": 1, "s": 1, "nao": 0, "n": 0, "passar": 2, "p": 2}
}

ANSWERS_TO_PRINT = {
    "en": "(y)es   (n)o   (p)ass",
    "pt": "(s)im   (n)ao   (p)assar"
}

characteristics = {
    "en": ["fly", "vertebrate", "insect", "carnivorous"],
    "pt": ["voa", "vertebrado"]}#, "inseto", "carnivoro"])}

animals = {
    "bird": {"fly", "vertebrate"},
    "ant": {"insect"},
    "lion": {"vertebrate", "carnivorous"},
    "elephant": {"vertebrate"},
    "fly": {"fly"}
    }


class Settings(object):
    def __init__(self, settings_dict):
        # convert dictionary to object
        try:
            self.language = settings_dict["language"]
        except KeyError:
            # language not yet was chosen
            self.choose_the_language()

    def choose_the_language(self):
        for language in characteristics:
            print language,
        self.language = raw_input("\nlanguage ?  ")

    def change_language(self):
        new_language = raw_input("")


class FileHandler(object):
    def __init__(self):
        self.settings_file_name = SETTING_FILE_NAME
        self.animals_file_name = ANIMALS_FILE_NAME

    def import_all_json_files(self):
        settings = self.try_open_json_file(self.settings_file_name)
        animals = self.try_open_json_file(self.animals_file_name)
        return settings, animals

    def try_open_json_file(self, json_file_name):
        try:
            print "try open the json file ..."
            content = self.open_json_file(json_file_name)
            print "json file %s open with sucess" % json_file_name
        except IOError:
            content = self.create_a_new_file_from_scrath(json_file_name)
        return content

    def open_json_file(self, json_file_name):
        f = open(json_file_name, "r")
        d = json.load(f)
        return d

    def create_a_new_file_from_scrath(self, json_file_name):
        print "\ncreate a new file from scrath"
        content = {}
        self.save_json_file(json_file_name, content)
        return content

    def save_json_file(self, json_file_name, content):
        print "saving %s ..." % json_file_name
        f = open(json_file_name, "w")
        json.dump(content, f)
        print "%s saved" % json_file_name


class Animals(object):
    def __init__(self, settings, animals_dict):
        self.language = settings.language
        try:
            a = animals_dict[self.language]
        except KeyError:
            a = {self.language: {}}
        self.dict = animals_dict
        # print 4, self.dict
        self.characteristics = characteristics[self.language]

        print self.dict
        while len(self.dict) < 2:
            msg = {
                "en": "there are less than 2 animals, please insert some animal",
                "pt": "ha menos de 2 animais, por favor insere um animal"}
            print msg[self.language]
            self.add_animal()
            # print 5, self.dict

    def add_animal(self):
        input_msg = {
            "en": "what is the name of the animal?  ",
            "pt": "qual e o nome do animal?  "}
        new_animal_name = raw_input(input_msg[self.language])
        # print 8, new_animal_name
        characteristics_of_new_animal = []
        for characteristic in self.characteristics:
            print characteristic
            input_msg_all_languages = {
                "en": "this animal have that characteristic",
                "pt": "esse animal tem essa caracteristica"}
            input_msg = "%s (%s) ?  " % (input_msg_all_languages[self.language], ANSWERS_TO_PRINT[self.language])
            while True:
                answer = raw_input(input_msg)
                if answer not in ANSWERS[self.language]:
                    msg = {
                        "en": "there are less than 2 animals in that language, please insert some animal",
                        "pt": "nao percebi essa resposta, por favor insere "}
                    continuo
                break
            if ANSWERS[self.language][answer] == 1:
                characteristics_of_new_animal.append(characteristic)
        # print 6, self.dict, 9, new_animal_name, 10, characteristics_of_new_animal
        self.dict[new_animal_name] = characteristics_of_new_animal
        # print 7, self.dict

    def add_characteristic(animal_name, characteristics):
        try:
            self.dict[animal_name].update(characteristics)
        except TypeError:
            self.dict[animal_name].update([characteristics])

    def change_language(self, new_language):
        pass

    def make_new_dict(self, animal_dict, characteristic, positve=True):
        new_dict = {}
        for animal in animal_dict:
            # print 1, animal
            if characteristic in animal_dict[animal] and positve:
                new_dict[animal] = animal_dict[animal]
            elif characteristic not in animal_dict[animal] and not positve:
                new_dict[animal] = animal_dict[animal]
        return new_dict

    def fetch_all_characteristic(self, animals):
        all_characteristic = set()
        for animal_characteristic in animals.values():
            # print animal_characteristic
            all_characteristic = all_characteristic.union(animal_characteristic)
        return all_characteristic


class Run(object):
    def __init__(self):

        f = FileHandler()
        settings_dict, animals_dict = f.import_all_json_files()

        self.settings = Settings(settings_dict)
        f.save_json_file(SETTING_FILE_NAME, self.settings.__dict__)

        self.animals = Animals(self.settings, animals_dict)
        print self.animals, self.animals.characteristics

        for characteristic in self.animals.characteristics:
            question = "{} ? ".format(characteristic)
            answer = raw_input(question).lower()
            while answer not in ["y", "n"]:
                print "\nplease insert [y]es or [n]o"
                answer = raw_input(question)
            answer = True if answer == "y" else False
            # print 3, self.animals.dict
            animals = self.animals.make_new_dict(self.animals.dict, characteristic, answer)
            # print 2, animals
            if len(animals) < 2:
                break
        print animals.keys()
        f.save_json_file(ANIMALS_FILE_NAME, self.animals.dict)


if __name__ == '__main__':
    Run()
