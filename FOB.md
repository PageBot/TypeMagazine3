~~~ 
page = doc[1]
content = page.select('Content')
page.name = 'Home'
page.url = 'index.html'

content = page.select('Content')
box = content.newBanner()

~~~

# Type Magazine 3

~~~
box = content.newIntroduction()
~~~

This issue...

~~~
section = content.newSection()
box = section.newMain()
~~~
AAAA

~~~
box = section.newSide()
~~~
BBB