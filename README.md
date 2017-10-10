# ITEK Network - github

______
For comments and suggestions or more information please contact me:

[eMail](mailto:hans@eaaa.dk)

[Linkedin](https://www.linkedin.com/in/hansjeppesen/){:target="_blank"}

______

## Introduction

This is meant as an introduction to networking using the Raspberry Pi. You will set up and use various networks. You will be introduced to basic networking through practical activities.

![computer network](/ITEK_01_network/images/network-cable-ethernet-computer-159304.jpeg)

In the first experiment we will use two Raspberry pi's to set up a small network. We will need to assign each raspberry pi a static IP address. If you need help with that, try lookin at this [tutorial](https://www.modmypi.com/blog/how-to-give-your-raspberry-pi-a-static-ip-address-update){:target="blank"}
The abbreviation IP stands for Internet Protocol. An Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication ([ref](https://tools.ietf.org/html/rfc760){:target="_blank"})

We will also try to setup GitHub and PyCharm so that you will be able to work on code in groups. It will also give you the possibility to clone or pull your code onto the Raspberry Pi. For setup see this short ["How to Guide"](ITEK_01_network/doc/git_pycharm.md){:target="_blank"}

```python
# chat.py  (c) 2013 @whaleygeek
#
# A simple internet-chat application

import network
import sys

def heard(phrase):
  print("them:" + phrase)

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

while network.isConnected():
  # phrase = raw_input() # python2
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
  
```

But first we need to understand the concept of ```computer networks```




### Support or Contact

Having trouble with codes or GitHub? Check out [documentation](https://help.github.com/categories/github-pages-basics/){:target="_blank"} or [RaspberryPi](https://www.raspberrypi.org/documentation/){:target="_blank"} and we’ll help you sort it out.
