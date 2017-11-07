import urllib.request

def main():
    urls = generate_urls()
    counter = 0
    for url in urls:
        counter += 1
        webpage = "webpage" + str(counter)
        contents = download_url(url)
        save_file(webpage, contents)

def generate_urls():
    url_template = "https://xboxgamertag.com/leaderboards/"
    urls = []
    for page in range(1752,1754):
        new_url = url_template + str(page) + "/"
        urls.append(new_url)
    return urls
        
def download_url(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('utf-8')

def save_file(filename, contents):
    file = open(filename,"w")
    file.write(contents)
    file.close()

main()