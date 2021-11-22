*** Settings ***
Resource  resource.robot
Test Setup Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Valid Password
    Input Credentials  aino  aino123
    Output Should Contain  jee

*** Keywords ***
Create User and Input New Command
    Input New Command
    Create User  kalle  kalle123
