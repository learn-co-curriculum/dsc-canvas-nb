import requests
import os
from dotenv import load_dotenv
load_dotenv()

import markdown2
import re 

from canvasapi import Canvas


def extract_github_details(repo_link:str)->(str, str):
    "Helper function to quickly retrieve username and repository from repo link."
    repo_link = repo_link.replace("https://github.com/", "")
    github_repo = re.sub("/.*$", "", repo_link)
    print(f"repo: {github_repo}")

    github_username = re.sub(".*/", "", repo_link)
    print(f"user: {github_username}")
    return github_repo, github_username


def get_github_readme(github_username:str, github_repo:str)->(str):
    """Constructs URL for the raw README of the GitHub repo supplied 
    in the `github_repo` arg. Then, submits `requests.get` to retrieve
    the text. Outputs the response text, convers from markdown to HTML.
    
    Input
    ---------------
    github_username (str): GitHub username for repo
    github_repo (str): Name of GitHub repo to retrieve
    
    Output
    ---------------
    html_content (str): Contents of README.md, converted to HMTL
    """
    # get the content of the GitHub README file
    github_readme_url = f"https://raw.githubusercontent.com/{github_username}/{github_repo}/master/README.md"
    github_readme_response = requests.get(github_readme_url)
    github_readme_content = github_readme_response.text

    # convert the GitHub README file content to HTML
    html_content = markdown2.markdown(github_readme_content)
    return html_content


