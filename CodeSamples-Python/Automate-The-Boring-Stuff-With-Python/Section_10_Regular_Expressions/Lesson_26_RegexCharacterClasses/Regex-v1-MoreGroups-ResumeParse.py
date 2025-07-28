# The regex method findall() is passed a string, and returns all matches in it, not just the first match.
# If the regex has 0 or 1 group, findall() returns a list of strings.
# If the regex has 2 or more groups, findall() returns a list of tuples of strings.
# \d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
# The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

# import the Regex modole
import re

# Create a Regex Pattern Matching Object with No Groups
phoneRegex_NoGroups = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Create a Regex Pattern Matching Object with 3 Groups
phoneRegex_With3Groups = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

# Create a String Variable based upon a sample Resume (https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4262459768)
resumeExample1 = '''
123 Elm Street, Fall River, MA 02723 Cell: 508-555-5555, Home: 508-555-1234

Machinify is the leading provider of AI-powered software products that transform healthcare claims and payment operations. Each year, the healthcare industry generates over $200B in claims mispayments, creating incredible waste, friction and frustration for all participants: patients, providers, and especially payers. Machinify’s revolutionary AI-platform has enabled the company to develop and deploy, at light speed, industry-specific products that increase the speed and accuracy of claims processing by orders of magnitude.

Machinify is hiring a Quality Assurance Engineer to build, design, and develop manual tools and tests with interest in growing their skills in automation testing.

We're the Healthcare industry’s most comprehensive application suite, powered by the combination of AI and deep clinical expertise. Our engineers leverage machine learning technology to build a better future for the patient, payer, and provide experience. Our teams are highly collaborative across all areas of the organization, autonomous in their ability to perform work, and highly impactful towards the success of the business.

What You’ll Do

Work with Product Manager and development team to clearly understand requirements
Develop/Maintain test cases for end-to-end testing of product
Create and maintain test data across test environments
Execute manual/automated functional and regression test cases, report, and documention of bugs
Ability to collaborate well with cross-functional teams and resolve any open issues
Provide timely QA updates to project managers and team leads

What You Bring

5+ years of manual software testing experience and strong analytical skills
Experience with System/Application Testing. 
Advanced understanding of SQL queries to analyze and manipulate data
Detailed knowledge of application functions, bug fixing, and testing protocols
You are self driven, motivated, and presents a sense of ownership
Critical thinking and problem solving skills
Can identify with being scrappy, adaptable, and ambitious
Comfortable with ambiguity and taking the initiative when required
Clear and collaborative communication skills 
Experience with one or more programming languages is a plus (preferably JavaScript, Python)
Healthcare domain knowledge is a plus

What We Offer

Work from anywhere in the US! Machinify is digital-first.
Flexible and trusting environment where you’ll feel empowered to do your best work
Unlimited PTO, recharge days and one no-meetings day a week
Medical/Dental/Vision for employees & their families
Competitive salary, equity, 401(k) sponsorship
Generous Learning and Development Reimbursement policy

The salary for this position is based on an array of factors unique to each candidate: Such as years and depth of experience, set skills, certifications, etc. The base salary range for this role is $140k to $170k. We are hiring for different levels, and our Recruiting team will let you know if you qualify for a different role/range. Salary is one component of the total compensation package, which includes meaningful equity, excellent healthcare, flexible time off, and other benefits and perks to meet the needs of each individual.

Equal Employment Opportunity at Machinify

Machinify is committed to hiring talented and qualified individuals with diverse backgrounds for all of its positions. Machinify believes that the gathering and celebration of unique backgrounds, qualities, and cultures enriches the workplace.'''

# Utilize re.search() to return the 1st Regex Pattern match identified
phoneRegex_With3Groups.search(resumeExample1)

# Utilize re.findall() to return a List of all the matches and create a variable to store the data
phoneRecords = phoneRegex_With3Groups.findall(resumeExample1)

# Print to screen the output
print(phoneRecords)