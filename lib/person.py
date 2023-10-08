#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        pass

    def get_name(self):
        return self.name
    pass

    def set_name(self, name):
        if isinstance(name, str):
            if name == "" or 1 < len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
            else:
                print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)
