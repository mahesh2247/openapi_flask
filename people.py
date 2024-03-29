# from app import db
# from flask import abort, request, make_response
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()


# # PEOPLE = {
# #     "Bunny": {
# #         "fname": "abc",
# #         "lname": "ccc"
# #     }
# # }


# class People(db.Model):
#     lname = db.Column(db.String(50), primary_key=True)
#     fname = db.Column(db.String(50))


# def read_all():
#     people = People.query.all()
#     return [{
#         'lname': person.lname,
#         'fname': person.fname
#     }
#     for person in people]
#     # return list(PEOPLE.values())

# def read_one(lname):
#     person = People.query.filter_by(lname=lname).first()
#     if person:
#         return {'lname': person.lname, 'fname': person.fname}
#     else:
#         abort(404, f"Person with last name {lname} not found")
#     # if lname in PEOPLE:
#     #     return PEOPLE[lname]
#     # else:
#     #     abort(
#     #         404, f"Person with last name {lname} not found"
#     #     )


# def create(person):
#     lname = person.get("lname")
#     fname = person.get("fname")

#     new_person = People(lname=lname, fname=fname)
#     db.session.add(new_person)
#     db.session.commit()

#     return {'lname': lname, 'fname': fname}, 201

#     # if lname not in PEOPLE.keys():
#     #     PEOPLE[lname] = {
#     #         "lname": lname,
#     #         "fname": fname
#     #     }
#     #     return PEOPLE[lname], 201
#     # else:
#     #     abort(
#     #         406,
#     #         f"Person with last name {lname} already exists"
#     #     )

# def update(lname, person):
#     updated_person = People.query.filter_by(lname=lname).first()
#     if updated_person:
#         updated_person.fname = person.get("fname")
#         db.session.commit()
#         return {'lname': lname, 'fname': person.get("fname")}
#     else:
#         abort(404, f"Person with last name {lname} not found")
#     # if lname in PEOPLE:
#     #     PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
#     #     return PEOPLE[lname]
#     # else:
#     #     abort(
#     #         404,
#     #         f"Person with last name {lname} not found"
#     #     )

# def delete(lname):
#     deleted_person = People.query.filter_by(lname=lname).first()
#     if deleted_person:
#         db.session.delete(deleted_person)
#         db.session.commit()
#         return {'lname': lname, 'message': f"{lname} successfully deleted"}, 200
#     else:
#         abort(404, f"Person with last name {lname} not found")
#     # if lname in PEOPLE:
#     #     del PEOPLE[lname]
#     #     return make_response(
#     #         f"{lname} successfully deleted", 200
#     #     )
#     # else:
#     #     abort(
#     #         404,
#     #         f"Person with last name {lname} not found"
#     #     )


from model import People, db
from schema import PeopleSchema
from flask import abort, jsonify, request


def read_all():
    people = People.query.filter().all()
    people_schema = PeopleSchema(many=True)
    return people_schema.jsonify(people), 200
   

def read_one(lname):
    try:
        people = People.query.filter_by(lname=lname).first()
        people_schema = PeopleSchema()
        if people is None:
            return {'error': 'lname does not exist!'}
        else:
            return people_schema.jsonify(people)
    except Exception as e:
        print(e)

    # person = People.query.filter_by(lname=lname).first()
    # if person:
    #     return {'lname': person.lname, 'fname': person.fname}
    # else:
    #     abort(404, f"Person with last name {lname} not found")

def create():
    data = request.get_json()
    try:
        new_person = People(**data)
        people_schema = PeopleSchema()
        db.session.add(new_person)
        db.session.commit()
        return people_schema.jsonify(new_person)
    except Exception as e:
        print(e)


    # lname = person.get("lname")
    # fname = person.get("fname")

    # new_person = People(lname=lname, fname=fname)
    # db.session.add(new_person)
    # db.session.commit()

    # return {'lname': lname, 'fname': fname}, 201

def update(lname, person):
    updated_person = People.query.filter_by(lname=lname).first()
    if updated_person:
        updated_person.fname = person.get("fname")
        db.session.commit()
        return {'lname': lname, 'fname': person.get("fname")}
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    deleted_person = People.query.filter_by(lname=lname).first()
    if deleted_person:
        db.session.delete(deleted_person)
        db.session.commit()
        return {'lname': lname, 'message': f"{lname} successfully deleted"}, 200
    else:
        abort(404, f"Person with last name {lname} not found")
