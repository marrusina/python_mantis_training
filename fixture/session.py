from fixture.navigation import NavigationHelper
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        NavigationHelper.open_home_page(self)
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        # Logout
        wd = self.app.wd
        #wd.find_element_by_css_selector("[class='user-info']").click()
        #wd.find_element_by_css_selector("a i[class='fa fa-sign-out ace-icon']").click()
        wd.find_element_by_link_text("Logout").click()


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username
        return self.get_logged_user()

    def get_logged_user(self,):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text
