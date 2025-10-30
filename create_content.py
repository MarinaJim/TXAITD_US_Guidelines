import random

users = ["waterlemon", "rotation"]

argumentative = [
    """Is it cheating when students use artificial intelligence to help them with their schoolwork? In your opinion, how, if at all, should students be allowed to use AI in school? What do you see as benefits and drawbacks of using AI for doing homework?""",
    """Should 16-Year-Olds Be Allowed to Vote? In your opinion, is the current minimum legal voting age of 18 fair and appropriate?  What influence would lowering the threshold to 16 years have on the society?""",
    """Boys Are Spending More Time Gaming. Is That a Problem? Some say video games are a chief reason boys and young men are struggling. Others say games serve an important role in teens’ lives. What do you think? What can gaming bring to a teen’s life? What other activities, if any, does it take away from?""",
    """Should Schools Ban Student Phones? More and more countries are cracking down on students’ use of cellphones. Are these restrictions fair? Can they work? Do you think that phones interfere with student’s academic learning, the quality of their social interactions or overall engagement in school?""",
    """Is It Ethical for Teachers to Use AI to Grade Papers? Many schools do not allow students to use artificial intelligence to complete their assignments. Should teachers be held to the same standard? Do you think teachers should be able to use the technology at all? If so, in which instances would it be acceptable, and what guidelines should teachers follow when using it?""",
    """Should Social Media Companies Be Responsible for Fact-Checking Their Sites? A few months ago, Meta, the company that owns Facebook and Instagram, has ended its longstanding fact-checking program. Is that a good idea? What could this mean for users? Do you believe social media companies should be responsible for fact-checking lies, misinformation, disinformation and conspiracy theories on their sites? Why or why not? To what extent does it matter if what we see on social media is true?""",
    """Should Single-Use Vapes Be Banned Everywhere? In an effort to protect young people’s health, England plans to ban disposable vapes next year. Do you think this measure will curb vaping among teens? To what extent do you think the government should have a role in trying to reduce smoking and vaping? Do you think your government should be doing more to discourage people from picking up the habits? Why or why not? What consequences could the ban have for the environment?""",
    """How Important Is a Free Press to Our Democracy? What role do journalists play in our society - whether they work for big national newspapers, niche podcasts or YouTube channels? What would happen if they couldn’t freely investigate and report the news? For example, what if journalists were barred from informing the public about the actions of powerful people like government officials, corporate executives, and celebrities? How would it affect our democracy?""",
    """Does Everyone Have a Responsibility to Vote? Is it OK not to vote, or is voting a civic duty? What to you are the most compelling reasons for showing up at the polls? What about those for sitting out? Why do you think so many people don’t vote? What do you think would encourage them to participate more?""",
    """Workers across industries are concerned about AI coming for their work. Are you worried about AI taking human jobs? Why or why not? Which types of work do you think are most vulnerable to automation? Do you think the fears about AI are overblown?""",
    """Should All Children Under 16 Be Barred From Social Media? Australia recently passed a law that does just that. Should other countries do the same? What is your reaction to Australia’s new law? Do you think it is a good idea? Will it be effective? What do you think are the negative effects of social media on young people? If you don’t think a similar law would work, what should be done to address these problems?""",
    """Should Grades Be Based on Excellence or Effort? Some people think that too many students today wrongly expect to be rewarded for their efforts rather than the quality of their work. Do you agree? Do you think marks are accurate reflections of students’ learning? What do you think student grades should be based on? How much, if at all, should effort and hard work factor in?"""
]

creative = [
    """What if people had microchips in their eyes that allowed them to record everything they see?""",
    """What if no one ever had to work again because robots took care of everything?""",
    """What if our memories could be stolen and sold on the black market?""",
    """What if we could restore the diminishing populations of endangered species by cloning them?""",
    """What if you could test the outcomes of different decisions in virtual reality with 100% accuracy?""",
    """What if the usage of cars for personal needs were banned?""",
    """What if there were a world where people spend all their personal time escaping to idyllic VR settings instead of confronting the challenges of real life?""",
    """What if vibe-coding became so popular that every IT company would switch to it?""",
    """What if the theory that COVID-19 vaccines contain microchips were true?""",
    """What if it were forbidden to sell or buy products containing meat?"""
]

user_html = ""
for user in users:
    random.seed(user)
    argumentative_for_user = random.sample(argumentative, 2)
    creative_for_user = random.sample(creative, 2)

    user_html += f"""
\"{user}\": {{
    \"argumentative\":
    [
    `{argumentative_for_user[0]}`,
    `{argumentative_for_user[1]}`
    ],

    \"creative\":
    [
    `{creative_for_user[0]}`,
    `{creative_for_user[1]}`
    ],
    }},
"""

index_html = r"""
<html>

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type">
    <style type="text/css">
        ol.lst-kix_fe9brg7u0cec-6.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-6 0
        }

        .lst-kix_cmtnlngtu4bi-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_cmtnlngtu4bi-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_cmtnlngtu4bi-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_101bpdgvbzvd-8 {
            list-style-type: none
        }

        .lst-kix_101bpdgvbzvd-3>li:before {
            content: "-  "
        }

        .lst-kix_fe9brg7u0cec-4>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-4, lower-latin) ". "
        }

        .lst-kix_101bpdgvbzvd-2>li:before {
            content: "-  "
        }

        .lst-kix_fe9brg7u0cec-5>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-5, lower-roman) ". "
        }

        .lst-kix_fe9brg7u0cec-7>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-7, lower-latin) ". "
        }

        .lst-kix_fe9brg7u0cec-6>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-6, decimal) ". "
        }

        .lst-kix_fe9brg7u0cec-8>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-8, lower-roman) ". "
        }

        .lst-kix_101bpdgvbzvd-0>li:before {
            content: "-  "
        }

        .lst-kix_x6aktldezdgv-1>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-1
        }

        .lst-kix_101bpdgvbzvd-1>li:before {
            content: "-  "
        }

        .lst-kix_cmtnlngtu4bi-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_cmtnlngtu4bi-8>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_fe9brg7u0cec-5 {
            list-style-type: none
        }

        ol.lst-kix_fe9brg7u0cec-6 {
            list-style-type: none
        }

        ol.lst-kix_fe9brg7u0cec-3 {
            list-style-type: none
        }

        ol.lst-kix_fe9brg7u0cec-4 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-4.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-4 0
        }

        ol.lst-kix_fe9brg7u0cec-7 {
            list-style-type: none
        }

        ol.lst-kix_fe9brg7u0cec-8 {
            list-style-type: none
        }

        .lst-kix_101bpdgvbzvd-6>li:before {
            content: "-  "
        }

        ol.lst-kix_fe9brg7u0cec-1 {
            list-style-type: none
        }

        ol.lst-kix_fe9brg7u0cec-2 {
            list-style-type: none
        }

        .lst-kix_101bpdgvbzvd-4>li:before {
            content: "-  "
        }

        .lst-kix_101bpdgvbzvd-5>li:before {
            content: "-  "
        }

        ol.lst-kix_fe9brg7u0cec-0 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-7.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-7 0
        }

        .lst-kix_fe9brg7u0cec-3>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-3, decimal) ". "
        }

        .lst-kix_x6aktldezdgv-3>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-3
        }

        .lst-kix_fe9brg7u0cec-2>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-2, lower-roman) ". "
        }

        .lst-kix_x6aktldezdgv-0>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-0
        }

        ol.lst-kix_x6aktldezdgv-1.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-1 0
        }

        .lst-kix_cmtnlngtu4bi-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_cmtnlngtu4bi-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_fe9brg7u0cec-1>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-1, lower-latin) ". "
        }

        .lst-kix_cmtnlngtu4bi-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_101bpdgvbzvd-7>li:before {
            content: "-  "
        }

        .lst-kix_fe9brg7u0cec-0>li:before {
            content: "" counter(lst-ctn-kix_fe9brg7u0cec-0, decimal) ". "
        }

        ol.lst-kix_fe9brg7u0cec-1.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-1 0
        }

        .lst-kix_fe9brg7u0cec-8>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-8
        }

        .lst-kix_101bpdgvbzvd-8>li:before {
            content: "-  "
        }

        .lst-kix_cmtnlngtu4bi-0>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_fe9brg7u0cec-8.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-8 0
        }

        ol.lst-kix_fe9brg7u0cec-4.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-4 0
        }

        ol.lst-kix_x6aktldezdgv-5.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-5 0
        }

        .lst-kix_fe9brg7u0cec-0>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-0
        }

        ol.lst-kix_x6aktldezdgv-0 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-8>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-8
        }

        ol.lst-kix_x6aktldezdgv-1 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-2 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-3 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-4 {
            list-style-type: none
        }

        .lst-kix_fe9brg7u0cec-6>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-6
        }

        ol.lst-kix_x6aktldezdgv-5 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-0 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-6 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-1 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-2>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-2
        }

        ol.lst-kix_x6aktldezdgv-7 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-2 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-8 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-3 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-4 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-5 {
            list-style-type: none
        }

        ul.lst-kix_101bpdgvbzvd-6 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-5>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-5
        }

        ul.lst-kix_101bpdgvbzvd-7 {
            list-style-type: none
        }

        ol.lst-kix_fe9brg7u0cec-3.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-3 0
        }

        .lst-kix_22x579xxms5k-2>li:before {
            content: "-  "
        }

        ul.lst-kix_22x579xxms5k-8 {
            list-style-type: none
        }

        ul.lst-kix_22x579xxms5k-6 {
            list-style-type: none
        }

        ul.lst-kix_22x579xxms5k-7 {
            list-style-type: none
        }

        .lst-kix_22x579xxms5k-1>li:before {
            content: "-  "
        }

        ol.lst-kix_x6aktldezdgv-6.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-6 0
        }

        .lst-kix_22x579xxms5k-0>li:before {
            content: "-  "
        }

        .lst-kix_x6aktldezdgv-3>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-3, decimal) ". "
        }

        .lst-kix_x6aktldezdgv-4>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-4, lower-latin) ". "
        }

        ol.lst-kix_x6aktldezdgv-3.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-3 0
        }

        ul.lst-kix_geynw9iyvxg3-8 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-2>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-2, lower-roman) ". "
        }

        .lst-kix_x6aktldezdgv-6>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-6, decimal) ". "
        }

        ul.lst-kix_geynw9iyvxg3-6 {
            list-style-type: none
        }

        ul.lst-kix_geynw9iyvxg3-7 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-7>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-7
        }

        ul.lst-kix_geynw9iyvxg3-4 {
            list-style-type: none
        }

        ul.lst-kix_22x579xxms5k-0 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-4 {
            list-style-type: none
        }

        ul.lst-kix_geynw9iyvxg3-5 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-0>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-0, decimal) ". "
        }

        .lst-kix_x6aktldezdgv-7>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-7, lower-latin) ". "
        }

        .lst-kix_x6aktldezdgv-8>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-8, lower-roman) ". "
        }

        ul.lst-kix_22x579xxms5k-1 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-5 {
            list-style-type: none
        }

        ul.lst-kix_geynw9iyvxg3-2 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-6 {
            list-style-type: none
        }

        ul.lst-kix_geynw9iyvxg3-3 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-7 {
            list-style-type: none
        }

        .lst-kix_fe9brg7u0cec-4>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-4
        }

        ul.lst-kix_geynw9iyvxg3-0 {
            list-style-type: none
        }

        .lst-kix_22x579xxms5k-4>li:before {
            content: "-  "
        }

        ul.lst-kix_22x579xxms5k-4 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-0 {
            list-style-type: none
        }

        ul.lst-kix_geynw9iyvxg3-1 {
            list-style-type: none
        }

        .lst-kix_x6aktldezdgv-1>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-1, lower-latin) ". "
        }

        ul.lst-kix_22x579xxms5k-5 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-1 {
            list-style-type: none
        }

        ul.lst-kix_22x579xxms5k-2 {
            list-style-type: none
        }

        .lst-kix_22x579xxms5k-3>li:before {
            content: "-  "
        }

        ul.lst-kix_cmtnlngtu4bi-2 {
            list-style-type: none
        }

        ul.lst-kix_22x579xxms5k-3 {
            list-style-type: none
        }

        ul.lst-kix_cmtnlngtu4bi-3 {
            list-style-type: none
        }

        ol.lst-kix_x6aktldezdgv-0.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-0 0
        }

        .lst-kix_22x579xxms5k-5>li:before {
            content: "-  "
        }

        .lst-kix_22x579xxms5k-6>li:before {
            content: "-  "
        }

        .lst-kix_fe9brg7u0cec-3>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-3
        }

        .lst-kix_22x579xxms5k-8>li:before {
            content: "-  "
        }

        ol.lst-kix_fe9brg7u0cec-2.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-2 0
        }

        .lst-kix_x6aktldezdgv-5>li:before {
            content: "" counter(lst-ctn-kix_x6aktldezdgv-5, lower-roman) ". "
        }

        .lst-kix_22x579xxms5k-7>li:before {
            content: "-  "
        }

        ol.lst-kix_fe9brg7u0cec-7.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-7 0
        }

        ol.lst-kix_fe9brg7u0cec-5.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-5 0
        }

        .lst-kix_geynw9iyvxg3-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_geynw9iyvxg3-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_geynw9iyvxg3-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_fe9brg7u0cec-2>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-2
        }

        .lst-kix_fe9brg7u0cec-5>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-5
        }

        .lst-kix_x6aktldezdgv-6>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-6
        }

        ul.lst-kix_cmtnlngtu4bi-8 {
            list-style-type: none
        }

        .lst-kix_fe9brg7u0cec-7>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-7
        }

        ol.lst-kix_x6aktldezdgv-8.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-8 0
        }

        .lst-kix_fe9brg7u0cec-1>li {
            counter-increment: lst-ctn-kix_fe9brg7u0cec-1
        }

        .lst-kix_geynw9iyvxg3-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_geynw9iyvxg3-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_geynw9iyvxg3-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_geynw9iyvxg3-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_x6aktldezdgv-4>li {
            counter-increment: lst-ctn-kix_x6aktldezdgv-4
        }

        .lst-kix_geynw9iyvxg3-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_geynw9iyvxg3-3>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_fe9brg7u0cec-0.start {
            counter-reset: lst-ctn-kix_fe9brg7u0cec-0 0
        }

        ol.lst-kix_x6aktldezdgv-2.start {
            counter-reset: lst-ctn-kix_x6aktldezdgv-2 0
        }

        li.li-bullet-0:before {
            margin-left: -18pt;
            white-space: nowrap;
            display: inline-block;
            min-width: 18pt
        }

        ol {
            margin: 0;
            padding: 0
        }

        table td,
        table th {
            padding: 0
        }

        .c9 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: center;
            height: 11pt
        }

        .c5 {
            color: #000000;
            font-weight: 700;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 13pt;
            font-family: "Arial";
            font-style: normal
        }

        .c1 {
            color: #000000;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 11pt;
            font-family: "Arial";
            font-style: normal
        }

        .c12 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: center
        }

        .c2 {
            padding-top: 0pt;
            padding-bottom: 12pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c0 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c16 {
            color: #000000;
            text-decoration: none;
            vertical-align: baseline;
            font-family: "Arial";
            font-style: normal
        }

        .c4 {
            text-decoration-skip-ink: none;
            -webkit-text-decoration-skip: none;
            color: #1155cc;
            text-decoration: underline
        }

        .c10 {
            text-decoration-skip-ink: none;
            -webkit-text-decoration-skip: none;
            text-decoration: underline
        }

        .c7 {
            background-color: #ffffff;
            max-width: 550pt;
            padding: 72pt 72pt 72pt 72pt;
            width:140%;
            margin-left: auto;
            margin-right: auto;
        }

        .c3 {
            color: inherit;
            text-decoration: inherit
        }

        .c17 {
            padding: 0;
            margin: 0
        }

        .c11 {
            margin-left: 36pt;
            padding-left: 0pt
        }

        .c21 {
            text-indent: 36pt
        }

        .c6 {
            font-weight: 700
        }

        .c15 {
            font-size: 13pt
        }

        .c20 {
            font-size: 16pt
        }

        .c8 {
            font-size: 14pt
        }

        .c22 {
            margin-right: -12.5pt
        }

        .c14 {
            font-style: italic
        }

        .c18 {
            font-size: 11pt
        }

        .c19 {
            font-size: 15pt
        }

        .c13 {
            height: 11pt
        }

        .title {
            padding-top: 0pt;
            color: #000000;
            font-size: 26pt;
            padding-bottom: 3pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .subtitle {
            padding-top: 0pt;
            color: #666666;
            font-size: 15pt;
            padding-bottom: 16pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        li {
            color: #000000;
            font-size: 11pt;
            font-family: "Arial"
        }

        p {
            margin: 0;
            color: #000000;
            font-size: 11pt;
            font-family: "Arial"
        }

        h1 {
            padding-top: 20pt;
            color: #000000;
            font-size: 20pt;
            padding-bottom: 6pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h2 {
            padding-top: 18pt;
            color: #000000;
            font-size: 16pt;
            padding-bottom: 6pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h3 {
            padding-top: 16pt;
            color: #434343;
            font-size: 14pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h4 {
            padding-top: 14pt;
            color: #666666;
            font-size: 12pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h5 {
            padding-top: 12pt;
            color: #666666;
            font-size: 11pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h6 {
            padding-top: 12pt;
            color: #666666;
            font-size: 11pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            font-style: italic;
            orphans: 2;
            widows: 2;
            text-align: left
        }
    </style>
</head>

<body class="c7 doc-content">
    <p class="c12"><span class="c16 c6 c20">Trustworthy and Explainable AI-generated Text Detection</span></p>
    <p class="c9"><span class="c1"></span></p>
    <p class="c12"><span class="c16 c6 c19">User Study Guidelines</span></p>
    <p class="c0 c13"><span class="c16 c6 c8"></span></p>
    <p class="c0"><span class="c6 c8">General information</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">This user study serves the project &ldquo;Trustworthy and Explainable AI-generated
            Text Detection&rdquo;. The goal of the study is to collect detailed interaction data between humans and
            LLMs, to later structure it into a publicly available dataset. With this dataset, we aim to study human-AI
            interaction patterns and differentiate between human-written and AI-generated text.</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c16 c6 c8">Guidelines</span></p>
    <p class="c0 c13"><span class="c6 c8 c16"></span></p>
    <p class="c0"><span>These guidelines provide the necessary information for you to participate in the user study. The
            study consists of three parts. First, you will fill out a survey on your background, including your age,
            English level, and previous use of LLMs. Then, you will start your interaction with the system. You will
            have a small warm-up during which you get familiar with the system. Then, you will write three texts on
            different topics </span><span class="c10">using LLM assistance</span><span class="c1">&nbsp;(mandatory): one
            argumentative, one creative, and one explanatory. Lastly, you will fill out a questionnaire about your
            experience with the system.</span></p>
    <p class="c2"><span><br></span><span class="c6">Qualifications</span><span>:</span><span
            class="c15">&nbsp;</span><span>To be allowed to participate, you have to have English skills of </span><span
            class="c10 c6">at least B1</span><span class="c1">.</span></p>
    <p class="c2"><span class="c6">Duration of study</span><span class="c1">: 60-80 minutes.</span></p>
    <p class="c2"><span class="c16 c6 c8">Privacy statement</span></p>
    <p class="c2"><span class="c1">All data in this study is processed according to the laws of the European General
            Data Protection Regulation (GDPR) and the Data Protection and Freedom of Information laws of the German
            state of Hesse (HDSIG). The data will only be used according to the descriptions in General
            information.</span></p>
    <p class="c2"><span class="c6">Collected Data</span></p>
    <p class="c2"><span class="c1">In the context of this study, the following anonymous data will be collected:</span>
    </p>
    <ul class="c17 lst-kix_cmtnlngtu4bi-0 start">
        <li class="c2 c11 li-bullet-0"><span class="c1">Background survey: all answers about your background information
                (age, gender, field of study and highest education, English skills, experience with LLMs). We do not
                save information about your name and email.</span></li>
        <li class="c2 c11 li-bullet-0"><span class="c1">User Study: Usage data of the tool including all interactions
                like button clicks, typing, content of LLM queries. We save your username, without saving the mapping to
                your email.</span></li>
        <li class="c2 c11 li-bullet-0"><span class="c1">User Experience Survey: all answers to questions regarding the
                use of the software.</span></li>
    </ul>
    <p class="c2"><span class="c16 c6 c18">Confidentiality</span></p>
    <p class="c2"><span class="c1">All data collected in this study will be handled confidentially and anonymously. The
            demographic information collected cannot be used to trace back to individuals. We will never ask you for
            your name or other clear personal information.</span></p>
    <p class="c2"><span class="c16 c6 c18">Storage</span></p>
    <p class="c2"><span class="c1">All data collected in this study is stored in Germany and will be deleted 10 years
            after collection. Participants can request their data to be deleted at any time by providing their
            pseudonym. The data can be used for research and can be published after anonymization. To guarantee
            anonymity, the data from the questionnaire will only be published in aggregate, and not with individual
            answers. In case of data publication, the data can no longer be deleted in the aggregated form. This consent
            form will be stored separated from the rest of the data and deleted after 10 years.</span></p>
    <p class="c2"><span class="c16 c6 c18">Rights of the Participants</span></p>
    <p class="c2"><span class="c1">Participation in this study is voluntary. At any time during the study, participants
            are free to terminate their participation and revoke their consent. All of the data related to these
            participants will be deleted. All participants have the right to get information on the personal data that
            is stored about them, and to request its deletion. In cases of dispute, participants have the right to file
            a complaint with the data protection officer of the state of Hesse (contact details below).</span></p>
    <p class="c0"><span class="c16 c6 c18">Contact</span></p>
    <p class="c0"><span class="c1">If you have questions, suggestions or complaints, please do not hesitate to contact
            the study coordinators.</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c16 c6 c18">Study coordinators</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">Marina Sakharova</span></p>
    <p class="c0"><span class="c4"><a class="c3"
                href="mailto:marina.sakharova@stud.tu-darmstadt.de">marina.sakharova@stud.tu-darmstadt.de</a></span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">Nils Dycke</span></p>
    <p class="c0"><span class="c4"><a class="c3"
                href="mailto:dycke@ukp.informatk.tu-darmstadt.de">dycke@ukp.informatk.tu-darmstadt.de</a></span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">Ilia Kuznetsov</span></p>
    <p class="c0"><span class="c4"><a class="c3"
                href="mailto:ilia.kuznetsov@tu-darmstadt.de">ilia.kuznetsov@tu-darmstadt.de</a></span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c16 c6 c18">Principal Investigator</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">Prof. Dr. Iryna Gurevych</span></p>
    <p class="c0"><span class="c1">Ubiquitous Knowledge Processing Lab (UKP)</span></p>
    <p class="c0"><span class="c1">FB 20</span></p>
    <p class="c0"><span class="c1">Technische Universit&auml;t Darmstadt</span></p>
    <p class="c0"><span class="c1">S2|02 B110</span></p>
    <p class="c0"><span class="c1">Hochschulstra&szlig;e 10</span></p>
    <p class="c0"><span class="c1">64289 Darmstadt</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c2"><span class="c16 c6 c8">Part 0: Background information survey</span></p>
    <p class="c2"><span>Before you start the main part of the study, please fill out </span><span class="c4"><a
                class="c3"
                href="https://www.google.com/url?q=https://forms.gle/iR31XdfywtF7GDTs7&amp;sa=D&amp;source=editors&amp;ust=1761666145166801&amp;usg=AOvVaw3uygvwfefJT4689-D0sLHB">this
                survey</a></span><span class="c1">&nbsp;on your background information. We ask questions like your age,
            English level, and field of study. </span></p>
    <p class="c2"><span class="c16 c6 c8">Part 1: Introduction to CARE</span></p>
    <p class="c2"><span class="c1">In this part, you will first log into our software for human-AI interaction. After
            the log-in, you will have a 5 minutes warm-up where you can test the system&rsquo;s capabilities. Then you
            will perform three writing tasks, &nbsp;ca. 15 minutes each. If you have any questions, please do not
            hesitate to ask for clarifications or technical assistance.</span></p>
    <p class="c2"><span class="c5">Log into CARE</span></p>
    <ul class="c17 lst-kix_geynw9iyvxg3-0 start">
        <li class="c2 c11 li-bullet-0"><span>Go to </span><span class="c4"><a class="c3"
                    href="https://www.google.com/url?q=https://txaitd.ukp.informatik.tu-darmstadt.de&amp;sa=D&amp;source=editors&amp;ust=1761666145168465&amp;usg=AOvVaw2gA6CB50wfKRk8R0c8X_8m">https://txaitd.ukp.informatik.tu-darmstadt.de</a></span>
        </li>
        <li class="c2 c11 li-bullet-0"><span class="c1">We have provided you with your username and password. Enter
                them to log into the system. </span></li>
    </ul>
    <p class="c2"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;"><img
                alt="" src="images/image1.png"
                style="width: 800px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <ul class="c17 lst-kix_geynw9iyvxg3-0">
        <li class="c2 c11 li-bullet-0"><span class="c1">After the login, you will be redirected to Documents section.
                You will work only with this part of the Software.</span></li>
    </ul>
    <p class="c2"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1200px; height: auto;"><img
                alt="" src="images/image6.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c2 c13"><span class="c1"></span></p>
    <p class="c2"><span class="c5">Task 0: Warm-up</span></p>
    <p class="c2"><span class="c1">This task&rsquo;s goal is for you to get familiar with the system. You will edit an
            example document with the help of LLMs..</span></p>
    <p class="c2"><span>In the Documents overview, you will see four documents for the warm-up and three tasks. The
            first document is </span><span class="c14">Task 0: Warm-up</span><span class="c1">. Click on &ldquo;Access
            document&rdquo; to open it.</span></p>
    <p class="c2"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1200px; height: auto;"><img
                alt="" src="images/image5.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c2"><span class="c1">You are now in the document editor where you can type your text and interact with
            LLMs.</span></p>
    <p class="c2"><span>There are two available types of interaction: </span><span class="c6">Revision
        </span><span>(grammar or stylistic fixes, reformulation) and </span><span class="c6">continuation </span><span
            class="c1">(text generation like essay wrap-up generation). To send a revision query, type some text and
            select the part that you want to be revised. You can then click on the &ldquo;Enter your query&rdquo; field
            and enter your query. If you don&rsquo;t type anything, the model will be asked to fix the grammar.</span>
    </p>
    <p class="c2"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1200px; height: auto;"><img
                alt="" src="images/image3.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c2"><span>To send a continuation query, insert the cursor in the place where you want the text to be
            continued and click </span><span class="c14">CTRL+Q</span><span class="c1">. Type your query. If you
            don&rsquo;t type anything, the model will be prompted to continue your text.</span></p>
    <p class="c2"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1200px; height: auto;"><img
                alt="" src="images/image2.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c2"><span class="c1">When the model answer comes back, a new window will appear. You will have the
            possibility to either accept or reject the proposed text. If you accept it, the text will be copied to the
            editor. </span></p>
    <p class="c2"><span class="c1">Note: you may edit your text while waiting for the response. Your changes will be
            merged with the model&rsquo;s changes.</span></p>
    <p class="c2 c22"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1200px; height: auto;"><img
                alt="" src="images/image4.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c2"><span class="c1">You may experiment with the system for max. 5 minutes. When the time is over, you
            will get a pop-up notification that you should start working on other tasks.</span></p>
    <p class="c2"><span class="c16 c6 c8">Part 2: LLM-powered writing</span></p>
    <p class="c2"><span class="c5">Task 1: Argumentative writing</span></p>
    <p class="c2"><span>In this part, you have 15 minutes to write an argumentative essay. You </span><span
            class="c10 c6">HAVE TO</span><span class="c1">&nbsp;interact with the LLM during your writing process.
        </span></p>
    <p class="c2"><span>Enter the Document named &ldquo;Task 1: Argumentative Writing&rdquo;. Select </span><span
            class="c6">one </span><span class="c1">of two following topics:</span></p>
    <ol class="c17 lst-kix_x6aktldezdgv-0 start" start="1" id="argumentative">
    </ol>
    <p class="c2"><span>Both topics contain several questions. Try to answer them all, or even come up with your own
            related questions. Your text </span><span class="c10 c6">has to</span><span class="c1">&nbsp;have clear
            structure and conclusion. Try to find strong arguments to defend your position on the topic, as well as to
            counter it with opposite arguments. Approximate expected length is 300-400 words, but it may vary.</span>
    </p>
    <p class="c2"><span class="c1">After 15 minutes are over, you get a notification that you should wrap-up your work
            and move on to the next part.</span></p>
    <p class="c2"><span class="c5">Task 2: Creative writing</span></p>
    <p class="c2"><span>In this part, you have 15 minutes to write a creative story. You </span><span
            class="c6 c10">HAVE TO</span><span class="c1">&nbsp;interact with LLMs during the writing. </span></p>
    <p class="c2"><span>Enter the Document named &ldquo;Task 2: Creative Writing&rdquo;. Select </span><span
            class="c6">one </span><span class="c1">of two following topics:</span></p>
    <ol class="c17 lst-kix_fe9brg7u0cec-0 start" start="1" id="creative">
    </ol>
    <p class="c2"><span class="c1">Both questions set up an imaginable scenario where one aspect of our world has
            changed. You have complete freedom - pick the tone, character, and style that appeal to you. Here are some
            ideas for inspiration:</span></p>
    <ul class="c17 lst-kix_22x579xxms5k-0 start">
        <li class="c2 c11 li-bullet-0"><span class="c1">Tell a story from the perspective of an inhabitant of the new
                world - describe your typical day and how the changes affect your life, work, relationships, etc.</span>
        </li>
        <li class="c2 c11 li-bullet-0"><span class="c1">Write a newspaper-style text that interviews several people from
                that world.</span></li>
        <li class="c2 c11 li-bullet-0"><span class="c1">Provide an analytical article that analyses the societal,
                economical, or cultural impact that such changes could have on our society.</span></li>
    </ul>
    <p class="c2"><span class="c1">Approximate expected length is 300-400 words, but it may vary. After 15 minutes are
            over, you get a notification that you should wrap-up your work and move on to the next part.</span></p>
    <p class="c2"><span class="c5">Task 3: Explanatory writing</span></p>
    <p class="c2"><span>In this part, you have 15 minutes to write an explanatory text. You </span><span
            class="c10 c6">HAVE TO</span><span class="c1">&nbsp;interact with LLMs during the writing. </span></p>
    <p class="c2"><span class="c1">Enter the Document named &ldquo;Task 3: Explanatory Writing&rdquo;.</span></p>
    <p class="c0"><span>Explain a concept or a phenomenon that you recently learned and found exciting. Maybe you
            watched a video about a certain historical period, read a paper with interesting approaches, or learned a
            new theory at your university. Explain it for </span><span class="c6">general audience</span><span
            class="c1">, in simple terms: What is the core idea? Where and why is it used? How does it work? What are
            the benefits and the drawbacks?</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">Examples may be:</span></p>
    <ul class="c17 lst-kix_101bpdgvbzvd-0 start">
        <li class="c0 c11 li-bullet-0"><span class="c1">Transformers architecture, used in Large Language Models like
                GPT-4, is a technology that revolutionized machine text generation and understanding&hellip;</span></li>
        <li class="c0 c11 li-bullet-0"><span class="c1">Social engineering is a psychological technique to
                &ldquo;hack&rdquo; people with the purpose to get access to restricted or personal information.
                &hellip;</span></li>
        <li class="c0 c11 li-bullet-0"><span class="c1">There are vast differences in railway systems throughout the
                world: in terms of reliability, coverage, speed. Japanese trains &hellip;</span></li>
    </ul>
    <p class="c0 c13"><span class="c1"></span></p>
    <p class="c0"><span class="c1">Your text should give a clear explanation on the concept/person/time
            period/technology etc, so that people without deep knowledge can get a good understanding from your
            text.</span></p>
    <p class="c2"><span class="c1">Approximate expected length is 250-400 words, but it may vary. After 15 minutes are
            over, you get a notification that you should wrap-up your work and move on to the survey.</span></p>
    <p class="c2"><span class="c6 c8">Part 3: User Experience Survey</span></p>
    <p class="c2"><span>After you finished all interactions, please fill out</span><span
            class="c6 c8">&nbsp;</span><span class="c4"><a class="c3"
                href="https://www.google.com/url?q=https://forms.gle/dUWvkoLqSWeDVnmq8&amp;sa=D&amp;source=editors&amp;ust=1761666145186429&amp;usg=AOvVaw0vioPrsnpzQr4tphr08yRl">user
                experience survey</a></span><span class="c1">. There, we ask about possible problems, limitations, and
            overall satisfaction. This helps us to understand how we can improve our software. </span></p>
    <p class="c2"><span class="c1">Thank you for your participation!</span></p>
    <p class="c0 c13"><span class="c1"></span></p>
</body>

</html>

<script>
    const topics = {
"""

index_html += user_html + """
    }
    const urlParams = new URLSearchParams(window.location.search);
    const userId = urlParams.get("id");
    const argumentative = document.getElementById("argumentative");
    const creative = document.getElementById("creative");
    if (userId && topics[userId]) {
        argumentative.innerHTML = `<li class="c2 c11 li-bullet-0"><span class="c1">${topics[userId].argumentative[0]}</span></li>
        <li class="c2 c11 li-bullet-0"><span class="c1">${topics[userId].argumentative[1]}</span></li>`
        creative.innerHTML = `<li class="c2 c11 li-bullet-0"><span class="c1">${topics[userId].creative[0]}</span></li>
        <li class="c2 c11 li-bullet-0"><span class="c1">${topics[userId].creative[1]}</span></li>`
    } else {
        argumentative.innerHTML = '<li class="c2 c11 li-bullet-0"><span class="c1">Invalid user ID. Please check your URL. </span></li>'
        creative.innerHTML = '<li class="c2 c11 li-bullet-0"><span class="c1">Invalid user ID. Please check your URL. </span></li>'
    }
</script>
"""

with open("index.html", "w") as f:
    f.write(index_html)