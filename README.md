![Film Night Logo](#)

# Site Purpose
A demonstration website for a fictional online film store which would allow
a user to purchase both digital and hard copies of films for instant access
and product delivery. 

The user can browse a range of titles, add them to a shopping basket, amend
the basket and checkout securely. Their digitally owned titles appear in a
separated list and these titles are removed from the main shopping browsing
list for the user. Further hard copies of digitally owned films can be
purchased but the user is prevented from purchasing a digital film once it
is owned.

The user would be able to access the digital content via the site were this a
a real service.

# Contents

1. UX Experience
2. Features
3. Technologies Used
4. Testing
5. Deployment
6. User Guide
7. Credits
8. Contributing
9. Support
10. License

# User Experience
## User Stories
|Story ID |User Type |I want to … |So that I can … |
|---------|----------|------------|----------------|
A1|Store Admin|Amend pricing|Maximise revenue|
A2|Store Admin|Add a new title|Attract new and existing custom with new purchase choices|
A3|Store Admin|Delete a title|If its no longer available to prevent re-funds|
A4|Store Admin|Amend stock levels|To reduce risk of out of stock purchases|
A5|Store Admin|Have an automated stock reduction on successful order|Minimise manual stock management|
S1|Shopper|See all titles|Make a choice on what to purchase|
S2|Shopper|Filter and sort titles|So I can focus my attention on titles I will be interested in|
S3|Shopper|See more detail on a title|So I can make an informed decision on whether to purchase|
S4|Shopper|Identify the titles I already own|So I don’t purchase them twice by accident|
S5|Shopper|Add a title to my basket|So I can review before purchase and purchase multiple titles|
S6|Shopper|Edit my basket|So I can amend before purchase|
S7|Shopper|Checkout securely|To make a purchase with confidence|
S8|Shopper|Store my delivery/billing details for future purchases|To make it quicker to checkout next time|
S9|Shopper|Access the digital copies of my purchased items|To consume content immediately|
S10|Shopper|Save titles on a shortlist for potential future purchases|Make quick purchases on my return visits|
S11|Shopper|See my previous orders|For personal financial administration|
S12|Shopper|Logout securely|Prevent unauthorised use of my account|


## Design
The Film Night site was designed around User Experience Design Principles. Target 
users were identified and business and user goals were defined. A minimum viable 
product was determined that could achieve these goals. Future app and business 
potential was also mapped out. The scope was set to ensure the project remained 
concise and fit the strategy, and the front and backend structure reflected this 
scope whilst identifying the various technologies that would be used in 
the initial app version. The skeleton of the site was defined using wireframe models, 
which assisted in making key design decisions prior to commencing site construction, 
including site responsiveness considerations. Surface design was considered to identify 
suitable look and feel for this site, which is aimed at a consumer audience.

A review meeting was held following the initial UXD process which refined some areas 
including suitable technologies and the scope of the project.

### Strategy
#### Project Idea:
An online store where users can buy digital, DVD or Blu-ray copies of films. The films 
database comes from a Kaggle dataset of the top 1000 movies as rated on IMDB. 
A user can browse and filter a collection of movie titles which includes a description, 
image, actors, director and genre, select titles they are interested in to add to a wish list, 
add titles to a shopping cart in a format of their choice and purchase these titles using a 
secure payment method. They will need to register as a user to access any of the content as 
this is critical to consuming digital content purchased. The user can benefit from saving 
shipping details for future purchases.

#### Business Goals
Obtain a reasonable market share in the digital content streaming market, competing with the 
likes of Netflix and Disney+, and the online physical media format retail market largely dominated 
by Amazon by harnessing a USP of offering both in one place.

#### Target Users
This product is primarily B2C focused with the intent to sell films/movies in either a digital or 
physical format to the customer. Customers will want to access this service on a range of devices 
including mobile and traditional desktop environments. Users may want to shortlist their potential 
purchases into a wish list, which will encourage future purchases and return footfall. Return users 
would wish to see their historic orders and if an item is purchased from their wish list this item 
should be removed or flagged as purchased. All films could be flagged as purchased to a logged in 
user on any of the pages which display films, and a list of “my films” would be advantageous in order 
to access the digital content. 

The business wants a simple payment structure where digital only purchases cost the least, followed by 
additional DVD costs and premium costs for purchasing Blu-ray. All purchases could include the base digital 
copy. Costs should be weighted based on the rating of the film/movie. 

Potential B2B users could be film distributors or studios to promote their content and product, however 
these will not be the initial focus of the site as the first step is to build a client base. 

#### User Goals
Access a range of films/movies online and decide on a format to purchase these movies which suits them. 
Be able to make an informed decision on whether the movie is of interest to them based on key information 
such as genre, actors, director, and a brief description. 

Make quick purchases with minimal user input and see their purchase history. Items should be priced in a 
familiar and predictable manner.

Instantly view the titles they own and titles that they are interested in owning. 

#### Opportunity Assessment
An opportunities vs feasibility assessment was conducted in order to identify the key areas which the 
project will initially focus upon to inform the scope phase of the design process and ensure a minimum 
viable product can be developed initially which fulfils the core requirements of the app in order to function. 

[Opportunity Assessment Analysis](#)

#### Minimum Viable Product
- A Django project consisting of several apps:
    - Home
    - Movies (2x models)
    - Profiles (1x models)
    - Basket
    - Checkout (1x model)
- A relational database consisting of several models:
    - Movies (Movies)
    - Pricelist (Movies)
    - Profile (Profiles)
    - Orders (Checkout)
- A site consisting of the following pages, generated via a template structure:
    - Home/landing page
        - Intro to site and purpose
        - Link to sign in
        - Link to register
    - Register page
    - Sign in page
    - Browse movies page
        - See owned titles (via a quick filter)
        - See wished for titles (via a quick filter)
    - Basket page
        - Remove items, add hard-copy formats
    - Checkout page
    - Profile page
        - View past orders
        - Update delivery/billing address details

#### Future Development
- User reviews
- User ratings
- User interactions (direct tags/suggestions to others, view other wish lists)
- Promoted content/product


### Scope
### Structure
### Skeleton
### Surface

# Features
## Existing Features
## Future Features

# Technologies Used
## Languages
## Frameworks, Libraries & Programs
### Technology
#### License

# Testing
## W3C Validation
## Chrome Lighthouse
## Browser Compatability
## Responsiveness
## User Stories
## Known Bugs

# Deployment
## Live Hosted Site 
## GitHub Pages
### Fork the Repository
### Clone the Repository
## Python Package Requirements
## Environment Variables
## Database

# User Guide

# Credits
## Code
## Content
## Media
## Acknowledgements

# Contributing

# Support

# License