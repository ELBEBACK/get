# How to get a branch from a server #
    1. Use *git fetch* to have up-to-date data
    2. Use *git checkout _branchname_* on the branch you want to get to get that branch locally
# How to merge branches #
    1. Get into 'target' branch, into which you are planning to merge another branch
    2. Use *git merge _branchname_* with a name of a branch that you are planning to merge into some other branch
    3. Push your changes
# What to do after the merge? #
    1. You can check the history of your repo with *git log*, check status
    2. Be aware of possible files replacement or similar undefined behaviour in initial branch with those merged from another branch, if those file has no 'common ancestors'