
# Terminal;
    -> A way to tell the kernel that, what we wanna do !
    -> 

# Shell;
    -> It comes between Terminal and kernel
    -> It converts our input into a machine[binary] language which the kernel of that machine understands
    -> Ex, bash [ Bourne Again Shell ], zsh [ Z Shell ], fish Shell, csh [ C Shell ], etc.
    -> 



# Navigating Through Linux System;

-> ls   ; list

-> pwd   ; print working directory

-> cd   ; change directory

-> cd ..   ; move one directory back

-> cd   ; back to home directory

-> cd Documents/   ; move to Documents directory [use Tab key to auto complete]

-> reboot   ; reboot the system [use sudo if needed !]

-> 



# Creating Files & Managing Directories;

-> touch file1   ; create an empty file

-> cat file1   ; prints file contents on terminal

-> echo Write whatever you want > file1   ; Write anything and save it to it's desired file


-> nano file2   ; edits desired file, if it unable to find that file, it creates a new file according to user's input
                -> write anything and press, ctrl + o   -> to write out & press enter to confirm
                -> ctrl + x   -> to exit nano editor


-> cat file2   ; read file instantly on terminal

-> nano file3.py   ; create a python file and code it

-> python3 file3.py   ; run a python file in terminal

-> mkdir directory1   ; make a folder/directory

-> cd directory1   ; go to directory1

-> cd ..   ; come back to previous directory

-> mv file3.py directory1   ; move file to another directory


-> cp file3.py file2   ; copy the file contents to another file
                        -> if file exists, it replaces it's previous contents
                        -> if file not found, it creates a new file according to user's input and copy the contents in that file

-> cp file3.py /home/hacker/test1   ; copy the same file to desired directory
                                    -> correct file/directory path is important to specify the particular file


-> rm file3.py   ; Remove the desired file

-> rm directory1 -r   ; Remove the desired directory


-> rm * -r   ; Remove all the files and directories from current working directory
             -> never run this commmand in slash ( / ) directory, it'll destroy the whole operating system

-> sudo rm -rf /*   ; Most deadly command, destroys the whole operating system !



# Network Commands & sudo privileges in Kali;

-> ifconfig   ; To know IP & MAC addresses 
               -> MAC address tells that, who you are ?
               -> IP address tells that, where you are ?

-> sudo su   ; Superuser do

-> sudo   ; Run commands with Superuser privileges

-> 



# 








# virtualbox (Additional);

-> sudo sh VBoxLinuxAdditions.run   ; Install full screen drivers in virtualbox of linux OS

-> 











