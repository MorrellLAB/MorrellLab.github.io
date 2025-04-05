#!/usr/bin/env python3

# Usage: python3 UpdateCitations.py
#   You must be in MorrellLab.github.io to run this (not a subdirectory)
#   You must have the following repository cloned into MorrellLab.github.io and renamed to "scholar"
#       https://github.com/ckreibich/scholar.py.git
#   Each publication to be updated must have a citation_url and a cluster (part of the url)

import sys
if not sys.version_info.major == 3 and not sys.version_info >= 3:
    sys.exit("Please use Python 3.3 or higher for this script")

import os
import time
try:
    import yaml
    import scholar.scholar as s
except ImportError as error:
    sys.exit("FAIL: Can't find " + error.name)

#   A function to use scholar.py to send a query and get information about citations
def send_query(cluster):
    """Send a query to Google Scholar and get number of citations and citation url"""
    try:
        assert isinstance(cluster, int)
    except AssertionError:
        raise
    querier = s.ScholarQuerier()
    settings = s.ScholarSettings()
    settings.set_citation_format(settings.CITFORM_NONE)
    querier.apply_settings(settings)
    query = s.ClusterScholarQuery(cluster)
    querier.send_query(query)
    ncites = querier.articles[0].attrs['num_citations'][0]
    curl = querier.articles[0].attrs['url_citations'][0]
    return(ncites, curl)


#   A function to parse our yaml/markdown documents using yaml.load_all
def parse_yaml(document):
    """Read a yaml document and return a dictionary with the name of the yaml document and dictionary of contents"""
    try:
        assert isinstance(document, str)
        this_yaml = (document, yaml.load_all(open('_publications/' + document, 'r'), Loader=yaml.SafeLoader).__next__())
        return this_yaml
    except AssertionError:
        raise
    except FileNotFoundError as error:
        sys.exit("Failed to find " + error.filename)


#   A function to write our yaml/markdown documents
def write_yaml(name, yaml_dict):
    """Write a yaml document to file"""
    try:
        assert isinstance(name, str)
        assert isinstance(yaml_dict, dict)
    except AssertionError:
        raise
    no_quotes = ('layout', 'paper_year', 'cluster')
    with open('_publications/' + name, 'w') as y:
        y.write('---')
        y.write('\n')
        for key, value in yaml_dict.items():
            if key in no_quotes:
                y.write(str(key) + ': ' + str(value))
            else:
                y.write(str(key) + ': "' + str(value) + '"')
            y.write('\n')
        y.write('---')


def main():
    #   Make sure we're in the right directory, exit if not
    if '_publications' not in os.listdir() or 'MorrellLab.github.io' not in os.getcwd():
        sys.exit("Can't find '_publications' directory. Please make sure you're in 'MorrellLab.github.io'")
    #   Get a list of publications
    print("Finding all publications", file=sys.stderr)
    publication_list = os.listdir('_publications')
    #   Read in publications
    print("Reading in the publications", file=sys.stderr)
    yaml_list = map(parse_yaml, publication_list)
    #   For every document in our list of yaml dictionaries
    for doc in yaml_list:
        #   given the yaml name and yaml dictionary
        (name, yaml_dict) = doc # TUPLE UNPACKING :O
        if 'cluster' in yaml_dict.keys(): # If we have a cluster ID
            print("Updating citations in", name, sep=" ", file=sys.stderr)
            ncites, curl = send_query(int(yaml_dict['cluster'])) # Get the number of citations and url
            yaml_dict['num_citations'] = ncites # Add ncites to our yaml dictionary
            yaml_dict['citation_url'] = curl # Add curl to our yaml dictionary
            write_yaml(name, yaml_dict) # Write it out
            print("Sleeping for 30 seconds", file=sys.stderr)
            time.sleep(30)


main()
