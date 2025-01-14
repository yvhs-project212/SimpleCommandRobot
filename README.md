# Project 212 Simple Command Robot TEMPLATE

This repo provides sample code using the [Command Robot](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html) framework.  This branch, called `template`, provides an empty robot template that does nothing.

To use this repo as a template for a new robot:

* First, create a repo on GitHub -- either in your personal GitHub collection,
  or possibly in the Project 212 collection of repos.  Open a web browser,
  go to your GitHub home page (`https://github.com/***YourUserName***`), click
  on the "Repositories" tab, then click the green "New" button.  Give your new
  repo a name, make it public, and leave it empty.  (No README, no .gitignore,
  no license.)
* Open a Git Bash shell, and change into your `repos` directory.
* Clone the SimpleCommandRobot repo, choosing a new name for your new
  robot directory (maybe the same as your new repo name!):
  <pre><code>git clone https://github.com/yvhs-project212/SimpleCommandRobot <b><i>my-new-directory</i></b></code></pre>
* Change into your new directory.
* Switch to the `template` branch:
  ```
  git checkout template
  ```
* Now we're going to do something tricky and dangerous: nuke everything that
  Git is storing for us!  We'll lose all the version history, all the branches,
  and everything else except the current version of the files!  But in this
  case, that's exactly what we want.  From your Git Bash shell, run this:
  ```
  rm -rf .git
  ```
* And to be even trickier, we're now going to convince Git that this is
  a clone of the new repository that you just created on GitHub!  Here's how
  we're going to do that:
  * Change back into your `repos` directory.  (You might be able to use
    `cd ..` if you want.)
  * Clone _your_ GitHub repo into a new directory called "temp":
    <pre><code>git clone https://github.com/<b><i>YourUserName</i></b>/<b><i>YourRepo</i></b> temp</code></pre>
  * This "temp" directory has all the Git information needed to convince Git
    that it's pointed at your new GitHub repo.  We're going to take that
    secret Git information and _move it to the other directory_, where we
    just nuked that directory's Git information!  Using the name you chose
    for your new project directory, run this:
    <pre><code>mv temp/.git <b><i>my-new-directory</i></b>
    rm -rf temp</code></pre>
* Now your new directory is a Git "remote" of your GitHub repo... which is
  new and empty.  we're going to pretend that we just wrote all this code on
  our own, and we want to add it to our Git repository.  The first thing we
  need to do is to check in the template code!  That way, when we look at
  what's changed, we only see our changes.  First, change back into your
  project directory, and then use `git add` to add everything in the
  now-current directory:
  <pre><code>cd <b><i>my-new-directory</i></b>
  git add .</code></pre>
* Next, commit these changes with a useful commit message:
  ```
  git commit -m "Start new project with SimpleCommandRobot template code"
  ```
* Finally, push that to GitHub!
  ```
  git push origin main
  ```