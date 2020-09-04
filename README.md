# Games, Ready, GO!

Deployed app:  https://milestone-4-gamesreadygo.herokuapp.com/

#### The brief for this project was –
This website was built to allow customers to purchase dog training sessions with a qualified concept based dog trainer. The site gives information about the type and methods of training; a way to contact the training company to ask any questions; a way to purchase various training packages - each with different inclusions; to register for an account and view ad update their profile details. The website allows users to see the new services the company will soon be providing.

## UX

This website is for customers that want to learn how to train their dogs through brain training games, or to target a specific behaviour problem that they are having.

### The user stories are -

**Customers of the website - I want to be able to**
* 	View services being offered so that I can select which one I want
*	Read about the company and style of training to decide whether it is right for me
*	 See future services that the company will be offering in order to plan future training goals
*	Register for an account to buy services and view online content
*	Log in and out to access my account
*	Recover forgotten account details
*	Receive confirmation of my order and registering of my account to verify these have been successful
*	 Have a user profile to view previous orders and store my information
*	Checkout securely to be confident in my purchase
*	Receive information on how to book sessions after purchase

**Site Owner - I want to be able to**
*	Receive an order
*	Obtain customer details
*	Take secure payments

## Wireframes

Please refer to the wireframes folder for individual page wireframes. 

## Features

**Existing Features**

*	**Homepage** – The homepage welcomes users the dog training website. There is a navigation menu bar at the top of the page, images to illustrate dog training throughout; a button directing to the training product page; a section to tell the user about the company and style of training or services they provide; and a contact form.
*	**Nav bars** – There are two nav bars in this website. The main nav bar on the desktop view comprises of the company logo which if clicked, directs users to the homepage; the page links which include Home and Training, these direct to the appropriate pages. There is also a Contact link which directs to the contact form on the homepage. On the right hand side of the nav bar there is the My Account dropdown menu which allows users to log in or out, register, or view their profile information. On a mobile view, the main nav bar collapses down to a drop down menu which encloses all of the previous links mentioned above. 
*	**Buttons** – There are various buttons used throughout the website to submit forms or to transfer to other pages or sections of the website.
*	**Coming Soon section** – This section allows the user to see what future services the company plans to offer. This allows them to plan ahead with their training needs.
*	**Contact Form** – The contact form on the home page allows users to make an enquiry with the company. Upon completion and submitting the form, the company will be sent an email containing the details entered into the form, and the user will receive an email confirming their form submission.
*	**Footer** – The footer contains the company logo which if clicked, takes the user back to the homepage; social media links which take the user to the respective social media websites; contact information for the company; and website links which take the user to the various pages on the website.
*	**Product Page**  – The services available are listed in cards on this page. The service is listed, along with the price and list of features included. The customer can click a button to take their selected product through to the checkout page. 
*	**Testimonials** – The testimonial section allows customers to see reviews of the services that they have received. 
*	**Checkout Pages** – The checkout page shows the product the customer has selected, and as the customer has had to log in to access this page, their details have been updated, and there is a form to enter the payment details and submit or cancel buttons. Following successful payment, the customer is directed to success page which gives further information and has a button directing back to the homepage. If the payment fails, the customer is directed to an error page which states no payment has been taken, with a button to take them back to the product page to retry their purchase.
*	**Profile Pages** – It is required that the customer signs up to account to make a purchase. Following sign up, they will need to verify the email address provided. They can then purchase a service, and view their profile information, reset passwords, update profile information and log in and out as needed. 



**Features Left to Implement**

*	Order information being saved to the database and being available to view and edit in the Django admin pages. With previous projects during this course, I have extended my deadlines in order to fix all the bugs and make the project the best that I feel it can be. This has hampered my progress and is not comparable to the real working environment where a deadline will not be able to be extended. Because my final deadline was upon me, I have made this functionality into a future feature to be implemented. Please see the debugging section for further information regarding this. 

*	Users being able to edit their profile information on the website. Due to time constraints I was not able to implement this fully for this project. 

*	Added defensive design into the contact form so that only valid email addresses can be submitted.  

*	Pages to add to the website include – a blog, a monthly club subscription service and online classes.
*	An online booking system so that customers can book the training sessions that they have purchased directly on the website.


## Technologies Used

**Balsamiq** – used to create the wireframes for the project.

**Bootstrap** – this framework was used to style, structure and create a responsive site.

**CSS** – used to style the site.

**Django** - object relational mapper, HTML templating, URL routing, form validation, authentication and admin.

**Django-Crispy-Forms** - styling of Django template forms.

**GitHub** - used for version control.

**Gitpod** - used to write the project code.

**Heroku** – used to deploy the project.

**HTML** – used to structure the site.

**JQuery / Javascript** - used for the interactive elements on the site.

**Markdown** - Readme was generated using markdown.

**PIP** - used to install extensions.

**Python** -  the project back-end functions are written using Python. 

**Stripe** - the payment API utilised for the checkout app of the project.

## Testing

All testing of the website was done manually. I was not able to run the HTML through any online validators as they could not get past the Django style of extending from other files.

*	**Home Page**
    *	Play now button - directs to product page - PASS

*	**Contact Form**
    *    All fields complete and valid - allows user to submit the form, and send email to company with details entered into the form – PASS
    * User received an email confirmation for submission – PASS
    * Some fields not complete - error shows – PASS
    * Fields not valid - error stating components that must be included to be valid – FAIL. Form allows submission with any data in fields (eg not a valid email address), see features left to implement for more information.

*	**Nav Bar - Desktop View**
    *   Company Logo - directs to home page - PASS
    *   Home - directs to home page - PASS
    *   Training - directs to product page - PASS
	* My Account - if user is logged in loads my profile, log out options in drop down menu – PASS
if user it not logged in loads register or log in options in drop down menu - PASS
	* Register - directs to sign up page - PASS
	* Log in - directs to log in page - PASS
	* Log out - directs to log out page - PASS
	* My profile - directs to profile page - PASS


*	**Nav Bar - Mobile View**
    * Dropdown menu loads when button pressed – PASS
    * Links all work as above - PASS

*	**Register for Account**
    *   All fields complete and valid - allows user to press sign up and register - PASS
	* Some fields not complete - error shows - PASS
	* Fields not valid - error stating components that must be included to be valid - PASS    
	* Confirmation fields not matching - error stating components that must be included to be valid - PASS
	* Back to log in button - directs to log in page - PASS
	* Sign in link - directs to log in page - PASS


*	**Log In / Log Out**
    *   Log in - directs to sign in page - PASS
	* Previously saved information - loads from the database to the correct fields - PASS
	* Sign in button - logs user in and directs to home page - PASS
	* Home button - directs to home page - PASS
	* Sign up button - directs to sign up page - PASS
	* Log out - directs to log out page - PASS
	* Cancel button - directs to home page - PASS
	* Log out button - logs out and directs to home page - PASS
*	**Password Reset**
    *   Back to login button - directs to sign in page - PASS
	* Fields complete and valid - reset password button pressed and email sent to user - PASS
	* Fields not valid - error stating components that must be included to be valid - PASS


*	**Footer**
    *   Company logo - directs to home page - PASS
    *   Social media links - directs to each social media website - PASS
    *   Home - directs to home page - PASS
	* Training - directs to product page - PASS
	* My account - if user not logged in - directs to log in page, then on to profile page - PASS
	 if user is logged in - directs to profile page - PASS

*	**Product Page**
    * Loads different products available from the json file in the database - PASS
	* Buy now buttons - if the user is logged in - directs to checkout page with specific product information passed through to the order details table- PASS
	if the user is not logged in - directs to log in page, then on to the checkout page with product information passed through to the order details table – PASS

*	**Checkout Page**
 	* Loads the product information from the product database into the order details table - PASS
    *   Loads the user details from the database into the user details section - PASS
	* Amend button - directs to edit profile page - PASS
	* Cancel button - directs to product page - PASS

*	**Stripe Payment** *   
	* Stripe success test card (4242 4242 4242 4242) - order completed, payment sent through to stripe, user directed to checkout success page - PASS
    *   Stripe error test card (4000000000003220) -  no order generated on stripe, directs payment fail page - PASS
	* Fields not complete - error stating required fields - PASS
	* Fields not valid - error stating components that must be included to be valid - PASS

*	**Checkout Success**
    * Gamechanger button - directs to homepage - PASS

*	**Checkout Fail**
    *   Try again button - directs to product page – PASS

*	**Profile Page**
    *   Loads the user information from the database - PASS
    *   Update button - directs to edit profile page - PASS

*	**Edit Profile Page**
    *   Advises of how to update profile information - PASS
	* Back button - directs to profile page - PASS



## Responsiveness of site:

To aid in creating a responsive site, I used Bootstraps Grid System and CSS. I checked the various break points to see if the page layouts worked on various device screen sizes, using Chrome Developer Tools. This was mostly done at the end of the project and was very time consuming. In future, I will endeavour to build responsiveness into my websites as I am building them.

**Nav bar:** For mobile views for the project, users will see that the full desktop nav bar is reduced to a menu button, which activates a dropdown menu containing the nav bar elements. 

**Page layout:** I experimented with various column sizes and layouts to achieve a site which was visually appealing and appropriate to the screen size it would be viewed on.
I had some problems when deploying to Heroku. The app changed some of the screen sizes that I had been working with in gitpod, which in turn knocked some of my styling out. I have fixed this as well as I can without redoing all the media queries as this meant having to deploy to Heroku to check the sizes each time a change was made. 

## Debugging:

**Issue:** Product information not passing through to the checkout page.

**Solution:** After spending many hours and days working on tweaks to my forms, models and views; I reached out to tutor support and after discussing with them, it was found that I need to add 'pk' into my checkout url on the product page. 

**Issue:** Orders not being added to the database, not showing in the backend admin.

**Solution:** Again, after spending days on this issue, trying various amendments and solutions that I found on google and Slack; I consulted tutor support. I was unable to utilise the advice they gave as I had problems with migrating my data. When this was resolved, I contacted tutor support again but was not successful in obtaining a solution to my problem. Because of time constraints and because the order information is available in the stripe dashboard, I decided that I could not spend any longer on this and sacrificed this functionality in order to meet my deadline. I left the code that I was working on in my files to 'show my working'.


**Issue:** Error when migrating models.

**Solution:** Previous migrations were deleted, ran migrate again and it was successful. 

**Issue:** Updated user information not passing through to the database.

**Solution:** Due to time constraints, I was unable to continue to work on this function and amended my project so that the user was directed to an information page detailing how to edit their profile. 

**Issue:** Stripe payments not working on Heroku.

**Solution:** Stripe keys input into the Heroku environment variables and settings.py amended to direct to these.
 
## Deployment

I used Gitpod to develop this project, along with Github for version control.
When I reached completion of the project, I then deployed to Heroku. 
All environment variable and secret keys have been stored inside an env.py file which has been hidden with the .gitignore command. This is to ensure the security of the website. Images have been stored on www.imgbb.com and static files are run from within the website static files. 

In order to develop my project I had to create a Github repository, and use this throughout the development process store all the versions of my project. Once the project was almost complete, I set up a Heroku app and linked it to my Github repository. I then added all relevant Config Vars to Heroku. This included things like the database url and secret keys stored in my env.py file.
Finally, with everything finished, I did a final push to Github and deployed to Heroku. 

In order to use this repository, you would need to clone the repository on Github, and follow the steps in your IDE to complete the clone process. 
You would need to run the following command in the terminal to set up the required features:

$ sudo pip3 -r install requirements.txt

All secret keys for Stripe, Production and Django settings in Heroku will need to be obtained individually by using a Django secret key generator. 

## Credits

*	This project was based on the Boutique Ado and Ecommerce mini projects in the Django module of the Code Institute Full Stack Developer Course.

*	Guidance on the models, forms and views were obtained from the projects, queries on Slack and tutor support.

#### Content

*	The content in the “about us, gamechanger section” on the homepage was taken from [Horton Dogs](http://www.hortondogs.co.uk/about "Horton Dogs"). All other content was written by myself.

*	This README file is based on the Code Institute template.


#### Media

*	The photo used in the coming soon blog image is my own. All other photos used in this site are from Google Images.
