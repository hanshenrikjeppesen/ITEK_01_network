# ITEK Network - github

For comments and suggestions or more information please contact me:

[eMail](mailto:hans@eaaa.dk)

[Linkedin](https://www.linkedin.com/in/hansjeppesen/){:target="_blank"}

test
______


### Introduction


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

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/hanshenrikjeppesen/ITEK_01_network/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
