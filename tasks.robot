*** Settings ***
Documentation       Template robot main suite.

Library             Collections
Library             MyCustomLibrary
Resource            keywords.robot
Variables           variables.py


*** Tasks ***
Task 1
    Abrir archivo Excel

