#!/usr/bin/env python3

import sys # System utilities
if not sys.version_info[0] == 3: # Check to ensure Python 3
    sys.exit("Please use Python 3 for this script")

try: # Try to import argparse
    import argparse
    import re # Enable regular expression
    import os # Operating system utilities
except ImportError: # Catch the error
    sys.exit("Please use Python 3 or higher")

class LabMeetingPage(object):
    def __init__(self, citation, url, leader, date):
        self.citation = citation
        self.url = url
        self.leader = leader
        self.date = date
        self._pullAuthorList()
        self._pullPublicationYear()
        self._pullArticleTitle()
        self._pullJournalTitle()

    def _pullAuthorList(self):
        """Pull the author list from a citation"""
        authorRegex = re.compile(r'([A-Za-z,\s\.]*)\(') # Pull all letters, commas, spaces, and periods until the first open-parenthesis
        self.authorList = authorRegex.search(self.citation).groups()[0].strip() # Get the author list, removing the last space

    def _pullPublicationYear(self):
        """Pull the publication year from a citation"""
        yearRegex = re.compile(r'\(([0-9]{4})') # Pull four numbers after the first open-parenthesis
        self.year = yearRegex.search(self.citation).groups()[0] # Get the year

    def _pullArticleTitle(self):
        """Pull the title of the article from a citation"""
        titleRegex = re.compile(r'\)\s([A-z\:\,\-\s]*)') # Pull all letters, colons, commas, hyphens, and spaces following the first close-parenthesis
        titleSearch = titleRegex.search(self.citation) # Obtain a regex object for this search
        self.articleTitle = titleSearch.groups()[0] # Get the title of the article
        self.titleEnd = titleSearch.end() # Get the ending position of the article title

    def _pullJournalTitle(self):
        """Pull the title of the journal from a citation"""
        journalRegex = re.compile(r'\s([A-z0-9\-\:\s]*)') # Pull all letters, numbers, colons, hypens, and spaces following a space
        self.journalTitle = journalRegex.search(self.citation, self.titleEnd).groups()[0] # Get the journal title, which comes after the article title

    def printValues(self):
        print("Author List:\t" + self.authorList)
        print("Publication year:\t(" + str(self.year) + ")")
        print("Article Title:\t" + self.articleTitle)
        print("Journal:\t" + self.journalTitle)

    def assembleMarkdownFile(self, outdirectory):
        """Assemble a markdown file for the website"""
        outfile = self.date + '-' + '-'.join(self.leader.split()) + '.md' # Create an outfile name
        ostream = open(outdirectory + '/' + outfile, 'w') # Open the output file for writing
        ostream.write('---\n') # Write the start of the YAML header
        ostream.write('layout: meeting\n') # Write the layout line
        ostream.write('meet_date: ' + self.date + '\n') # Write the meeting date line
        ostream.write('leader: "' + self.leader + '"\n') # Write the meeting leader line
        ostream.write('paper_author: "' + self.authorList + '"\n') # Write the paper author line
        ostream.write('paper_year: ' + str(self.year) + '\n') # Write the publication year line
        ostream.write('paper_title: "' + self.articleTitle + '"\n') # Write the article title line
        ostream.write('paper_journal: "' + self.journalTitle + '"\n') # Write the journal title line
        ostream.write('paper_url: "' + self.url + '"\n') # Write the paper url line
        ostream.write('---\n') # Write the end of the YAML header
        ostream.close() # Close the output file


def makeArgumentParser():
    """Set and parse the arguments"""
    Arguments = argparse.ArgumentParser( # Start the argument parser
        add_help=True, # Add a help interface
        usage='%(prog)s [infile]', # Usage information
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''\
Input a text file in the following format:
    Citation for article
    URL to article
    Meeting date
    Meeting leader
    ''' # Description on how to format the input file
    )
    Arguments.add_argument( # Add an argument
        'infile', # Called infile
        # dest='infile', # Goes to 'infile'
        type=str, # It's a string
        default=None, # No default
        metavar='INFILE',
        help="Name of input file" # Help message
    )
    return(Arguments)


def readInputFile(infile):
    """Read the input file and collect citation, url, meeting leader, and meeting date"""
    try:
        inString = open(infile).read() # Read the input file as a string
    except FileNotFoundError:
        raise
    inputVals = inString.split('\n') # Split into a list
    return(inputVals[0], inputVals[1], inputVals[2], inputVals[3]) # Return the four lines from the input file as separate strings


def main():
    """Read in a text file and create a lab meeting web page for 'MorrellLab.github.io'"""
    parser = makeArgumentParser() # Create our argument parser
    if not sys.argv[1:]: # If we don't have enough arguments
        sys.exit(parser.print_help()) # Exit with our help message
    if not 'MorrellLab.github.io' in os.getcwd() and '_meetings' in os.listdir('.'): # If we don't have the correct directory structure...
        sys.exit("Please be in the 'MorrellLab.github.io' directory and ensure the '_meetings' directory is present") # Exit with error
    else: # Otherwise
        outdirectory = os.getcwd() + '/_meetings/' # Create an output directory name
    args = vars(parser.parse_args()) # Parse the arguments and create dictionary out of them # Parse the arguments and create a dictionary out of them
    try:
        citation, url, date, leader = readInputFile(args['infile']) # Read in the input file and collect the citation, url, date, and leader
    except FileNotFoundError as e:
        sys.exit("Failed to find file: " + e.filename)
    page = LabMeetingPage(citation, url, leader, date) # Create a lab meeting page
    page.assembleMarkdownFile(outdirectory) # Write the lab meeting page


main() # Run  program
