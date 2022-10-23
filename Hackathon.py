# ServiceDesk.py
# Helpful stuff for students
# Cassidy, Hannah, Amanda
# 10/22/22


def main():
    name = input("Input name here: ")
    print("========== \nHello", name + "! Welcome to MaristAssist.")
    print("""
        This program is designed help Marist students with general questions.
        Let's go!

==========
        """)
    ##degree works

    count = 0
    gpa = False
    classes = False
    advisor = False
    credit = False
    major = False
    prof = False

    while count == 0:
        user_input = input(
            "What do you need help with? Type 'help' for a list of possible keywords "
        ).lower()
        sentence_list = user_input.split()
        x = 0
        for word in sentence_list:
            if word == "gpa" or word == "grade" or word == "grades":
                print("You asked about GPA")
                x, count = 1, 1
                gpa = True
            elif word == "classes" or word == "class":
                print("You asked about classes")
                x, count = 1, 1
                classes = True
            elif word == "advisor" or word == "advisors":
                print("You asked about an advisor")
                x, count = 1, 1
                advisor = True
            elif word == "credit" or word == "credits":
                print("You asked about credits")
                x, count = 1, 1
                credit = True
            elif word == "majors" or word == "major" or word == "minors" or word == "minor":
                print("You asked about a major/minor")
                x, count = 1, 1
                major = True
            elif word == "service" or word == "services":
                print("You asked about services")
                x, count = 1, 1
                prof = True
            elif word == "help":
                print(
                    "Try searching for any of the following keywords: gpa, classes, advisor, credit, major, minor, services"
                )
                x = 1
                continue
        if x == 0:
            print(
                "This is not a valid command. Try typing 'help' for a list of possible keywords."
            )

    print("Type the letter of the question you need help with:")

    ##guide for gpa
    if gpa == True:
        spec_input = input("""
    a. What is my GPA?
    b. Can I register for classes with my current GPA?
    """).lower()

    ##guide for classes
    elif classes == True:
        spec_input = input("""
    b. Can I register for classes with my current GPA?
    c. Where is my class?
    """).lower()

    ##guide for advisor
    elif advisor == True:
        spec_input = input("""
    d. Who is my advisor?
    """)

    ##guide for credits
    elif credit == True:
        spec_input = input("""
    h. How many more credits do I need to graduate?
    i. How many credits do I have?
    """)

    ##guide for majors/minors
    elif major == True:
        spec_input = input("""
    e. How do I change my major/minor?
    f. How do I add a major/minor?
    g. What is a pathway and how do I declare a one?
    """)

    ##guide for services
    elif prof == True:
        spec_input = input("""
    j. How do I contact Career Services?
    k. How do I contact Health Services?
    l. How do I contact Financial Services?
    m. How do I contact services for Accomidations and Accessibility?
    n. How do I contact Counsiling Services?
    o. How do I contact the Academic Learning Center?
    """)

    ##guide for each letter (a or b)
    if spec_input == "a" or spec_input == "b":
        print("""
Knowing your GPA is useful!
Let's calculate your it.
Note: If you have below a 1.0, you cannot register!
""")

        def gpa_calculator(grades):
            points = 0
            i = 0
            grade_c = {
                "A": 4,
                "A-": 3.7,
                "B+": 3.3,
                "B": 3.0,
                "B-": 2.7,
                "C+": 2.3,
                "C": 2.0,
                "C-": 1.7,
                "D+": 1.3,
                "D": 1.0,
                "F": 0
            }
            if grades != []:
                for grade in grades:
                    points += grade_c[grade]
                gpa = points / len(grades)
                return gpa
            else:
                return None

        grade = input("Input grades separated by spaces: (Ex. A B+ D A-):")
        grades = grade.split()
        gpa = (gpa_calculator(grades))
        if gpa > 1.0:
            print("GPA:", (gpa_calculator(grades)))
            print("You are eligable for registration. \n==========")
        else:
            print("GPA:", (gpa_calculator(grades)))
            print("""
    I'm sorry you cannot register at this time.
    Please speak with your advisor.
==========
    """)

    ##guide for (d)
    elif spec_input == "d":
        print(
            "Please enter which school you are in (Communication and the Arts, Computer Science and Mathematics, Liberal Arts, Management, Science, Social and Behavioral Sciences, Professional Programs). \nEmail one of these department chairs for information. For general inquiries, email advising@marist.edu"
        )
        school = input("School of:").lower()
        if school == "communication and the arts":
            print('''
            Art & Digital Media: Anne Bertrand-Dewsnap Anne.Bertrand@Marist.edu
            Communication: Kevin Lerner kevin.lerner@marist.edu
            Fashion: Jennifer Finn jennifer.finn@marist.edu
            Film, Television, Games & Interactive Media: Jeff Bass Jeff.Bass@marist.edu
            Music: Arthur Himmelberger arthur.himmelberger@marist.edu
            ''')
        elif school == "computer science and mathematics":
            print('''
            Computing Technology: Donald Shwartz Donald.Schwartz@Marist.edu 
            Mathematics: James Helmreich James.Helmreich@Marist.edu
            ''')
        elif school == "liberal arts":
            print('''
            English: Eileen Curley Eileen.curley@marist.edu
            History: Kristin Bayer kristin.bayer@marist.edu
            Modern Languages and Cultures Department: Dr. Patricia Ferrer-Medina patricia.ferrer@marist.edu
            Philosophy and Religious Studies Department: Dr. Joseph Campisi joseph.campisi@marist.edu
            Political Science: Dr. Jessica Boscarino Jessica.Boscarino@marist.edu
''')
        elif school == "management":
            print('''
            Economics, Accounting, and Finance: Xiaoli Wang xiaoli.wang@marist.edu
            Management: Dr. Ken Sloan Ken.Sloan@marist.edu
            Organization and the Environment: Dr. Pamela J. Harper Pamela.harper@marist.edu
            Public and Nonprofit Administration: Dr. Tony J. Carrizales tony.carrizales@marist.edu
''')
        elif school == "science":
            print('''
            Athletic Training: Michael Powers Michael.powers@marist.edu
            Biology Dr. Raymond L. Kepner, Jr. Ray.Kepner@marist.edu
            Chemistry, Biochemistry & Physics: Dr. John Morrison Galbraith John.Galbraith@marist.edu
            Environmental Science & Policy Department: Dr. Richard S. Feldman Richard.Feldman@marist.edu
            Medical Laboratory Sciences: Terrance Paskell Terrance.paskell@marist.edu
            Physician Assistant Studies: Jeffrey Midgley Jeffrey.midgley@marist.edu
            Physical Therapy: Dr. James G. Rauh james.rauh@marist.edu
''')
        elif school == "social and behavioral sciences":
            print('''
            Criminal Justice: Dr. Addrain Conyers Addrain.Conyers@marist.edu
            Education: Dr. Carol R. Rinke carol.rinke@marist.edu
            Social Work: Dr. Daria V. Hanssen Daria.Hanssen@marist.edu
            Psychology: Dr. Ryan Kinlaw Ryan.Kinlaw@marist.edu
''')
        elif school == "professional programs":
            print("Christie Alfaro Christie.Alfaro@marist.edu")

        else:
            print(
                "Hmm, you haven't typed any of the valid options. If you are an undeclared major or have general questions, email Advising@marist.edu."
            )

    ##guide for (c)
    elif spec_input == "c":
        print("Ok! You have your classes. Let's help you find them!")

        def location(building, roomnum):
            if building == "LT":
                print(
                    "\nYou should go to Lowell Thomas! This is the brick and stone building near the construction site with a big glass entry way."
                )
                if roomnum < 100:
                    print(
                        'Your class is downstairs. Enter the staircase from the back entrance, or enter the front then go to the left and down the hallway to find the staircase/elevator.'
                    )
                elif roomnum < 130:
                    print(
                        "Your class is on the first floor to the left if you enter through the main doors."
                    )
                elif roomnum < 200:
                    print(
                        "Your class is on the first floor to the right if you enter through the main doors."
                    )
                else:
                    print(
                        "Your class is on the second floor. Use the stairs or elevator directly when you walk in."
                    )
            elif building == "HC":
                print(
                    "\nYou should go to Hancock! This is the large stone building to the right of the Campus Green (looking at the water)."
                )
                if roomnum < 1000:
                    print(
                        'Your class is downstairs. The staircase and elevator are next to the entrance.'
                    )
                elif roomnum < 2000:
                    print(
                        "Your class is on the first floor to the right if you enter through the main doors."
                    )
                elif roomnum < 3000:
                    print(
                        "Your class is on the second floor. Use the stairs or elevator directly when you walk in."
                    )
                else:
                    print(
                        "Your class is on the third floor. Use the stairs or elevator directly when you walk in."
                    )
            elif building == "ST":
                print(
                    "\nYou should go to Steel Plant! This is the brick and steel building just past the underpass."
                )
                if roomnum < 200:
                    print('Your class is on the first floor.')
                else:
                    print(
                        "Your class is on the second floor. Use the stairs or elevator juat past the cafe."
                    )
            elif building == "LB":
                print(
                    "\nYou should go to the Library! This is the large stone building at the top of the campus green."
                )
                if roomnum < 100:
                    print('Your class is on the "quiet" first floor.')
                elif roomnum < 200:
                    print('Your class is on the "main" second floor.')
                else:
                    print(
                        "Your class is on the third floor. Use the stairs to the right as you enter the main study area of the library. Or use the elevator."
                    )
            elif building == "MU":
                print(
                    "\nYou should go to the Music classrooms! These rooms are in the student center by the entrance with wooden doors and a hanging lantern."
                )
                if roomnum > 3200:
                    print(
                        "Your class is down the small hallway across from the recital hall."
                    )
                else:
                    print("Your classroom is downstairs near the practice rooms.")
            elif building == "FF":
                print(
                    "\nYou should go to 51 Fulton! Once you cross the overpass, follow the signs that point you to the grey and red building."
                )
                if roomnum < 100:
                    print('Your class is on the first floor.')
                elif roomnum < 200:
                    print('Your class is on the second floor.')
                else:
                    print(
                        "Your class is on the third floor. Use the stairs to the right as you enter the main study area of the library. Or use the elevator."
                    )
            elif building == "FN":
                print(
                    "\nYou should go to Fontaine Hall! Go towards the constuction site, and follow the road until you see a light grey building with large windows at the entrance."
                )
                if roomnum < 200:
                    print('Your class is on the first floor.')
                elif roomnum < 300:
                    print('Your class is on the second floor.')
                elif roomnum < 400:
                    print("Your class is on the third floor.")
                else:
                    print("Your class is on the fourth floor.")
            elif building == "DN":
                print(
                    "\nYou should go to Donnelly Hall! This is the round, grey building near the football field."
                )
                if roomnum < 200:
                    print(
                        'Your class is on the first floor. Go down the stairs at the entrance'
                    )
                else:
                    print(
                        "Your class is on the second floor. Go up the stairs at the entrance"
                    )
            elif building == "AH":
                print(
                    "\nYou should go to the Science and Allied Health Building! This is the stone building just past the underpass with a big glass windows above the entry way "
                )
                if roomnum < 200:
                    print(
                        'Your class is on the first floor. Go down the stairs at the entrance'
                    )
                else:
                    print(
                        "Your class is on the second floor. Go up the stairs at the entrance"
                    )
            print(
                "Look for the specific room number on or near each classroom door.\n")

        location_input = input("building and room number (Ex. LT 133):")
        location_split = location_input.split(" ")
        building = location_split[0]
        roomnum = int(location_split[1])
        location(building, roomnum)

    ##guide for (h)
    elif spec_input == "h":
        current_credits = int(
            input("Please enter the number of credits you currently have: "))
        remaining_semesters = int(
            input("Please enter how many remaining semesters you have : "))
        remaining_credits = 120 - current_credits
        credits_per_semester = remaining_credits / remaining_semesters
        print(
            f"""You currently have {current_credits} and need {remaining_credits} more.
To graduate on time, you need {credits_per_semester} credits per semester.""")

    ##guide for (i)
    elif spec_input == "i":
        total_credits = 0
        total_classes = int(
            input(
                "Please enter the total number of classes you have taken or have been enrolled in: "
            ))
        print(
            "You will enter how many credits each class you have taken (or are taking) is one at a time. "
        )
        for classes in range(0, total_classes):
            total_credits += int(input("Enter the amount of credits for a class: "))
        print(f"You currently have {total_credits} credits.")

    ##guides for (e and f)
    elif spec_input == "e" or spec_input == "f":
        print(
            "Fill out the form at https://my.marist.edu/documents/810944/815970/changemajor.pdf/f05ed0eb-1516-4391-8512-8f92dffef12e and email it directly to the Chairperson or Dean of the School where the major/minor is located. They will forward this form to the registrar's office.")

    ##guides for (g)
    elif spec_input == ("g"):
        print(
            "Every student must declare a pathway by the end of their freshman year. To complete a pathway, students take 4 courses drawn from at least 3 of the disciplinary areas.")
        pathways = input("Would you like to see a list of the possible pathways? Yes or No?:").lower()
        if pathways == "yes":
            print('''
      African Diaspora Studies
      American Studies
      Cognitive Science Studies
      Contemporary European Studies
      Environmental Studies
      French
      Gender Studies
      Global Studies
      Hudson River Valley Regional Studies
      Italian
      Jewish Studies
      Latin American & Caribbean Studies
      Medieval & Renaissance Studies
      Public Health Studies
      Quantitative Studies
      Religion & Society
      Social Justice, Law, and Ethics
      Spanish
      Studies in Political Economy
      Technology & Society

      For more info: go to https://www.marist.edu/academics/core/pathways
      ''')
        else:
            print("Ok. For more info go to https://www.marist.edu/academics/core/pathways")



    ##guides for services (j-o)
    elif spec_input == "j":
        print("Contact info: career.services@marist.edu or 845-575-3547")
        print("Located in the Library")
    elif spec_input == "k":
        print("Contact info: health.services@marist.edu or 845-575-3270")
        print("Located in Murray Student Center")
    elif spec_input == "l":
        print("Contact info: studentfinancialservices@marist.edu or 845-575-3230")
        print("Located in Donnelly Hall")
    elif spec_input == "m":
        print("Contact info: accommodations@marist.edu or 845-575-3274")
        print("Located in Donnelly Hall")
    elif spec_input == "n":
        print("Contact info: counseling.services@marist.edu or 845-575-3314")
        print("Located in Midrise")
    elif spec_input == "o":
        print("Contact info: academiclearningcenter@marist.edu or 845-575-3300")
        print("Located in the Library")

    print(
        "Thanks for using MaristAssist! If you need any additional information, please visit 'https://www.marist.edu/request-information'.")


main()
