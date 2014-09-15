robotframework-imaging
======================

Compare two images using the root mean squared analysis 
Image analysis is a science in itself as visual perception is very complicated but sometimes it is
possible to do things simply. The general use case seems to be look for and highlight differences.
or this it's difficult to beat the compare suite of ImageMagick. Of course, you can roll your own
equivalent with Python and PIL.

However, I wanted a measure of "closeness" between two images - I am comparing a host of websites and checking that the right logo is more or less in the right place. This is incredibly easy to do with the naked eye but surprisingly difficult programmatically, at least I've found it so. Of course, effbot has already provided a basic comparison implementation based on the root mean square: http://effbot.org/zone/pil-comparing-images.htm. As I couldn't initially get this to work on my system I worked though it and was reminded of something Guido said at PyCon 2011 about accepting map, filter and reduce too easily into the language. Taken on their own these functions are just about readable but throw in some lambdas and I, at least, am lost. If anyone else is going to work with your code think about adding one or two lines for readability.

Fortunately, the introduction of list comprehensions and some aggregate functions (sum, max, etc.) have made their use more or less optional for general code with reduce being moved to the functools module for specific cases. Stepping through the nested calls:

sq is a generator expression that works through the histogram of the different images. enumerate handily gives us an index that we used to have to generate from the length of the list or a counter. Left-to-right ordering in the expression makes it easier to understand that we are working on the values from the for loop, avoiding the need of a lambda. We use a generator expression as this is an intermediary result.

sum_of_squares simply adds all the items in expression and is directly equivalent to `reduce(operator.add, sq). Big win in readability!

rms gives the square root of the sum of squares. Easy enough to plug sum(sq) directly for brevity while maintaining clarity but spelled out here for didactic purposes. Having to use float() to avoid integer division (this is written for Python 2.x) is probably the biggest wart in this line: as long as any the numbers is a float in the calculation then the result will also be a float.
