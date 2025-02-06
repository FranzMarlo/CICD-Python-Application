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
    person.name = "Test"
    assert not person.surname
    
def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 22

def test_add_job(person: Person):
    person.add_job("Software Tester")
    assert person.jobs == ["Software Developer", "Software Tester"]

def test_empty_jobs(person: Person):
    person_no_jobs = Person("John Doe", 30)
    assert person_no_jobs.jobs == []

def test_add_multiple_jobs(person: Person):
    person.add_job("Data Scientist")
    person.add_job("Product Manager")
    assert person.jobs == ["Software Developer", "Data Scientist", "Product Manager"]

def test_forename_with_multiple_spaces():
    person = Person("John Michael Doe", 40)
    assert person.forename == "John"

def test_surname_with_multiple_spaces():
    person = Person("John Michael Doe", 40)
    assert person.surname == "Doe"

def test_no_surname_for_single_name():
    person = Person("John", 40)
    assert person.surname is None

def test_celebrate_birthday_multiple_times(person: Person):
    for _ in range(5):
        person.celebrate_birthday()
    assert person.age == 26

def test_add_job_with_duplicate_titles(person: Person):
    person.add_job("Software Developer")
    assert person.jobs == ["Software Developer", "Software Developer"]

