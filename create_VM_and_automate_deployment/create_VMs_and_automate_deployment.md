# Create a single Virtual Machine and automate a template to create a fleet of Virtual Machines.

## First step

This project will use Google's Cloud Platform(GCP). Here is how the console
looks and we will create one virtual machine with the Ubuntu operating system.
Below is the GCP console, the creation of the first VM, and the VM running.

![console](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/console.PNG)

![first_vm](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/create_instance.PNG)

![running](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/ssh_on_browserWindow.PNG)

## second step

Within the virtual machine, we log into github and clone a repo. The contents of
this repo will be automated to execute upon booting the virtual machine. This is
done by copying the python script into a **systemd** file. When we reboot the
machine we go to the browser to see its output.

![clone](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/controlling_vm.PNG)

![service](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/create_service.PNG)

![output](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/output.PNG)

## third step

Now that we have automated what we want into one virtual machine, we can create
a **disk image** of it to use as a **template** and **orchestrate** the template
into creating a whole **fleet of virtual machines**.
First we create a disk image of the first virtual machine, then create a
template that uses that image.

![disk_image](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/create_image.PNG)

![template](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/choose_our_image.PNG)

For the next step, I chose to do it in the google's GLI(terminal) just to
demonstrate it can be done both in the web browser console or the command line.

![terminal](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/gcloud_init.PNG)

![command](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/create_fleet.PNG)

## Finally

After creating 8 different virtual machines sharing the same instructions
 instance from our original template, we check to see that they are running both through the console
and command line, as well as the output of two in the web browser.

![fleet_addresses](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/fleet_running.PNG)

![fleet_console](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/fleet_running_console.PNG)

![final_output](https://github.com/r0meroh/python_automations/blob/master/create_VM_and_automate_deployment/create_vm_automate_deployment_images/fleet_working.PNG)
