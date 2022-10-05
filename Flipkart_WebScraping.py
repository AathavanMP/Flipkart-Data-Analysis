#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd


# # HTTP Request:
# # store website in variable:

# In[2]:


url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'


# # Get Request:

# In[3]:


response = rq.get(url = url)


# # Status Code:

# In[4]:


response.status_code              # When ever we see status code as 200 then it is 100% successfull.


# # Soup Object:

# In[5]:


Soup = bs(response.content, 'html.parser')


# In[6]:


Soup.prettify


# # Results:

# In[7]:


results= Soup.find_all('a', {'class':'_1fQZEK'})


# In[8]:


results


# In[9]:


len(results)


# In[10]:


results[0]


# In[11]:


results[0].text


# # Target Necessary Data:

# # Name
# # Price
# # Review Rating
# # Review Count
# # Product Id
# # Product Detail

# # Name

# In[12]:


results[0].find('div', {'class':'_4rR01T'}).get_text()                              ##  results were changed, need to check once  ##


# # Price

# In[13]:


results[0].find('div', {'class':'_30jeq3 _1_WHN1'}).get_text()


# # Old Price:

# In[14]:


results[0].find('div', {'class':'_3I9_wc _27UcVY'}).get_text()                         # Found Error


# # Rating Points:

# In[15]:


results[0].find('div', {'class':'_3LWZlK'}).get_text()


# # Rating Counts:

# In[16]:


results[0].find('span', {'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0', '  ').split('  ')[0]                               # Altered


# # Review Counts:

# In[17]:


results[0].find('span', {'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0', '  ').split('  ')[1]                             # altered


# # Product Details

# In[18]:


results[0].find('ul', {'class':'_1xgFaf'}).get_text()                      


# # Realtive URL:

# In[19]:


#extract the relative url:
results[0].find('a', {'class':'_1fQZEK'})


## Can't extract the relative url ##


# # Put everything inside a for - loop:

# In[20]:


modelname = []
price = []
oldPrice = []
ratings = [] 
ratingCounts = []
reviewCounts = []
productDetails = []

for result in results:
    
    #modelname:
    try:
            modelname.append(result.find('div', {'class':'_4rR01T'}).get_text())
    except:
            product_name.append('n/a')
            
    # price:
    try:
            price.append(result.find('div', {'class':'_30jeq3 _1_WHN1'}).get_text())
    except:
            price.append('n/a')
            
    # Old price:
    try:
            oldPrice.append(result.find('div', {'class':'_3I9_wc _27UcVY'}).get_text())
    except:
            oldPrice.append('n/a')
    
    #ratings:
    try:
            ratings.append(result.find('div', {'class':'_3LWZlK'}).get_text())
    except:
            ratings.append('n/a')
            
    #ratings counts:
    try:
            ratingCounts.append(result.find('span', {'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0', '  ').split('  ')[0])
    except:
            ratingCounts.append('n/a')
            
            
    #reviewCounts:
    try:
            reviewCounts.append(result.find('span', {'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0', '  ').split('  ')[1])
    except:
            reviewCounts.append('n/a')
                    
    #ProductDetail:
    try:
            productDetails.append(result.find('ul', {'class':'_1xgFaf'}).get_text())
    except:
            productDetails.append('n/a')


# In[21]:


len(modelname)


# In[22]:


len(productDetails)


# In[23]:


len(oldPrice)


# # Combine urls:

# In[ ]:





# # Create Dataframe in Pandas:

# In[24]:


Products = pd.DataFrame({'Name':modelname,'Price':price,'Old_Price':oldPrice, 'Ratings':ratings,
                        'Rating_Counts':ratingCounts, 'Review_Counts':reviewCounts,
                        'Product_Details':productDetails})


# In[25]:


Products


# In[26]:


# Successfully extracted for the 1st page:


# # Output in Excel

# In[ ]:





# # Part 2 : Pagination - Scrape 20 pages:

# In[29]:


modelname = []
price = []
oldPrice = []
ratings = [] 
ratingCounts = []
reviewCounts = []
productDetails = []

for i in range(1,406):
    
    # url:
    url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+ str(i)
    
    # request:
    response = rq.get(url = url)
    
    # Soup:
    Soup = bs(response.content, 'html.parser')
    
    # Result:
    results= Soup.find_all('a', {'class':'_1fQZEK'})
    
    # Loop through results:
    
    for result in results:
    
            #modelname:
            try:
                    modelname.append(result.find('div', {'class':'_4rR01T'}).get_text())
            except:
                    product_name.append('n/a')

            # price:
            try:
                    price.append(result.find('div', {'class':'_30jeq3 _1_WHN1'}).get_text())
            except:
                    price.append('n/a')

            # Old price:
            try:
                    oldPrice.append(result.find('div', {'class':'_3I9_wc _27UcVY'}).get_text())
            except:
                    oldPrice.append('n/a')

            #ratings:
            try:
                    ratings.append(result.find('div', {'class':'_3LWZlK'}).get_text())
            except:
                    ratings.append('n/a')

            #ratings counts:
            try:
                    ratingCounts.append(result.find('span', {'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0', '  ').split('  ')[0])
            except:
                    ratingCounts.append('n/a')


            #reviewCounts:
            try:
                    reviewCounts.append(result.find('span', {'class':'_2_R_DZ'}).get_text().replace('\xa0&\xa0', '  ').split('  ')[1])
            except:
                    reviewCounts.append('n/a')

            #ProductDetail:
            try:
                    productDetails.append(result.find('ul', {'class':'_1xgFaf'}).get_text())
            except:
                    productDetails.append('n/a')


# In[30]:


Products = pd.DataFrame({'Name':modelname,'Price':price,'Old_Price':oldPrice, 'Ratings':ratings,
                        'Rating_Counts':ratingCounts, 'Review_Counts':reviewCounts,
                        'Product_Details':productDetails})


# In[31]:


Products


# In[32]:


Products.to_csv('Products1.csv')

