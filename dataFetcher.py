# file for fetching data from CENTRAL XNAT

from pyxnat import *


class Fetcher:

    selector = Interface(config = 'ConfigFile/central.cfg')

    def getProjects(self):

        # Returns a json table with all visible project details or public projects  to user

        try:
            print("Processing............")
            output = self.selector.select('xnat:projectData').all() 
            return output
        except:
            print("ERROR : Unable to connect to the database")
            return None


    def getSubjects(self):

        # Returns a json table with all visible subjects details or public subjects to the user

        try:
            print("Processing............")
            output = self.selector.select('xnat:subjectData').all()
            return output
        except:
            print("ERROR : Unable to connect to the database")
            return None

    def getExperiments(self):

        # Returns a json table with all visible project details or public projects to user

        try:
            print("Processing............")
            output = self.selector.select('xnat:mrSessionData').all()
            return output
        except:
            print("ERROR : Unable to connect to the database")
            return None