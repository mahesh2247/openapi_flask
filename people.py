from flask import abort, request, make_response

PEOPLE = {
    "Bunny": {
        "fname": "abc",
        "lname": "ccc"
    }
}

def read_all():
    return list(PEOPLE.values())

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )


def create(person):
    lname = person.get("lname")
    fname = person.get("fname")

    if lname not in PEOPLE.keys():
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname
        }
        return PEOPLE[lname], 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists"
        )

def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )