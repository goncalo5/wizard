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
    "pt": ["voador", "vertebrado"]}#, "inseto", "carnivoro"])}

animals = {
    "bird": {"fly": 1, "vertebrate": 1},
    "ant": {"insect": 1},
    "lion": {"vertebrate": 1, "carnivorous": 1},
    "elephant": {"vertebrate": 1},
    "fly": {"fly": 1}
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
            # print "try open the json file ..."
            content = self.open_json_file(json_file_name)
            # print "json file %s open with sucess" % json_file_name
        except IOError:
            content = self.create_a_new_file_from_scrath(json_file_name)
        return content

    def open_json_file(self, json_file_name):
        f = open(json_file_name, "r")
        d = json.load(f)
        return d

    def create_a_new_file_from_scrath(self, json_file_name):
        # print "\ncreate a new file from scrath"
        content = {}
        self.save_json_file(json_file_name, content)
        return content

    def save_json_file(self, json_file_name, content):
        # print "saving %s ..." % json_file_name
        f = open(json_file_name, "w")
        json.dump(content, f)
        # print "%s saved" % json_file_name


class CommonFunctions(object):
    @staticmethod
    def check_bool_answer(answer, language):
        if answer in ANSWERS[language]:
            res = ANSWERS[language][answer]
            return res  # return 0 or 1 or 2
        else:
            msg = {
                "en": "I don't get your answer, please insert",
                "pt": "nao percebi essa resposta, por favor insere"}
            print "%s %s" % (msg[language], ANSWERS_TO_PRINT[language])


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
        self.dict[new_animal_name] = {}
        input_msg = {
            "en": "please, insert some characteristic, the %s is?  " % new_animal_name,
            "pt": "por favor insere alguma caracteristica, o/a %s e'?  " % new_animal_name}
        self.fetch_all_characteristic()
        print self.characteristics
        if len(self.characteristics) < 1:
            new_characteristic_name = raw_input(input_msg[self.language])
            self.add_characteristic(new_animal_name, {new_characteristic_name: 1})
        else:
            for animal in self.dict:
                if self.dict[animal] == self.dict[new_animal_name]
        # print 8, new_animal_name

        # print 6, self.dict, 9, new_animal_name, 10, characteristics_of_new_animal

        print 7, self.dict

    def add_characteristic(self, animal_name, characteristics):
        print self.dict
        self.dict[animal_name].update(characteristics)

    def check_if_there_are_animals_with_same_characteristics(self):
        for animal in self.dict:


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

    def fetch_all_characteristic(self):
        self.characteristics = {}
        for animal in self.dict:
            for characteristic in self.dict[animal]:
                if characteristic not in self.characteristics:
                    self.characteristics[characteristic] = [0, 0]
                y_n = self.dict[animal][characteristic]
                self.characteristics[characteristic][y_n] += 1

    def choose_the_best_question(self):
        n = float(len(self.dict))
        # min_close2mid: 0 - 0.5
        # where 0 is the best which reduce 50% of the options and 0.5 is the worst which don't reduce nothing
        min_close2mid = 0.5
        for characteristic in self.characteristics:
            print 5, characteristic
            close2mid = min(abs(float(self.characteristics[characteristic][0]) / n), abs(float(self.characteristics[characteristic][1]) / n))
            if close2mid < min_close2mid:
                min_close2mid = close2mid
                self.best_question = characteristic


class Run(object):
    def __init__(self):

        f = FileHandler()
        settings_dict, animals_dict = f.import_all_json_files()

        self.settings = Settings(settings_dict)
        f.save_json_file(SETTING_FILE_NAME, self.settings.__dict__)

        self.animals = Animals(self.settings, animals_dict)
        print self.animals, self.animals.characteristics

        self.all_answers = {}
        animals_left = self.check_all_characteristics()
        if len(animals_left) == 1:
            print animals_left
            if self.check_if_is_the_animal() == 0:
                self.add_new_animal()
        elif len(animals_left) == 0:
            self.add_new_animal()
        f.save_json_file(ANIMALS_FILE_NAME, self.animals.dict)

    def check_all_characteristics(self):
        all_possible_animals = self.animals.dict.keys()
        for characteristic in self.animals.characteristics:
            input_msg_all_languages = {
                "en": "the animal have the characteristic %s?" % characteristic,
                "pt": "o animal e' %s?" % characteristic}
            input_msg = "%s (%s)   " % (input_msg_all_languages[self.settings.language], ANSWERS_TO_PRINT[self.settings.language])
            while True:
                answer = CommonFunctions.check_bool_answer(raw_input(input_msg), self.settings.language)
                if answer is not None:
                    self.all_answers[characteristic] = answer
                    break
            print self.all_answers

            print 3, self.animals.dict
            for animal in self.animals.dict:
                if animal not in all_possible_animals:
                    continue
                print 4, animal, all_possible_animals
                if self.animals.dict[animal][characteristic] != answer:
                    all_possible_animals.remove(animal)
                if len(all_possible_animals) < 2:
                    return all_possible_animals
        return all_possible_animals

    def check_if_is_the_animal(self):
        input_msg_all_languages = {
            "en": "was this the animal you were thinking?",
            "pt": "era esse o animal que estavas a pensar?"}
        input_msg = "%s (%s)   " % (input_msg_all_languages[self.settings.language], ANSWERS_TO_PRINT[self.settings.language])
        while True:
            answer = CommonFunctions.check_bool_answer(raw_input(input_msg), self.settings.language)
            if answer is not None:
                return answer

    def add_new_animal(self):
        input_msg_all_languages = {
            "en": "what is the animal you were thinking?",
            "pt": "qual era o animal que estavas a pensar?"}
        input_msg = "%s   " % (input_msg_all_languages[self.settings.language])
        name_of_the_new_animal = raw_input(input_msg)
        for characteristic in self.animals.characteristics:
            if characteristic not in self.all_answers:
                input_msg_all_languages = {
                    "en": "the animal have the characteristic %s?" % characteristic,
                    "pt": "o animal e' %s?" % characteristic}
                input_msg = "%s (%s)   " % (input_msg_all_languages[self.settings.language], ANSWERS_TO_PRINT[self.settings.language])
                while True:
                    answer = CommonFunctions.check_bool_answer(raw_input(input_msg), self.settings.language)
                    if answer is not None:
                        self.all_answers[characteristic] = answer
                        break
                print self.all_answers
        self.animals.dict[name_of_the_new_animal] = self.all_answers



if __name__ == '__main__':
    Run()
