# Hellball main file, houses main code.

from random import randint
from statistics import mean
from values import firstNames, lastNames, ethnicities, quirks, battingStyles, pitchingStyles

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
  playerSeed.append(randint(1, 29))

  # Quirk ID 2
  quirk2 = randint(1, 29)
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

  # Pitching Style
  playerSeed.append(randint(0, 19))

  # Batting Style
  playerSeed.append(randint(0, 19))

  return playerSeed

def generateTeam():
  # Generate a team

  team = []

  for player in range(1, 27):
    player = generatePlayer()
    team.append(player)
        
  return team

def printPlayers(team, i):
  # Print out sexily ;)

  print("TEAM " + str(i))
  for player in team:
    print("Name: " + firstNames[player[0]], lastNames[player[1]])
    print("Ethnicity: " + ethnicities[player[2]])
    print(str(player[3]) + " Years Old")
    print("Quirk 1: " + quirks[player[4]])
    print("Quirk 2: " + quirks[player[5]])
    print("Creativity: " + str(player[6]) + "\tDexterity: " + str(player[7]) + "\tPerception: " + str(player[8]))
    print("Intelligence: " + str(player[9]) + "\tAdaptability: " + str(player[10]) + "\tStrength: " + str(player[11]))
    print("Patience: " + str(player[12]) + "\tInsight: " + str(player[13]) + "\tNerves: " + str(player[14]))
    print("Pitching Style: " + pitchingStyles[player[15]])
    print("Batting Style: " + battingStyles[player[16]])
    print("Pitching Score: " + str(mean([player[6], player[7], player[8], player[9], player[14]])))
    print("Batter Score: " + str(mean([player[10], player[11], player[12], player[13], player[14]])))
    print("\n")

def main():
  # Generate Two Teams
  for i in range(1, 3):
    team = generateTeam()
    printPlayers(team, i)


if __name__ == "__main__":
  main()
