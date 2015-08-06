# GOPDebateBingo
This is the code behind a debate bingo game featuring this year's wealth of Republican options. 

It's relatively simple -- it wraps a few clever Python generators together to randomize and invert a 5x5 bingo matrix, then uses simple string logic to build a webpage out of the generator's output. It was a test case to experiment with using WSGI to generate Python webpages, in hopes of eventually building out more complicated web apps. It was also a test case for making a page simple enough it could also be loaded on mobile, to make it more playable. Possible future enhancements:

   - Drop down box to select the set of statements to build a bingo board out of.
   - Checkboxes to enable or disable specific groups of items (like candidate-specific results, quotes, etc).
   - Javascript additions to add mouseover actions and other fun-though-unnecessary stuff.

To see the bingo 'app' in action, [check it out on Gothic Ginobili.](http://gothicginobili.com/gopdebate)
