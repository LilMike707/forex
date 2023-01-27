### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

    Python is server side, and JS is client side


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
    you can use a try: testing method
    you can set c with a default value of none


- What is a unit test?

    a test that tests a small peice of code. usually one function

- What is an integration test?

    testing multiple peices of an app to make sure they work together

- What is the role of web application framework, like Flask?

    to make server side coding easier. flask handles a lot of things in the background that would take forever to write by hand

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    you might use foods/pretzel if you are visiting a page about pretzels. use type=pretzel if you are searching for a specficic type of food

- How do you collect data from a URL placeholder parameter using Flask?

    request.url

- How do you collect data from the query string using Flask?

    request.args

- How do you collect data from the body of the request using Flask?

    request.data

- What is a cookie and what kinds of things are they commonly used for?

    cookies are saved pieces of data for when a user visits the site. search history, visited pages, etc

- What is the session object in Flask?

    the session object is data saved about a user but it only persists for as long as the window is open

- What does Flask's `jsonify()` do?

    takes flask data and returns it as json so it can be used