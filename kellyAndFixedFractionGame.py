# Simulation code for the paper "Game of Fitness: Kelly betting in a limited environment leads to logistic growth"

import random
import pygame
import numpy as np
import json
import time
import math


# REGION - Simulation Parameters
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 40 # 20 x 20 tiles = 400 tiles in total
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
NO_TILES = GRID_WIDTH * GRID_HEIGHT
# END REGION


pygame.init()


# REGION simulation graphics parameters, configurable
FPS = 10
TIME_STEPS = 100 
NUM_RUNS = 10000
# END REGION


# REGION reproduction parameters, configurable
# Moore neighbourhood radius ρ (i.e in level = 1, organism has 8 neighbors; level = 2: organism has 24 neighbours)
# Maximum level is level = 19 to allow organisms in the corners to reproduce within the whole grid. 
level = 19

# Information parameter α (i.e. when tile_selection_bias = 0: pure random selection;
# 1: perfect avoidance of occupied tiles; 0.5 - equal chance of perfect avoidance and random selection)
tile_selection_bias = 1
# END REGION


# REGION Pygame Parameters
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Enables the graphical interface
clock = pygame.time.Clock()
# Colors
BLACK = (0, 0, 0) # unoccupied tiles
WHITE = (255, 255, 255)  # tdepleted tiles
YELLOW = (255, 255, 0) # occupied by live organisms
# END REGION


# Class for organisms
class Organism:
    def __init__(self):
        pass

    
# REGION Helper functions
# Graphical interface function, drawing the grid
def pygame_draw(organisms, depleted_tiles):
    screen.fill(BLACK)  # Clear the screen for the new frame
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))
    # Drawing depleted tiles in WHITE
    for position in depleted_tiles:
        pygame.draw.rect(
            screen,
            WHITE,  
            (
                position[0] * TILE_SIZE,
                position[1] * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ),
        )
    # Drawing orrganisms in YELLOW
    for position in organisms:
        pygame.draw.rect(
            screen,
            YELLOW,
            (
                position[0] * TILE_SIZE,
                position[1] * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ),
        )
    pygame.display.flip()
    clock.tick(FPS)


# Function that calculates the probability of success pn according to equation (15):
def calculateProbabilityOfSurvival(emptyTiles, depleted_tiles):
    available_tiles = NO_TILES - len(depleted_tiles)  # Total habitable tiles (all except white)
    return emptyTiles / available_tiles if available_tiles > 0 else 0  # Avoid division by zero


# Function that calculates the bid size based on equation (14):
def calculateBetSize(p, organisms):
    b = len(organisms) * (2 * p - 1)  # b = S(2p - 1)
    b = round(b)
    if b < 0: # Avoid negative values
        b = 0
    return b


#calculating the bet size for fractional Kelly strategy (like half Kelly when kellyFraction = 0.5)
def calculateFractionalKellyBetSize(p, organisms, kellyFraction):
    #b = b from full kelly * kellyFraction
    bFull = len(organisms) * (2 * p - 1)

    b = kellyFraction * bFull
    b = round(b)


    if b < 0: # Avoid negative values
        b = 0
    return b


# function for constant fractional betting strategy
def calculateFixedFractionBetSize(fractionToBet, organisms):
    #b = S * fraction
    b = len(organisms) * fractionToBet
    b = round(b)


    if b < 0: # Avoid negative values
        b = 0
    return b



# Function that returns neighbotoing positions of an organism based on the Moore radius ρ:
def get_neighboring_positions(position, level):
    col, row = position
    neighboring_positions = []
    # If level is at or above the grid's maximum size, return all positions except the current one
    if level >= max(GRID_WIDTH, GRID_HEIGHT):
        return [
            (c, r) 
            for c in range(GRID_WIDTH) 
            for r in range(GRID_HEIGHT) 
            if (c, r) != position
        ]
    # Iterate through the neighborhood defined by the level
    for dx in range(-level, level + 1):
        for dy in range(-level, level + 1):
            # Exclude the organism's own position
            if dx != 0 or dy != 0:
                neighboring_position = (col + dx, row + dy)
                # Ensure the neighboring position is within the grid bounds
                if 0 <= neighboring_position[0] < GRID_WIDTH and 0 <= neighboring_position[1] < GRID_HEIGHT:
                    neighboring_positions.append(neighboring_position)
    return neighboring_positions


# Function that returns a tile that an organism selects for reproduction based on information parameter α:
def get_random_tile_within_neighborhood(position, level, organisms, depleted_tiles):
    # Get neighboring positions based on level
    neighboring_positions = get_neighboring_positions(position, level)

    # Available tiles are all habitable tiles: unoccupied(black) and occupied(yellow)
    # Unhabitable depleted (white) tiles are removed from the selection
    available_tiles = [pos for pos in neighboring_positions if pos not in depleted_tiles]
    
    # Empty tiles are tiles that are available(habitable) and unoccupied(black)
    empty_tiles = [pos for pos in available_tiles if pos not in organisms]

    # When tile selection bias = 1, organism chooses from black tiles (unoccupied), which guarantees reproduction
    if tile_selection_bias == 1:
        return random.choice(empty_tiles) if empty_tiles else None  # Skip reproduction if no empty tiles
    
    # When tile selection bias is less than 1, organism chooses from a set of both occupied and unoccupied tiles,
    # which does not guarantee success
    selected_tiles = empty_tiles if random.random() < tile_selection_bias and empty_tiles else available_tiles
    return random.choice(selected_tiles) if selected_tiles else None
# END REGION


# Main logic funciton 
def optimalKelly():
    running = True
    timeStep = 0 # start with timestep 0
    organisms = {(10, 10): Organism()}  # Start with 1 organism at (10,10) coordinate on the grid
    depleted_tiles = set()  # Set to track depleted tiles
    live_counts = [1] # add the initial 1 organism to the count
    p = [1]  # add the initial probability of survival
    depleted_counts = [0]  # Track depleted tiles count over time
    while running:
        timeStep += 1 

        #for optimal kelly:
        #b = calculateBetSize(p[timeStep - 1], organisms) #calculating how many organisms will reproduce/use s1 strategy
       
        # for fractional kelly:
        #kellyFraction = 0.75
        #b = calculateFractionalKellyBetSize(p[timeStep - 1], organisms, kellyFraction) #calculating how many organisms will reproduce/use s1 strategy

        # for fixed fractional betting:
        fractionToBet = 1
        b = calculateFixedFractionBetSize(fractionToBet, organisms)

        # for going all in:
        #b = len(organisms)



        organisms_list = list(organisms.items())
        random.shuffle(organisms_list) 
        selected_organisms = organisms_list[:b]  #selected_organisms is a list of randomly selected organisms of length b
        new_organisms = {} #to store offsprings
        to_remove = set() #to store parents to kill
        chosen_positions = set() # Store positions that have been chosen for reproduction

        for position, organism in selected_organisms:
            new_position = get_random_tile_within_neighborhood(position, level, organisms, depleted_tiles)
            if new_position is None: # in case when all positions are depleted or occupied
                to_remove.add(position) # reproduction fails 
            elif new_position in organisms or new_position in chosen_positions:
                to_remove.add(position) #reproduction fails
            else:
                new_organisms[new_position] = Organism() # add a new organism
                chosen_positions.add(new_position)

        for position in to_remove:
            del organisms[position]
            depleted_tiles.add(position)

        #update organisms after reproduction
        organisms.update(new_organisms)
        live_counts.append(len(organisms))

        #pygame_draw(organisms,depleted_tiles)  # comment out this line if you want to disable graphical interface

        depleted_counts.append(len(depleted_tiles))  # Record number of depleted tiles

        # Calculate probability of survival
        emptyTiles = NO_TILES - len(organisms) - len(depleted_tiles) # number of unoccupied tiles (black)
        p.append(calculateProbabilityOfSurvival(emptyTiles, depleted_tiles))

        # for the heatmap
        final_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)
        for position in organisms:
            if position is not None:
                final_grid[position[0], position[1]] = 1
            else:
                print("Warning: 'None' position was found in the organisms list and was skipped.")

        if len(organisms) == 0 or timeStep >= TIME_STEPS or emptyTiles==0:
            running = False

    final_grid_list = final_grid.tolist()

    print(final_grid_list)

    return live_counts, timeStep, p , depleted_counts, final_grid_list



# Function that runs the simulation multiple times and saves results to JSON for plotting
def main():
    aggregated_live_counts = []
    aggregated_depleted_tiles = []
    aggregated_final_grids = []

    for _ in range(NUM_RUNS):
        live_counts, _, _ , depleted_counts, final_grid_list = optimalKelly()
     
        aggregated_live_counts.append(live_counts)
        aggregated_depleted_tiles.append(depleted_counts)
        aggregated_final_grids.append(final_grid_list)
   
    data = {
        'live_counts': aggregated_live_counts,
        'depleted_tiles_counts': aggregated_depleted_tiles,
        'final_grids': aggregated_final_grids
    }
    with open('simulation_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
