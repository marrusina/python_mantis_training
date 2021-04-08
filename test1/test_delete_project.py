from fixture.project import Project
import random


def test_delete_project(app, db):
    if len(db.get_projects_list()) == 0:
        app.project.add_project(Project(name="Project to delete"))
    old_projects = app.soap.get_list_soap(username=app.config["web"]["username"], password=app.config["web"]["password"])
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.soap.get_list_soap(username=app.config["web"]["username"], password=app.config["web"]["password"])
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)