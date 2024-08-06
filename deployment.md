
1. install heroku cli :
```
brew tap heroku/brew && brew install heroku
```

2. log in 
```
heroku login
```

3. Prepare the app
   1. create requirements file
      ```
      pip freeze > requirements.txt 
      ```
    2. Create a `Procfile`: Create a file   named Procfile in the root directory of your project with the following content:
    ```
    web: python app.py # for Heroku
    web: gunicorn app:app # for render.com
    ```
    3. Create a `runtime.txt` file (optional): Specify the Python version by creating a `runtime.txt` file:
    ```
    python-3.11.6
    ```
4. Initial Git
   ```
    git init
    git add .
    git commit -m "Initial commit"
   ```
5. Push to github
    ```
    git remote add origin <your-repo-url>
    git push -u origin master
    ```
   you can also push using this remote address: `git remote set-url origin https://<TOKEN>@github.com/username/repository.git`


6. Create Heroku app
   ```
   heroku create
   ```
