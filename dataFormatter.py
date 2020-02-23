import dataFetcher

class Formatter:

    data = dataFetcher.Fetcher()            # Data Fetcher Object

    def projectsFormatter(self):

        # Show the important fields of the project

        projectsTable = self.data.getProjects()

        if(projectsTable != None):
            
            print("PROJECT DETAILS")
            print("Number of project visible are ",len(projectsTable))
            print("\n\n\n\n")

            # Looping through each project to show the important fields

            for project in projectsTable:

                print("Project Creation Date : ", project['insert_date'])
                print("Project Owner Name: ", project['insert_user'])
                print("Project Name : ", project['name'])
                print("Project Description : ", project['description'])
                print("Project Users : ", project['project_users'].split('<br/>'))
                print("Project Visibility : ", project['project_access']) 
                print("Project Members : ", project['project_members'].split('<br/>'))
                print("Project Collaborators : ", project['project_collabs'].split('<br/>'))
                print("\n\n\n\n")

        else:
            
            print("Please check username or password in your configuration file")


    def subjectsFormatter(self): 

        # Show the the important fields of subjects

        subjectsTable = self.data.getSubjects()

        if(subjectsTable != None):
            
            print("SUBJECT DETAILS")
            print("Number of subjects visible are ",len(subjectsTable))
            print("\n\n\n\n")

            # Looping through each subject to show the important fields

            for subject in subjectsTable:

                print("Subject Creation Date : ", subject['insert_date'])
                print("Subject Creator Name: ", subject['insert_user'])
                print("Subject associated with ",subject['project'],"project")
                print("Subject Gender ", subject['gender_text'])
                print("Subject Handedness : ", subject['handedness_text'])
                print("Subject Date of Birth : ", subject['dob'])
                print("Subject Education : ", subject['educ']) 
                print("Subject SES : ", subject['ses'])
                print("Subject Race : ", subject['race'])
                print("Subject Ethnicity : ", subject['ethnicity'])
                print("\n\n\n\n")

        else:
            
            print("Please check username or password in your configuration file")


    def stats(self):

        # Show the overall data counts present on XNAT 

        projectsTable = self.data.getProjects()
        subjectsTable = self.data.getSubjects()
        experimentsTable = self.data.getExperiments()

        # Counter variable for different fields

        counterLH = 0
        counterRH = 0
        counterUH = 0
        counterM = 0
        counterF = 0
        counterU = 0

        # Looping through each subject to get the required count

        for subject in subjectsTable:

            gender = subject['gender_text']
            hand = subject['handedness_text']

            if(gender == 'M'):
                counterM = counterM + 1
            elif(gender == 'F'):
                counterF = counterF + 1
            else:
                counterU = counterU + 1

            if(hand == 'R'):
                counterRH = counterRH + 1
            elif(hand == 'L'):
                counterLH = counterLH + 1
            else:
                counterUH = counterUH + 1


        print("Number of Projects : ", len(projectsTable))
        print("Number of Subjects : ", len(subjectsTable))
        print("Number of Mr Sessions : ", len(experimentsTable))
        print("Number of Left handed subjects : ", counterLH)
        print("Number of Right handed subjects : ", counterRH)
        print("Number of Unknown handed subjects : ", counterUH)
        print("Number of Male subjects : ", counterM)
        print("Number of Female subjects : ", counterF)
        print("Number of Unknown gender subjets : ",counterU)