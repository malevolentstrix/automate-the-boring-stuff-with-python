# "Random Chore Assignment Emailer" project in Chapter 18 of the book
# CTRL + C can be used to stop the execution
# By JITHIN JOHN
import ezgmail
import smtplib, random, time
mymailid = 'jithintvm2@gmail.com'
print("Enter the password")
mypassword = input()
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(mymailid, mypassword)
targetids = ['jithintvm1@gmail.com','jithintvm2@gmail.com']
emailswithchores = {}
while True:
    chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
    for email in targetids:
        random_chore = random.choice(chores)
        emailswithchores[email] = random_chore
        chores.remove(random_chore)
    for email in emailswithchores:
        assigned_chore = str(emailswithchores[email])
        smtp_obj.sendmail(mymailid, email, assigned_chore)
    try:
        time.sleep(604800)
    except KeyboardInterrupt:
        break
smtp_obj.quit()