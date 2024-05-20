 Navigating and sharing long URLs is a pain. The reason behind so long URLs is the number of trackers in a link, loaded up content (multiple directories) of heavy sites, etc. 
 
 We all use URL shorteners for that purpose to shorten the long URLs to a few characters, which makes them easier to share and navigate through and also look clean and elegant.
 
 To start with, we need to install the required modules that would ease out our work considerably for coding a URL shortener. We begin with the installation of the python library using the pip package manager.

Pyshorteners is Python library to wrap and consume the most used URL shorteners APIs.

In a python file, we begin with importing the required modules.

import pyshorteners

We take input from the user at this point, we could have done the inputting part later in our code, but that would let us change the basic/permanent structure of the code, which we are going to change for every URL shortener’s APIs.

Now we initialize the pyshortener library’s class object to start shortening our URLs.

type_tiny = pyshorteners.Shortener()

You are required to pass the name along with the location of the PDF if it’s not in the same directory as the python script.

short_url = type_tiny.tinyurl.short(long_url)

print("The Shortened URL is: " + short_url)

In the output, we get the shortened URL in a form like – “https://tinyurl.com/mbq3m”. And the TinyURL is because the URL shortener package – Pyshortener uses Tinyurl API by Default.
