from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class School(db.Model):
    __tablename__ = 'school'
    id_school = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id_school, name):
        self.id_school = id_school
        self.name = name

    def __repr__(self):
        return 'id_school: {}, name: {}'.format(self.id_school, self.name)


class Study(db.Model):
    __tablename__ = 'study'
    id_study = db.Column(db.Integer, primary_key=True)
    id_school = db.Column(db.Integer, ForeignKey('school.id_school'), nullable=False)
    id_sdic = db.Column(db.Integer)
    name = db.Column(db.String(120), nullable=False)
    id_area = db.Colum(db.String(50))

    def __init__(self, id_study, id_school, name, id_area):
        self.id_study = id_study
        self.id_school = id_school
        self.name = name
        self.id_area = id_area

    def __repr__(self):
        return 'id_study: {}, id_school: {}, id_sdic:{}, name: {}, id_area: {}'.format(self.id_study, self.id_school, self.id_study,
                                                                          self.name, self.id_area)


wg_member = db.Table('wg_member',
                     db.Column('work_group_id', db.Integer, db.ForeignKey('work_group.id_work_group')),
                     db.Column('person_id', db.Integer, db.ForeignKey('person.id_person'))
                     )


class WorkGroup(db.Model):
    __tablename__ = 'work_group'
    id_work_group = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    permanent = db.Column(db.Integer, default=0)
    organizers = db.relationship('Person', backref='work_group', lazy='select')
    members = db.relationship('Person', secondary=wg_member, backref=db.backref('work_groups', lazy='select'))

    def __init__(self, id_work_group, name, permanent):
        self.id_work_group = id_work_group
        self.name = name
        self.permanent = permanent

    def __repr__(self):
        return 'id_work_group: {}, name: {}, permanent: {}, organizers: {}, members: {}'.format(self.id_work_group,
                                                                                                self.name,
                                                                                                self.permanent,
                                                                                                self.organizers,
                                                                                                self.members)


class Person(db.Model):
    __tablename__ = 'person'
    id_person = db.Column(db.Integer, primary_key=True)
    nia = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    id_study = db.Column(db.Integer, ForeignKey('study.id_study'), nullable=False)
    course = db.Column(db.Integer, nullable=False)
    work_group_organizer = db.Column(db.Integer, db.ForeignKey('work_group.id_work_group'), nullable=True)
    imagen = db.Column(db.String(256), nullable=False)

    def __init__(self, id_person, nia, name, surname, id_study, course, work_group_organizer, imagen):
        self.id_person = id_person
        self.nia = nia
        self.name = name
        self.surname = surname
        self.id_study = id_study
        self.course = course
        self.work_group_organizer = work_group_organizer
        self.imagen = imagen

    def __repr__(self):
        return 'id_person: {}, nia: {}, name: {}, surname: {}, id_study: {}, course: {}, work_group_organizer: {}'.format(
            self.id_person, self.nia, self.name, self.surname, self.id_study, self.course, self.work_group_organizer)


class Delegate(db.Model):
    __tablename__ = 'delegate'
    id_delegate = db.Column(db.Integer, ForeignKey('person.id_person'), primary_key=True)
    course = db.Column(db.Integer, default=0)
    study = db.Column(db.Integer, default=0)
    school = db.Column(db.Integer, default=0)
    assembly = db.Column(db.Integer, default=0)
    senate = db.Column(db.Integer, default=0)

    def __init__(self, id_delegate, course, study, school, assembly, senate):
        self.id_delegate = id_delegate
        self.course = course
        self.study = study
        self.school = school
        self.assembly = assembly
        self.senate = senate

    def __repr__(self):
        return 'id_delegate: {}, course: {}, study: {}, school: {}, assembly: {}, senate: {}'.format(self.id_delegate,
                                                                                                     self.course,
                                                                                                     self.study,
                                                                                                     self.school,
                                                                                                     self.assembly,
                                                                                                     self.senate)


class Privilege(db.Model):
    __tablename__ = 'privilege'
    id_privilege = db.Column(db.Integer, primary_key=True)
    id_app = db.Column(db.Integer, nullable=False)
    id_person = db.Column(db.Integer, ForeignKey('person.id_person'), unique=True, nullable=False)
    role = db.Column(db.Integer, nullable=False)

    def __init__(self, id_privilege, id_app, id_person, role):
        self.id_privilege = id_privilege
        self.id_app = id_app
        self.id_person = id_person
        self.role = role

    def __repr__(self):
        return 'id_privilege: {}, id_app: {}, id_person: {}, role: {}'.format(self.id_privilege, self.id_app, self.id_person, self.role)


class Area(db.Model):
    __tablename__ = 'area'