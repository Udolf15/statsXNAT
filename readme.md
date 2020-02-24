# statsXNAT

statsXNAT is a set of programs which gives the user to get an overview of the data present at XNAT servers. statsXNAT uses pyXNAT to connect to the XNAT servers using RESTful Web services provided by XNAT.


## Dependencies

 - [pyXNAT](https://pyxnat.github.io/pyxnat/index.html) 

## Getting Started
- ```pip3 install -r requirements.txt```
- ```python3 configFileGenerator.py```
- ```python3 dataView.py```

## Flow Diagram

The following diagram show the flow of information from different part of the program

```mermaid
graph LR
A[dataView] -- Request to dataFormatter --> B((dataFormatter))
B((dataFormatter)) -- Request to dataFetcher --> C((dataFetcher))
C((dataFetcher)) -- Request to XNAT server using pyXNAT --> D((XNAT Server))
D((XNAT Server)) -- Response to dataFetcher using pyXNAT--> C((dataFetcher))
C((dataFetcher)) -- Data to dataFormatter for formatting --> B((dataFormatter))
B((dataFormatter)) -- Data provided to dataView --> A((dataView))
```