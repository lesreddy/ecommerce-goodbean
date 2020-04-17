## Testing

- [**User Stories**](#user-stories)
- [**Validation**](#validation)
- [**Pages**](#pages)
- [**Responsiveness**](#responsiveness)
 - [**Bugs**](#bugs)


### User Stories

Referring user stories in UX of Readme Goodbean responds in the following way:


As a visitor to Goodbean I expect:
1. To find what I am looking for easily and effectively - Yes (simple easily navigatable design)
2. To use it effectively from any device including Mobile, Tablet and Desktop - Yes (fully responsive)
3. Be confident in the purchasing process so that it feels secure and reliable - Yes (stripe functionality)
4. To be able to make contact with Goodbean easily if needed - Yes (contact form)
5. To be given a premium high quality experience to match the premium nature of the product - yes (could be more polish here or there)
6. To be simple an uncluttered drawing my attention to the most important area of each page. - yes (again, simple design makes it clear)
7. To be able to search for products - Yes (search functionality)
8. To be able to review, edit and delete products - Yes can do a review but cannot edit and delete yet 
9. To access Social Media sites from the main site - Yes
10.  To access the location of the business from the main site. - Yes


### Validation

* Ran [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the css file and also [W3C Markup Validation Service](https://validator.w3.org/) to validate the html markup.

### Pages - Manually Tested Notes

#### Home Page

- Opens on the landing page and users can access the ordering secion if order now button selected
- scrolls down through through images 
- User can access all main pages from navbar, all work ok
- User can access all links in footer
- Future improvement would be to disable the search box until used (jquery)


#### Products Page

- User can see all products clearly 
- Future improvement would be to add more products and have a sub menu off the navbar with all different categories
- parallax scrolling works well
- There is an error when qty is 0 and 'view carts' is pressed.  The best way to resolve this is to remove the button and only when a qty is put in would the button appear (jquery or js)

#### About Page

- Users can see extra information about the products clearly and easily
- Originally wanted to wire the reviews through this screen but as I linked this page through the products app cluttering up.  In hindsight would have created a separate abouts app rather than a separate reviews app and wired all the about and reviews info through it.
- Future improvement would be to create a separate model for this page so that an admin user could create a new about card for each new product rather than hardcoding each additional product.

#### Login Page

- All links tested ok
- Login tests all ok

#### Password Reset Page

- Tested ok once deployed to Heroku

#### Cart Page

- Future improvement would be to enable the remove product icon (rubbish bin) this is not currently working.

#### Contact Page

- Everything tested ok on this page

#### Review Content Page

- Everything tested ok on this page

#### Review Details Page

- Small bug here on testing when review goes to 100 button moves down, on noticing too late to fix

#### Checkout Page

- Everything works fine on this page although styling needs improve when multiple quantities of product chosen

#### Profile Page

- No links work on this page, will fix in the future.
- When deployed to heroku had an issue with this page so had to redesign.

### Responsiveness

Goodbean was designed for mobile, tablet and desktop and on all tests I performed it was fully responsive.

### Django Testing

I did not attempt any in Django testing as my time was consumed by learing the other components of Django to put the project together.  This is a big opportunity for future learning.


### Bugs

- Gitpod caused me some bugs in developing.  An upgrade issue somehow caused a problem which meant losing a days work.  I attempted communicating directly with Gitpod to try and remedy an issue with the icon settings in Gitop IDE, each time I login I have to set something in preferences for them to work.  Currently still not fixed.

- Had many attempts at trying to fix the basic JS function which turns off the messages after 4 seconds.  Whilst it works it generates a null error in the console.  I know its something to do with firing the settimeout function only when required but couldnt completely fix.

-  Not exactly a bug but spent a good amount of time trying to complete the CRUD process in the reviews app, could not get the update (edit review) and delete (delete review) part of this process to work so its another future learning opportunity to complete this.