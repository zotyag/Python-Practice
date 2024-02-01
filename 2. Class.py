from datetime import date
import csv
import re


class Person:
    allcont = []
    file = open("countries of the world.csv", "r")
    reader = csv.DictReader(file)
    for row in reader:
        allcont.append((row["Country"]).strip())
    file.close()

    def __init__(self, name: str, country: str, dob: str):
        self.name = name
        self.country = country
        self.dob = dob
        self.age = self.determine_age()

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.dob}, Age: {self.age}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        if country not in Person.allcont:
            raise ValueError("Invalid country")
        self._country = country

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, dob: str):
        if not re.search("^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$", dob):
            raise ValueError("Invalid Day Of Birth")
        testing = dob.strip().split("-")
        try:
            date(int(testing[0]), int(testing[1]), int(testing[2]))
        except ValueError:
            raise ValueError("Invalid Day Of Birth")
        self._dob = dob
        self.age=self.determine_age()

    def determine_age(self):
        today = str(date.today())
        today = today.split("-")
        dob = self.dob.split("-")
        end = date(int(today[0]), int(today[1]), int(today[2])) - date(int(dob[0]), int(dob[1]), int(dob[2]))
        return int(end.days / 365)

    def validname(name):
        if name:
            return True

    def validcountry(country):
        if country in Person.allcont:
            return True

    def validdob(dob):
        if re.search("^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$", dob):
            testing = dob.strip().split("-")
            try:
                date(int(testing[0]), int(testing[1]), int(testing[2]))
                return True
            except:
                return False


def main():
    nev = "John"
    orszag = "Germany"
    dob = "1969-11-26"

    if Person.validname(nev) and Person.validcountry(orszag) and Person.validdob(dob):
        no1 = Person(nev, orszag, dob)
        print(no1)


if __name__ == "__main__":
    main()
