# file for fetching data from CENTRAL XNAT

from pyxnat import Interface


class Fetcher:

    try: # Checking if the configuration file is created
        selector = Interface(config = 'ConfigFile/central.cfg')
    except:
        print("Please create the configuration file first")
        exit(1)

    output = ""

    def get_projects(self):

        # Returns a json table with all visible project details or public projects  to user

        try:
            print("Processing............")
            self.output = self.selector.select('xnat:projectData').all() 
        except:
            print("ERROR : Unable to connect to the database")
            self.output = None
            
        return self.output


    def get_subjects(self):

        # Returns a json table with all visible subjects details or public subjects to the user

        try:
            print("Processing............")
            self.output = self.selector.select('xnat:subjectData').all()
        except:
            print("ERROR : Unable to connect to the database")
            self.output = None

        self.output

    def get_experiments(self):

        # Returns a json table with all visible project details or public projects to user

        try:
            print("Processing............")
            self.output = self.selector.select('xnat:mrSessionData').all()
        except:
            print("ERROR : Unable to connect to the database")
            self.output = None

        return self.output