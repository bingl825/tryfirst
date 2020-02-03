from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from main import app,db,User,Diary,Project,ProjUser



manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command("server",Server('0.0.0.0'))
manager.add_command("db",MigrateCommand)

@manager.shell
def make_shell_contet():
    return dict(app = app, db = db, User = User, Diary = Diary, Project = Project,ProUser = ProjUser)

if __name__ == "__main__":
    manager.run()


