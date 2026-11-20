Steps for reproduction:
1. Download the Qualitas Corpus: http://qualitascorpus.com/
2. unzip the Qualitas Corpus into one project.
3. For each java project in the Qualitas Corpus put the following:
    1. A projectlist.txt file with the name of the project file in the java project.
    2. A designiteJava.jar file found in the script folder into that java project (Found in this repository or https://www.designite-tools.com/docs/installation.html)
    3. Download the DesigniteAndPMDRunFinal.sh and P_valueCalculationFinal.py (found in this repository)
   
       Download the PMD:
       
                 a. found:https://sourceforge.net/projects/pmd/files/pmd/6.3.0/
                 b. Link the pmd.run file to where you have that downloaded
4. Now Run the DesigniteAndPMDRunFinal.sh


AI Statement:
We used AI to create our p_value comparison script as well as a bash script for running the PMD and the designitejava.jar.
AI was also used for troubleshooting problems.

Prompts used:

"We are doing a project where we need to compare static analysis warnings and architectural smells using p-value comparison. Write a script that runs PMD and Designite and compares their outputs using p-value analysis, reading project names from a file named projectList.txt"
"🔍 Running PMD analysis with rulesets:" (error output)
"================ [COMBINED SYSTEM-WIDE GLOBAL Analysis] ================" (incorrect results output)

We also asked if a different method would improve our output :"What would be a better way of checking the correlation bettween architectural smells and warnings than using PMD and DesigniteJava"
