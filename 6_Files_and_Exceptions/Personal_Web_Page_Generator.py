# (a). Personal Web Page Generator  (15 points)
# Write a program that asks the user for his or her name, then asks
# the user to enter a sentence that describes himself or herself.
# Here is an example of the program’s screen:

# Enter your name: Julie Taylor [Enter]
#  Describe yourself: I am a computer science major, a member of the
#  Jazz club, and I hope to work as a mobile app developer after I
#  graduate. [Enter]
# Once the user has entered the requested input, the program should
# create an HTML file, containing the input, for a simple Web page.
# Here is an example of the HTML content, using the sample input
# previously shown:

# <html>
#  <head>
#  </head>
#  <body>
#     <center>
#        <h1>Julie Taylor</h1>
#     </center>
#     <hr />
#     I am a computer science major, a member of the Jazz club,
#     and I hope to work as a mobile app developer after I graduate.
#     <hr />
#  </body>
#  </html>

# Use the data input as sample input.
# Copy and paste the html output, and UPLOAD it too.
# Name the file as LASTNAME.html (use your LASTNAME)

# NOTE: Name the file with your LASTNAME.html
#       It will show up automatically in your repl.it


def main():
  name = input("Enter your name: ")
  description = input("Describe yourself: ")

  temp = f"""<html>
  <head>
  </head>
  <body>
     <center>
      <h1>{name}</h1>
     </center>
     <hr />
      {description}
     <hr />
  </body>
  </html>
  """

  with open("pashinyan.html", "w") as file:
    file.write(temp)


if __name__ == "__main__":
  main()

# Test 1
#     Input: Enter your name: Julie Taylor
#            Describe yourself: I am a computer science major,
#                               a member of the Jazz club, and I hope to work as
#                               a mobile app developer after I graduate.
#    output: <html>
#            <head>
#            </head>
#            <body>
#               <center>
#                 <h1>Hayk</h1>
#               </center>
#               <hr />
#                I am a computer science major, a member of the Jazz club,
#                and I hope to work as a mobile app developer after I graduate.
#               <hr />
#           </body>
#           </html>

# Test 2
#     Input: Enter your name: Jhon Doe
#            Describe yourself: I am a Web Developer
#    output: <html>
#            <head>
#            </head>
#            <body>
#               <center>
#                 <h1>Jhon Doe</h1>
#               </center>
#               <hr />
#                I am a Web Developer
#               <hr />
#           </body>
#           </html>
