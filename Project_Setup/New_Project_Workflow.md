# New Project Workflow

## Step 1

Create project folder.

Example:

mkdir project_name

or

project_name/

## Step 2

Initialize Git.

Command:

git init

## Step 3

Create README.md. (touch README.md)

Document project purpose.

## Step 4

Create GitHub repository.

Use the same project name whenever possible.

## Step 5

Connect local repository to GitHub.

git remote add origin <repository-url>

## Step 6

Create first commit.

git add .
git commit -m "Initial commit"

## Step 7

Push project.

git push -u origin main

## Step 8

Create virtual environment.

python -m venv venv

## Step 9

Activate virtual environment.

source venv/bin/activate

or

venv\Scripts\activate

## Step 10

Install required packages.

pip install package_name

Example:

pip install pandas

pip install pytest

etc


## Step 11

Create requirements file.

pip freeze > requirements.txt

## Step 12

Create tests.

Use pytest.

## Step 13

Configure GitHub Actions.

Automate testing after each push.