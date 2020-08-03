# This is a quick set up of a NGINX server using Vitual Machines(VM) in Google Cloud
# platform(GCP)

## First Step

In previous programs/files/projects I have demonstrated how to create a Virtual
Machine within the Python_automations repo. So in here, we won't go through the
steps of that again.

After creating the VM, we **ssh** into it whether it be through the console or
the GLI.

Once we are in the VM, we use **sudo** command to access **root** in order to
update the operating system to the latest patch and also install the NGINX
Library.

![sudo](https://github.com/r0meroh/python_automations/blob/master/nginx_server/sudo.PNG)

## Final step

Once the NGINX server library is installed on our system, we create an instance
of it and use our external I.P. address for our VM in the console to see nginx_server
on our browser window.

![create](https://github.com/r0meroh/python_automations/blob/master/nginx_server/nginx_install_run.PNG)

## up and running

![browser](https://github.com/r0meroh/python_automations/blob/master/nginx_server/nginx_browser.PNG)
