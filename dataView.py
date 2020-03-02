print("\nProcessing............")

from src import dataFormatter

# View class
class View:

    formatter = dataFormatter.Formatter()
    opted = 0

    # Option that are available now
    def view_options(self):
        
        print("\n")
        print("View all the projects visible to you press 1")
        print("View all the subjects visible to you press 2")
        print("View the stats of the XNAT visible to you press 3")

        self.opted = int(input("Enter your choice : "))
        self.view_selected()

    def view_selected(self):

        if(self.opted == 1):
            self.formatter.projects_formatter()
        elif(self.opted == 2):
            self.formatter.subjects_formatter()
        elif(self.opted == 3):
            self.formatter.stats()
        else:
            print("Wrong Choice\n")
            print("Run the program again")

if __name__ == "__main__":
    view = View()
    view.view_options()