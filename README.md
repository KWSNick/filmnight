![Film Night Logo](static/media/filmNightLogo.png)

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

[Opportunity Assessment Analysis](static/docs/opportunityAssessment.pdf)

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
- Multiple pages
    - Use a full stack framework to build a template page structure to speed up development and reduce 
    code duplication.
    - Use a modified HTML/CSS/JS Library Navbar component.
        - Various navbar items only visible depending on login state/user authorisation
    - A Visually appealing logo that clearly informs the user of the brands purpose.
    - Use of card-components to display individual items within databases i.e. movies. 
    - Use database item fields to sort, filter and search for items i.e. rating, genre and name. 

At the scope stage of the planning process the user stories (presented at the top of the User Experience 
section) were identified and mapped out.

### Structure
#### Database
A relational database was used consisting of four data tables to hold data on the films in the store,
user profile information, order histories and a pricelist.

![Planned Database Structure](static/media/plannedDatabaseStructure.jpg)

SQlite will provide the relational database during production and Postgres will be used to provide the 
relational database in final deployment. 

#### Site Pages
The site will be based around a framework template design, offering a common navbar and footer throughout, 
however content within the navbar and footer may alter depending upon the user-login state, current page etc. 

All authorised pages will be accessible from all other pages. 

Forms will utilise a common styling and restrict user input to defined options where possible to aid document 
grouping and linking. Forms will offer validation where possible. 

Django will be used to provide the framework using its built in templating language.

Bootstrap 5 will provide the library for styling of the site as it is designed to be responsive across devices 
and focus on mobile media sizes. 

JQuery will be utilised for any Javascript functionality to speed up development. 

![Planned Site Structure](static/media/plannedSiteStructure.jpg)

### Skeleton
The site will be responsive across all device sizes and utilise Bootstrap 5 breakpoints to achieve this. The site 
will be equally user friendly on any device size. 

|Breakpoint	|Class infix |Dimensions |
|-----------|------------|-----------|
|X-Small| None| <576px |
|Small| sm| ≥576px |
|Medium| md| ≥768px |
|Large| lg| ≥992px |
|Extra large| xl| ≥1200px |
|Extra extra large| xxl| ≥1400px |

Common device sizes are:
- Mobile Phones
- Recreational Tablets 
- Professional Tablets 
- Laptops and Desktops
- TVs, projectors and high definition monitors

[Wireframes](static/docs/Wireframes.pdf) were constructed in Pencil Wireframes in order to provide a design brief for the project and map out key
design features prior to app production, maximise coding productivity and minimise mission creep. The final product is 
compared to the wireframes within this document.

### Surface
The site is designed for general consumers so needs to appeal to this potential customer base with a recognisable, 
memorable brand. It should clearly convey as much of the purpose of the site as is practicable within its title, 
supported by short succinct content immediately displayed to users upon their initial visit. Brand name ideas were 
brainstormed along with potential logo icons.

#### Name Ideas
- Film House
- Projector Room
- Projectionist
- Film Can
- Magic Lantern
- Film Shack
- Film Night
- Motion Picture Store
- What to Watch

![Logo Icon Ideas](static/media/logoIconIdeas.jpg)

#### Colours
Many existing streaming services use dark background colour schemes with contrasting light text. This site will conform 
to this convention, using grey to black gradients and solid black backgrounds with, white, off-white/grey and red text 
to provide the user with the expected feel of a movie streaming and purchase site. 

Buttons will utilise expected colour conventions, Green for positive call to actions such as sign in, sign up and add to 
basket, grey for less favourable options such as return to browsing and red for delete and remove functions. 

![Planned Colour Pallette](static/media/plannedColorPallette.jpg)
Colour palettes were collated using material designs colour tool https://material.io/resources/color 

Where icons are used they will be suitable to describe the function, heading or label they are associated with.

#### Fonts
As a site which aims to appeal to the consumer some display stylisation is desirable for some headers and key links, 
however the main body of content should be plain, easily readable, but also be space efficient due to the small card 
area available for individual items on the pages which utilise cards. 

A short list of handwriting style fonts was identified from Google fonts for the header. Of this shortlist Zilla Slab 
Highlight was selected to provide header font sparingly. 

![Header Font Shortlist](static/media/fontHeaderShortlist.jpg)

A short list of handwriting style fonts was identified from Google fonts for the main body text. Of this shortlist 
Barlow Semi Condensed was selected as it clear legible text which was not highly weighty, whilst being space efficient 
through its slightly condensed nature. 

![Body Font Shortlist](static/media/fontBodyShortlist.jpg)

# Features
## Existing Features
*Requires Content*

## Future Features
- User can leave reviews
- User can rate films
- User can provide interactions (direct tags/suggestions to others, view other wish lists)
- Promoted content/product from third party partners

# Technologies Used
## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/), [Python BSD 0-clause License](https://docs.python.org/3/license.html#bsd0)

## Frameworks, Libraries & Programs
### [Django](https://www.djangoproject.com/)
Django is a full stack framework based on python, designed to allow developers to quickly create apps.
It was used as the foundation for this project, providing the templating, and functionality such as URLs.

#### License
Django is an open source project and can be utilised under the 
[BSD 3-clause](https://github.com/django/django/blob/main/LICENSE) license.

### [JQuery](https://jquery.com/)
jQuery is a JavaScript library designed to make html traversal and manipulation much simpler than raw JavaScript, 
by presenting the author with a wealth of simple code and commands which call on much more complex functions.

jQuery was utilised to improve the targeting of elements and provide some support for animation and user interaction 
where possible.

#### License
jQuery is provided under the [MIT License](https://tldrlegal.com/license/mit-license)

### [Google Fonts](https://fonts.google.com/)
Google Fonts offers open source font styling options for personal and commercial use. 2 fonts were used within this project.

### [Font Awesome 5.15.3](https://fontawesome.com/)
Font Awesome provided various icons for the project through its free service. 

#### License 
[Font Awesome License Page](https://fontawesome.com/license)
[Icons are licensed under the CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
[Fonts are licensed under SIL OFL 1.1](https://scripts.sil.org/OFL)
[Code is licensed under MIT](https://opensource.org/licenses/MIT)

#### License
The use of this product was inline with Google API's terms of service [Google Fonts Terms](https://developers.google.com/terms)

### [Bootstrap 5](https://getbootstrap.com/)
Bootstrap is a mobile-first HTML, CSS and JavaScript Library which provides responsive design tools that were applied to
this project. 

#### License
Bootstrap is used under the [MIT License](https://github.com/twbs/bootstrap/blob/main/LICENSE)

### [LogoMakr](https://logomakr.com/)
LogoMakr is an online logo creating environment and was utilised to create the logo for the project. 

#### License
[LogoMakr is approved for both personal and commercial use.](https://logomakr.com/getstarted/terms-conditions/)

### [Git](https://git-scm.com/)
Was used for version control in the IDE via the terminal. 

#### License
Git is released under the [GNU General Public License](https://opensource.org/licenses/GPL-2.0)

### [GitHub](https://github.com/)
The projects' code is stored on GitHub.

### [Heroku](https://www.heroku.com/)
The live site is hosted on Heroku, which is connected to the GitHub repository.

### [PostgresSQL](https://www.postgresql.org/)
Is an open source object relational database system. This project utilises Postgres as an add-on within Heroku to store the
data required for the live project. 

#### License
Postgres is open source and released under a bespoke [PostgresSQL license](https://www.postgresql.org/about/licence/) 
similar to the BSD or MIT licenses.

### [SQLite](https://www.sqlite.org/index.html)
Is an open source C based relational database engine and was utilised as the data store within the development area.

#### License
SqLite is [public domain](https://www.sqlite.org/copyright.html)

### [Pencil](https://pencil.evolus.vn/)
Was used to create the wireframes during the planning phase. 

# Testing
*Requires Content*

## W3C Validation
*Requires Content*

## Chrome Lighthouse
*Requires Content*

## Browser Compatability
*Requires Content*

## Responsiveness
*Requires Content*

## User Stories
*Requires Content*

## Known Bugs
*Requires Content*

# Deployment
The Site is stored on GitHub pages and hosted on Heroku. These are linked by connecting the github repository to the 
Heroku app workspace.

It consists of 1 Master branch and no other branches. 

## Live Hosted Site
*Requires Content*

## GitHub Pages
The GitHub Repository for containing the source code for this project can be found here: https://github.com/KWSNick/filmnight

### Fork the Repository
To make a copy of this repository form the master GitHub pages to your own GitHub account:
1. Log in to GitHub using your credentials. 
2. Navigate to the repository given above. 
3. Locate the "Fork" button in the top right of the repository page, on the same line as the repository name. 
4. Click the "Fork" button and the project will be copied into a new repository in your account.

### Clone the Repository
To make a copy of the forked repository within your github account:
1. Log in to GitHub using your credentials.
2. Go to your repositories.
3. Open the repository you wish to clone. 
4. Locate the button above the repository table labelled "Code" with a download icon. 
5. Copy the HTTPS link provided. 
6. Open your chosen IDE on your machine and navigate to a terminal.
7. change your working directory to where you would like your clone to be created.
8. Type 'git clone' and paste the HTTPS link you copied.
9. Press enter and your local clone will be created. 

## Python Package Requirements
*Requires Content*

## Environment Variables
*Requires Content*

## Database
*Requires Content*

# User Guide
*Requires Content*

# Credits
## Code
*Requires Content*

## Content
### [Kaggle IMDB Movies Dataset](https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
The data used to create the movie database for this project came from a [Kaggle](https://www.kaggle.com/) Dataset 
collated by **Harshit Shankhdhar** who initially harvested it from [IMDB](https://www.imdb.com/) via webscraping methods.

Kaggle allows users to publish and find datasets for use in projects such as machine learning and web development. 

#### License
The IMDB Movies Dataset is provided under the [Creative Commons Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
License. 

## Media
### Database Images
The poster images were provided via URL link contained within the Kaggle dataset. These are hosted on Amazon Web Services.

*Requires Content*

## Acknowledgements
*Requires Content*

# Contributing
This project is a closed example for educational and ability demonstration purposes. Contribution is not permitted at 
this time.

# Support
For queries or support contact nicholasbowley@googlemail.com.

# License
This site is licensed under the 2-Clause BSD License

Copyright 2021 Nicholas Bowley

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the 
following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following 
disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following 
disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE 
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.