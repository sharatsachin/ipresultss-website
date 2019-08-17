# ipuresultss website hosted on [Heroku](https://ipuresultss.herokuapp.com/)

### The inspiration

This project was born out of necessity, the need to be view and check marks and ranks of IPU students. 
Every semester, results for various courses at IPU are released in the form of clunky [PDF's](https://github.com/sharatsachin/ipresultss-website/tree/master/PDF's) that look as follows.

![](https://i.imgur.com/wQA3VwO.jpg)

Looking at the pdf, it is impossible to tell at a clange the marks and percentages of the students, as well as check ranklists. This website was created to simplify that.

My first attempt at solving this was creating code to solve the problem at a limited stage, simply for my own class. I could copy and paste text from the section of the pdf containing my class, and simply save it in an input file to generate the results.

[Here](https://github.com/sharatsachin/ipresultss-website/tree/master/1st-attempt) is my first attempt at solving the problem.

The problem with this code was that it only showed the percentages and ranks, but did not display the individual subjects. Also this code was not portable, as specific variable values such as the credits for each subject had to be changed manually to accurately calculate marks for various courses and streams.

This leads to my second attempt at solving the problem, a full fledged website that displayed the results of the student in an elegant way. Also, it does not need to be modified for different pdfs and courses, it works for all of them.

[Here](https://github.com/sharatsachin/ipresultss-website/blob/master/Scripts-PDF-to-json.ipynb) is my second attempt at writing a script to extract useful data from the pdf dump, with the live version of the website hosted on [Heroku](https://ipuresultss.herokuapp.com/)

Here is a screenshot of the results page.

![](https://i.imgur.com/ZmIGnrG.png)
