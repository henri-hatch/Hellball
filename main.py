# Hellball main file, houses main code.

from random import randint
from values import firstNames, lastNames, ethnicities, quirks

def generatePlayer():
  # Generate a list of random numbers to create random players

  # Instantiate List
  playerSeed = []

  # First Name
  playerSeed.append(randint(0, 199))

  # Last Name
  playerSeed.append(randint(0, 199))

  # Ethnicity
  playerSeed.append(randint(0, 8))

  # Age
  playerSeed.append(randint(18, 55))

  # Quirk ID
  playerSeed.append(randint(0, 18))

  # Quirk ID 2
  quirk2 = randint(1, 19)
  if quirk2 != playerSeed[4]:
    playerSeed.append(quirk2)
  else:
    playerSeed.append(0)

  # Creativity
  playerSeed.append(randint(0, 100))

  # Dexterity
  playerSeed.append(randint(0, 100))

  # Perception
  playerSeed.append(randint(0, 100))

  # Intelligence
  playerSeed.append(randint(0, 100))

  # Adaptability
  playerSeed.append(randint(0, 100))

  # Strength
  playerSeed.append(randint(0, 100))

  # Patience
  playerSeed.append(randint(0, 100))

  # Insight
  playerSeed.append(randint(0, 100))
  
  # Nerves
  playerSeed.append(randint(0, 100))

  # Pitching Style (Not implemented yet)
  # playerSeed.append(randint(1, 25))

  # Batting Style (Not implemented yet)
  # playerSeed.append(randint(1, 25))

  return playerSeed

def generateTeam():
  # Generate a team

  team = []

  for player in range(1, 27):
    player = generatePlayer()
    team.append(player)
        
  return team

def printPlayers(team):
  # Print out sexily ;)

  print("TEAM " + str(team))
  for player in team:
    print(firstNames[player[0]], lastNames[player[1]])
    print(ethnicities[player[2]])
    print(str(player[3]) + " Years Old")
    print(quirks[player[4]])
    print(quirks[player[5]])
    print("\n")

def main():
  # Generate Two Teams
  for i in range(1, 3):
    team = generateTeam()
    printPlayers(team)


if __name__ == "__main__":
  main()
