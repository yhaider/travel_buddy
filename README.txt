
Below are the different possible routes for Travel Buddy:

- Starts at ‘localhost:8000’

Different Routes:

‘/‘  - redirects to main

‘/main’ - Login and registration page for Travel Buddy

‘/travels’ - Homepage once the user has logged in

‘/travels/add’ - Routes to a new page where the user can add a trip

‘/travels/destination/(?P<number>\d+)’ - Routes to the information page for the destination associated with that number

‘/travels/join/(?P<number>\d+)’ - Allows the user to join another user’s trip