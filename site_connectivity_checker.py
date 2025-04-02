import urllib.request as urllib

def main(url):
    print("Check connectivity...")
    
    response = urllib.urlopen(url)
    
    print(f" The url: {url} connected successfully.")
    print("Your url responce code: ",response.getcode())
    
    
print("This is site connectivity checker.")

url_input = input("Enter the url: ")

main(url_input)