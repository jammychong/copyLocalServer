# copyLocalServer
File Explorer script to copy files from two folders and create the required directories to copy, useful for copying between local and server folders.

Scripts registers commands to be accessible in the file right-click menu option inside File Explorer!

Download the repository to a permanent place in your C: drive, follow the installation process below or follow the copyLocalServer_instruction.pdf.

# Details

The copy to local/server will create the folder path and copy your file to the corresponding destination, it will not copy the file if it exists in order to prevent an unwanted overwrite, it will create a txt file in your current folder with the prefix “exists”. To overwrite the file use copy/overwrite to local/server, it will delete the text file created by the copy to local/server if it exists.

Since the scripts do not access the file explorer’s dialog messages neither progress bar, the script will communicate statuses and errors through a series of text files in the current folder. 

# Installation

1.  Make sure you have python 3 install in your computer. To check if python is installed go to the command prompt and type “where python”, you’ll get a path if python is installed in your computer. Otherwise download and install the latest python here: https://www.python.org/downloads/.
3.	Download the copyLocalServer repository in a permanent place in your C drive.
4.	Open the settings.txt file and replace the local and server drives with your own (line 2 and 3, lower case sensitive), do not delete the first line with instructions.
          Ex: 	local_drive=S:\Server
          server_drive=\\NetworkDrive
4.	Right-Click the install.bat file and run as administrator.
5.	Go to explorer, right-click a file and you should see the copy options.

# Uninstall

1.  Right-Click the uninstall.bat file and run as administrator.
2.  That's it!

# Notes

Feel free to change the icon.ico with your custom icon or your organization.
