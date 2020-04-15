
<p align="center">
<img src="https://i.ibb.co/k2Vgn7b/Readme-Logo.png" alt="Readme-Logo" href="https://les-goodbean.herokuapp.com/" target="_blank" rel="noopener" alt="Goodbean Logo" aria-label="Goodbean Logo" />
</p>

<br>


## Introduction

[Goodbean](https://les-goodbean.herokuapp.com/) is a student Website utilising many recently learnt skills encompassing HTML, CSS, BOOTSTRAP4, JAVASCRIPT(& JQUERY), and PYTHON.  It is builty using the DJANGO Framework and it showcases a mock ecommerce website selling premium coffee beans.  It is the final of 4 projects in for the Diploma in full stack development trough the coveted Code Institute. 

Click [here](https://les-goodbean.herokuapp.com/) to see the deployed app in Heroku.



## Table of Contents

1. [**Site Purpose**](#site-purpose)
2. [**UX**](#ux)
    - [Goals](#developer-goals)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)

3. [**Features**](#features)
    - [Current-Features](#current-features)
    - [Impending-Features](#impending-features)

4. [**Information Architecture**](#information-architecture)
    - [Models](#models)

5. [**Applied Technologies**](#applied-technologies)

6. [**Testing**](#testing)
    
7. [**Deployment**](#deployment)
    - [Local Execution](#local-execution)
    - [Heroku Deployment](#heroku-deployment)

8. [**Credits**](#credits)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

9. [**Final Notes**](#final-notes)


# Site Purpose

Goodbean is essentially a sales site so its main function and purpose is to sell as much premium coffee as possible on a safe and secure platform.

# UX

## Goals

### User Goals
1. Select suitable coffee using other customer reviews in flavour descriptive explanations
2. Buy from a trustyworthy online store.
3. Be drawn into the site with a stylish landing page and easy navigation
4. Create an online experience that conjurs a familiarity of what one would expect a coffee sales website to be based on coffee itself 
5. Quality product more of a focus than price sensitive value

### Business Goals
1.  Create a framework which seamlessly leads a potential customer to make a positive purchasing decision
2.  Be clear on what is marketed at every touchpoint of the site.
3.  Build up various interaction points through email subscription, contact page and review feedback to continually improve based on this feedback.
4.  Successfully market the premium aspect of the product to ensure price is not the main focus

## User Stories

As a visitor to Goodbean I expect:
1. To find what I am looking for easily and effectively
2. To use it effectively from any device including Mobile, Tablet and Desktop.
3. Be confident in the purchasing process so that it feels secure and reliable.
4. To be able to make contact with Goodbean easily if needed
5. To be given a premium high quality experience to match the premium nature of the product.
6. To be simple an uncluttered drawing my attention to the most important area of each page.
7. To be able to search for products.
8. To be able to review products.
9. To access Social Media sites from the main site
10.  To access the location of the business from the main site.

## Design

Goodbean is selling a premium coffee product so the design choices were based on what creates a premium feel and good colours and fonts associated with coffee.

### Fonts

'Amarand' was chosen for the main heading fonts which appeals covers off a premium, yet stylish feel which also resonates with a coffee feeling

'Open Sans' was chosen for the main secondary font which gives a clear and fresh feel.

### Colours

1. Main Site Colours - Black(#000), White(#111), GoldenRod(#DAA317), Wheat(#F5DEB3)


<div align=center>
<img src="https://i.ibb.co/sKs0LRN/Main-Site-Colours.png" alt="Main-Site-Colours" border="0">
</div>



2. Product Colours - OxfordBlue(#02114A), SpartanCrimson(#901616), MughalGreen(#2D6539)

<div align=center>
<img src="https://i.ibb.co/4WVbXzv/productcolours.png" alt="productcolours" border="0" />
<div>

The main site colours were chosen to align with an expected coffee style for the user and also strike a premium look

The product colours were chosen to really draw the attention of the user to them whilst matching in contrast to a premium shade.


## Wireframes

1. Mobile wireframes can be found at
2. Tablet wireframes can be found at
3. Desktop wireframes can be found at

# Features

## Current Features

1. Consistent Elements Throughout - this includes the navbar, main colour scheme and footer.
2. Home Landing Page - Sets the tone with a clean premium look which is designed to build value in the goodbean product.
3. Products Page - Showcases all products in a clean clear premium style design.
4. Accounts Function - Allows users to create new accounts, log in, register, log out and also has a profile page.
5. Search Function - Allows users to search for products.
6. Cart Page - Shows the products the user has selected.
7. Checkout Page - Shows the products the user has selected and allows user to enter payment details.
8. Google Maps API in footer - Allows user to click in to see exactly where Goodbean is located.
9. Parallax scrolling - Implemented on the products, reviews and about page.
10. User can add their own review on the review page and also see other reviews left by customers on that product.

## Impending Features

1. To get a working rubbish bin icon on the cart page, ie the user clicks on the bin and it removes the product
2. Create links from the profile page which allow users to edit their login and security details, payment options, address details and to track orders.
3. Add more products to the site.
4. Finish the review app, I found the code for creating the views for this page challenging, I need to learn more about the nuts and bolts of Python, Django and database manipulation to implement the full CRUD process here. Still need to put an Update (edit) review feature and Delete feature in this section.


# Information Architecture

During the build phase Goodbean used the built in to Django SQLite database, however on deployment to Heroku this changed to the PostgreSQL SQL compliant relational Database.

## Models

The Checkout, Home, Product and Review apps utilise models as part of their functionality.

### Checkout App

Order Model

| Name | Validation | Field Type |
| ----------- | ----------- | ----------- |
| full_name | max_length=50, blank=False | CharField | 
| phone_number | max_length=20, blank=False | CharField | 
| country | max_length=40, blank=False | CharField |
| postcode | max_length=20, blank=True | CharField |
| town_or_city | max_length=40, blank=False | CharField |
| street_address1 | max_length=40, blank=False | CharField |
| street_address2 | max_length=40, blank=False | CharField |
| county | max_length=40, blank=False | CharField |
| date | | DateField |

This Model was referenced directly from the tutorial in Code Institute, it is not my own original code.

OrderLineItem Model

| Name | Validation | Field Type |
| ----------- | ----------- | ----------- |
| order | Order, null=False | ForeignKey | 
| product | Product, null=False | ForeignKey | 
| quantiy | blank=False | IntegerField |

This Model was referenced directly from the tutorial in Code Institute



[![Build Status](https://travis-ci.org/lesreddy/ecommerce-goodbean.svg?branch=master)](https://travis-ci.org/lesreddy/ecommerce-goodbean)