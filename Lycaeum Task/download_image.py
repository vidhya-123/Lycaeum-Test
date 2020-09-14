import requests,re,os,bs4
import urllib.request
url = 'https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628990-7950'           # To store url
print("The Given URL is :",url)
response = requests.get(url)                                                            # Request to url webpage
bs = bs4.BeautifulSoup(response.text,"html.parser")                                     # bs object holds html content of the webpage
list_imgs = bs.find_all('img')                                                          # To find out all image tags
no_of_imgs = len(list_imgs)                                                             # To find total number of img tags
j=1                                                                                     # Set j=1
for imgTag in list_imgs:                                                                # Loop to check all image links
    try:
        imgLink = imgTag.get('src')                                                     #To store image src into imgLink
        head_tail = os.path.split(imgLink)                       # Using split(),break the imgLink in two parts
        if re.match('^aamir',head_tail[1]) :                     # Check the file name starts with "aamir"
            filename = head_tail[1]                              # Store file name into 'filename'
            file_des = os.path.join('folder', filename)          # Here joining the folder path with filename which Specifies file destination
            urllib.request.urlretrieve(imgLink,file_des)         # Retrieves the data from imgLink and store to file_des
            print("image{} downloaded successfully". format(j))
            j=j+1                                                # Increment j value
    except Exception as e:
        print(e)









