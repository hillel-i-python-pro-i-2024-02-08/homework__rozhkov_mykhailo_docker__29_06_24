# Homework docker CLI app example

This project is an example of usage docker with docker compose for CLI app

The app generate random human's data and print it in console table  
Also all info about app work will contain in file app.log in logs folder  
You can customize count of fake data in table and seed for faker in .env file; just rename .env.example in .env and set values  
If you run script in terminal use cli args option:

```
python app/main.py --count 7 --seed 10
```

## Run

To run the app from zero use comand below:

```
make d-run
```

This will build docker images and run container which will use seed and count values from .env in work and save logs into app.log file

## Dev

To start dev with install all dependencies use next command:

```
make init-dev
```

It will install all dependencies in virtual environment for start work with project

## Tech stack

- **Python** - Main PL
- **Docker** - Deploy
- **Compose** - Containering
- **faker** - Randomazing data
- **typer** - CLI args
- **rich** - Beatiful output in console
- **python-dotenv** - Reading .env variables
