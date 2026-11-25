# Module 1: Git and GitHub Fundamentals

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
