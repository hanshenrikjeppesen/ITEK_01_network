# ITEK Network - github

______
For comments and suggestions or more information please contact me:

[eMail](mailto:hans@eaaa.dk)

[Linkedin](https://www.linkedin.com/in/hansjeppesen/){:target="_blank"}

______

## Introduction

This is meant as an introduction to networking using the Raspberry Pi. You will set up and use various networks. You will be introduced to basic networking through practical activities.

In the first expriment we will use the following python code to make a simple network chat.

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

![computer network](/ITEK_01_network/images/network-cable-ethernet-computer-159304.jpeg)


### Support or Contact

Having trouble with codes or GitHub? Check out [documentation](https://help.github.com/categories/github-pages-basics/){:target="_blank"} or [RaspberryPi](https://www.raspberrypi.org/documentation/){:target="_blank"} and we’ll help you sort it out.
