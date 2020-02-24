# statsXNAT

statsXNAT is a set of programs which gives the user to get an overview of the data present at XNAT servers. statsXNAT uses pyXNAT to connect to the XNAT servers using RESTful Web services provided by XNAT.


## Dependencies

 - [pyXNAT](https://pyxnat.github.io/pyxnat/index.html) 

## Getting Started
- For installing the required dependencies type ```pip3 install -r requirements.txt``` 
- For generating the central.cfg file           ```python3 configFileGenerator.py```      
- For running the main program                  ```python3 dataView.py```               

## Flow Diagram

The following diagram show the flow of information from different modules of the program

![Flow Diagram](https://github.com/Udolf15/statsXNAT/blob/master/images/flowDiagram.png)