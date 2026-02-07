# ECS639U Group Coursework

**Shakil** Assigned to develop the entire frontend and assist with backend development and testing and implemented Pinia stores for state management, configured Vue Router, set up Tailwind CSS styling, created CSRF utilities, contributed to backend API integration and performed testing of the app. 

**Riaz** Assigned to develop backend functionality including API endpoints and database models. Implemented Django API views for items (`items_api.py`), bids (`bids_api.py`), questions (`questions_api.py`) and notifications (`notifications_api.py`), created the auction closing service with email notifications (`auctions.py`), set up the cron job management command (`close_auctions.py`), and configured URL routing for all API endpoints.

**Jishad** Assigned to develop backend functionality including authentication and user management. Built the authentication system with login/signup views (`auth_api.py`, `auth_pages.py`), designed and implemented database models (User, Item, Bid, Question, Reply, Notification), created the profile API (`profile_api.py`), set up Django project configuration (`settings.py`), configured database connections, implemented statistics API (`stats_api.py`) and handled Django admin configuration.

Everyone did there assigned work.

Admin:
Username: shakil
Password: !@£$%^&*

Test Users:
Username: QWERTY
Password: qwerty12345678

Username: Shakil23
Password: Password: 12345678

Username: poiuytr
Password: 09876543

Username: test123
Password: point099

Username: helloworld
Password: worldhello


OpenShift Link: https://group22-web-apps-ec23087.apps.a.comp-teach.qmul.ac.uk


## Local development

To run this project in your development machine, follow these steps:

1. Create and activate a conda environment

2. Download this repo as a zip and add the files to your own private repo.

3. Install Pyhton dependencies (main folder):

    ```console
    $ pip install -r requirements.txt
    ```

4. Create a development database:

    ```console
    $ python manage.py migrate
    ```

5. Install JavaScript dependencies (from 'frontend' folder):

    ```console
    $ npm install
    ```

6. If everything is alright, you should be able to start the Django development server from the main folder:

    ```console
    $ python manage.py runserver
    ```

7. and the Vue server from the 'frontend' sub-folder:

    ```console
    $ npm run dev
    ```

8. Open your browser and go to http://localhost:5173, you will be greeted with a template page.

## OpenShift deployment

Once your project is ready to be deployed you will need to 'build' the Vue app and place it in Django's static folder.

1. The build command in package.json and the vite.config.ts files have already been modified so that when running 'npm run build' (on Mac and Linux) the generated JavaScript and CSS files will be placed in the mainapp static folder, and the index.html file will be placed in the templates folder:

    ```console
    $ npm run build
    ```

    If using Windows run

    ```console
    $ npm run build-windows
    ```

2. You should then follow the instruction on QM+ on how to deploy your app on EECS's OpenShift live server.

## License

This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to [CC0](http://creativecommons.org/publicdomain/zero/1.0/).
