"This Documents covers Git Basics"

"""
    Directory = Folder

PWD - Present working directory
ls - list 
cd 

git --version
git repo - directory ( files & directory )
Git storage - .git - Git stores all of its extra information in a directory called dot-git, 
        located in the repo's main directory. Git expects this information to be laid out in a particular way, so we should not edit or delete dot-git.

git init name - creating a new repo
git status

Converting a project into a repo
    from that repo run git init without a name
    * Dont create nested repo's

Git Workflow
    3 core steps
        edit & save files on local
        add the files to the staging area - keeps track of what has been modified
        commit the files

git add readme.md 
git add .  - all files
git commit -m "msg"
    -m  allows a log message without opening a text editor

Version history
    git commit structure - 3 parts
        commit
            contains the metadata - author log & commit time
        Tree
            tracks the location & names of files & directories
        blob
            binary large object 
            may contain data of any kind
            lobs contain a compressed snapshot of the file's contents when the commit happened

    git hash
        we mentioned a unique identifier called a hash, This is a 40-character string of numbers and letters like this
    
    git log
        commit information using the git log command, displaying all commits made to the repo in reverse chronological order
        space & q

        git log -3  ( 3 comits recent )
        git log report.md 
        git log --since="month day year"
        git log --since="" --until=""
            natural language ( 2 weeks ago ) & date format is also allowed
        git show hash value( may be first 8-10 of hasj value )
        git log -2

    Comparing Versions
        git diff - we compare the last committed version of our report with a modified version that is not in the staging area
        git diff --staged report.md ( compare last commited t staging area file )
        git diff --staged ( without the file name ) - Comparing multiple staged files
        comparing 2 commits
            git log -  for hashes
            git diff hash1 hash 1
            git diff HEAD~1 HEAD
                HEAD - recent commit
                HEAD~1 - previous commit

    Restoring & Reverting files
        Restoring a repo to a state prior to previous commit
        git revert / git revert --no-edit HEAD
            reinstates previous version & makes a commit
            Restores all files updated in the given commit
            provide a reference HEAD, hash etc
            Works on commits
        
            revert without commiting ( bring files into the staging area )
                git revert -n HEAD
            
        Revert a single file
            git checkout
            e.g. git checkout HEAD~1 -- report.md ( will be in the staging area use git status to check )
                 git commit -m "" for commit

        Unstaging a file
            git restore --staged filename ( back to the working area )

What Next
    Branches
    remote repos
    Rebasing
    bisecting
    submodules        
"""
