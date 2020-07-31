# Deployment using Puppet

In this project the configuration software management tool **Puppet** is used.
The goal is to use a manifest to run an automation script to ensure that a fleet
of computers have a chosen set of programming resources installed, if not, the
script will install them autonomously.

*First Step*

 We ensure -python- is installed by creating a simple template that checks if
 it's installed.

 ![python](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/ensure_python_is_installed_rules.PNG)

 *Second Step*

A manifest is created to retrieve the current machine's info to correctly
identify which ever machine is currently in use.

![machine_info](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/get_info_of_master.PNG)

The template looks like this for the class and the $facts we ask for.

![machine_info_template](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/get_info_from_windows.PNG)

![facts_machine_info](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/add_to_template.PNG)

We also have another class named 'Packages' that installs certain programming
languages based on the $facts received from machine_info.

![packages](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/add_nodejs_rule.PNG)

We connect a second virtual machine by asking for an IP address.

![another_vm](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/obtain_another_ip.PNG)

we connect to it and run our current puppet module.

![connect_to_host](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/puppet_and_master.PNG)


*Third Step*

We create a reboot class to ensure that machines in the fleet do not stay running
past 30 days. Upon checking if the current machine has been on for more than 30
days, it will trigger a reboot sequence based upon what operating system puppet
detects.

![reboot](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/reboot_manifest.PNG)

We add it to the site.pp file

![node_manifest](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/include_in_site.PNG)

*Finally*

Here is the host Node displaying that all the classes in the site.pp file were
added to its catalog. We also check to make sure that the language GO was
installed, since machine_info dictated this node was a debian machine.

![host_machine_info](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/is_debian.PNG)


![complete](https://github.com/r0meroh/python_automations/blob/master/deployment_using_puppet/deployment_with_puppet_images/reboot_applied_to_hostpuppet.PNG)
