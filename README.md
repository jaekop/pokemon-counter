# pokemon-counter

Small side project I created that generates the counter to any pokemon (Before Gen 7).

I use a large csv file to parse the data and manipulate it.
I use pillow and tkinter to create the custom made GUI.
I use collections to be able to quantify the information.

**FAQ:**

**How does the counter generator logic work?**
It typically sorts for resitant first so that it cant hit them, then it tries to find either a 4x or a 2x effectiveness so it can hit strong.

**How does the search function work?**
It primarily checks if the string fits any pokemon in the csv file. Then it checks if its found in any part of a pokemon that exists. And to
predict typos it checks if it has above 75% of the same individual characters in any string in the csv file.

**What side is the counter?**
Due to confusion, I'd like to clarify that the counter is on the LEFT side. the RIGHT side is the pokemon you would like to find a counter to.

**Recent Fixes:**
Made it reccomend in a new formula, and now it reccomnds double types and not singular types only. And now it works for 95% of the Data Set. 

**Future Fixes:**
Fix why it reccomend anything for aegislash or other pokemon.

Overall, this is a small side project that I made for fun. Enjoy!
