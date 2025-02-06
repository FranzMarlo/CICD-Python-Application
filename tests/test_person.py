from beings import Person

import pytest

@pytest.fixture()
def person():
    return Person("Test Name", 21, jobs=["Software Developer"])

def test_init(person: Person):
    assert person.name == "Test Name"
    assert person.age == 21
    assert person.jobs == ["Software Developer"]
    
def test_forename(person: Person):
    assert person.forename == "Test"
    
def test_surname(person: Person):
    assert person.surname == "Name"

def test_no_surname(person: Person):
    person.name = "Name"
    assert not person.surname
    
def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 22

def test_add_job(person: Person):
    person.add_job("Software Tester")
    assert person.jobs == ["Software Developer", "Software Tester"]
