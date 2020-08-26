# Towers of Hanoi

A simple package created to simulate the playing the Towers of Hanoi game.

The object of the game is as follows:

Given 3 towers, disks are placed on the first tower in order from largest disk at the bottom
to smallest disk on top.

It is the objective of the player to move all the disks from the first tower to the third tower.

The player is only allowed to move one disk at a time and no larger disk can be placed on a smaller disk.

The player can place the disk on any of the towers at any turn. For the game to be complete
all disks need to be moved from the first tower to the last tower in order from largest disk
at the bottom to smallest disk on top.

This program initiates the game with a given number of disks passed as an argument at
initialization of the game.

The program the steps through each second printing out the current state of the towers.

After each second the program moves a given disk appropriately and prints the next state.
The program continues this pattern until all disks are moved from Origin tower to Target tower.

To start the game run the following command from within the package containing the main.py module.

    python3 main.py

### The system consists of the following classes:

#### Game

Stores the current state of the game. The class plays the game with a recursive call the
self.play_game method until all disks are moved. After 0.5 second sleep the move function
is called and the game is printed.

#### Stack

Represents a tower on which disks can be placed. It keeps track of number of disks on tower,
it is able to add a new disk to the tower or remove a disk from the top.

#### Disk

This is the actual disk which is placed on the tower. The disk is comprised of a size of integer and color string. Disks are created when the game is initialized. Disk sizes are given in multiples of 2. Currently a limited amount of disks can be created due to the limited colours available to choose from when creating disks. This can be improved by importing a colour list.
