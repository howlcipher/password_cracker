
# Check two passwords between the three different method
*** Settings ***
Library         Password_Cracker.py     ${password1}    WITH NAME    PC1    
Library         Password_Cracker.py     ${password2}    WITH NAME    PC2    

*** Variables ***
${password1}     abc
${password2}     password

*** Test Cases ***
1 -- method: password_cracker_one from python
    ${result}      PC1.Password Cracker One   
    Log            ${result}
1 -- method: password_cracker_two from python
    ${result}      PC1.Password Cracker Two
    Log            ${result}
1 -- method: password_cracker_three from python
    ${result}      PC1.Password Cracker Three
    Log            ${result}

*** Test Cases ***
2 -- method: password_cracker_one from python
    ${result}      PC2.Password Cracker One   
    Log            ${result}
2 -- method: password_cracker_two from python
    ${result}      PC2.Password Cracker Two
    Log            ${result}
2 -- method: password_cracker_three from python
    ${result}      PC2.Password Cracker Three
    Log            ${result}

