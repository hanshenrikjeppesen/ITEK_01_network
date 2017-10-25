# File Server: Set up Samba

Once set up, you can mount your home file server on all the other computers on your network, and use it as a convenient place to store everything from music files you want to share with your housemates, to backups of important documents and save-game files you’d like to share between computers.
We’re going to update our repository index, make sure our operating system is fully updated, and install Samba using apt-get. Open a Terminal and type:

```
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install samba samba-common-bin
```
