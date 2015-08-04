import os
import sys
import random

sys.path.insert(0, os.path.dirname(__file__))

bingoStmts = ["Fake Southern accent by a non-Southerner",
    "Never forget... Benghazi!",
    "Mike Huckabee forces a folksy sigh/pause",
    "Mike Huckabee proposes stopping abortion with troops",
    "'All Lives Matter'",
    "Huge slam on Planned Parenthood straight outta nowhere",
    "Incredibly lame joke about Hillary Clinton",
    "Someone asks 'Who is Ben Carson?'",
    "Religious liberty is used to justify oppression",
    "Chris Christie is personally called out",
    "Mentions of unions/right to work",
    "Mentions 'coalition building', has <5% in the polls",
    "'Under my Flat Tax plan...'",
    "Donald Trump insults someone to their face",
    "Comparison of Obamacare and slavery",
    "Obvious Ohio pandering",
    "Shout out to my homie Ayn Rand",
    "Welfare recipients should pass a drug test",
    "Incredibly lame joke about LeBron James",
    "Ted Cruz talks about the American Dream",
    "Reference to the rust belt being built on manufacturing",
    "Reference to the Founding Fathers",
    "Use of the word 'secular'",
    "'Ronald Reagan'",
    "'Protect our borders'",
    "Rand Paul mentions the Federal Reserve",
    "Uncomfortable Cecil the Lion 'joke'",
    "Raise the wage ceiling, not the floor",
    "Reference to a TV show that ended before 2008",
    "Someone calls Obama a Socialist",
    "'Barack Hussein Obama'",
    "Mentions of Martin Luther King in any context",
    "Joke about Chris Christie's weight",
    "Argument about NSA surveillance",
    "Attacking the 'Liberal Media'",
    "Mentions of Jon Stewart in any context",
    "'European-style welfare state'",
    "Tax cuts as an economic solution",
    "Obama is weak on Iran",
    "Repeal Roe v. Wade",
    "We are a Christian Nation",
    "At least one candidate is missing a flag pin",
    "Only 51% of people pay taxes",
    "'Liberty'",
    "Mentions Sharia law or Radical Islam",
    "'SuperPAC'",
    "Reference to 'the party of Abraham Lincoln'",
    "Mention of U.S. Constitution",
    "Mention of Israel",
    "Candidates try to outdo each other on abortion policy",
    "American Exceptionalism",
    "Obama 'apologizes for America'",
    "Jeb Bush gets condescending",
    "Scott Walker is going to 'take on special interests'",
    "China isn't playing fair for some reason",
    "Activist judges",
    "Restore America's greatness",
    "Awkward attack on career politicians from Trump",
    "'Hey, y'all, let's ban same-sex marriage!'",
    "Illegal immigrants are taking our jobs",
    "Washington is the problem",
    "John Kasich loses his nerve and starts shouting",
    "Free trade is a fake idea",
    "Something about not being a scientist",
    "Jokes about gun control",
    "Reference to mundane things as 'too Hollywood'",
    "Largely incoherent soundbite about racism",
    "The 'Democrat' Party",
    "Radical environmentalism",
    "'I'm not concerned about the polls!'",
    "Ham-handed 9/11 reference",
    "Team America: World Police (except in reality)"]

 
def list_of_columns(
    numbers=range(1, len(bingoStmts)),
    num_of_columns=5,
    num_of_rows=5
):
    slice_length = len(numbers) // num_of_columns
    return [
        sorted(
            random.sample(
                numbers[i * slice_length: (i + 1) * slice_length],
                num_of_rows
            )
        )
        for i in range(num_of_columns)
    ]

def list_of_rows(list_of_columns):
    return [list(row) for row in zip( *list_of_columns)]

def insert_free_spaces(numbers, coords=[(2, 2)]):
    return [
        [
            bingoStmts[n] if not (x, y) in coords else "<span style='color:blue;font-weight: bold;'>(FREE SPACE) </br> AN ANSWER GOES LONG!</span>"
            for x, n in enumerate(numbers[y])
        ]
        for y in range(len(numbers))
    ]

def prepend_title_row(numbers):
    return [['B', 'I', 'N', 'G', 'O']] + numbers

def card_data():
    return prepend_title_row(
        insert_free_spaces(
            list_of_rows(
                list_of_columns()
            )
        )
    )


class BuildHTML(list):
    def get_html(self):
    	html = ["<html>","","<head>","<title>GOP Debate Bingo!</title>","</head>","","<body>"]
    	
    	html.append("<h1 style='text-align: center; font: 200% arial black, sans-serif;text-decoration: underline;'>08/2015 -- Republican Debate Bingo!</h1>")
    	html.append("")
    	html.append("<p style='font: 75% helvetica neue, verdana, sans-serif; text-align:justify; width: 60%;margin-left:20%;margin-right:20%;'>Hello all! <a href='https://twitter.com/docrostov'>Aaron McGuire (@docrostov)</a> here, editor of the hibernating <a href='http://gothicginobili.com'>Gothic Ginobili NBA blog</a> and a Data Scientist/Statistician. While talking with a bunch of friends about the upcoming GOP fracas, I realized that this year's inaugural debate could make an excellent bingo game. With ten candidates facing off in a Thunderdome-style showdown, what sort of things would the candidates be yelling this year? Thankfully, I know basic Python, and was able to build a neat randomizer that creates a random bingo board from an uncomfortably large list of possible outcomes at Thursday's debate. <br><br>Reload the page to get a brand new bingo board!</p>")
        html.append("<table style='border: 10px solid black; border-top: 0px solid black; border-collapse: collapse; font-family:helvetica neue, verdana, sans-serif; font-size:75%; text-align: center; width:70%; padding:10px; margin-left: 15%; margin-right: 15%'>")
        i = 1
        for row in self:
            if i>1:
                html.append("<tr style='height: 110px;'>")
            
                for col in row:
                    html.append("<td style='border: 2px solid #f1f1f1; text-align:center; width: 20%;'>{0}</td>".format(col))
            
                html.append("</tr>")
            else:
                html.append("<tr style='color: #ffffff; background-color: #000000;'>")
                
                for col in row:
                    html.append("<td style='font-size: 200%; text-align:center; padding: 25px; width:20%;'>{0}</td>".format(col))
                
                html.append("</tr>")
                i+=1
        html.append("</table>")
        html.append("")
        html.append("<p style='font: 60% helvetica neue, verdana, sans-serif; text-align: center; width: 50%;margin-left:25%;margin-right:25%'>Bingo board generated in Python 2.7 using WSGI.</p>")
        html.append("")
        html.append("<p style='font: 60% helvetica neue, verdana, sans-serif; text-align: center; width: 50%;margin-left:25%;margin-right:25%'>Credit to <a href='http://cognitivedissonance.tumblr.com/post/15975136995/gop-debate-bingo-for-jan-16th-and-jan-19th'>CognitiveDissonance</a> for some of the questions, and <a href='https://gist.github.com/matthiaseisen/2af0d71870427c6bdfd6'>Matthias Eisen</a> for some of the bingo code. Code built by <a href='https://twitter.com/docrostov'>Aaron McGuire.</a></p>")
        html.append("")
        html.append("</body>")
        html.append("")
        html.append("</html>")
        return '\n'.join(html)


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/HTML')])
    response = BuildHTML(card_data()).get_html()
    return [response.encode()]
