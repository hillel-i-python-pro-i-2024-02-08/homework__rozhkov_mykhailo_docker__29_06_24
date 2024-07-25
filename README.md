# Homework Docker CLI App Example

This project is an example of using Docker with Docker Compose for a CLI app.

The app generates random human data and prints it in a console table.  
Also, all information about the app's work will be contained in the `app.log` file in the `logs` folder.  
You can customize the count of fake data in the table and the seed for faker in the `.env` file; just rename `.env.example` to `.env` and set the values.  
If you run the script in the terminal, use the CLI args option:

```shell
python app/main.py --count 7 --seed 10
```

## Run

To run the app from scratch, use the command below:

```shell
make d-homework-i-run
```

This will build the Docker image and run the container, which will use the seed and count values from the .env file and save logs into the app.log file.

## Dev

To start development with all dependencies installed, use the following command:

```shell
make init-dev
```

This will install all dependencies in a virtual environment to start working with the project.

## Tech stack

- **Python** - Main programming language
- **Docker** - Deployment
- **Compose** - Containerization
- **Faker** - Random data generation
- **Typer** - CLI arguments
- **Rich** - Beautiful console output
- **python-dotenv** - Reading .env variables
