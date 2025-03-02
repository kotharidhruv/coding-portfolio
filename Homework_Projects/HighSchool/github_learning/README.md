# Git Branching

In Git, branching is a new or separate version of the main repository that people use for development or enhancement of their code for a given project. Branches allow multiple people to work on different parts of the project without impacting the main branch. When the work is complete, a branch can be merged into the main project. You can switch between branches and work on different projects without interfering with each other.

Below is an example of Git branching:

You have a main repository called `python_programs`. Since we are working in our local repository and do not want to disturb the main project, we will create a new branch:

```bash
git branch python_programs_wordcnt
```

This will create a new branch called python_programs_wordcnt.

You can confirm that the new branch was created by:

```bash
git branch
```

You should see your newly created branch.

Now we can move to the new branch and write or edit the program:

```bash
git checkout python_programs_wordcnt
```

You can also switch to the new branch directly while creating a new branch by using the -b option like below:

```bash
git checkout -b python_programs_wordcnt
```

Now you can open any editor and write/modify the code. For this example, we are modifying a word count program to display the count:

``` python
#wordcount.py
def word_count(string):
    words_split = "Geeksforgeeks is best Computer Science Portal".split()
    ws_len = len(words_split)
    print("Length of words you entered is: ", ws_len)

test_string = "This is almost end of summer"
word_count(test_string)
```

We have made changes to the above file and want to merge them into the main branch.

We can check the status of the current branch:

```bash
git status
```

It will show something like this:

```bash
On branch python_programs_wordcnt
Changes not staged for commit:
  (use "git add ..." to update what will be committed)
  (use "git restore ..." to discard changes in working directory)
        modified:   wordcount.py

Untracked files:
  (use "git add ..." to include in what will be committed)
        wordcount.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Now we have to stage the file for commit. We can add the file to the staging environment for this branch by:

```bash
git add --all
```

Using --all will stage all changed (new, modified, and deleted) files instead of individual files.

You can check the status of the branch:

```bash
git status
```

You should see something like this:

```bash
On branch python_programs_wordcnt
Changes to be committed:
  (use "git restore --staged ..." to unstage)
    modified: wordcount.py
```

If the changes look good, we can commit them to the branch:

```bash
git commit -m "added print statement"
```

Now we have a new branch that is different from the main branch.

You can switch between the branches or work on different branches at the same time and follow above steps. Once you have branch ready with the required change you can follow below steps to merge the new branch to the main branch

```bash
git checkout master
Switched to branch ‘master’
```
This will switch to the master branch. Now we can merge the current branch(master) with python_programs_wordcnt 

```bash
git merge python_programs_wordcnt 
Updating 09e3bed..dga27ab
Fast-forward
 wordcount.py | 1 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Since there were no other changes made to master while we were working so git sees this as a continuation of master. So it can “Fast-forward”, just by posting both master and emergency-fix to the same commit.

As master and python_programs_wordcnt are essentially same now, we can delete python_programs_wordcnt as it is no longer needed.

```bash
git branch -d python_programs_wordcnt
Deleted branch python_programs_wordcnt (was dga27ab)
```

# Git Operations

git init - Creates an empty Git repository. After the command is used, a .git directory is created with sub directors and template files. Once repository is initialized, the process of creating other files begins
```bash
git init
```

git status - It tells the current state of the repository and lists all the modified files that are ready to be added to the local repository. It shows the current working branch and the files that are not committed. If there are no changes, it will show the message no changes to commit, working directory clean.
```bash
git status
```

git add - After checking status of the files, git add command is used to add those files to the staging area. Before running commit command, “git add” command must be used to add any new or modified files.
```bash
git add <FileName>
git add .
```

git commit - This command makes sure all the changes are saved to the local repository. You can use git commit -m “<message>” to describe about changes that were made

git branch - is used to determine what brand the local repository is on. With this command we can add, delete and list local branches

```bash
git branch <BranchName>
git branch -a
git branch -d <BranchName>
```

git checkout - is used to switch between branches and is useful when you want to work on different branch. This command works on files, commits and branches
```bash
#Checkout an existing branch
git checkout <BranchName>

# Checkout and create a new branch
git checkout -b <NewBranchName>
```

git merge - is used to integrate branches together. This command combines changes from one branch to another branch. It is used to merged changes in the staging branch to the main branch.
```bash
git merge<BranchName>
```

git clone - is used to create a local working copy of an existing remote repository. This command downloads the remote repository to the computer.
```bash
git clone <RemoteUrl>
```

git pull - is used to fetch and merge changes from the remote repository to the local repository. If you want to copy all files from the master branch of the remote repository to the local repository by following command
```bash
git pull origin master 
```

git push - is used to transfer the commits or pushing the content from the local repository to the remote repository. Once the local repository has been changes with the required changes, this command is used to push local changes to the main branch.
```bash
git push -u origin master
```

git stash -  takes your modified tracked files and saves it on a pile of incomplete changes that you can reapply at any time. You can use stash pop to go back and work on it. This command helps a developer to switch branches to work on something else without committing to incomplete work.
```bash
git stash -u
```
git log - shows the order of the commit history of a repository. It helps in understanding the state of the current branch by showing the commits that lead to this state.
```bash
git log
```



