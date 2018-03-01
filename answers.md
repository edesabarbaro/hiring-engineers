# Solutions Engineer Test

Disclaimer: before doing this test, I had never installed a VM, barely used a terminal and I wasn't familiar with command lines, coding or doing everything from a command prompt. I learned everything in order to pass this test, hence made a lot of mistakes that took some time to correct (and to understand). I will detail every step of my learning and the discoveries I made, as well as how I corrected the mistakes.

First, I started by reading the [Github introduction guide](https://guides.github.com/activities/hello-world/) and followed it to create my own repository [hello-world](https://github.com/edesabarbaro/hello-world) as I had never used Github before. I read about Markdown files to understand what they were and to make sure I could format this text correctly. I explored the [Datadog Github environment](https://github.com/DataDog) to see what projects looked like, then I read the whole exercice again and started it.

Thank you for taking the time to consider my application!

## Table of content

You can find [at this address](https://imgur.com/a/GMviG) the full imgur album with the screenshots for the first installation.
 
- [Prerequisites - Setup the environment](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#prerequisites---setup-the-environment)
    - [Installing a VM](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#installing-a-vm)
    - [Installing Datadog Agent](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#installing-datadog-agent)
- [Collecting metrics](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#collecting-metrics)
    - [Adding tags](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#adding-tags)
    - [Adding a database](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#adding-a-database)
    - [Creating a custom metric](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#creating-a-custom-metric)

As I decided to start again from scratch after doing this, you can find the second album [at this address](https://imgur.com/a/UYjEX).

- [Creating a new VM to start again](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#creating-a-new-vm-to-start-again)

- [Visualizing Data](https://github.com/edesabarbaro/hiring-engineers/blob/master/answers.md#visualizing-data)
    


## Prerequisites - Setup the environment

### Installing a VM

> You can utilize any OS/host that you would like to complete this exercise. However, we recommend one of the following approaches:
> You can spin up a fresh linux VM via Vagrant or other tools so that you don’t run into any OS or dependency issues. Here are instructions for setting up a Vagrant Ubuntu 12.04 VM.
> You can utilize a Containerized approach with Docker for Linux and our dockerized Datadog Agent image.


I decided to follow the suggestion and to install a Vagrant Ubuntu 12.04 VM. I downloaded Vagrant and VirtualBox, then checked with the cmd on Windows with `vagrant -v` if Vagrant was properly installed, and the command returned a positive answer with Vagrant 2.0.2. 
- I checked Vagrant's page [how to install it](https://www.vagrantup.com/docs/) and the steps to follow.
- For VirtualBox, I just installed it directly [from the website](https://www.virtualbox.org/).

I tried to run the VM directly from Windows cmd with `vagrant init hashicorp/precise64` but it did not work: I realised the terminal on Windows was not able to do that, as this was not the first time I had used this terminal and encountered other issues in the past.

<a href="https://i.imgur.com/1ObSIUb.jpg" title="Checking Vagrant installation">
<img src="https://i.imgur.com/1ObSIUb.jpg" width="400" height="217" alt="Checking Vagrant installation"></a>

<a href="https://i.imgur.com/QXXRfO5.jpg" title="Issue with Vagrant authorization">
<img src="https://i.imgur.com/QXXRfO5.jpg" width="400" height="217" alt="Issue with Vagrant authorization"></a>


So, after googling a bit, I downloaded Cmder and initialized the VM with `vagrant init hashicorp/precise64`. However, when the VM tried to boot, I ended up with a first error: `VT-x is disabled in the BIOS for all CPU modes`. So I rebooted my own computer to access Bios and enable Intel Virtualization.

<a href="https://i.imgur.com/aga7EEy.jpg" title="Booting VM on Vagrant">
<img src="https://i.imgur.com/aga7EEy.jpg" width="400" height="217" alt="Booting VM on Vagrant"></a>

<a href="https://i.imgur.com/9fhm1tX.jpg" title="VT-x error on Cmder">
<img src="https://i.imgur.com/9fhm1tX.jpg" width="400" height="217" alt="VT-x error on Cmder"></a>


Then, I was faced with a second error `Timed out while waiting for the machine to boot`. This time, a simple restart allowed me to boot the VM properly. I was finally able to start the VM with Cmder, with the name `Barbosa_default_1518895422216_47501`.

<a href="https://i.imgur.com/DR1LWuV.jpg" title="Timed out while waiting boot">
<img src="https://i.imgur.com/DR1LWuV.jpg" width="400" height="217" alt="Timed out while waiting boot"></a>

<a href="https://i.imgur.com/Y276y5p.jpg" title="VM started">
<img src="https://i.imgur.com/Y276y5p.jpg" width="400" height="217" alt="VM started"></a>


I was now facing a new issue: on VirtualBox, the VM appeared as Powered Off. However the name was only `Barbosa`. It gave a `file not found` error when trying to start it.

I went to look for the missing file and realized there were two different VMs, one named `Barbosa` and the other one `Barbosa_default_1518895422216_47501`. I knew the second one was the one I had just created, so `Barbosa` should not appear in VirtualBox.

<a href="https://i.imgur.com/qdPR9lH.jpg" title="VM appears as off on VirtualBox">
<img src="https://i.imgur.com/qdPR9lH.jpg" width="400" height="217" alt="VM appears as off on VirtualBox"></a>

<a href="https://i.imgur.com/kvjgmCt.jpg" title="VM is duplicated">
<img src="https://i.imgur.com/kvjgmCt.jpg" width="400" height="217" alt="VM is duplicated"></a>


In the folder `Barbosa_default_1518895422216_47501` I was indeed able to find the missing file. I tried to start the VM directly from the folder, but had a new error with `E_FAIL`.

<a href="https://i.imgur.com/VR2BvdW.jpg" title="Missing file in second folder">
<img src="https://i.imgur.com/VR2BvdW.jpg" width="400" height="217" alt="Missing file in second folder"></a>

<a href="https://i.imgur.com/AoTVEze.jpg" title="Error when starting second VM">
<img src="https://i.imgur.com/AoTVEze.jpg" width="400" height="217" alt="Error when starting second VM"></a>

I restarted VirtualBox, this time with admin rights after googling what the issue might be. I deleted `Barbosa` and started `Barbosa_default_1518895422216_47501`, it worked! The terminal finally started correctly and was asking for the login.

<a href="https://i.imgur.com/v1KAg38.jpg" title="Terminal is up">
<img src="https://i.imgur.com/v1KAg38.jpg" width="400" height="217" alt="Terminal is up"></a>

<a href="https://i.imgur.com/6F1Eqag.jpg" title="Terminal is up">
<img src="https://i.imgur.com/6F1Eqag.jpg" width="400" height="217" alt="Terminal is up"></a>

I logged in using the username and password vagrant/vagrant. The keyboard was set to qwerty (my own keyboard had no issue with azerty), so I entered `sudo loadkeys fr` to modify it.
- I also realized at that point that I was not able to copy/paste anything into the terminal. I tried [installing the Guest addition](https://askubuntu.com/questions/22743/how-do-i-install-guest-additions-in-a-virtualbox-vm/22745#22745) but I was unable to do so. After trying a lot of different things without success (or without fully understanding what I was doing), I decided to manually type every command myself: at least, that would allow me to fully understand how spacing/indentation works, even if that would be time-consuming!

<a href="https://i.imgur.com/1Wv51kb.jpg" title="Changing keyboard language">
<img src="https://i.imgur.com/1Wv51kb.jpg" width="400" height="217" alt="Changing keyboard language"></a>

### Installing Datadog Agent

> Then, sign up for Datadog (use “Datadog Recruiting Candidate” in the “Company” field), get the Agent reporting metrics from your local machine.


Once connected to the VM - I did not use SSH at that point as I didn't know how to do it, so I admit that I used vagrant/vagrant as username and password every time I connected to my VM - I was able to install the agent as requested. On the right screenshot, proof that the website detected the agent reporting!
 - I used the step-by-step installation because I wanted to really understand what was going on when installing the agent.
 - I made a few errors during the installation because I wasn't familiar yet with the Terminal, but quickly corrected them.

<a href="https://i.imgur.com/9LTUJC6.jpg" title="Installing Datadog agent">
<img src="https://i.imgur.com/9LTUJC6.jpg" width="400" height="217" alt="Installing Datadog agent"></a>

<a href="https://i.imgur.com/BlhpbYG.jpg" title="Agent reporting">
<img src="https://i.imgur.com/BlhpbYG.jpg" width="400" height="217" alt="Agent reporting"></a>

## Collecting metrics

### Adding tags 

> Add tags in the Agent config file and show us a screenshot of your host and its tags on the Host Map page in Datadog.

I added tags to the config file using `sudo nano /etc/dd-agent/datadog.conf`, then saved. At that point, I had never modified a file so I did not know that '#' were made for comments lines only. I added the tags on the wrong line and then added them manually on the Host Map. Though I felt something was wrong, I wasn't sure how to correct it and left it as such.

<a href="https://i.imgur.com/aCvy6Ta.jpg" title="Adding tags">
<img src="https://i.imgur.com/aCvy6Ta.jpg" width="400" height="217" alt="Adding tags"></a>

<a href="https://i.imgur.com/sfYy0EH.jpg" title="Host Map tags">
<img src="https://i.imgur.com/sfYy0EH.jpg" width="400" height="217" alt="Host Map tags"></a>

### Adding a database

> Install a database on your machine (MongoDB, MySQL, or PostgreSQL) and then install the respective Datadog integration for that database.

I proceeded to install MySQL after that.
- To install it, I followed the process [from the documentation](https://docs.datadoghq.com/integrations/mysql/).
- I installed it with `sudo apt-get install dd-check-mysql`.
- Then I tried following the documentation to give the correct authorizations and create a user.

<a href="https://i.imgur.com/138JZZj.jpg" title="Installing MySQL">
<img src="https://i.imgur.com/138JZZj.jpg" width="400" height="217" alt="Installing MySQL"></a>

<a href="https://i.imgur.com/i0wVxAA.jpg" title="Creating MySQL password">
<img src="https://i.imgur.com/i0wVxAA.jpg" width="400" height="217" alt="Creating MySQL password"></a>

I was faced with several errors when trying to configure MySQL. First, I tried to configure a password, which was denied. So I troubleshot the issue by googling and reconfigured MySQL and I was finally granted access.

<a href="https://i.imgur.com/iyCwOVJ.jpg" title="Reconfiguring MySQL">
<img src="https://i.imgur.com/iyCwOVJ.jpg" width="400" height="217" alt="Reconfiguring MySQL"></a>

<a href="https://i.imgur.com/hPH2zrp.jpg" title="MySQL user OK">
<img src="https://i.imgur.com/hPH2zrp.jpg" width="400" height="217" alt="MySQL user OK"></a>

I made a test with Grant and got an error `Missing replication client grant`, so I gave the rights and got a `MySQL grant - OK` in return.

<a href="https://i.imgur.com/I4XHU8M.jpg" title="Grant error">
<img src="https://i.imgur.com/I4XHU8M.jpg" width="400" height="217" alt="Grant error"></a>

<a href="https://i.imgur.com/mSnHF33.jpg" title="MySQL grant OK">
<img src="https://i.imgur.com/mSnHF33.jpg" width="400" height="217" alt="MySQL grant OK"></a>


After that, I also gave the performance_schema rights.
- I started following the [configuration to connect the Agent to MySQL](https://app.datadoghq.com/account/settings#integrations/mysql).
- I tried typing the config in the yaml file exactly like I could see it on the documentation.

<a href="https://i.imgur.com/P64d7Lx.jpg" title="performance_schema rights">
<img src="https://i.imgur.com/P64d7Lx.jpg" width="400" height="217" alt="performance_schema rights"></a>

<a href="https://i.imgur.com/e9EWlZ7.jpg" title="Configuring yaml file">
<img src="https://i.imgur.com/e9EWlZ7.jpg" width="400" height="217" alt="Configuring yaml file"></a>

There was an issue with the file however. I did not know how yaml file worked, so I google the issue again and found out that:
- yaml files are very dependent on indentation
- So I tried to modify every space on the file and was not immediately able to find where the issue was
I had already created a password when setting up the user. So, when I tried to modify the yaml file using the documentation, I did not click on "generate a password". This cause the indentation to be very different from what it should be.

Since I had never seen a yaml file before, I was trying to reproduce exactly what I was seeing, and could not correct my mistake. After looking for a while, I decided to generate a password just to see what would happen. It became suddenly clear: I could see what my mistake was with the indentation, and corrected it immediately.

<a href="https://i.imgur.com/cB3TW8g.jpg" title="Error on yaml file">
<img src="https://i.imgur.com/cB3TW8g.jpg" width="400" height="217" alt="Error on yaml file"></a>

<a href="https://i.imgur.com/BmZIg36.jpg" title="Documentation doesn't show correct indentation">
<img src="https://i.imgur.com/BmZIg36.jpg" width="400" height="217" alt="Documentation doesn't show correct indentation"></a>

The left screenshot (28) shows the corrected yaml file after changing the indentation. The right screenshot (29) shows the result of the command `sudo /etc/init.d/datadog-agent info`.

<a href="https://i.imgur.com/8osWDmY.jpg" title="Indentation is now correct">
<img src="https://i.imgur.com/8osWDmY.jpg" width="400" height="217" alt="Indentation is now correct"></a>

<a href="https://i.imgur.com/SB6rDWc.jpg" title="Info on agent is ok">
<img src="https://i.imgur.com/SB6rDWc.jpg" width="400" height="217" alt="Info on agent is good"></a>

MySQL was correctly installed!

<a href="https://i.imgur.com/YiyuXuh.jpg" title="MySQL reporting">
<img src="https://i.imgur.com/YiyuXuh.jpg" width="400" height="217" alt="MySQL reporting"></a>

### Creating a custom metric

> Create a custom Agent check that submits a metric named my_metric with a random value between 0 and 1000.

Here, I made a mistake that made me lose a lot of time.
- I used [the documentation](https://docs.datadoghq.com/agent/agent_checks/) to try to create the Agent check.
- After reading it, I decided to make an integration and started following the indications, instead of using [Your first check](https://docs.datadoghq.com/agent/agent_checks/#your-first-check)
- So I installed ruby and wget

<a href="https://i.imgur.com/zq1paOE.jpg" title="Installing ruby">
<img src="https://i.imgur.com/zq1paOE.jpg" width="400" height="217" alt="Installing ruby"></a>

<a href="https://i.imgur.com/Je3VXdi.jpg" title="Ruby installed">
<img src="https://i.imgur.com/Je3VXdi.jpg" width="400" height="217" alt="Ruby installed"></a>

Then, I proceeded to install git. I ended up after that with an error: `Could not locate gemfile`.

<a href="https://i.imgur.com/lPY17Zc.jpg" title="Installing git">
<img src="https://i.imgur.com/lPY17Zc.jpg" width="400" height="217" alt="Installing git"></a>

<a href="https://i.imgur.com/aKFIJPG.jpg" title="Could not locate gemfile">
<img src="https://i.imgur.com/aKFIJPG.jpg" width="400" height="217" alt="Could not locate gemfile"></a>

 So after googling again, I used the `bundle init` command which allowed to create a gemfile, and made the install again successfully.
 (I apologize, there is no screenshot number 36, I forgot to add this number when creating the files)

<a href="https://i.imgur.com/Iwp2KCj.jpg" title="Bundle init">
<img src="https://i.imgur.com/Iwp2KCj.jpg" width="400" height="217" alt="Bundle init"></a>

<a href="https://i.imgur.com/JOjWBk5.jpg" title="Info are still OK">
<img src="https://i.imgur.com/JOjWBk5.jpg" width="400" height="217" alt="Info are still OK"></a>

After doing this, I realized I had made a mistake! It seemed very difficult to make the first check, and when scrolling down I saw the "Your first check" menu. I also did a bit of googling and ended up finding this article on [how to monitor MySQL with Datadog](https://www.datadoghq.com/blog/mysql-monitoring-with-datadog/) which made me understand that it was easier than expected.

I decided to follow [Your first check](https://docs.datadoghq.com/agent/agent_checks/#your-first-check) instructions, and immediately created the needed files: random.py and random.yaml in the correct directories.
- Here again, I made a mistake: I used a `random.random` function instead of `random.randint` to define the metrics.
- I corrected that mistake later.

<a href="https://i.imgur.com/pBOLTKa.jpg" title="Creating the random.py file">
<img src="https://i.imgur.com/pBOLTKa.jpg" width="400" height="217" alt="Creating the random.py file"></a>

<a href="https://i.imgur.com/OYQZwk1.jpg" title="Creating the random.yaml file">
<img src="https://i.imgur.com/OYQZwk1.jpg" width="400" height="217" alt="Creating the random.yaml file"></a>

> Change your check's collection interval so that it only submits the metric once every 45 seconds.
> Bonus Question: Can you change the collection interval without modifying the Python check file you created?

If you modify the yaml file instead of the python file, you can add the collection interval directly. This was indicated [on this page](https://docs.datadoghq.com/agent/agent_checks/#configuration): "`min_collection_interval` can be added to the `init_config` section to help define how often the check should be run."
I also found [this help article](https://help.datadoghq.com/hc/en-us/articles/203557899-How-do-I-change-the-frequency-of-an-agent-check-) confirming that it could be added to the yaml file directly.

<a href="https://i.imgur.com/JrUjVRR.jpg" title="Min collection interval">
<img src="https://i.imgur.com/JrUjVRR.jpg" width="400" height="217" alt="Min collection interval"></a>


## Creating a new VM to start again

> After doing all this and finishing the part "Collecting Metrics", I decided to start over again to make sure I had fully understood how everything worked.

I did not want to keep going without making sure I new how to boot a VM properly and I wanted to be able to do all this correctly, without making mistakes. I also knew I had made two errors because it didn't feel right at the time I made them: first with the tags, and then with the random value on my metric.

- So I deleted my VM and created a whole new one, it took me about an hour to do everything again.
- I reconfigured the Agent with the correct tags, which appeared automatically in the Host Map this time.

<a href="https://i.imgur.com/vuOhtTK.jpg" title="Tags are correct">
<img src="https://i.imgur.com/vuOhtTK.jpg" width="400" height="217" alt="Tags are correct"></a>

- Then, I installed and configured MySQL again, and granted the correct permissions.

<a href="https://i.imgur.com/FI3EHCt.jpg" title="MySQL config 1">
<img src="https://i.imgur.com/FI3EHCt.jpg" width="400" height="217" alt="MySQL config "></a>

<a href="https://i.imgur.com/ytRZnId.jpg" title="MySQL config 2">
<img src="https://i.imgur.com/ytRZnId.jpg" width="400" height="217" alt="MySQL config 2"></a>

- I was however met by an error I didn't encounter the first time with innodb. I removed it after seeing that it was not compatible with MySQL 5.5, and it worked without problem after that.

<a href="https://i.imgur.com/zYHcsjn.jpg" title="MySQL yaml file">
<img src="https://i.imgur.com/zYHcsjn.jpg" width="400" height="217" alt="MySQL yaml file"></a>

<a href="https://i.imgur.com/5Q2TDs0.jpg" title="Error with innodb">
<img src="https://i.imgur.com/5Q2TDs0.jpg" width="400" height="217" alt="Error with innodb"></a>



<a href="https://i.imgur.com/5KYF4Ty.jpg" title="Yaml file">
<img src="https://i.imgur.com/5KYF4Ty.jpg" width="400" height="217" alt="Yaml file"></a>

<a href="https://i.imgur.com/Ay8Ggmt.jpg" title="Info ok">
<img src="https://i.imgur.com/Ay8Ggmt.jpg" width="400" height="217" alt="Info ok"></a>

Then, I created the my_metric.py file again, this time I corrected the random.randint!

<a href="https://i.imgur.com/RyjPvBt.jpg" title="My metric py file">
<img src="https://i.imgur.com/RyjPvBt.jpg" width="400" height="217" alt="My metric py file"></a>

<a href="https://i.imgur.com/HFVhydP.jpg" title="My metric yaml file">
<img src="https://i.imgur.com/HFVhydP.jpg" width="400" height="217" alt="My metric yaml file"></a>

I finally managed to obtain a nice metric board!

<a href="https://i.imgur.com/8732CuL.jpg" title="My metric">
<img src="https://i.imgur.com/8732CuL.jpg" width="400" height="217" alt="My metric"></a>

## Visualizing Data

> Utilize the Datadog API to create a Timeboard that contains:

> Your custom metric scoped over your host.
> Any metric from the Integration on your Database with the anomaly function applied.
> Your custom metric with the rollup function applied to sum up all the points for the past hour into one bucket
> Please be sure, when submitting your hiring challenge, to include the script that you've used to create this Timemboard.


<a href="https://i.imgur.com/VXAFKqU.jpg" title="Creating timeboard">
<img src="https://i.imgur.com/VXAFKqU.jpg" width="400" height="217" alt="Creating timeboard"></a>

```
#!/usr/bin/env python

from datadog import initialize, api

import urllib3
urllib3.disable_warnings()     

options = {
    'api_key': 'MYAPIKEY',
    'app_key': 'MYAPPKEY'
}

initialize(**options)

title = "Visualizing Data for Barbosa"
description = "Timeboard using Datadog's API"
graphs = [

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "my_metric{host:precise64}"}
        ],
        "viz": "timeseries"
    },
    "title": "My metric scoped over my host"
},

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "anomalies(avg:mysql.performance.cpu_time{host:precise64}, 'robust', 2)"}
        ],
        "viz": "timeseries"
    },
    "title": "Anomalies on MySQL for CPU time"

},

{
    "definition": {
        "events": [],
        "requests": [
            {"q": "avg:ùy_metric{host:precise64}.rollup(sum, 3600)"}
    ],
        "viz": "timeseries"
    },
    "title": "Rollup for My metric over the past hour"

}]

read_only = True
api.Timeboard.create(title=title,
                     description=description,
                     graphs=graphs,
                     read_only=read_only)
                     
```

**Unfinished yet**
