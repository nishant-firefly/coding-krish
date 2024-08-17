# Krish Coding## Getting Started

This guide will help you clone the repository, create a new branch, make changes, and push your code to your own branch named `coding_level_1`.

### Prerequisites

#### Make sure you have Git installed on your system. You can check this by running:

```bash
git --version
```

#### Add Ssh key :

```

To securely connect to GitHub, you can use SSH keys:

ssh-keygen -t rsa -b 4096 -C "<you_email>"

copy cat ~/.ssh/id_rsa.pub

Go to GitHub, navigate to Settings > SSH and GPG keys, and click New SSH key.
Paste your key and save.

```
#### Clone you repository :

```
git clone git@github.com:nishant-firefly/coding-krish.git

cd coding-krish

git status

git branch

```
#### Create new branch and push/pull changes:

```
git checkout -b coding_level_1
git branch

--> Do you coding in the files in Visual Studio Code <---
git add .
git commit -m "Add feature or fix description"
git push origin coding_level_1

```
