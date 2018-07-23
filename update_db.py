#! /usr/bin/env python3

import csv, sys
from modelos import db, Person, Study, School, Delegate
from flask import Flask

if len(sys.argv) != 2:
    print("La ejecución de este script debe ser: python3 update_db.py /ruta/al/fichero.csv")
    sys.exit(1)

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db.app = app
#db.init_app(app) # IMPORTANTE: Comentar si la BBDD ya está creada

school = {
    'CCSSJJ': 1,
    'EPS': 2,
    'HUM': 3,
    'COLME': 6,
    'COLMEL': 8,
    'POST': 27,
    'POSTL': 28
}

with open(str(sys.argv[1])) as file:
    delegades = csv.DictReader(file, delimiter=',', quotechar='"')
    for delegade in delegades:
        study = Study.query.filter(Study.id_school == school.get(delegade.get('center')),
            Study.name.like(delegade.get('study'))).first()

        exist_person = Person.query.filter(Person.nia == delegade.get('nia')).first()
        if exist_person is not None:
            print('[ERROR] {} already processed')
        else:
            person = Person(
                delegade.get('nia'),
                delegade.get('name').title(),
                '{} {}'.format(delegade.get('surname1').title(),
                    delegade.get('surname2').title()),
                study.id_study,
                int(delegade.get('course')))
            print('Processing {}'.format(person))
            db.session.add(person)
            db.session.commit()

            if 'Sub' in delegade.get('delegate'):
                dele = Delegate(person.id_person, 1, 0, 0, 0, 0)
            else:
                dele = Delegate(person.id_person, 2, 0, 0, 0, 0)
            print('Processing {}'.format(dele))
            db.session.add(dele)
db.session.commit()