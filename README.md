# Timepiece
[View the live project here](https://malikdobbs-timepiece.herokuapp.com/)

[View the repo in GitHub](https://github.com/malikdobbs/timepiece)

* This is the promotional website for Timepiece. Timepiece is an watches e-commerce store where users can find luxury watches to buy and share some of their favourite watch designs with their friends, family members and anyone else. 

## User Experience (UX)

### User Stories

* As a customer I want to easily understand the main purpose of this website and whether i wish to return to this website for future visits
* As a customer I want to be able to find different products and descriptions on the watches sold that may be of interest to me
* As a customer I want to be able to click on the products through the click of 1 button
* As a customer I want to have the ability to create an account if i wish to join your community
* As a customer I want to be able to log into my own account easily
* As a customer I want to be able to log out of my own account
* As a customer I want to be able to create a profile so that i can view any orders i have created, update my delivery information in case i want to order more products
* As a customer I want to be able to search for products easily, to find what i am looking for
* As a customer I want to be able to easily navigate throughout the website without having to look all over for navigation links
* As a customer I want to be able to view products I've added to my shopping bag/cart
* As a customer I want to be able to remove/update items from my cart in case I change my mind or added something to my bag/cart by mistake
* As a store owner i want to be able to edit my products and update info such as price, images, description etc
* As a store owner I want to be able to delete my recipes
* As a fstore owner I want to be able to search recipes by either there name or description of that recipe

## Scope

Timepiece is centered around the CRUD (create, read, update and delete) functionality and has been created using Django framework system for creating the application using jinja notation, HTML, CSS, JS and Python. The features I want to implement to this app, as follows:

* CRUD opeations to allow users interaction with the app
* Functionality to allow users to purchase products from our website
* Functionality to allow users to view products
* Functionality to allow users to view blog post and comment on blogs
* Functionality to allow super users to add, edit and delete products from the store
* Functionality to allow users to search fproducts
* Functionality to allow users to create an account
* Responsive design and beautiful looking application on all devices

## Structure

* Products will be stored in the app on the Products page for all users to view. Each product has a product detail page which can be viewed by clicing on the specific product card/link in the products view
* Users will be able to search for products via either the name of a product or key words from the description of the products on the website
* Users will be able to add items to their basket, edit and remove products from their basket via easy to use navigation buttons
* Store owners will be able to edit or delete products via simple and easy to use buttons on the products and products details page

## Skeleton

Find below links for my wireframes, showing how i planned for my web pages to be structured and layout on different device sizes such as laptop, tablet and mobile:

### Wireframes

The Wireframes have been creating using balsamiq:

* [Index Page](https://github.com/malikdobbs/timepiece/blob/main/media/Home%20Page.png)

* [Log In Page](https://github.com/malikdobbs/timepiece/blob/main/media/Login%20Page.png)

* [Register Page](https://github.com/malikdobbs/timepiece/blob/main/media/Register%20Page.png)

* [Products Page](https://github.com/malikdobbs/timepiece/blob/main/media/Products%20Page.png)

* [Product Details Page](https://github.com/malikdobbs/timepiece/blob/main/media/Product%20details%20page.png)

* [Add Product Page](https://github.com/malikdobbs/timepiece/blob/main/media/Add%20product%20page.png)

* [Edit Product Page](https://github.com/malikdobbs/timepiece/blob/main/media/Edit%20Product%20Page.png)

* [Contact Us Page](https://github.com/malikdobbs/timepiece/blob/main/media/Contact%20Us%20Page.png)

* [Blog Page](https://github.com/malikdobbs/timepiece/blob/main/media/Blog%20Page.png)

* [Blog Post Page](https://github.com/malikdobbs/timepiece/blob/main/media/Blog%20Post%20Page.png)

## Surface

### Design

Timepiece uses [Bootstrap](https://materializecss.com/) as a framework to help create a beautiful website that users will enjoy viewing and using. Bootstrap helped to create the layout of the web page using divs, cards, navbars and forms for a simple, easy to use and interactive website for users to create and share recipes. Also, Google Fonts has been imported into my CSS file for good looking typography. The colour scheme I have used is to represent a  simple and classy webpage

* #3A3845 is the main colour used throughout the website. This has been used as the main colour throughout the whole website and on the navbars
* #F3E9DD is used as the font colour for most of the font throughout the website
* Syncopate has been imported from Google for all headers and navbar elements
* Montserrat has been imported from Google to be used as my secondary font for all other information throughout the website.

## Features

* The navbar has a logo in the top left hand corner which if clicked, will take users back to the home page. The navbar also displays different links to the user depending on whether they're logged in or not.
* If the user has an account and is logged in they will be able to view the following: profile page, all products, watches, accessories, jewellery and blog  dropdown navbar link, and log out. 
* If the user is not logged into the website the links visible to them will show as follows: all products, watches, accessories, jewellery and blog  dropdown navbar link, and log in and register links.
* Users have the ability to add and remove items from the shopping bag.
* Users have the ability to create an account and log in to the store
* Users can search for any of the products in the store by using keywords or the exact product they're looking for.
* Users can see detailed information for any product they've clicked on and choose the quantity of how many items they want to purchase
* If the user is a store owner and logged in they will have an additional link to "Product Management" so that they can add or remove products from the store
* The website has been created to be visible and accessible on different device screens such as: Android, IOS, Windows, MacBooks and tablets.
* All visitors can search for products on the website via the search box on all pages throughout the e-commerce store
* Registered users can edit and delete their profile information, by navigating to their profile link via the navbar and updating information if they choose to

## Future Features

* Create a contact us form for users to get in touch with the owner of the website if they have any complaints or feedback to provide regarding their experience using Timepiece e-commerce store
* I would like to implement a function that allows users who have created an account to create new blog posts to share information with the community
* I would like to incorporate a newsletter feature for users where they will receive advice on new products coming out soon, watch/jewellery care and special/promotional offers etc


## Deployment

### Heroku Deployment

To Deploy your app to Heroku, please follow the steps below:

1. Login to Heroku
2. On the main dashboard, create a new app
3. Give your app a name, select your region where you reside
4. Select deploy tab at the top of the page and scroll down to deployment method
5. Select GitHub as your deployment method
6. Login using your GitHub login details
7. Enter your username and search for the repository in the repo-name box
8. Connect to the specific respoitory you wish to connect to
9. Beneath manaul deploy, choose your branch and select deploy branch
10. Enable automatic deploys
11. Your project is now deployed
