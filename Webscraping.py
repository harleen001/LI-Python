sample_html= '''<html>
<head>
    <title>abc : Developed for Developers by Developers for the betterment of Development.</title>
    <script src="static/script1.js"></script>
    <script src="static/script2.js"></script>
    <link rel="stylesheet" href="static/stylesheet.css" type="text/css" />
</head>
<body>
    <p id='start'>Welcome to abc</p>
    <p id='main_para'>We regularly publish tutorials on various topics
    (Python, Machine learning, Data Visualization, Digital Marketing, etc.) regularly explaining
    how to use various Python libraries.</p>
    <p id='sub_para'>Below are list of Important Sections of Our Website : </p>
        <ul>
            <li><a href='https://abc.com/blogs'>Blogs</a></li>
            <li><a href='https://abc.com/tutorials'>Tutorials</a></li>
            <li><a href='https://abc.com/about'>About</a></li>
            <li><a href='https://abc.com/contact-us'>Contact US</a></li>
        </ul>
    <p id='end'>Please feel free to send us mail @ abc07@gmail.com if you need any
    information about any article or want us to publish article on particular topic.</p>
</body>
</html>'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(sample_html, 'html.parser')

print("------------------PRINTING COMPLETE------------------------")
print(soup)

print("------------------PRINTING SCRIPT------------------------")
print(soup.script)


print("------------------PRINTING LINK------------------------")
print(soup.link)


print("------------------PRINTING TITLE------------------------")
print(soup.title)


print("------------------PRINTING BODY------------------------")
print(soup.body)

print("------------------PRINTING LINK TYPE------------------------")
print(soup.link["type"])


print("------------------PRINTING ANCHOR TAG------------------------")
print(soup.a["href"])


print("------------------PRINTING COMPLETE------------------------")
print(soup.text)


print("------------------PRINTING NAVBARS STRIPPED TEXT------------------------")
print(soup.ul.get_text().strip())


print("--------------------FINDING FIRST-----------------")
out = soup.find("a")
print(type(out))
print(out)

print("---------------------PRINT ALL LI------------------------")
abc=soup.find_all("li")
print(abc)

print("--------------------FINDING ALL PREVIOUS ELEMENTS--------------------")
out = soup.ul.find_all_previous()
print(type(out))
print(out[:5])

print("-------------------FINDING PARENT----------------------")
print(soup.li.find_parent())


print("-----------------FINDING ALL NEXT SIBLINGS/ALSO PREVIOUS")
print(soup.p.find_next_siblings(name="p"))

print("--------------PREVIOUS ONES-----------------")
print(soup.find(id="end").find_previous_sibling())


print("-------Find All Previous Siblings of Given HTML Tag-------")
print("------ALL PREVIOUS SIBLINGS OF PARAGRAPH--------")
print(soup.find(id="end").find_previous_siblings(name="p"))