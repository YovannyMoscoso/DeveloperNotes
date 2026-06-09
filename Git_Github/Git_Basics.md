# Git Workflow for New Projects (IS 601)

## 1. Verify Git Installation

### What does it do?

Checks whether Git is installed and shows the installed version.

### Why?

Without Git installed, none of the Git commands will work.

```bash
git --version
```

---

## 2. Verify Git Configuration

### What does it do?

Shows the username and email associated with your commits.

### Why?

Every commit is linked to a user identity.

Check username:

```bash
git config --global user.name
```

Check email:

```bash
git config --global user.email
```

View all Git settings:

```bash
git config --global --list
```

If username or email are not configured:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Verify:

```bash
git config --global --list
```

---

## 3. Create a Project Folder

### What does it do?

Creates a directory for the new project.

### Why?

Keeps project files organized.

```bash
mkdir ProjectName
cd ProjectName
```

Example:

```bash
mkdir A03_Interactive_Calculator
cd A03_Interactive_Calculator
```

---

## 4. Initialize a Git Repository

### What does it do?

Turns a regular folder into a Git repository.

### Why?

Allows Git to track changes.

```bash
git init
```

Verify:

```bash
git status
```

---

## 5. Rename the Default Branch to Main

### What does it do?

Changes the default branch name from master to main.

### Why?

GitHub uses main as the standard branch.

Check current branch:

```bash
git branch
```

Rename:

```bash
git branch -M main
```

Verify:

```bash
git branch
```

---

## 6. Create Basic Project Files

### What does it do?

Creates the standard files used in most Python projects.

```bash
touch README.md
touch .gitignore
touch requirements.txt
```

---

## 7. Create a Virtual Environment

### What does it do?

Creates an isolated Python environment for the project.

### Why?

Prevents package conflicts between projects.

Create environment:

```bash
python -m venv venv
```

Activate in Linux / WSL:

```bash
source venv/bin/activate
```

Activate in PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Verify Python location:

```bash
which python
```

Verify Pip location:

```bash
which pip
```

---

## 8. Install Required Packages

### What does it do?

Installs project dependencies.

Example:

```bash
pip install pytest pytest-cov
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

## 9. Configure .gitignore

### What does it do?

Tells Git which files should not be tracked.

### Why?

Avoids committing temporary or unnecessary files.

Example:

```text
venv/
__pycache__/
.pytest_cache/
.coverage
htmlcov/
.env
```

---

## 10. Check Repository Status

### What does it do?

Shows modified, new, staged, and untracked files.

### Why?

This is one of the most frequently used Git commands.

```bash
git status
```

---

## 11. Add Files to the Staging Area

### What does it do?

Marks files to be included in the next commit.

### Why?

Git does not automatically include every file change.

Add all files:

```bash
git add .
```

Add a specific file:

```bash
git add README.md
```

Verify staged files:

```bash
git status
```

---

## 12. Create a Commit

### What does it do?

Creates a snapshot of the project.

### Why?

Allows you to track project history and restore previous versions.

```bash
git commit -m "Initial project structure"
```

---

## 13. View Commit History

### What does it do?

Displays all commits in the repository.

Detailed history:

```bash
git log
```

Short history:

```bash
git log --oneline
```

Graph view:

```bash
git log --oneline --graph --all
```

---

# Branch Management

## View Existing Branches

### What does it do?

Shows all branches in the repository.

```bash
git branch
```

---

## Create a New Branch

### What does it do?

Creates a separate line of development.

```bash
git branch add-tests
```

---

## Switch to an Existing Branch

### What does it do?

Moves you to another branch.

```bash
git switch add-tests
```

---

## Create and Switch to a New Branch

### What does it do?

Creates a branch and immediately switches to it.

```bash
git switch -c add-tests
```

---

## Verify Current Branch

### What does it do?

Shows which branch you are currently using.

```bash
git branch
```

Example:

```text
* add-tests
  main
```

---

## Merge a Branch into Main

### What does it do?

Combines changes from another branch into main.

Switch to main:

```bash
git switch main
```

Merge:

```bash
git merge add-tests
```

---

## Delete a Branch

### What does it do?

Removes a branch that is no longer needed.

```bash
git branch -d add-tests
```

---

# GitHub Integration

## Check Existing Remote Repositories

### What does it do?

Shows the remote repositories connected to your local repository.

```bash
git remote -v
```

---

## Connect Local Repository to GitHub

### What does it do?

Adds a GitHub repository as the remote destination.

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Example:

```bash
git remote add origin https://github.com/yovannymoscoso/A03_Interactive_Calculator.git
```

---

## Verify Remote Connection

```bash
git remote -v
```

---

## First Push to GitHub

### What does it do?

Uploads your local repository and establishes tracking.

```bash
git push -u origin main
```

---

## Future Pushes

### What does it do?

Uploads new commits to GitHub.

```bash
git push
```

---

## Pull Changes from GitHub

### What does it do?

Downloads and merges changes from GitHub.

```bash
git pull
```

---

# Useful Commands

## Show Changes Not Yet Staged

```bash
git diff
```

---

## Show Staged Changes

```bash
git diff --staged
```

---

## Show Remote Details

```bash
git remote show origin
```

---

## Unstage a File

### What does it do?

Removes a file from the staging area without deleting it.

```bash
git restore --staged filename
```

---

## Restore a File to the Last Commit

### What does it do?

Discards local changes.

```bash
git restore filename
```

---

# Typical Git Workflow

```text
Create Project Folder
        ↓
git init
        ↓
git branch -M main
        ↓
Create Files
        ↓
git status
        ↓
git add .
        ↓
git commit -m "message"
        ↓
git remote add origin <repository-url>
        ↓
git push -u origin main
```

# Typical Branch Workflow

```text
main
  ↓
git switch -c new-feature
  ↓
Make Changes
  ↓
git add .
  ↓
git commit -m "message"
  ↓
git switch main
  ↓
git merge new-feature
  ↓
git push
```
