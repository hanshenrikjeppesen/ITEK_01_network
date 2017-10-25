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

In this example, we need to add the following entry:

```
[WORKGROUP]
Comment = pi shared folder
Path = /home/pi/remote
Browseable = yes
Writeable = yes
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest = yes
read only = no
force user = root
Guest = yes
```

This means that anyone will be able to read, write, and execute files in the share, either by logging in as a Samba user (which we’ll set up below) or as a guest. If you don’t want to allow guest users, omit the guest ok = yes line.

You could also use Samba to share a user’s home directory so they can access it from elsewhere on the network, or to share a larger external hard disk that lives at a fixed mount point. Just create a smb.conf entry for any path you want to share, and it’ll be made available across your network when you restart Samba.

Create a user and start Samba

```sudo smbpasswd -a pi```

Then set a password as prompted.

__let’s restart Samba:__

```sudo /etc/init.d/samba restart```

From now on, Samba will start automatically whenever you power on your Pi.

Lets try to find it on the network

In windows 10 we need a work-around:



