# Blog with Django

## Project Scope
In this project, the idea is make a blog, containing posts with images, texts, author, create date, and other features. In addition, it also contains pages, that example "About me" or others, link to other web sites, search bar and search filters.
The focus of this project was the functionalities of the admin area, such as enabling or disabling parts of the page, the post cover, the search bar, create new pages and new post in the admin area, in addition to other administrative functions.

## Stacks and tecnical explications
At the back-end i used Python as a base, HTML and CSS for the front-end, PostgreSql as DataBase because is a power DB with exact pattern matching and i went to learn more about her in the practice, docker and docker compose to containerizing the versions and make possible run the aplication in others machines and the Django Framework because is a complete web framework with security (Such as Axes feature) and authentication features e develop base.

## Learnings
I learned work in the all process of a web aplication, since develop environment setup, back-end base, conections behind of the fininshed web site, the intersection between the Data Base, back-end and front-end, containerisation of aplications, and the Deploy process (At this project i don't mantain the Google Cloud Platform server activated because the costs are high for just one project, but in the future, i pretend develop a porfolio web site with all my projects together).

## Demonstration
<img width="1355" height="717" alt="image" src="https://github.com/user-attachments/assets/07c4bbdb-dd9b-4cc9-bda4-290ad03fb8eb" />
<img width="1351" height="723" alt="image" src="https://github.com/user-attachments/assets/c0d47768-4112-444f-80f9-7d76792eac4b" />
<img width="1364" height="721" alt="image" src="https://github.com/user-attachments/assets/359b9fcd-f38b-4ee1-a073-c91b28383538" />
<img width="1358" height="720" alt="image" src="https://github.com/user-attachments/assets/a190b0c3-2f2b-44cd-be0e-66166d0a539a" />
<img width="1357" height="723" alt="image" src="https://github.com/user-attachments/assets/f37bff1f-47f0-45d0-a7d4-788e23ab2b4e" />

## How to Run Locally (Setup)
To run this project on your local machine, you will need to have Docker and Docker Compose installed.

### 1. Clone the repository:

Bash
git clone git@github.com:GuilhermeANunes/projeto_blog_django_26.git
cd your-repository-name

### 2. Configure the environment variables:
   
Create a .env file in the root directory. You can use a .env.example file as a reference to set up your PostgreSQL database credentials and your Django secret key.

### 3. Build and start the containers:

Bash
docker-compose up --build

### 4. Create a superuser (to access the Admin area):

With the containers running, open a new terminal window/tab and apply the database migrations:

Bash
docker-compose run --rm djangoapp python manage.py createsuperuser

### 5. Access the application:
   
Open your web browser and navigate to http://localhost:8000
To access the administrative panel and test its features, go to http://localhost:8000/admin/

## Projects for the Future
Using this acquireds knowledges, i want make more robusts aplications, with more structured features and learn more about software develop, Software architeture, Data Science and CyberSecurity.

## Author and Contacts
I am Guilherme Nunes, a Corporate Banking professional transitioning into backend software development and technology. I have an extensive background in Corporate Finance, credit analysis, and accounting, with a track record of managing relationships with large-scale companies (BRL 50M to BRL 1B in annual revenue). I am leveraging this analytical expertise to build robust tech solutions, aiming to generate real business value and drive corporate growth through well-structured data and efficient backend architecture.

LinkedIn: https://www.linkedin.com/in/guilherme-nunes-cea-575596203
