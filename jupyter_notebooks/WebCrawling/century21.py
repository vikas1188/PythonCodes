
# coding: utf-8

# In[86]:


import requests

from bs4 import BeautifulSoup

r= requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c= r.content

soup = BeautifulSoup(c,"html.parser")

soup

all = soup.find_all("div",{"class":"propertyRow"})

all

len(all)

all[0]

all[0].find_all("h4",{"class":"propPrice"})

all[0].find_all("h4",{"class":"propPrice"})[0].text.replace("\n","")

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","")



page_nr = soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr)


# In[60]:


l=[]
for item in all:
    d={}
    d["Price"]=(item.find("h4",{"class","propPrice"}).text.replace("\n",""))
    addresses = item.find_all("span",{"class":"propAddressCollapse"})
    d["Address"]=addresses[0].text 
    d["Locality"]=addresses[1].text
    try:
        d["Beds"]=(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        d["Beds"]=(None)
    try:
        d["Area"]=(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        d["Area"]=(None)
    try:
        d["Full Bath"]=(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        d["Full Bath"]=(None)
    try:
        d["Half Bath"]=(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        d["Half Bath"]=(None)
    for column_group in item.find_all("div", {"class":"columnGroup"}):
        for feature_group, feature_name in zip (column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=(feature_name.text)
    l.append(d)
    print(" ")
    #print(len(addresses))
    #for address in addresses:
   #     print( address.find_all("span",{"class":"propAddressCollapse"})[0].text)


# In[62]:


len(l)


# In[63]:


import pandas
df = pandas.DataFrame(l)


# In[64]:


df


# In[65]:


df.to_csv("WebScraping.csv")


# In[88]:


l=[]
page_nr = soup.find_all("a",{"class":"Page"})[-1].text
# print(page_nr)
base_url = "https://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    url=base_url+str(page)+".html"
    r=requests.get(url)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"propertyRow"})
   
    for item in all:
        d={}
        d["Price"]=(item.find("h4",{"class","propPrice"}).text.replace("\n",""))
        addresses = item.find_all("span",{"class":"propAddressCollapse"})
        try:
            d["Address"]=addresses[0].text 
        except:
            d["Address"]=None
        try:
            d["Locality"]=addresses[1].text
        except:
            d["Locality"]=None
        try:
            d["Beds"]=(item.find("span",{"class":"infoBed"}).find("b").text)
        except:
            d["Beds"]=(None)
        try:
            d["Area"]=(item.find("span",{"class":"infoSqFt"}).find("b").text)
        except:
            d["Area"]=(None)
        try:
            d["Full Bath"]=(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
        except:
            d["Full Bath"]=(None)
        try:
            d["Half Bath"]=(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
        except:
            d["Half Bath"]=(None)
        for column_group in item.find_all("div", {"class":"columnGroup"}):
            for feature_group, feature_name in zip (column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=(feature_name.text)
        l.append(d)
# len(all)


# In[89]:


len(l)


# In[90]:


import pandas
df1 = pandas.DataFrame(l)


# In[91]:


df1


# In[92]:


df1.to_csv("WebScrappingDataFor37Locations.csv")

