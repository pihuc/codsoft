import random
import re

class chatbot:
    negative_responses = ("no", "nope", "nay", "i dont think so", "i'm not sure", "maybe not", "not sure")
    exit_commands = ("Thankyou, that is all", "exit", "pause", "quit", "perhaps next time","None")
    positive_responses = ("yes", "sure", "yeah", "okay", "ok", "k" )

    def __init__(self):
        self.support_responses = {
            'ask_about_company': r'.*\s*company.*',
            'ask_about_Jobs': r'.*\s*job.*',
            'ask_about_internships': r'.*\s*internship.*',
            'ask_about_services': r'.*\s*service.*',
            'ask_about_products': r'.*\s*product.*',
            'ask_about_support': r'.*\s*customer.*support.*help.*'
     }
        self.intern_responses = {
            'Web Development': r'\b1\b',
            'Android Development': r'\b2\b',
            'Data Science': r'\b3\b',
            'Java Programming': r'\b4\b',
            'C++ Programming': r'\b5\b',
            'Python Programming': r'\b6\b',
            'UI/UX Design': r'\b7\b',
            'Artificial intelligence': r'\b8\b',
            'Machine learning': r'\b9\b',
            'Flutter Developer': r'\b10\b',
            'ReactJS Developer': r'\b11\b',
            'JavaScript Developer': r'\b12\b'
        }

    def greet(self):
        self.name = input("Hello, Welcome to the CodSoft website. May I know your name?\n",)
        will_help = input(f"Hi {self.name}. You are now talking to the CodSoft Chatbot. If at any point you would like to exit the chat, please type 'Exit'. Do you require our services today?. \n").lower()
        if will_help in self.negative_responses:
            print("Alright. I hope you are satisfied with our service. Have a nice day!")
            return
        self.chat()

    def exit(self,will_help):
        for command in self.exit_commands:
            if command in will_help:
                print("Thankyou for using the CodSoft chatbot today. I hope you had a great experience. Have a nice day!")
                exit()
        return False
    def no_match_intent(self):
        return "exit"

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == "ask_about_company":
                return self.ask_about_company()
            elif found_match and intent == "ask_about_Jobs":
                return self.ask_about_Jobs()
            elif found_match and intent == "ask_about_internships":
                return self.ask_about_internships()
            elif found_match and intent == "ask_about_services":
                return self.ask_about_services()
            elif found_match and intent == "ask_about_products":
                return self.ask_about_products()
            elif found_match and intent == "ask_about_support":
                return self.ask_about_support()
        return self.no_match_intent()

    def chat(self):
        reply = input("How can I help you?").lower()
        while not self.exit(reply):
            will_help = self.match_reply(reply)
            reply = input("What would you like to explore our Jobs, Services, Products or Internships?")
            print(reply)

    def ask_about_company(self):
        responses = ["We, at CodSoft, provide IT services and IT consultancy that specializes in creating innovative solutions for businesses.\n We are passionate about technology and believe in the power of software to transform the world.\n At CodSoft, we believe practical knowledge is the key to success in the tech industry.\n Our aim is to help students lacking basic skills by offering hands-on learning through live projects and real-world examples.\n You can refer to our website https://www.codsoft.in/ for more information."
                          "CodSoft is an IT services and consultancy company that specializes in creating  innovative solutions for businesses. \n Would you like to explore what all we offer?"]
        res = input(random.choice(responses))
        if res in self.positive_responses:
            explore = input("What would you like to explore our Jobs, Services, Products or Internships?")
            print(explore)
            return explore
        return "no"

    def ask_about_Jobs(self):
        responses = ("At Codsoft, we offer two Two Job Programs, Campus Ambassador and Promotion Executive. \nThe Campus Ambassador Program provides valuable experience in talent acquisition, employee engagement, and campus outreach. \nDevelop leadership skills, build a professional network, and contribute to our organization's growth. \nTo apply, follow the link https://docs.google.com/forms/d/e/1FAIpQLSf3nRnzasF0jqSqG0krVGtQcq9k5Q-MaHma3hlinBQLeUGU4Q/closedform . "+
                     "Codsoft is thrilled to present captivating part-time job opportunities for individuals passionate about promoting our services and attracting new clients. \nAs a CodSoft promoter, you will have the incredible opportunity to earn a generous 20% commission for every confirmed client you successfully bring to us. \nJoin our team today by the link https://docs.google.com/forms/d/e/1FAIpQLSf3nRnzasF0jqSqG0krVGtQcq9k5Q-MaHma3hlinBQLeUGU4Q/closedform and unlock the potential to earn substantial rewards for your effort")
        return print(responses)

    def ask_about_internships(self):
        main_text = ["We are passionate about technology and believe in the power of software to transform the world. \n Our internship program is just one of the ways in which we are investing in the future of the industry.\n We provide programs on \n 1. Web Development,\n 2. Android Development, \n 3.Data Science, \n 4. Artificial Intelligence, \n 5. Machine Learning, \n 6. Java Programming, \n 7. C++ Programming, \n 8. Python Programming, \n 9. UI/UX Design, \n 10. Flutter Development,\n 11.ReactJS Development, \n 12. JavaScript Development. \nPlease select the number of the program you wish to explore.",
                     "We are passionate about technology and believe in the power of software to transform the world. \nOur internship program is just one of the ways in which we are investing in the future of the industry. \nYou can explore our internship programs by going to the link https://www.codsoft.in/internships ."]
        reply = input(random.choice(main_text))
        will_help = self.match_intern_reply(reply)
        return "exit"




    def match_intern_reply(self, reply):
        for intent, regex_pattern in self.intern_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == "Web Development":
                print("The internship provides practical work experience and an introduction to crafting and enhancing web-based systems.\nThis opportunity offers engaging challenges and real-world projects, allowing you to gain hands-on experience in the dynamic fields of web and app development.\nFollow the link https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform and apply now!")
                return self.ask_about_company()
            elif found_match and intent == "Android Development":
                print("Android, the user-friendly open-source operating system, has transformed the way we access internet applications and carry out important tasks on our mobile devices. \nAt CODSOFT, we understand the growing preference for mobile usage and offer the ideal starting point for your app development journey. \nDiscover the simplicity of creating your first app with us and unlock a world of endless possibilities in the realm of mobile innovation. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform?usp=send_form .")
                return self.ask_about_Jobs()
            elif found_match and intent == "Data Science":
                print("Remote Data Science Internships Are A Unique Chance To Gain Experience In The Midst Of The Virtual Workforce While Remaining Immersed In One Of The Top Organizations In The Field. \nData Analysis Internships Are Some Of The Most Competitive And Popular Within The Broader Data Science Field. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform .")
                return self.ask_about_support()
            elif found_match and intent == "Java Programming":
                print("Become a Java programming master from the convenience of your own home and unlock incredible job prospects with our certification program. \nJoin our comprehensive 4-week internship program, where you'll learn everything from web application development to deployment using Java Build a solid foundation for your career with hands-on training and real-world application in a supportive and collaborative environment. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform?usp=send_form .")
                return self.ask_about_services()
            elif found_match and intent == "UI/UX Design":
                print("Gain mastery in UI/UX Design from the comfort of your home and open doors to amazing job opportunities with our certification program. \nEnroll in our intensive 4-week internship, where you'll acquire knowledge in web application development and deployment . \nEstablish a strong base for your career and real-world implementation within a supportive and collaborative setting. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform?usp=send_form .")
                return self.ask_about_products()
            elif found_match and intent == "Artificial intelligence":
                print("Gain mastery in Artificial intelligence from the comfort of your home and open doors to amazing job opportunities with our certification program. \nEnroll in our intensive 4-week internship, where you'll acquire knowledge in web application development and deployment . \nEstablish a strong base for your career and real-world implementation within a supportive and collaborative setting. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform?usp=send_form ." )
                return self.ask_about_support()
            elif found_match and intent == "C++ Programming":
                print("Gain mastery in C++ programming from the comfort of your home and open doors to amazing job opportunities with our certification program. \nEnroll in our intensive 4-week internship, where you'll acquire knowledge in web application development and deployment using C++. \nEstablish a strong base for your career and real-world implementation within a supportive and collaborative setting. \nApply now! https://forms.gle/yeU4BUGeeBAUxtMp8 .")
                return self.ask_about_support()
            elif found_match and intent == "Python Programming":
                print("Join our 4-week comprehensive internship program and master the fundamentals of programming in Python from the comfort of your own home. \nGain the skills and knowledge to apply for exciting job opportunities in the field. \nIn this program, you will learn everything from web development to the deployment of Python-based web applications. \nGet certified and enhance your career prospects. \nDon't miss this opportunity to excel in Python programming! \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform?usp=send_form .")
                return self.ask_about_support()
            elif found_match and intent == "Machine learning":
                print("Gain mastery in Machine learning from the comfort of your home and open doors to amazing job opportunities with our certification program. \nEnroll in our intensive 4-week internship, where you'll acquire knowledge in web application development and deployment . \nEstablish a strong base for your career and real-world implementation within a supportive and collaborative setting. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd9wZJpC7Q_T3VcxOQ7YRACFcor6N-psh060RrIwZb7tGBBvw/viewform?usp=send_form .")
                return self.ask_about_support()
            elif found_match and intent == "Flutter Developer":
                print("As a Flutter Developer intern, you will be involved in developing cross-platform mobile applications using Flutter, a UI toolkit from Google. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd3_jhOZw3Qw4MBEceGtmvmkc7MEa1x9WoJ0jrAYFDHZ6-44g/viewform?usp=send_form .")
                return self.ask_about_support()
            elif found_match and intent == "ReactJS Developer":
                print("As a ReactJS Developer intern, you will work on building and maintaining web applications using the React JavaScript library. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd3_jhOZw3Qw4MBEceGtmvmkc7MEa1x9WoJ0jrAYFDHZ6-44g/viewform?usp=send_form .")
                return self.ask_about_support()
            elif found_match and intent == "JavaScript Developer":
                print("As a JavaScript Developer intern, you will contribute to the development of interactive web applications using JavaScript. \nApply now! https://docs.google.com/forms/d/e/1FAIpQLSd3_jhOZw3Qw4MBEceGtmvmkc7MEa1x9WoJ0jrAYFDHZ6-44g/viewform?usp=send_form .")
                return self.ask_about_support()
        return self.no_match_intent()
    def ask_about_services(self):
        responses = ["We provide website and web application development, Ecommerce development, and mobile app development services. \nYou can follow our services page to know more indetail about the services. \nClick on the link below! https://www.codsoft.in/services .",
                     "To apply for our services like website, ecommerce or mobile app development, visit the contact page https://www.codsoft.in/contact-us and we will get you in touch with the responsible authorities."]
        return print(random.choice(responses))

    def ask_about_products(self):
        responses = ["Directly talk to our experts by applying on this page! https://www.codsoft.in/contact-us ",
                     "We provide various products suitable for comapny, blog, hospital, ecommerce, job board, and restaraunt websites. \nVisit our products page to know more! https://www.codsoft.in/products ."]
        return print(random.choice(responses))

    def ask_about_support(self):
        responses = ["Visit our home page for more information https://www.codsoft.in/ .",
                     "Visit our contact page to contact concerned authorities https://www.codsoft.in/contact-us .",
                     "You can have a look at our terms and conditions for more information https://www.codsoft.in/terms-and-conditions ."]
        return print(random.choice(responses))



bot = chatbot()
bot.greet()