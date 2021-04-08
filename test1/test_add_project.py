from model.project import Project

def test_add_project(app, db, json_project):
    project = json_project
    app.navigation.open_home_page()
    old_projects = app.soap.get_list_soap(username=app.config["web"]["username"], password=app.config["web"]["password"])
    app.project.create(project)
    new_project = app.soap.get_list_soap(username=app.config["web"]["username"], password=app.config["web"]["password"])
    print("old", old_projects)
    print("new", new_project)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)









