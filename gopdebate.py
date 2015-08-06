import os
import sys
import random

sys.path.insert(0, os.path.dirname(__file__))

bingoStmts = ["Fake Southern accent by a non-Southerner",
    "Weird Hulk Hogan reference in connection to political correctness rant",
    "Never forget... Benghazi!",
    "Mike Huckabee forces a folksy sigh/pause",
    "Mike Huckabee proposes stopping abortion with troops",
    "Excuses for the smoldering wreck that is the Kansas budget",
    "'All Lives Matter'",
    "Wanton mockery of the $15 minimum wage campaign",
    "Donald Trump interrupts another candidate's answer just to be a prick",
    "Rant about ISIS that fundamentally misunderstands what it is",
    "McCarthy-esque fearmongering about Bernie Sanders",
    "Huge slam on Planned Parenthood straight outta nowhere",
    "Incredibly lame joke about Hillary Clinton",
    "Someone asks 'Who is Ben Carson?'",
    "Religious liberty is used to justify oppression",
    "Chris Christie is personally called out",
    "'Take America back!'",
    "Mentions of unions/right to work",
    "Mentions 'coalition building', has <5% in the polls",
    "'Under my Flat Tax plan...'",
    "Donald Trump insults someone to their face",
    "Comparison of Obamacare and slavery",
    "Donald Trump doubles down on his 'McCain's a pansy' talk",
    "Obvious Ohio pandering",
    "Claims they'll win [INSERT MINORITY HERE] for the GOP",
    "Shout out to my homie Ayn Rand",
    "Marco Rubio makes a tone deaf Miami Heat joke (... again)",
    "Welfare recipients should pass a drug test",
    "Incredibly lame joke about LeBron James",
    "Ted Cruz talks about the American Dream",
    "A tone-deaf advertiser confusingly advertises 'Straight Outta Compton' during the debate",
    "Reference to the rust belt being built on manufacturing",
    "Reference to the Founding Fathers",
    "Use of the word 'secular'",
    "'Ronald Reagan'",
    "'Protect our borders'",
    "Rand Paul mentions the Federal Reserve",
    "Uncomfortable Cecil the Lion 'joke'",
    "The student debt crisis was caused by big government",
    "Raise the wage ceiling, not the floor",
    "Reference to a TV show that ended before 2008",
    "Someone calls Obama a Socialist",
    "'Barack Hussein Obama'",
    "The police don't need body cameras, because we have COPS",
    "Mentions of Martin Luther King in any context",
    "Joke about Chris Christie's weight",
    "Carson or Paul slams the other's M.D. as illegitimate",
    "Candidate claims they will stop Hillary Clinton, as though she is a runaway train",
    "'Cap-and-Trade'",
    "Rand Paul defends his father's stance on something",
    "Rand Paul rebukes his father's stance on something",
    "Rand Paul uses his M.D. to establish credentials in an entirely different field",
    "Argument about NSA surveillance",
    "Attacking the 'Liberal Media'",
    "'The Iran deal is a betrayal of the American people'",
    "Mentions of Jon Stewart in any context",
    "Scott Walker mentions the # of elections he's won, ignoring that one was a recall vote",
    "'European-style welfare state'",
    "Tax cuts as an economic solution",
    "Obama is weak on Iran",
    "Jeb Bush slams his brother on anything of note",
    "Ted Cruz makes a 'Ted Cruise' joke",
    "Repeal Roe v. Wade",
    "We are a Christian Nation",
    "At least one candidate is missing a flag pin",
    "Only 51% of people pay taxes",
    "'Liberty'",
    "Incongruous pandering to Israel",
    "Mentions Sharia law or Radical Islam",
    "Someone -- ANYONE -- actually mentions student debt as an issue",
    "'SuperPAC'",
    "Reference to 'the party of Abraham Lincoln'",
    "Mention of U.S. Constitution",
    "Mention of Israel's unerring U.S. loyalty",
    "Candidates try to outdo each other on abortion policy",
    "American Exceptionalism",
    "Obama 'apologizes for America'",
    "Jeb Bush gets condescending",
    "Scott Walker is going to 'take on special interests'",
    "China isn't playing fair for some reason",
    "Activist judges",
    "Crowd inexplicably cheers an openly discriminatory gaffe",
    "Restore America's greatness",
    "Awkward attack on career politicians from Trump",
    "'Hey, y'all, let's ban same-sex marriage!'",
    "Illegal immigrants are taking our jobs",
    "Fearmongering about the U.S. becoming Greece, completely missing the irony",
    "Washington is the problem",
    "Shout out to my homie Tim Tebow",
    "'ACORN'",
    "John Kasich loses his nerve and starts shouting",
    "Free trade is a fake idea",
    "Something about not being a scientist",
    "The audience goes dead silent at an obvious applause line for Christie or Kasich",
    "Jokes about gun control",
    "Reference to mundane things as 'too Hollywood'",
    "Largely incoherent soundbite about racism",
    "The 'Democrat' Party",
    "Radical environmentalism",
    "'I'm not concerned about the polls!'",
    "Ham-handed 9/11 reference",
    "Team America: World Police (except in reality)",
    "Obamacare infringes on poorly articulated freedoms",
    "Blames Obama for the bailouts",
    "Chris Christie says something completely crazy to try and nudge into news coverage",
    "'All Cops Matter'",
    "Fannie and Freddie",
    "Bellicose rhetoric about challenging Putin",
    "Nuclear energy isn't dangerous, unless it's in Iran",
    "A candidate says 'THIS PRESIDENT...' as though he's lecturing America"]

 
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
            bingoStmts[n] if not (x, y) in coords else "<span style='color:#FFC0C0;font-weight: bold;font-size:100%;'>(FREE SPACE) </br> AN ANSWER GOES LONG!</span>"
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
    	html = ["<html>","","<head>","<title>GOP Debate Bingo!</title>","<style>a:link, a:visited, a:hover {color: #FF0000} input{background-color:#910000; font-weight: bold; text-decoration: underline; color:#ffffff; border:2px solid #910000; font: 110% arial black, sans-serif;}</style>","</head>","","<body bgcolor='#FFC0C0' link='#970808'>"]
    	
    	html.append("<h1 style='background-color: #910000; text-align: center; font: 180% arial black, sans-serif; color: #E34848; text-decoration: underline; width: 80%; margin-left:10%; margin-right:10%'>August 2015: Republican Debate Bingo!</h1>")
    	html.append("")
    	html.append("<p style='padding: 10px; background-color: #FFADAD; color: #6B0000; font: 75% helvetica neue, verdana, sans-serif; text-align:justify; width: 60%;margin-left:20%;margin-right:20%;'>Hello all! <a href='https://twitter.com/docrostov'>Aaron McGuire (@docrostov)</a> here, editor of the hibernating <a href='http://gothicginobili.com'>Gothic Ginobili NBA blog</a> and a Data Scientist/Statistician. While talking with a bunch of friends about the upcoming GOP fracas, I realized that this year's inaugural debate could make an excellent bingo game. With ten candidates facing off in a Thunderdome-style showdown, what sort of things would the candidates be yelling this year? Thankfully, I know basic Python, and was able to build a neat randomizer that creates a random bingo board from an uncomfortably large list of possible outcomes at Thursday's debate. <br><br><div style='text-align:center;'><FORM><INPUT Type='button' VALUE='Click here to generate a new Bingo Board!' onClick='history.go(0)'></FORM></div></p>")
        html.append("<table style='border: 10px solid #910000; border-top: 5px solid #6B0000; border-collapse: collapse; font-family:helvetica neue, verdana, sans-serif; font-size:80%; text-align: center; width:70%; padding:10px; margin-left: 15%; margin-right: 15%'>")
        i = 1
        for row in self:
            if i>1:
                html.append("<tr style='height: 110px; background-color: #E34848; color: #ffffff;'>")
            
                for col in row:
                    html.append("<td style='border: 3px solid #D41C1C; text-align:center; width: 20%; padding: 15px;'>{0}</td>".format(col))
            
                html.append("</tr>")
            else:
                html.append("<tr style='color: #ffffff; background-color: #910000; border: 0px solid black;'>")
                
                for col in row:
                    html.append("<td style='font: 150% arial black, sans-serif; border: 0px solid black; text-align:center; padding: 25px; width:20%;'>{0}</td>".format(col))
                
                html.append("</tr>")
                i+=1
        html.append("</table>")
        html.append("")
        html.append("<p style='padding: 10px; background-color: #FFADAD; color: #6B0000; font: 60% helvetica neue, verdana, sans-serif; font-weight: bold; text-align: center; width: 50%;margin-left:25%;margin-right:25%'>Bingo board generated in Python 2.7 using WSGI.</p>")
        html.append("")
        html.append("<p style='padding: 10px; background-color: #FFADAD; color: #6B0000; font: 60% helvetica neue, verdana, sans-serif; font-weight: bold; text-align: center; width: 50%;margin-left:25%;margin-right:25%'>Credit to <a href='http://cognitivedissonance.tumblr.com/post/15975136995/gop-debate-bingo-for-jan-16th-and-jan-19th'>CognitiveDissonance</a> for some of the questions, and <a href='https://gist.github.com/matthiaseisen/2af0d71870427c6bdfd6'>Matthias Eisen</a> for some of the bingo code. Code built by <a href='https://twitter.com/docrostov'>Aaron McGuire.</a></p>")
        html.append("")
        html.append("</body>")
        html.append("")
        html.append("</html>")
        return '\n'.join(html)


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/HTML')])
    response = BuildHTML(card_data()).get_html()
    return [response.encode()]