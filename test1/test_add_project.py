from model.project import Project
import time
from fixture.navigation import NavigationHelper
from fixture.application import Application
import pytest


def test_add_project(app, db, json_project):
    project = json_project
    app.navigation.open_home_page()
    #app.session.login("administrator", "root")
    #assert app.session.is_logged_in_as("administrator")
    #app.navigation.open_manage_page()
    #app.navigation.open_project_page()
    #time.sleep(5)
    old_projects = db.get_projects_list()
    app.project.create(project)
    new_project = db.get_projects_list()
    old_projects.append(project)
    #print(">>>>",old_projects)
    #print(">>>>", new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)








