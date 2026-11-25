# Getting Started with Git and GitHub

- **Course URL:** https://www.coursera.org/learn/getting-started-with-git-and-github
- **Crawled at:** 2026-11-24T15:49:17.451289
- **Extracted:** 19/19 items (13 videos, 6 readings) | 60,982 chars

---

## Module 1: Git and GitHub Fundamentals

### 1. [VIDEO TRANSCRIPT] Course Introduction Video • 3 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/HPf1W/course-introduction
- **Method:** `dom_transcript` | **Length:** 2974 chars

Welcome to this introductory course on Git and GitHub. Git and GitHub are widely used in the industry for version control and collaborative software development. Version control and collaboration software are crucial for completing software development projects effectively. Employers expect skills in Git and GitHub for software development careers. This course suits anyone who wants to learn version control and collaboration with Git and GitHub. No prior background knowledge is required, just basic computer and IT literacy. This course is particularly suitable for those interested in roles such as software engineers, application developers, data scientists, and data engineers.

We're excited that you're here. Your instructors for this course are Rav Ahuja and Upkar Lidder. Rav Ahuja is a global program director at IBM and leads growth strategy, curriculum creation, and partner programs for the IBM Skills Network. Upkar Lidder is a senior product manager with 15 plus years of experience in IT development, including team management and functional and technical leadership roles. When you complete this course, you will understand basic Git and GitHub concepts in the context of distributed version control. You will be able to create repositories, collaborate on team projects by sharing and integrating your changes, and even build a GitHub portfolio. Now, let's look at what you will learn from the four modules in this course.

The first module begins with the basics of Git and GitHub. It covers repositories and how to edit and push files in GitHub. This module will also introduce you to GitHub branches. As part of hands-on activities, you will create a GitHub account and a project repository. You will also create branches and merge a pull request on the web user interface. In module two, you will learn about Git workflow and Git commands. You'll also learn to use branches, fork, and clone public repositories, and collaborate using Git commands.

As part of hands-on activities, you will use cloning and forking in a GitHub project. In module three, you'll consolidate your learning with a two-part final project, one based on the GitHub User Interface, or UI, and the other on the Git Command Line Interface, or CLI. You'll apply your knowledge by creating a GitHub project, adding, committing, pushing files, sharing the project publicly. Additionally, you'll explore an optional topic on GitHub Copilot. In the final module, you'll explore optional topics on using GitHub from your Windows desktop. You will learn to install Git Bash, generate an SSH key, and add it to GitHub. To get the most from your course, watch all videos, complete the hands-on activities to practice your new skills, attempt all quizzes, complete the final project, and create your shareable portfolio.

Remember to use the discussion forum to connect and collaborate with your peers or seek assistance from the course staff. Let's get started on this exciting journey!

---

### 2. [VIDEO TRANSCRIPT] Overview of Git and GitHub Video • 3 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/Q2qCC/overview-of-git-and-github
- **Method:** `dom_transcript` | **Length:** 3557 chars

[MUSIC] Welcome to overview of Git and GitHub. In this video, you will learn what Git and GitHub are, along with some basic terms related to Git and GitHub. You will also grasp the concept of the version control system and how it is related to Git and GitHub. Git and GitHub are popular environments among developers and data scientists, but you can't discuss them without a basic understanding of version control. A version control system lets you track your changes to the source code. This makes it easy for you to recover older versions of your document if you make a mistake. Along with this, it makes collaboration with other team members much easier.

Here's an example to illustrate how version controls work. Let's say you have a shopping list and want your roommates to confirm the things you need and add additional items. Without version control, you've got a big mess to clean up before you can go shopping. With version control, you know exactly what you need after everyone has contributed their ideas. Git is free and open-source software distributed under the General Public License (GNU). Git is a distributed version control system (DVCS), meaning users anywhere in the world can have a copy of your project on their computer. When they've made changes, they can sync their version to a remote server to share it with you.

Git isn't the only version control system out there, but the distributed aspect is one of the main reasons it has become one of the most popular version control systems available. Version control systems are widely used for things involving code, but you can also version control images, documents, and any number of file types. Note that Git also supports branching strategies, such as feature branching, to organize and manage development. You can use Git without a web interface using your command line interface, but GitHub is one of the most popular web-hosted services for Git repositories. Others include GitLab, Bitbucket, and beanstalk. There are a few basic terms that you will need to know before you get started. The secure shell (SSH) protocol is a method for secure remote login from one computer to another.

A repository contains your project folders that are set up for version control. A fork is a copy of a repository. A pull request is how you request that someone review and approve your changes before they become final. A working directory contains the files and subdirectories on your computer that are associated with a Git repository. Commit is a snapshot of the project's current state at a specific point in time, along with a description of the changes made. A branch is a separate line of development that allows you to work on features or fixes independently. Merging combines changes from one branch into another, typically merging a feature branch into the main branch.

Cloning creates a local copy of a remote Git repository on your computer. Let's recap. In this video, you learned that: Git is a versatile version control system used for tracking changes in code, and collaborating with others on software projects. Due to a distributed version control system, Git enables you to revert to the previous state, or review the history of the project. Git supports branching strategies such, as feature branching, to organize and manage development. GitHub is one of the most popular web-hosted services for Git repositories. Basic terms associated with Git and GitHub are: SSH protocol, repository, fork, pull request, working directory, commit, branch, merge, and clone.

[MUSIC]

---

### 3. [VIDEO TRANSCRIPT] Introduction to GitHub Video • 4 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/Vtjgd/introduction-to-github
- **Method:** `dom_transcript` | **Length:** 3981 chars

(Music) Welcome to Introduction to GitHub After watching this video, you will be able to: Describe the purpose of source repositories and explain how GitHub satisfies the needs of a source repository. Linux development in the early 2000’s was managed under a free-to-use system known as BitKeeper. In 2005, BitKeeper changed to a for-fee system which was problematic for Linux developers for many reasons. Linus Torvalds led a team to develop a replacement source-version control system. The project ran in a short a timeframe and the key characteristics were defined by a small group. These include: Strong support for non-linear development. (Linux patches were then arriving at a rate of 6.7 patches per second) Distributed development.

Each developer can have a local copy of the full development history. Compatibility with existing systems and protocols. This was necessary to acknowledge the diversity of the Linux community. Efficient handling of large projects. Cryptographic authentication of history. This makes certain that distributed systems all have identical code updates. Pluggable merge strategies.

Many pathways of development can lead to complex integration decisions that might require explicit integration strategies. What is special about the Git Repository model? Git is designed as a distributed version-control system. Primarily focused on tracking source code during development. Contains elements to coordinate among programmers, track changes, and support non-linear workflows. Created in 2005 by Linus Torvalds for distribution of Linux kernels. Git is a distributed version-control system that is used to track changes to content.

It serves as a central point for collaboration with a particular focus on agile development methodologies. In a central version control system, every developer needs to check out code from the central system and commit back into it. As Git is a distributed version control, each developer has a local copy of the full development history, and changes are copied from one such repository to another. Each developer can act as a hub. When Git is used correctly, there is a main branch that corresponds to the deployable code. Teams can continuously integrate changes that are ready to be released and can simultaneously work on separate branches in between releases. Git also allows centralized administration of tasks with access-level controls for each team.

Git can co-exist locally such as through the GitHub Desktop client or it can be used directly through a browser connected to the GitHub web interface. IBM Cloud is based on sound and established open-source tools including Git repositories, often called repos. GitHub is an online hosting service for Git repositories. GitHub hosted by a subsidiary of Microsoft. GitHub offers free, professional and enterprise accounts. As of August 2019, GitHub had over 100M repositories. A Repository is: A data structure for storing documents including application source code.

A repository can track and maintain version-control. GitLab is a complete DevOps platform, delivered as a single application. GitLab provides access to Git repositories, controlled by source code management. With GitLab, developers can: Collaborate, reviewing code, making comments and helping to improve each other’s code. Work from their own local copy of the code. Branch and merge code when required. Streamline testing and delivery with Built-in Continuous Integration (CI) and Continuous Delivery (CD).

In this video, you learned: GitHub is the online hosting service for Git repositories. Repositories store documents including application source code and enable contributors to track and maintain version-control. What is special about the Git Repository model? Git is designed as a distributed version-control system. Primarily focused on tracking source code during development. Contains elements to coordinate among programmers, track changes, and support non-linear workflows.

---

### 4. [VIDEO TRANSCRIPT] GitHub Repositories Video • 4 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/NPMOC/github-repositories
- **Method:** `dom_transcript` | **Length:** 3290 chars

(Music) Welcome to GitHub Repositories! After watching this video, you will be able to: Explain how to sign up for a GitHub account and describe how to create a repository. Signing up for a free, personal account on GitHub is quick and easy. Start at the GitHub site, https://github.com You’ll need to choose a username, enter your email address and select a password, then click Sign up for GitHub. Next, you’ll have a short test to prove that you’re a person. Click Verify and solve the puzzle presented. When you’re done, click join a free plan and then you’ll be taken to a screen where you can select the type of account – most likely a free, personal account is all that you’ll want.

Choose to set up a personal, free account, which is the default. GitHub asks some questions about your work, programming experience and interests. You can skip these if you want. Finally, you’ll have to respond to an email that you receive which proves that you linked to GitHub from an account that you access GitHub provides you with some starting points. You can choose to create a repository or an organization, or you can take the Introduction to GitHub course. Remember, a repository is a data structure for storing documents including application source code which tracks and maintains version-control. An organization is a collection of user accounts that owns repositories.

Organizations have one or more owners, who have administrative privileges for the organization. Or you can skip this for now and get straight to work. GitHub provides many resources to help you work effectively. When you have time, read the GitHub guide. The heart of a Git-based project is the repository. This contains all your code and the related artifacts, including things like: A README file to describe the purpose of the project. A license to express the ways in which people can use your code, Etc.

You can also make your repository private (only available to people with accounts that have permission to see it) or public (searchable and seen by everyone). When you create your repository, you’ll notice that it has a number of tabs, and is opened to the Code tab. Code – this is where all the source files reside. Git was initially created as a source code repository and now all sorts of files end up in here. If you created a README and/or license, that’s all that’s here right now. Issues – as you can imagine, you can track and plan with tools such as “Issues” that lists all open items against your project base. Pull Requests – this is part of the mechanism for collaborating with other users.

Pull requests define changes that are committed and ready for review before being merged into the main branch. Projects – all the tools for managing, sorting, planning, etc. your various projects. This is the core of the collaborative power of GitHub. Wiki, Security, and Insights – often left for more advanced users, these tools provide a communication base to the external user community. Settings – GitHub allows for a lot of personalization, including changing the name of your repository and controlling access. In this video, you learned: How to create and verify a GitHub account. Repositories are storage structures that can hold Code, track Issues, and enable you to collaborate with others.

---

### 5. [VIDEO TRANSCRIPT] GitHub - Getting Started Video • 3 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/fe489/github-getting-started
- **Method:** `dom_transcript` | **Length:** 2478 chars

In the previous video, you learned about Git and GitHub. Before you continue with this video, register for a GitHub account and log in. Let’s start by creating a new repository. Click + then click New Repository. To create a new repository, you need to provide these details: give your new repository a name; optionally, add a description of your repository; choose the repository visibility - whether you want it to be public or private; and choose the option to Initialize this repository with readme file. Then click Create Repository. You will now be redirected to the repository you have created. The root folder of your repository is listed by default and it has just one file ReadMe.md. Now, it’s time to edit the readme. You can do this in your browser. Just click the pencil to open the online editor and you can change the text of the readme. To save your changes to the repository, you must commit them. After you have made your changes, scroll down to the Commit changes section. Add a commit message and optionally add a description, then click Commit changes. The "commit changes" is used to save your changes to the repository. Go back to the home screen by clicking the repository name link. Note that the readme file is updated and verify your changes. Let’s learn how to create a new file using the built-in web editor provided by GitHub which runs in the browser. Click Add File, then click Create New File to create the new file. To create a python file called firstpython.py. First, provide the file name. Next, add a comment that describes your code, then add the code. Once finished, commit the change to the repository. You can see that your file is now added to the repository and the repository listing shows when the file was added or changed. When you need to change the file, you can edit it again. Click the file name, and then click the pencil icon, make your edits and commit the changes. You can also upload a file from your local system into the repository. From the home screen of the repository, click Add File and choose the Upload files option. Click Choose Your Files and select the files you want to upload from your local system. The file upload process may take a short time, depending on what you are uploading. Once the files finish uploading, click Commit Changes. The repository now reflects the files that were uploaded. In this video, you learned how to create a repository, edit files, and commit changes using the web interface.

---

### 6. [READING] Summary: Getting Started with Git and GitHub Reading • 2 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/supplement/IGsZk/summary-getting-started-with-git-and-github
- **Method:** `dom_reading_cml` | **Length:** 1075 chars

In this module, you learned that:

- Git is a versatile version control system used for tracking changes in code and collaborating with others on software projects.
- Due to a distributed version control system, Git enables you to revert to the previous state or review the project’s history.
- GitHub is one of the most popular web-hosted services for Git repositories.
- Repositories are storage structures that store documents, including application source code, and enable contributors to track and maintain version control.
- Git repository model
- Primarily focused on tracking source code during development.
- Contains elements to coordinate among programmers, track changes, and support non-linear workflows.
- Repositories are storage structures that hold code and track version history using Git; platforms like GitHub extend these repositories with additional features such as issue tracking and collaboration tools.
- GitHub enables you to create repositories, edit files using the web interface, commit the changes to the file, upload the files, and a lot more.

---

### 7. [VIDEO TRANSCRIPT] GitHub Branches Video • 4 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/Vfgp4/github-branches
- **Method:** `dom_transcript` | **Length:** 4225 chars

Welcome to GitHub branches. After watching this video, you will be able to explain the purpose of branches in GitHub and describe how to merge changes into branches. All files in GitHub are stored on a branch. The main branch is definitive, it stores the deployable version of your code. The main branch is created by default, however, you can use any branch as the main, finished, deployable version of the code. When you plan to change things, you create a new branch and give it a descriptive name. The new branch starts as an exact copy of the original branch.

As you make changes, the branch you created holds the changed code. To create a new branch, click the dropdown branch Main, add new branch name into a new branch text and select "Create Branch". GitHub branches can be very complex for large software projects. For a simple project such as the ones we are exploring, consider the following. Start with a common base, the initial source for this project. At one point, the code is branched while new features are developed. In this example, both branches are undergoing changes.

When the two streams of work are ready to merge, each branch's code is identified as a tip, and the two tips are merged into a third combined branch. Developers work on source files in a branch. Since some projects take a while, the source doesn't make sense right away. To change the contents of a file, select the file, click the pencil icon, make the changes, commit the changes. When the developer has completed their assigned work, to save their changes, they commit the code. Commit indicates that the developer is convinced that the code represents a stable platform for the feature or set of features being developed. When a developer commits a change source to their path, they are required to write a comment that describes the changes.

The comment should be meaningful and descriptive. The developer can choose to commit to the current branch or create a new branch. Finally, click "Commit changes". Some best practices while writing a comment: don't end the comment message with a period, keep commit messages under 50 characters. Use the extended window for the details. Always write in an active voice. Pull is used to initiate the merging of branches in a way to capture changes.

A pull request makes the proposed committed changes available for others to review and use. A pull can follow any commits even if the code is unfinished. A pull requires a user to approve the changes. This can be the author of the change or can be assigned within the team. Note that GitHub automatically makes a pull request on your behalf if you make a change on a branch that you do not own. Since the log files are immutable, it is always possible to find the person who approve the merge of the change. To open a pull request, click "Pull requests" and select "New pull request".

Select the new branch from the compare box. Scroll down to view the changes. Confirm that the changes are what you want to assess. Add a title and description to the request. Click "Create pull request." The intent of Git repository is for the main branch to be the only deployed code. Developers can change source files in a branch, but the changes are not released until they are committed.

A pull command is issued, the code is reviewed and approved. The approved code is merged back into the main code. To merge a committed code change into your main code, click "Merge pull request," click "Confirm merge". When all changes for a branch are complete, that branch is considered obsolete and should be deleted. In this video, you learned all files in GitHub exist on a branch. The main branch contains the finished deployable version of the code. Create new branches when you need to change the code.

The new branch starts as an exact copy of the original branch. As you make changes, the branch that you created holds the changed code. More than one branch can be undergoing changes at the same time. Saved changes are called commits. Pull requests enable other users to review and use the proposed changes committed. When you are ready to merge the changed code into the main branch, you merge the committed code changes into your main code.

---

### 8. [READING] Summary: Branches with GitHub Reading • 2 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/supplement/0Bjpw/summary-branches-with-github
- **Method:** `dom_reading_cml` | **Length:** 494 chars

In this module, you learned that:

- A branch is a snapshot of your repository to which you can make changes.
- In the child branch, you can build, make edits, test the changes, and then merge them with the main branch.
- To ensure that changes are made by one member, do not impede or affect the workflow of other members, multiple branches can be created and merged with the main branch.
- A pull request is a way to notify other team members of the changes and edits made to the main branch.

---

## Module 2: Git Commands and Managing GitHub Projects

### 1. [VIDEO TRANSCRIPT] Overview of Git Workflows Video • 6 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/ZL8gJ/overview-of-git-workflows
- **Method:** `dom_transcript` | **Length:** 6124 chars

[MUSIC] Welcome to the overview of Git workflows. After watching this video, you will be able to describe the steps in a Git workflow and explain the workflow in real life scenario. Imagine yourself joining a team developing features for an e-commerce platform. Your task is to add a product recommendation feature. The team uses git and GitHub for version control and collaboration. How will you collaborate effectively with the team using git and GitHub? A clear understanding of git workflows ensures you can use git effectively for version control and collaboration.

The knowledge will help you avoid issues such as code conflicts and unintentionally overriding a team member's work. The first step is cloning a repository that your team has hosted on GitHub. Cloning creates a copy of the project's code, and its complete version history from the remote repository on your local computer. The connection established during cloning enables you to push code changes to the remote repository. You can also pull any changes from the remote repository to your local repository and update it. You can implement the product recommendation feature by updating the project files in your local repository. As a developer, you might try multiple ways to code the feature.

You may not want the changes to affect the main branch until the code is ready. A good practice is to create a branch from the main branch, and then work on the newly created branch. A branch in git is an isolated development space based on the main branch where you can make changes. In this case, add a feature without interfering with the main code base. After developing the feature, the next step is to select the changed files and move them to a staging area. The staging area is a temporary storage space where you collect the selected files before asking git to save them in the local repository. You can now commit the files to the newly created branch.

Committing files allows you to record the changes and ensure your new feature becomes a part of the branch. When you commit files, including a commit message provides context for you and your team members to understand the change. For example, include a commit message like implemented product recommendation feature. The next step is pushing the changes in the branch to the remote repository. Most often, the code is reviewed by a maintainer who is responsible for managing the repository before it is merged into the main branch in the remote repository. To merge the branch, you create a pull request. It is a request to the maintainer to review and approve the changes in the branch.

After the maintainer merges the pull request, the changes in the branch will be reflected in the main branch. Similarly, if you have maintainer access, you will receive pull requests from your team members and you will review and approve their requests. You learned about the typical workflow in a software development project. There may be situations where you start a project from scratch and intend to collaborate with others. You can initialize a local project directory as a git repository so that git starts tracking changes in your project directory. The next step is to select all project files that you want git to track, move them to a staging area, and then do an initial commit. After this, you will create a blank repository and link your local git repository to the remote repository.

Then you will push all project files from your local repository to the remote repository. Other developers can clone the remote repository and follow the regular workflow for updating project files. Let's understand the workflow better with a use case. A company assigns a team of developers, testers, and product manager to a new web application development project. Anne, the lead developer, initializes a git repository in her working directory. She creates project files, moves them to the staging area, and does the initial commit. She then pushes the commit to a blank remote repository she created.

All developers clone the remote repository and start working on it by creating branches. One of the developers, John, is responsible for implementing a user authentication feature. He creates a new branch named User Auth from the main branch. John completes the feature development and commits to the User Auth branch. After thorough testing, he pushes the branch to the remote repository and creates a pull request. Anne reviews the pull request and approves it to merge the changes into the main branch so other developers can access the changes made by John. Similarly, other developers push commits to the remote repository for the features they worked on.

At this stage, feature development is complete and the project is ready to be released. Anne creates a release branch named Release 1.0 from the main branch in the remote repository. The team pulls the changes from the remote repository so that their local repository is up to date. They perform final testing, bug fixes and documentation updates in the Release 1.0 branch. After testing, they commit the changes, push the commits to the remote repository, and create a pull request. Anne reviews and merges the changes into the main branch and tags the release as Release 1.0. Let's now recap what you learned.

In this video, you learned about the steps in a git workflow. When you join an existing project, first clone the remote repository. Then create a branch from the main repository and work on the branch. Add updated files to the staging area and commit to the branch. Push commits to the remote repository. Create a pull request to merge the branch into the main branch, which will be reviewed and approved by the maintainer. When you start a new project, initialize a local git repository.

Then select select the files you want Git to track, move them to a staging area and perform an initial commit. Create a blank remote repository and establish a link with your local repository. Push the changes so other developers can clone this remote repository and follow the regular workflow for updating project files. [MUSIC]

---

### 2. [VIDEO TRANSCRIPT] Overview of Git Commands Video • 5 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/1LQzR/overview-of-git-commands
- **Method:** `dom_transcript` | **Length:** 4428 chars

Welcome to Overview of Git Commands. In this video, you will examine some basic Git Commands and the functions and applications of basic Git Commands. Git Commands are used for various purposes such as tracking and saving changes and sharing your changes with others. Typically, many of these activities are performed through the web interface. Command Line Interface or CLI is another option to perform these activities. Let's consider a scenario to understand some general command line commands such as mkdir, cd that can help in smooth functioning of the project. We will also discuss some basic Git Commands such as git init, git add, git commit, git log, git branch, git checkout, git merge, and git status.

Consider you are a part of a web developer who wants the addition of a new HTML file to enhance the features of his web application. In this scenario, you wish to experiment with your codes without disturbing the main code. Let's explore the steps. Let's start by creating a new directory named MyRepository by using the mkdir command. The mkdir command stands for make directory. Once you have created the directory, navigate to the directory using CD, MyRepository command. This command is used to navigate into a specific directory.

Now, let us now create a new repository in this directory using the git init command. It sets up the necessary files and data structure for Git to start managing your project's version control. You can create a new HTML file that has the necessary content. Let's say you create index.html file. Now add this newly created file to the staging area using git add command. This command moves changes from the working directory to the staging area. Now you decide to commit the addition of the new HTML file with a message.

For this, you use the git commit-m command that takes your staged snapshot of changes and saves them to the project with a descriptive message. This message explains the purpose of the git commit. So in this case, created a new HTML file can be your commit message. If you wish to review the commit history to confirm the commit is recorded, run the git log command. It enables you to browse previous changes made to a project. Here, your commit history will reflect created a new HTML file. Now what if you want to experiment with your code, but you do not want to disrupt the current flow?

Let's learn to create a branch using git branch command. To work in the isolation, you can use git branch command that lists, creates, renames, and even deletes branches within a Git repository. So, say you want to create a branch called Codelist. For this, you may use the git branch command. To switch to the newly created branch to start the development, use the git checkout command. The git checkout command lets you switch between the existing branches. You can now make the changes to the index.html file in the code_list branch.

Once done, run the git add changes to add the newly made changes in your file to the staging area. As stated earlier, let's now commit the new changes made in the code_list branch with a descript message such as updated index.html file in branch. Let's now browse the commit log in the code_list branch using the git log command. Your output will now display updated index.html file in branch. To see the status of all the changes you made in your Git working directory, let's run the git status command. This command git provides information about the state of your files in relation to the repository. Finally, git merge lets you put everything back together again and merge the feature branch with the main branch.

In this example, we will use git checkout command to navigate to the main branch first, then use the git merge followed by the branch name, which in this case is the code_list. Let's now recap what you learned. In this video, you learned about the CLI commands that you can use to perform various activities. The commands are mkdir to create a new directory, cd to navigate to a specific directory, git init to initiate a Git repository, git add to move the changes from the working directory to the staging area, git commit to commit the changes to the project, git log to browse the previous changes, git branch to create a new branch, git checkout to switch between the existing branches, git merge to update the branches with the main branch, and git status to see the status of your working directory.

---

### 3. [VIDEO TRANSCRIPT] Demo: Working with Branches using Git Commands Video • 4 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/b690l/demo-working-with-branches-using-git-commands
- **Method:** `dom_transcript` | **Length:** 4077 chars

[MUSIC] Welcome to the video Demo: Working with Branches using Git Commands. In this video, you will examine the functions of various git commands and how to manage git branches using commands. Branches allow you to work on features, experiments, or fixes independently in a structured and organized manner. The git branching workflow is crucial in version control and collaboration when working on software development projects. The workflow allows the teams to work on different features, bug fixes, or experiment in isolation without disrupting one another's code. Let us now focus on how to efficiently use git commands to facilitate the branching workflow process. To do so, first, let us clone the repository so that you can have a copy of that repository on your local machine.

Navigate to the GitHub repository, then click Code and copy the URL under the HTTPS section in the terminal window and change to the target directory. When you want to create a copy of the repository, run the git clone command with the repository URL. Once you have the copy, you can create branches, make changes, and sync those changes. Changed to the directory that was cloned Now let us focus on the git branch command. Run the git branch command, followed by the desired branch name to create a new branch so that you can work on it without impacting the main code. Let's say that to create a branch named PATCH-1-ADDING-HEADERS, you will execute git branch PATCH-1-ADDING-HEADERS. The new branch created will be a copy of the branch you are currently on.

Note that you will not be taken to the newly created branch automatically. To switch to branch PATCH-1-ADDING-HEADERS, use the git checkout PATCH-1-ADDING-HEADERS command. Now that you are on branch PATCH-1-ADDING-HEADERS, you can make your changes. While on the PATCH-1-ADDING-HEADERS branch, let's say you add a header such as welcome to KIV to your index.html file. Next, run the git status command to check the status of your working directory. This will highlight the modifications made to your index.html file. To stage the changes in your PATCH-1-ADDING-HEADERS branch, execute the git add index.html command.

This command will specify that the changes are now ready to be committed. You can finally run the git commit -m command with the message Added header to save your changes. The -m in the git commit command adds a message to your changes. Now the changes in the index.html file are part of your PATCH-1-ADDING-HEADERS branch's history. Let us now focus on merging the PATCH-1-ADDING-HEADERS branch with the main branch. To do so, firstly, switch back to the main branch by running the git checkout main command. By doing so, you are no longer on the PATCH-1-ADDING-HEADERS branch.

Now run the git merge PATCH-1-ADDING-HEADERS command. This command will integrate your changes from the PATCH-1-ADDING-HEADERS branch into the main branch. The header change from PATCH-1-ADDING-HEADERS is now incorporated into the index.html file located in the main branch. To make these changes accessible in your remote repository, use the git push -u origin main command. This command will push the main branch, including the changes merged from the PATCH-1-ADDING-HEADERS branch, to your remote repository. Finally, run the git status command to ensure the changes have been made and the branch is up to date. That's it.

You have come to the end of this video. In this video, you learned how to effectively work with branches using git commands. You started by listing branches with the git branch command, then created the PATCH-1-ADDING-HEADERS branch using the git branch PATCH-1-ADDING-HEADERS command. Then you switched to the new branch using git checkout PATCH-1-ADDING-HEADERS command, made and staged changes using git status, git add index.html, git commit -m commands. And finally, merged PATCH-1-ADDING-HEADERS with the main branch using git checkout main and git merge PATCH-1-ADDING-HEADERS. You concluded this exercise by pushing the main branch to your remote repository using git push -u origin main. [MUSIC]

---

### 4. [VIDEO TRANSCRIPT] Cloning and Forking GitHub Projects Video • 5 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/0CWLT/cloning-and-forking-github-projects
- **Method:** `dom_transcript` | **Length:** 4690 chars

Welcome to Cloning and Forking GitHub Projects. After watching this video, you will be able to clone and sync repositories. Fork a project to make a base for a new project. Use git commands to communicate with other developers. GitHub has over 100 million existing repositories, including some very useful projects. Whether you are joining a team or basing your own project on prior work, some of the most powerful tools are forking and cloning a repository. Cloning generally refers to creating a copy of a repository on your local machine.

Cloned copies can be kept in sync between the two locations. Forking allows you to modify or extend a project without affecting the original project. Frequently this is used to take an existing project and make it the starting point for your new project. Clone a GitHub repository. Navigate to the repository that you want to clone. Under the repository name, click Code. In the Clone with HTTPS section, click the Clipboard button to copy the URL.

To download the source code, you can click Download Zip, but without the version control information. On your local machine, open a terminal window and change to the directory where you want the clone to be copied. Type git clone, followed by pasting the URL that you copied above, and then press Enter to execute the cloning. When you have made your changes and are ready to sync your code back to GitHub, first you must run the git add files command. This moves the changed files into a staging area on your local repository. The staging area is an area where commits can be formatted and reviewed before completing the commit. Next, when you are ready, run git commit -m message, and this will commit changes in the staging area.

When you are ready to move your changes fully into the GitHub repository, use the git push command. This will push all the committed changes into the repository. Remote repositories are repositories that are stored elsewhere, on the internet, on your network, even on your local computer. You can have several remote repositories, each of which generally is either read-only or read-write for you. Collaborating with others involves managing these remote repositories and involves push, pull, and fetch operations to and from them when you need to share work. Use git push to transfer your changes to the remote repo. Use git fetch to transfer any changes from the remote repo to your local repo.

It does not merge those changes to the branch you are working on. You can perform a merge manually if you want. Use git pull to transfer any changes from the remote repo to your local repo and merge them to a branch. Users use the terms upstream and origin when talking about remote repos. Origin generally refers to your fork and upstream refers to the original work. These are the norms. You can of course name them anything you like.

Forking is used to take a copy of a GitHub repository and use it as the base for a new project. You can also use forking to submit back changes into the original repository. This is also used to independently make changes to a project. In that instance, when you are satisfied with your changes, submit a pull request to the original project owner. They can decide whether or not to accept your changes. It is often a legal requirement to keep a copy of the license file. Even if no legal requirement exists, it's good practice.

Navigate to the repository that you want to fork. In the top right corner, click the fork button. To keep a fork in sync with the original work from a local clone, first create a local clone of the project. To configure git to sync your fork, open a terminal and change to the directory containing the clone. Type git remote -v. This gives you the remote repository. Type git remote add upstream with the pasted-in directory that you used in creating your clone.

Adding upstream adds the original repository as a new remote repository labeled upstream. If you type git remote -v, you'll see the change reflected. Other commands of interest include git fetch upstream to grab upstream branches and git merge upstream/main, which merges changes into the main branch. You will also see git pull upstream used to fetch and merge the remote branch in the same step. Git pull upstream reduces the number of steps to sync with a remote branch, but the automatic merges are not always desired. In this video, you learned GitHub has over 100 million existing repositories that you can use. You can clone a repository to copy it to your local machine and sync changes back to the original repository.

You can fork a repository to use it as the base for a new project or to work on a project independently.

---

### 5. [VIDEO TRANSCRIPT] Cloning versus Forking Video • 6 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/7zKO3/cloning-versus-forking
- **Method:** `dom_transcript` | **Length:** 6138 chars

Welcome to cloning versus forking. Until now, you have delved into the concepts of cloning and forking, but have you ever paused to think about their differences? In this video, you will learn the difference between cloning and forking repositories and when to use them. You will also describe the cloning and forking workflow. GitHub allows multiple developers to collaborate on their code base in parallel. A project in GitHub.com resides either as a public or private repository. Each developer working on that project may have their own copy of the repository on their computer which they refer to as their local repo, and one that is on GitHub.com which they refer to as the remote repo.

Let's say you have an existing project named Grand Messaging, and you are looking to create a new or derivative project, Grand Messaging Plus, which offers additional features and improvements over the original. There's no need for you to start creating your code base again, you can simply fork the existing Grand Messaging project, create Grand Messaging Plus, and develop on top of the existing code base, offering new and improved features. To fork a public project, you can go to its GitHub project page and select Fork at the top of the page. This fork option is available only while using the web interface. There is no native git command to create a fork. The repo from which you create the fork is referred to as the original upstream repository. Once you fork the original upstream, the forked copy of the repo becomes the origin, and developers with access to the origin can create clones of it on their local machines.

After cloning, you can create branches and easily make changes to the code base, like adding features, enhancements, or fixing bugs. Finally, you can add, commit, and push your changes to the branch and request to merge the branch with the main branch in the origin. However, it is important to note that the synchronization of changes using push and merge can only be done with repos that the developers have right access to. But what if you want to contribute your changes back to the original upstream that you do not have right access to from where it was forked? In that case, you can submit a pull request for your proposed changes by selecting New pull request from the Pull requests tab. The maintainers of the upstream project can review the changes in the pull request, provide feedback, and merge accordingly unless there are any conflicts to be resolved. Now, let's look at how you can create branches and synchronize changes.

To create a branch, you can use The git branch command and then make the branch active using the git checkout command. Once changes are made, save and stage them using git add and git commit. After the intended changes are completed, you should set up an upstream branch for the newly created branch and push the changes to the new branch, then you raise a request to the maintainer to merge the changes in the new branch to the main branch after reviewing it. Let us revisit the forking workflow. First, you create a fork of an upstream project which then becomes the origin. The developer can create clones on the local machines, make changes, and then use git push to push the updated main branch back to the origin by creating pull requests. The upstream project maintainers review the changes and then merge if there are no conflicts.

One thing to note about the git merge command is that it lets you take independent lines of development in git branches and integrate them into a single branch. Now, let's say a new developer joins your project to upgrade the Grand Messaging to Grand Messaging Plus. How are you going to share the remote repo with the new developer to collaborate on the project? This is where cloning comes to your rescue. You can clone any public repo in GitHub or a private repo that you have access to by going to that repo and selecting the Code button. You can then get the entire code base of the remote repo in various ways. GitHub also gives you the ability to copy the HTTPS URL and then execute the git clone URL command from your local machine.

After cloning, you can follow the same process of updating your code base and merging with the main branch. Let us quickly look at the entire clone workflow. Cloning comes into the picture once you have forked your repo and it has now become the origin. You then use the origin to create an identical copy of the remote repo using the git clone command that the developer can use on their computer. Then, the new developer creates a new branch, makes changes, and saves them using add and commit operations. After that, they push the new branch to the origin to get their changes reviewed. A reviewer or maintainer uses the git fetch or git pull command to get the latest copy of the repo and the git diff command to help identify and compare the changes in the branch.

Once reviewed, they can use git checkout and merge the branch to the main. Lastly, anyone with maintainer access can create a pull request to the original upstream to initiate the changes in the original repo. Let's recap. In this video, you learned that if you want to create a derivative project from another project, as the starting point, you can choose to fork a project. The repo that you fork from is referred to as the upstream repo. To contribute your changes back to the upstream project for which you do not have right access, you can submit a pull request, commonly referred to as PR. The maintainers of the upstream project can review the changes in the pull request, provide feedback, and merge accordingly unless there are any conflicts to be resolved.

You can create an identical copy of the remote repo using the git clone operation. The remote repo from which the project is cloned is also referred to as the origin. To create branches and synchronize changes, the git commands used are : git branch to create a branch, git checkout to activate the branch, git add and git commit to save changes, git push to push the branch to the remote repo, and git merge to merge the changes to the main branch.

---

### 6. [VIDEO TRANSCRIPT] Managing GitHub Projects Video • 3 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/UR6eC/managing-github-projects
- **Method:** `dom_transcript` | **Length:** 3117 chars

Welcome to managing GitHub projects. In this video, you'll identify the common roles of version control or Git in the project and list Git commands to communicate with other developers. You already know that GitHub is a popular platform for version control and project management. You require managing your GitHub projects for effective collaboration and project organization. Multiple roles are involved in managing a project; a developer, an integrator, and a repository administrator. A developer working as a participant in a group project needs to learn how to communicate with others and to use these commands in addition to the ones needed by a standalone developer. When working with Git, you can use Git commands or desktop tools such as GitHub Desktop.

Git clone is used to create a copy from upstream, a remote shared repository that the developer wants to work on. Git pull and git fetch are used to pull or fetch the repository from origin to keep up to date with the upstream. Git push is used to push commits to the shared repository if you adopt a concurrent versioning system for the repository workflow, and git request, pull creates a summary of changes for your upstream to pull. An integrator in a group project receives changes made by others, reviews and integrates them, responds to pull requests, and publishes the result for others to use. Integrators use the following commands in addition to the ones needed by participants. Git pull helps you merge with your trusted lieutenants. Git revert will undo any botched commits.

Git push will help to publish the project from the local repo to the remote repo. The repository administrator structures how the repository is organized and how users interact with the repository. They also manage communities, asset types, relationships, categories and attributes. A repository administrator sets up and maintains access to the repository for developers. They also configure the servers needed for accessing the web services and documentation, define email and index settings, and manage the look and feel of the application. Repository admins can use GitHub actions to automate software workflows including continuous integration and continuous delivery or CICD. Let's recap. In this video, you learned that multiple roles are involved in managing a project; developer, integrator and repository administrator.

Each role uses different Git commands to communicate with collaborators. A developer working in a group project uses commands like git clone, git pull, git fetch, git push, and git request pull. In addition to the ones needed by a standalone developer, an integrator in a group project reviews and integrates changes made by others. Integrators use commands like git pull, git revert, and git push, in addition to the ones needed by participants. The repository administrators structure how the repository is organized and how users interact with the repository. They also configure the servers needed for accessing the web services and documentation, define email and index settings, and manage the look and feel of the application.

---

### 7. [READING] Summary: Git Workflows with Git Commands Reading • 2 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/supplement/izSAt/summary-git-workflows-with-git-commands
- **Method:** `dom_reading_cml` | **Length:** 2090 chars

In this module, you learned that:

- GitHub has over 100 million repositories. You can clone a repository and sync changes back to the original. You can also fork a repository and use it as the base for the new project or work on that project independently.
- The steps included in a GitHub workflow are: - Clone the remote repository or initialize a Git repository. - Move files to a staging area. - Perform an initial commit. - Create a branch and work on it. - Add files to the staging area and commit. - Push local commits to the remote repository. - Create a pull request for review and merging. - Use the pull operation to update the local repository.
- Multiple roles are involved in managing a project: Developer, Integrator, and Repository Administrator. - A Developer working in a group project uses commands like git clone, git pull, git fetch, git push, and git request-pull in addition to the ones needed by a standalone developer. - An Integrator in a group project reviews and integrates changes made by others. Integrators use commands like git pull, git revert, and git push in addition to the ones needed by participants. - Repository Administrators structure how the repository is organized and how users interact with the repository. They also configure the servers needed for accessing the web services and documentation, define email and index settings, and manage the look and feel of the application.
- The following table shows various Git commands:

| git init | git checkout | git revert | git format-patch | git fetch upstream |
| --- | --- | --- | --- | --- |
| git status | git merge | git config --global user.email | git request-pull | git merge upstream/main |
| git add . | git clone | git config --global user.name | git send-email | git pull upstream |
| git commit | git pull | git remote -v | git am | git web |
| git log | git push | git remote rename | git daemon | git instaweb |
| git reset | git --version | git remote add origin | git remote -v | git-pull downstream |
| git branch | git diff | git remote | git remote add upstream | git-rerere |

---

## Module 3: Final Project and Assessment

### 1. [VIDEO TRANSCRIPT] [Optional] GitHub Copilot
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/lecture/9Kj6D/optional-github-copilot
- **Method:** `dom_transcript` | **Length:** 4855 chars

Welcome to GitHub Copilot. After watching this video, you'll be able to describe the features of GitHub Copilot and the typical workflow that you might follow when using GitHub Copilot. Imagine you have a friend who teams up with you on a project, helping you write code faster and better by providing hints and suggestions, that would be awesome. GitHub Copilot is designed to do exactly this using the power of artificial intelligence or AI. GitHub Copilot is an AI powered tool that assists developers in writing code. It is designed to work as a plug-in for various code editors, including Visual Studio code, and provides contextual code suggestions. Let's look at the features of GitHub Copilot.

The first one is code auto-completion. GitHub Copilot suggests whole lines or blocks of code based on the context of the code you are currently working on. It can complete entire functions, classes, or other code structures. GitHub Copilot offers real-time suggestions as you code, making the development process smoother. You can save time on writing repetitive or standard code. GitHub Copilot generates suggestions based on the code context, including function names, variable names, and even algorithm implementation. For example, while coding in a Python project, when you start writing a for loop and declare a variable such as total underscore, quantity, GitHub Copilot can provide suggestions for the loop structure and calculations.

It supports a wide range of programming languages and is designed to provide you assistance across various popular languages such as Python, JavaScript, Java, C++, and many more. GitHub Copilot integrates with various popular code editors and integrated development environments or IDs such as Pycharm. This makes it easy for you to access it from various development environments. GitHub Copilot keeps learning from the shared knowledge in public code, documents, and educational resources. It uses this knowledge to make better suggestions over time. How would you use GitHub Copilot in your work? Let's look at the typical workflow that you might follow when using GitHub Copilot.

The first step is installing the GitHub Copilot extension in your Visual Studio code environment. You can find it in the Visual Studio code marketplace. After you install the extension, you will activate the extension within Visual Studio code. This step typically involves signing in with your GitHub account and allowing the necessary permissions. You will then open an existing coding project or create a new one. GitHub Copilot will work within the context of the programming language and framework you are using. You will begin writing code as you normally would.

GitHub Copilot will start to provide suggestions and autocompletion based on the context of your code. For example, when you start writing a function in your code, GitHub Copilot generates function bodies. Another example is where GitHub Copilot offers auto-completion suggestions for variable names when you begin declaring a new variable. To accept a suggestion, you can use the tab key or select the suggestion. After generating or editing the code, you will review it to ensure it aligns with your project's requirements and best coding practices. You will test the code to verify that it functions as expected. If any problems come up, you will need to debug the code in the same way you would with any other code.

GitHub Copilot does not help you with debugging. So it's important to perform this step to make sure the code works properly. After you are satisfied with the code, you can commit the changes to your version control system such as Git, and push the changes to the remote repository. Make sure you document any code changes or additions with comments and explanations so that other developers can easily comprehend the code. GitHub Copilot helps you work faster, especially with repetitive or standard code segments. However, remember that it is just a tool to assist you and must not be relied upon for writing critical or complex code. You should use it wisely, review suggestions, and make sure the code is good, secure, and follows best practices.

Let's now recap what you learned. In this video, you learned about GitHub Copilot. GitHub Copilot is an AI-powered tool that assists developers in writing code. It provides features such as code auto-completion and real-time and contextual code suggestions. It supports a wide range of programming languages, popular code editors, and IDEs. GitHub Copilot keeps learning from shared knowledge to make better suggestions over time, you can install the GitHub Copilot extension, activate it, and use it for existing projects or new projects. You must review the suggestions from GitHub, address any issues through debugging, and make sure the code is good, and follow best practices.

---

### 2. [READING] Congratulations and Next Steps
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/supplement/iSx0q/congratulations-and-next-steps
- **Method:** `dom_reading_cml` | **Length:** 731 chars

Congratulations on completing the course on Git and GitHub! We hope you enjoyed it and find great satisfaction using your new skills in the workplace or elsewhere.

The Git and GitHub course is a part of multiple programs. As a next step, you are encouraged to explore other courses in the below-mentioned programs:

- IBM Front-End Developer Professional Certificate
- Applied Software Engineering Fundamentals Specialization
- IBM Full Stack Software Developer Professional Certificate
- IBM DevOps and Software Engineering Professional Certificate
- IBM Back-End Development Professional Certificate

You are encouraged to advance your learning by going through the following links:

- https://git-scm.com/
- https://github.com/

---

### 3. [READING] Thanks from the Course Team
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/supplement/IMBWM/thanks-from-the-course-team
- **Method:** `dom_reading_cml` | **Length:** 1306 chars

The entire course team thanks you for taking this course. We hope you enjoyed it and wish you the best in applying your new knowledge and skills.

We encourage you to rate the course and provide a review. Your feedback is much appreciated.

Best regards,

Course Team

- - -

This course has been brought to you through the involvement of the following team of contributors:

#### Primary Instructors

- Upkar Lidder [ LinkedIn | Twitter: @lidderupk ]
- Rav Ahuja [ LinkedIn ravahuja | Twitter @ravahuja ]

#### Other Contributors & Staff

Project Lead: Rav Ahuja

Subject Matter Experts:  Upkar Lidder, Rav Ahuja, Tapan Kumar, Lavanya T.S.

Instructional Designers:   Maureen McElaney, Lavanya TS, Malika Singla, Aije Egwaikhide, Gagandeep Singh, Sameeksha Saxena, Chitra Nair

Lab and Project Authors:   Malika Singla, Upkar Lidder, Lavanya T.S., Anamika Agarwal, K. Sundararajan

#### Production Team

Project Managers: Alison Woolford, Nancy Varkey

Video Production: Simer Preet, Rajeev Kumar, Prayas Gupta

Publishing: Santosh Sahu, Rachael Jones, Madhumita Pati

QA: Kunal Merchant, Pornima More, Praveen Thapliyal, Rahul Rawat, Vandana Menon

Narration: Bella West, Sarah Ruth

Teaching Assistants and Forum Moderators

Teaching Assistants:  Lavanya R, K Sundararajan, Ritika Joshi, Rajashree Patil

---

## Module 4: [Optional] Working with GitHub from Your Windows Desktop

### 1. [READING] Using Git Commands from your Desktop (Optional) Reading • 10 min
- **URL:** https://www.coursera.org/learn/getting-started-with-git-and-github/supplement/DLU0O/using-git-commands-from-your-desktop-optional
- **Method:** `dom_reading_cml` | **Length:** 1352 chars

In the previous labs you used a Cloud-based IDE to work with Git commands. In many cases, you will be developing code on your own workstation on your desktop/laptop. Linux systems typically come pre-installed with Git commands or if needed you can install them using dnf on rpm based distributions (e.g. Red Hat / Fedora):

sudo dnf install git-all

or, apt on Debian-based distributions (e.g. Ubuntu):

sudo apt install git-all

On MacOS you can activate Git by typing:

git version

However if it is not installed, or if you want to update it, you can download and install the latest version of the MacOS Git Installer, and run the above command to verify the version.

On Windows based systems, you can install Git Bash by downloading the Git for Windows installer. Git Bash includes popular Linux Bash shell commands (such as ls, pwd, cat, etc.) as well as Git commands.

You can also get the GitHub desktop for Windows and MacOS, which provides a UI for GitHub on your desktop.

When you are working with GitHub repositories from your desktop you will also need to setup an ssh key.

The remaining labs in this module are optional however recommended for those with a Windows desktop. In the following labs you will install Git Bash on your Windows machine, and configure an ssh key to work with your GitHub repo using Git commands on your system.

---
