from bs4 import BeautifulSoup
import requests,sys,csv,json

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())
separatorItems = "-----------------------------------------------\n"
separatorParts = "===============================================\n"


# Part 1 ============================================================
print("< Juan Jose Elgueta 20180396>")
print(separatorParts)

print("1. Portal \n")

print(f"GET the title and print it: {soup.title.string}")
print(separatorItems)
direccion = ""

footer = soup.find(id = "footer").find(class_ = "span4")

for string in footer.strings:
    direccion += " " + str(string).strip()
print(f"GET the complete adress of UFM: {direccion}")
print(separatorItems)

phone_email = ""
for string in footer.find_next_sibling().strings:
    phone_email += " " + str(string).strip()
print(f"GET phone number and email info: {phone_email}")
print(separatorItems)

upper_menu = soup.find(id = "menu-table")
print(f"GET all items that are part of the upper nav menu: ")
for string in upper_menu.strings:
        print("-" + string.string.strip())
print(separatorItems)

print("find all properties that have href:")
for link in soup.find_all('a'):
    print("-" + link.get('href'))
print(separatorItems)

print("GET href of  UFMail button:")
ufmail = soup.find(id = "ufmail_")['href']
print(f"{ufmail}")
print(separatorItems)

print("GET href of  MiU button:")
ufmail = soup.find(id = "miu_")['href']
print(f"{ufmail}")
print(separatorItems)

print("get hrefs (src) of all <img>:")
imgs = soup.find_all("img")
for img in imgs:
    print(f"-{img['src']}")
print(separatorItems)

count = 0 
for a in soup.find_all('a'):
    count += 1
print(f"count all <a>: {count}")

print(separatorParts)

# 1.1 

with open('persons.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for a in soup.find_all('a'):
        text = a.string
        href = a['href']
        filewriter.writerow([f'{text}',f'{href}'])
csvfile.close()


#part 2 =======================================================

url="http://ufm.edu/Estudios"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

print("2. Estudios \n")
print("display all items from topmenu: ")
topmenu = soup.find(id = "topmenu")
for string in topmenu.find_all('li'):
            print("-" + string.string.strip())
print(separatorItems)

print(" display ALL Estudios (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus)")
for estudios in soup.find_all(class_ = "estudios"):
    print ("-" + estudios.string)
    if estudios.find_next_sibling('p').find('b') is not None:
        estudio = estudios.find_next_sibling('p').find_all('b')
        for est in estudio:
            print ("   -"+ est.string)
print(separatorItems)

print("display from leftbar all <li> items:")
leftbar_items = soup.find(class_ = "leftbar").find_all('li')
for li in leftbar_items:
    print("-" + li.string)
print(separatorItems)

print("get and display all available social media with its links (href) class=social pull-right:")
for link in soup.find(class_ = "social pull-right").find_all('a'):
    print ("-" + link['href']) 
print(separatorItems)

print("count all <a> :")
count = 0
for a in soup.find_all('a'):
    count +=1
print(count)


print(separatorParts)

# for div in soup.find_all("div"):
#     print(div)
#     print("--------------------------")