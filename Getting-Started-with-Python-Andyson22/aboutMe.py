fullName = "Anderson Lonh"
favoriteNickname = "Andy"
age = 17
haveUsedPythonBefore = True

favoriteHobbies = ["basketball", "Volleyball", "Dance"]

favoriteThings = {
  "Sports" : [favoriteHobbies[1], "ball"], 
  "Tv Show": "Grey's Anatomy", 
  "Video Game" : "Call of Duty"
}


print(fullName, favoriteNickname, age,haveUsedPythonBefore, "\n")

print(favoriteHobbies, "\n")

print(favoriteThings['Sports'][0])

all_vars = dict(vars())

