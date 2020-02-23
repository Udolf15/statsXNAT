# file for fetching data from CENTRAL XNAT

from pyxnat import *


class Fetcher:

    selector = Interface(config = 'ConfigFile/central.cfg')

    def getProjects(self):

        # Return a json table with all visible project details or public projects  to user

        try:
            output = self.selector.select('xnat:projectData').all() 
            return output
        except:
            print("ERROR : ",SystemError)
            return None


    def getSubjects(self):

        # Return a json table with all visible subjects details or public subjects to the user

        try:
            output = self.selector.select('xnat:subjectData').all()
            return output
        except:
            print("ERROR : ",SystemError)
            return None

    def getExperiments(self):

        # Return a json table with all visible project details or public projects to user

        try:
            output = self.selector.select('xnat:mrSessionData').all()
            return output
        except:
            print("ERROR : ",SystemError)
            return None