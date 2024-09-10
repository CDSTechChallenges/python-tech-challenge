# Welcome to CodigoDelSur Python Tech Challenge

To set up the app you will need Python3 on your environment. You will also need an API testing platform (we recommend Postman but you are free to use any platform of your choice) 

## Setup instructions
- Clone the repo
- You can create a virtual env
- Install dependencies from `requirements.in`
- Create a PostgreSQL database and setup the file `config.py` with the database uri
- Run the app -> `python3 app.py`
- In the API platform make a GET request to `http://localhost:<port(5000)>/api/health` and get a welcome message to confirm the server is running
- Run the app to create dummy data -> `python3 generate_data.py`
- Check and test that endpoints are working.
