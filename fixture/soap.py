from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_soap(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        def convert(p):
            return Project(id=str(p.id), name=p.name, description=p.description)

        project_data_array = client.service.mc_projects_get_user_accessible(username=username, password=password)
        project_list = list(map(convert, project_data_array))
        return project_list
