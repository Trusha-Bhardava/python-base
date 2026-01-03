Function:

function is block of code that perform specific task.
it is basic piece of logic that you can reuse 
it declare using def keyword.

work of function:
1. take input 
2. perform the logic
3. return output

advantage of function:
1.readability
2.reuse-ability (modurability)
3.Debugging


Modules:

module is python script containing python code. 
it can function,classes,and variable that can be used in other python script.
it can help you to organize,reuseable and maintaaniable code.
for using module, you can import it.

ex =
    import mymodule         # import file name 
    a=mymodule.person["age"]
    print(a)

 extra kindly note:

 1. talking to aws API => Boto3
 2. github => github
 3. jira => jira
 4. http => request    


packages:

   packages is collection of modules. 
   we consume the packages but we don't write packages as much as devlopers write.
   if your code written in multiple file you can bundle of all this file in pacakge.

steps for packages:

      you can import packages according to particular project requirement. you first created your own virtual environment and crate multiple project on it. select your project and import package. so it is most efficient way to import package. 

 1. login  to machine (ssh to machine)
 2. using command switch to virtual environment
 3. each project one virtual environment
 4. switch to project
 5. install require packages


command for these process:
  
1. pip install virtualenv
2. python -m venv "project-name"     # -m is refer to calling module venv
3. source project-abc/bin/activate
4. pip install jira                  # import jira or any other package
5. pip list | grep jira              # to check jira installed or not
6. deactivate                        # to out of project
