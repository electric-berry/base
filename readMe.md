# EVops

## What does it do?

EVops is a submission to the PA Raspberry PI Competition 2023. In accordance with the prompt of "accelerating the energy transition",
EVops aims to optimize the placement of EV chargers within the UK.

## How does it do this?

The script accesses traffic and count points from the Department of Transport and optimises the placement of ev chargers for profitability. This is done with a genetic algorithm, with fitness calculated by simulating road traffic as a random BFS between the count points given by the Department of Transport.
