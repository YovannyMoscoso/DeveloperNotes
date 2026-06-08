# Virtual Environment

## What is it?

An isolated Python environment for a specific project.

## Why use it?

Avoid dependency conflicts between projects.

## Create Environment

python -m venv venv

## Activate Environment

Windows:

venv\Scripts\activate

Linux:

source venv/bin/activate

## Deactivate Environment

deactivate

## Common Structure

project/
│
├── venv/
├── app.py
└── requirements.txt