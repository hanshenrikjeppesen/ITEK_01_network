# File Server: Set up Samba

Once set up, you can mount your home file server on all the other computers on your network, and use it as a convenient place to store everything from music files you want to share with your housemates, to backups of important documents and save-game files you’d like to share between computers.

We’re going to update our repository index, make sure our operating system is fully updated, and install Samba using apt-get. Open a Terminal and type:

```
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install samba samba-common-bin
```
## Create a shared directory

We’re going to create a dedicated shared directory on our Pi’s micro SD hard disk. You can put it anywhere, but ours will be in the user (pi) file system.

```
sudo mkdir -m 1777 /home/pi/remote
```
This command sets the sticky bit (1) to help prevent the directory from being accidentally deleted and gives everyone read/write/execute (777) permissions on it.

## Configure Samba to share the directory

```
sudo nano /etc/samba/smb.conf
```

