class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife_person = Person.people[wife_name]
            current_person.wife = wife_person

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband_person = Person.people[husband_name]
            current_person.husband = husband_person
    return result
