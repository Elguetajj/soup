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
print(f"GET all items that are part of the upper nab menu: ")
for string in upper_menu.strings:
        print("-" + str(string).strip())
print(separatorItems)

print("find all properties that have href:")
for link in soup.find_all('a'):
    print(link.get('href'))
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
    print(f"{img['src']}")
print(separatorItems)

count = 0 
for a in soup.find_all('a'):
    count += 1
print(f"count all <a>: {count}")

print(separatorParts)







# for div in soup.find_all("div"):
#     print(div)
#     print("--------------------------")