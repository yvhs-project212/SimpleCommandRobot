# Project 212 Simple Command Robot TEMPLATE

This repo provides sample code using the [Command Robot](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html) framework.  This branch, called `template`, provides an empty robot template that does nothing.

To use this repo as a template for a new robot:

* First, create a repo on GitHub -- either in your personal GitHub collection,
  or possibly in the Project 212 collection of repos.  Open a web browser,
  go to your GitHub home page (<code>https://github.com/<b><i>YourUserName</i></b></code>),
  click on the "Repositories" tab, then click the green "New" button.  Give
  your new repo a name, make it public, and leave it empty.  (No README, no
  .gitignore, no license.)
* Open a **Git Bash** shell, and change into your `repos` directory.
* If you don't already have a copy of the SimpleCommandRobot repo, clone it:
  ```
  git clone https://github.com/yvhs-project212/SimpleCommandRobot
  ```
  If you do already have a copy, make sure it's current by pulling from GitHub:
  ```
  cd SimpleCommandRobot
  git pull
  ```
* Run the `new-project.sh` script:
  <pre><code>./new-project.sh https://github.com/<b><i>YourUserName</b></i>/<b><i>YourNewProjectName</b></i></code></pre>
  This will create a new folder on your machine with the same name as the
  GitHub repo.  If you want the folder to have a different name, you can give
  the script an extra parameter:
  <pre><code>./new-project.sh https://github.com/<b><i>YourUserName</b></i>/<b><i>YourNewProjectName  AlternateDirectoryName</b></i></code></pre>
* Your new project should be ready for you to start editing it!
