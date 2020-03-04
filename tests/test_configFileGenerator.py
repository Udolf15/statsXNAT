import pytest
import configFileGenerator
import os.path

config_object = configFileGenerator.ConfigFileGenerator()

# Function for testing the name and password entered 
def test_name_and_pass():

    config_object.name_and_pass(testCheck=1)

    assert config_object.name == 'testUser'
    assert config_object.password == 'testPassword'

# Function for testing the file generated is present in
# correct location with expected name
def test_generator():

    # config_object have the attributes from the above test function
    # thus config_object will use those attributes to generate the file
    config_object.generator()   
    assert os.path.exists('ConfigFile/central.cfg')
