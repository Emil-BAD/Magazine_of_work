from flask import Flask

from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

surname = input('surname')
name = input('name')
age = int(input('age'))
position = input('position')
speciality = input('speciality')
address = input('addres')
email = input('email')
hashed_password = input('password')


def main():
    db_session.global_init("db/blogs.db")
    run = True
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    user.hashed_password = hashed_password
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = db_sess.query(User).first()
    db_sess.commit()
    job = Jobs(team_leader=user.id, job='deployment of residential modules 1 and 2', work_size=15, collaborators='2, 3',
               is_finished=False)
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()
