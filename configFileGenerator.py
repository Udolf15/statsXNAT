from pyxnat import Interface


class ConfigFileGenerator:

    name = ""
    password = ""

    def nameAndPass(self):

        self.name = input("Enter Username : ")
        self.password = input("Enter Password : ")

    def generator(self):

        central = Interface(server = 'https://central.xnat.org',
                            user = self.name,
                            password = self.password    )

        central.save_config('ConfigFile/central.cfg')
        

if __name__ == "__main__":
    ConfigObj = ConfigFileGenerator()
    ConfigObj.nameAndPass()
    ConfigObj.generator()
