# EVopt

## What does it do?

EVops is a submission to the PA Raspberry PI Competition 2023. In accordance with the prompt of "accelerating the energy transition",
EVops aims to optimize the placement of EV chargers within the UK.

## How does it do this?

The script accesses traffic and count points from the Department of Transport and optimises the placement of ev chargers for profitability. This is done with a genetic algorithm, with fitness calculated by simulating road traffic as a random BFS between the count points given by the Department of Transport.

## Setting Up the Environemnt:

1. Create and Activate a conda virtual environment:

``` shell
conda create -n evops
conda activate evops
```

2. Install pip within the virtual environment:

``` shell
conda install pip
```

3. Install all dependencies from requirements.txt:

``` shell
pip install -r requirements.txt`
```

4. Enter the working repository and run the code:

```shell
cd evops
python app.py
```
to run the latest development version, run

```shell
cd evops
python app_test.py
```

You should see the following output:

``` text
WebSocket transport not available. Install simple-websocket for improved performance.
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.68.58:8080
```

5. Click or copy one of the addresses into your web browser







