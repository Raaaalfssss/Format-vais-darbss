
password= ("python123")
guess = (input("Ievadi paroli"))
while guess != password:
    if guess > password:
        print("Piekļuve liegta!")
    elif guess < password:
        print("Piekļuve liegta!")
    guess = (input("mēgini vēlreiz"))
if guess == password:
        print("Piekļuve atļauta!")