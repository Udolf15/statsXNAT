from pyxnat import Interface
import getpass

class ConfigFileGenerator:

    name = ""
    password = ""

    def name_and_pass(self): # Function for taking input from the users

        self.name = input("Enter Username for central XNAT server : ")
        self.password = getpass.getpass("Enter Password for central XNAT server : ")

    def generator(self): # Function for creating the configuration file

        central = Interface(server = 'https://central.xnat.org',
                            user = self.name,
                            password = self.password    )

        central.save_config('ConfigFile/central.cfg')
        print("Configuration file Created...........")

if __name__ == "__main__":
    ConfigObj = ConfigFileGenerator()
    ConfigObj.name_and_pass()
    ConfigObj.generator()
