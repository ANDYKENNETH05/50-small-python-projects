import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for birthdayB in birthdays[a + 1:]:
            if birthdayA == birthdayB:
                return birthdayA


print("""Birthday Paradox, by Al Sweigart
It's not actually a paradox,
it's a surprising result!
""")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Ask for number of birthdays
while True:
    print('How many birthdays shall I generate? (Max 50)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 50):
        numBdays = int(response)  # ✅ renamed from num8days to avoid confusion
        break
print()

# ✅ Generate birthdays
print('Here are', numBdays, 'birthdays:')
birthdays = getBirthdays(numBdays)

for i, birthday in enumerate(birthdays):
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    if i != 0:
        print(', ', end='')
    print(dateText, end='')

print('\n')

# ✅ Find matching birthday
match = getMatch(birthdays)

print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# ✅ Run 100,000 simulations
print('Generating', numBdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print("Let's run another set of simulations.")
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) is not None:
        simMatch += 1

print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")
