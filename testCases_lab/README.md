# This lab implements unit testing with unittest library #

---

*  **File containing data**

This file is not available since this lab was conducted through a remote connection
to an offsite linux distro. Here is a image of it

![data](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/find_file_original.PNG)

* **Original python script before Tests**

Here is the python script that we will write tests for and make adjustments accordingly

![script](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/original_script.PNG)

* **First test case**

First test is pretty simple, just make sure the script works correctly under ideal input

![first_test](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/test_script.PNG)

![first_result](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/test_successfull.PNG)


* **Second Test**

Next we create a test for missing parameters, it fails because the script is brittle in its
current state and the test cases expose that. So we change the script accordingly.

![second_test](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/script_update.PNG)

![second_result](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/time_for_new_testCase.PNG)

![update_script](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/try_except.PNG)

* **Last Test**

Finally we test for no parameters and an entry not in the set as test cases 
and all the tests finish successfully.

![last_test](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/last_test.PNG)

![final_result](https://github.com/r0meroh/python_automations/blob/master/testCases_lab/testcase_images/last_everything_works.PNG)
