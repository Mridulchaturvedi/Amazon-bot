# Amazon-bot
this is a automated bot having many small yet interective functions like:-

PRODUCT DETAILS PAGE :--  

					 This function is automated using SElenium library to open amazon page and take user to detail page of inputed keywords mainly work on pages which is having html classes of one product per line the page is limited to mobile or electronic catagories 
   :-- 

 NOTE :- function can only be ascess through bot with keyword like buy,details,add to ,cart 



 SCRAPER :-- 

					 This Function is main foucus of project it takes user arguments as input for amazon search field and retrive all data on that page and after converting it to nice dataframe show back to user which is understable,module used for this function is beatufull Soup and pandas for dataframe  

 NOTE :- function can be ascess through bot or function menue with keyword like buy,details,add to ,cart 

 AMAZON always changes its ui and features so there is possiblities of errors which can be rectified by just changing single line in soup 



 Todays Deal :-- 

					 This is bot module which takes user argument and takes user to todays Deal section on Amazon where user can select deals and offer which ever user find interesting   

 NOTE :- function can be ascess through bot only with keyword like Offer,deals,todays offer 

 AMAZON always changes its User Interface so there is possiblities of  opening anather page which can be rectified by just changing single line in soup 



 DATE AND TIME :-- 

					 This is simple function which displays todays DATE in Graphity form  

 NOTE :- function can be ascess through bot only with keyword like todays,date 



 PRICE PREDECTION :-- 

					 This is Function contains SUPERVISED LEARNING for predecting price of product with user input of some co related features in this model we used Random Forest for predection AS other regresin models not Performing Well this Model Alread have Scraped Data file Attached From which it Takes Training and testing sets And Predicts Price . Still Tuning of some features Required on this Model 

 NOTE :- function can be ascess through bot or function menue with keyword like Predict 

 Module Needs Some Tuning and Features Training if Accurasy Is below 40% above 60% is good & Considerable 


 SCRAPER :-- 

					 This Function is main foucus of project it takes user arguments as input for amazon search field and retrive all data on that page and after converting it to nice dataframe show back to user which is understable,module used for this function is beatufull Soup and pandas for dataframe  

 NOTE :- function can be ascess through bot or function menue with keyword like buy,details,add to ,cart 
 
 
 all these functions are automated which also include opne chrome by bot and navigate throug given command
