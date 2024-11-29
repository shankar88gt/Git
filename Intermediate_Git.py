"""
Intermediate Git
    Branches
    Remotes
    Conflicts

You shd know
    How git stores data
    create repos
    make commits
    compare version
    revert versions


Branches
    individual version of a repo
    raches to systematically track multiple versions of the files

    In each branch
        some files might be the same
        other might be different
        some may not exist at all

    Why use branch?
        Live system
            Works as expected
            default branch = Main
        Feature development
            branch from main
            mutiple copies from main for multiple developers - simultaneously work
        compare the state of a repo between branches
        combine contents, pushing a new feature to the live system
        Each branch shd have a specific purpose

    git branch
        listing all branches
    git switch main
        switch to main
    git branch speed-test
        create a new branch called speed-test
        move to speed-test
        git switch speed-test

        combine both the cmds
            git switch -c speed-test

        new branch = "branching off"

    git diff main summary-statistics
        diff between two branches
        if the diff is large - produces large outputs
    
    Navigating large git outputs
        press space and q to quit
    
    rename a existing branch
        git branch -m feature_dev chatbot - #( old new )
        confirm using git branch

    delete a branch
        git branch -d chatbot
        produces an error if not merged
        delete branch -D chatbot ( 100% confident although recovery is possble )

    Merging Branches
        The purpose of branches
            each branch shd have a particular purpose
                developing a new feature
                debugging an error
            once the task is complete, we incorporate changes into production
            main = ground truth
            When merging 
                Source = merge from ( llm )
                destination = merge into ( main )
            
            to Merge
                move to destination 
                    git switch main
                git merge llm
                    merge llm to main
            from another branch
                git merge llm main ( source destination)

        Linear commit history : branched off main to create llm
        Fast forward : point main to the last commit int he llm branch

    Merge Conflicts
        inability to resolve differences int he contents of one of more files between branches
        e.g edit the same file in two branches

        make edits to resolve conflicts in each file
            nano Readme.md
            <<<<<< new branch  to  =========   - contents int he new branch
            ==========  to >>>>>>>>> Head -  contetns extra in Main branch
            rest in both branches

            Save ctrl + O enter
            exit ctrl + X

            then git add  followed by commit

    Remote repos - remotes
        local repos
        Remote repo - back up & colloboration

        Cloning - copy 
            git clone path-toproject-repo 
            git clone /home/shshd/repo new repo -  cloning a local repo ( local to local )

            copy remotes
                git clone URL 
                    git remembers where the original was
                    git stores a remote tag in the new repo's configuration
                    list all remotes - git remote / git remote -v ( verbose )

            Ctreating a remote 
                git remote add name URL

            Git Fetch origin
                fetch all remote branches
                might create new local branches if they existed in the remote
                Doesnt merge the remote contents into local repo

                fetch a remote branch
                    git fetch origin main
                
            Sunchronization Content
                git merge origin - merge origin remote default branch into the local repo;s current branch

            Git Pull - Fetch & merge from remote's default into the local repo's current branch
                git pull origin - defaults to main
                git pull origin dev - from branch dev

            Git push
                save changes locally first
                push into remote from local_branch
                    git push remote local_branch

            
            Summary
                Branches
                    see all branches - git branch
                    switch - git switch hotfix / git switch -c hotfix
                    compare - git diff main hotfix
                    rename - git branch -m hotfix 
                    Delete - git branch -d/-D hotfix

                Merging
                    from main, to merge llm into main
                        git merge llm
                    from another branch 
                        git merge llm main

                Working with Remotes
                    copy - git clone URL
                    info - git remote -v
                    Add new remote - add remote george URL

                Sync
                    git fetch origin
                    git pull origin
                    git push origin llm








            



         









        





"""