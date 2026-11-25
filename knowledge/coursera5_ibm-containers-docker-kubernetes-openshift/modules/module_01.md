# Module 1: Containers and Containerization

### 1. [READING] IBM Product Spotlight: IBM Turbonomic
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/0DqEU/ibm-product-spotlight-ibm-turbonomic
- **Method:** `dom_reading_cml` | **Length:** 688 chars

Welcome to the course! As you learn about containers and Kubernetes, discover how IBM Turbonomic uses AI to automatically optimize resource allocation across cloud environments.

IBM Turbonomic is an AI-powered application resource management platform that helps ensure workloads always have the resources they need while avoiding overprovisioning.

#### What You Can Do with IBM Turbonomic

- Automatically optimize Kubernetes resource allocation
- Reduce cloud costs without compromising performance
- Right-size containers and workloads using AI-driven insights
- Maintain application performance across hybrid cloud environments

Explore IBM Turbonomic: https://ibm.biz/coursera-turbo

---

### 2. [VIDEO TRANSCRIPT] Course Introduction
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/Ixxgm/course-introduction
- **Method:** `dom_transcript` | **Length:** 3459 chars

[Music] Welcome to this introductory course on Containers and Kubernetes. My name is Alex Parker and I'm Upkar Lidder. This course was made for anybody who wants to learn how to design, develop, deploy, manage secure applications on public, private, and hybrid cloud platforms. By the end of this course, you will not only have a running application on public cloud but also have a really good understanding of Kubernetes and Containers. Containerization is not a new technology, but it rose to greater prominence in 2013 with the release of Docker, and it hasn't stopped growing since. In fact, containers have become the technology for modern cloud native development. The analyst firm Gartner predicts that by 2023 over 70 percent of global organizations will be running more than two containerized applications in production, up from less than twenty percent in 2019.

The Cloud Native Computing Foundation known as CNCF conducts annual surveys to discern where and how cloud native technologies are being adopted. The 2019 survey indicates that 84 percent of respondents are using containers in production up from 74 percent in 2018; and 23 percent in the first survey in 2016. These trends clearly demonstrate that containers aren't a passing fad or a niche technology but an industry changing revolution that will impact organizations small and large, and developers worldwide. Likewise, Kubernetes, an open source platform for orchestrating running containers was developed and contributed to the open source community by Google in 2015. The Cloud Native Computing Foundation did a survey in 2019 and found that the number of users or respondents who were interested in cloud native computing technologies went up from 58 percent to 78 percent from the previous year. Kubernetes is the third largest platform for number of committers on GitHub as well as second largest for a number of issues and pull requests only after the Linux Kernel. A thriving ecosystem surrounds the open source Kubernetes platform including applications for cloud security, service mesh as well as other cloud native technologies.

As a result of these things, Kubernetes and Containers have become the de facto standards when talking about cloud native applications, also making them the foundation for any cloud computing related learning. This course will introduce you to Containers, Docker, and container registries, to get you started with the foundations of this technology. Then you'll learn about the need for container orchestration in Kubernetes specifically, including its architecture, the different resources you can deploy in Kubernetes, and how to put those pieces together to deploy a working application. And finally, you'll learn about the Kubernetes ecosystem, including Red Hat OpenShift and Istio, and how these tools can make your journey to containerization, and your subsequent use of containers so much better. The course contains several hands-on labs that will help you apply the content you learn. If you do not have the resources to set up a Kubernetes cluster, the course will provide an environment free of charge which will help you to finish the labs. The prerequisites for this course include basic computer and cloud literacy, as well as an understanding of core cloud concepts.

In addition, understanding of the command line and how to use shell commands will greatly benefit you during this course. Let's get started! Let's get started!

---

### 3. [READING] Course Overview
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/QoHsc/course-overview
- **Method:** `dom_reading_cml` | **Length:** 5042 chars

Hello, and welcome to this course!

In this course, you’ll learn how to build cloud-native applications using modern containerization tools and technologies, including Docker, container registries, Kubernetes, Red Hat OpenShift, and Istio. You’ll also gain practical knowledge of how to deploy and scale applications across public, private, and hybrid cloud environments.

The skills taught in this course are valuable for professionals in software development, back-end and full-stack development, cloud architecture, cloud engineering, DevOps, site reliability engineering (SRE), cloud networking, and many other technology roles.

### Prerequisites

No prior knowledge of containers is required. However, a basic understanding of cloud computing and programming concepts is recommended.

### Course Objectives

By the end of this course, you will be able to:

- Explain how containers enable applications to move efficiently across environments.
- Build cloud-native applications using Docker, Kubernetes, OpenShift, and Istio.
- Describe Kubernetes architecture and use Kubernetes to manage the full container lifecycle.
- Create and use YAML deployment files to configure and deploy Kubernetes resources such as Pods, Services, and ReplicaSets using a declarative approach.

This course consists of five modules. We recommend setting aside several hours each week to complete the course successfully within five weeks.

The course also includes several hands-on labs that allow you to practice and apply what you learn. To provide greater flexibility, you can choose between two lab options based on your preferred programming language and Professional Certificate track. More details are provided in the next reading:

Lab Options by Programming Language

### Module 1: Containers and Containerization

Begin by learning the core concepts, features, benefits, and use cases of containers. You’ll explore Docker fundamentals, understand how Docker works, and discover why it has become a preferred tool for developers.

You’ll learn how to build container images using Dockerfiles, create and run containers, and work with the Docker command-line interface (CLI). You’ll also explore Docker objects, image naming conventions, networking, storage, and plugins, while gaining insight into Docker architecture and containerization concepts.

By the end of the module, you’ll be able to pull images from Docker Hub, run containers, build and tag images using Dockerfiles, and push images to a container registry.

### Module 2: Kubernetes Basics

In this module, you’ll learn the fundamentals of container orchestration and understand why orchestration is essential for managing complex containerized applications.

You’ll explore Kubernetes architecture, including control plane components and controllers, and learn about key Kubernetes objects such as Pods, ReplicaSets, and Deployments. You’ll also work with the Kubernetes command-line interface, kubectl, to create and manage resources within a Kubernetes cluster.

Additionally, you’ll compare imperative and declarative approaches to managing Kubernetes resources.

By the end of the module, you’ll use kubectl to create Pods, Deployments, and ReplicaSets, and observe Kubernetes load balancing in action on a live cluster.

### Module 3: Managing Applications with Kubernetes

In Module 3, you’ll learn how Kubernetes helps manage and scale applications effectively.

You’ll explore ReplicaSets, autoscaling, rolling updates, ConfigMaps, Secrets, and service bindings. You’ll learn how Kubernetes scales applications dynamically to meet demand and how rolling updates allow you to deploy application changes with minimal disruption.

You’ll also discover how ConfigMaps and Secrets help manage configuration data and sensitive information separately from application code.

By the end of this module, you’ll be able to scale and update applications deployed on Kubernetes.

### Module 4: The Kubernetes Ecosystem: OpenShift, Istio, and More

This module introduces you to the broader Kubernetes ecosystem and additional tools that support cloud-native application development.

You’ll examine the similarities and differences between Red Hat OpenShift and Kubernetes and explore OpenShift architecture, build strategies, BuildConfigs, and deployment triggers. You’ll also learn how Operators simplify application deployment and management.

Finally, you’ll explore the Istio service mesh and learn how it manages and secures communication between application services.

By the end of the module, you’ll use the oc CLI to interact with an OpenShift cluster and deploy an application from source code stored in a Git repository.

### Module 5: Final Assignment

In the final project, you’ll apply the tools and concepts learned throughout the course to deploy a simple guestbook application using Docker and Kubernetes. The application will be deployed and managed on OpenShift.

Congratulations on taking this step to expand your knowledge and advance your career. Enjoy the journey!

---

### 4. [READING] Lab Options by Programming Language
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/qXdOz/lab-options-by-programming-language
- **Method:** `dom_reading_cml` | **Length:** 960 chars

To enrich your learning experience, this course offers hands-on labs in two programming languages: Python and JavaScript.

You can choose labs based on your preferred technology or the Professional Certificate (PC) track you are pursuing:

- Option A – Python Labs: Offered as the default lab version for this course.
- Option B – JavaScript Labs: Suggested if you’re pursuing a JavaScript PC.

Labs are available in both the language versions. Please select the version that best aligns with your learning path or interests.

This flexible approach allows you to work in the language you’re most comfortable with while engaging with the core concepts of the course.

Note: The labs in Option B have the similar duration as those in Option A – Python Labs; however, they are designated as 1 minute here to ensure the overall course duration remains unaffected.

Explore your options, choose what suits you best, and enjoy the learning journey.

Happy learning!

---

### 5. [VIDEO TRANSCRIPT] Introduction to Containers Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/3XHL5/introduction-to-containers
- **Method:** `dom_transcript` | **Length:** 5275 chars

Welcome to “Introduction to Containers.” After watching this video, you will be able to identify the traditional computing issues for software development, define a container and describe its characteristics, and list container benefits and challenges, and popular container vendors. Cloud-native is the newest application development approach for building scalable, dynamic, hybrid cloud-friendly software. And container technology is a powerful part of that approach. Let’s check out the analogy of a shipping container. The modern shipping industry standardized a set of container sizes, so no matter what item is shipped, the container size remains the same. Standardization significantly improves shipping efficiency.

Logistics staff select container transport options such as ships, planes, trains, and trucks, based on the container’s size and the client’s delivery needs. Digital container technology is similar. Containers solve the problem of making software portable so that applications can run on multiple platforms. A container, powered by the containerization engine, is a standard unit of software that encapsulates the application code, runtime, system tools, system libraries, and settings necessary for programmers to build, ship, and run applications efficiently. Operations and underlying infrastructure issues are no longer blockers. You can quickly move applications from your laptop to a testing environment, from a staging environment to a production environment, from a physical machine to a virtual machine, or a private cloud or public cloud, and always know that your application will work correctly. A container can be small, just tens of megabytes, and developers can almost instantly start containerized applications.

With these capabilities, containers serve as the foundation for today’s development and deployment solutions standards. Let’s examine some of the development and deployment challenges organizations encounter with traditional computing environments. In traditional environments, developers can’t isolate the app and allocate or designate specific storage and memory resources for apps on physical servers. Servers are often underutilized or overutilized, leading to poor utilization and a poor return on investment. Traditional deployments require comprehensive provisioning resources and expensive maintenance costs. The limits of physical servers can constrain application performance during peak workloads. Applications are not portable across multiple environments and operating systems.

Implementing hardware for resiliency is often time-consuming, complex and expensive. Traditional on premises IT environments have limited scalability, and Finally, automation is challenging when distributing software to multiple platforms and resources using traditional environments. Containers enable organizations to overcome these challenges. Container engines virtualize the operating system and are responsible for running containers. Platform-independent containers are lightweight, fast, isolated, portable, and secure and often require less memory space. Binaries, libraries, and other entities within the container enable apps to run, and one machine can host multiple containers. Containers help programmers quickly deploy code into applications Containers are platform-independent and can run on the cloud, desktop, and on-premises Containers being operating system-independent, run on Windows, Linux, or Mac OS.

Containers are also programming language and IDE independent—whether you are running Python, Node, Java, or other languages. Containers enable organizations to: Quickly create applications using automation. Lower deployment time and costs. Improve resource utilization, including CPU and memory. Port across different environments, and support next-gen applications, including microservices. Using containerization is not without its challenges. Server security can become an issue if its operating system is affected.

Developers can become overwhelmed when managing thousands of containers. Converting monolithic legacy applications can be a complex process, and Developers can experience difficulty right-sizing containers for specific scenarios. Next, let’s learn about some of the more popular container vendors. Docker is a robust platform and the most popular container platform today. Podman is a daemon-less container engine that is more secure than Docker. Developers often prefer LXC for data-intensive applications and operations. And, Vagrant offers the highest levels of isolation on the running physical machine.

In this video, you learned that organizations are moving to containers to overcome challenges around isolation, utilization, provisioning, performance, and more. A container is a standard unit of software that encapsulates everything needed to build, ship, and run applications. Containers are operating system, programming language, and platform-independent. They lower deployment time and costs, improve utilization, automate processes, and support next-gen applications (microservices). Developers may find that management, legacy project migration, and right-sizing are significant challenges. And finally, major container vendors include Docker, Podman, LXC, and Vagrant.

---

### 6. [VIDEO TRANSCRIPT] Introduction to Docker Video • 3 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/xpnLH/introduction-to-docker
- **Method:** `dom_transcript` | **Length:** 2535 chars

Welcome to Introduction to Docker. After watching this video, you will be able to Define what Docker is Describe the Docker process and underlying technology List the benefits of Docker containers and Identify the challenges of Docker containers Available since 2013, the official Docker definition, paraphrased, states that Docker is an open platform for developing, shipping, and running applications as containers. Docker became popular with developers because of its simple architecture, massive scalability, and portability on multiple platforms, environments, and locations. Docker isolates applications from infrastructure, including the hardware, the operating system, and the container runtime. Docker is written in the Go programming language. Docker uses Linux kernel features to deliver its functionality. Docker also uses namespaces to provide an isolated workspace called the container.

And Docker creates a set of namespaces for every container and each aspect runs in a separate namespace with access limited to that namespace. Docker methodology has inspired additional innovations, including complementary tools such as Docker CLI, Docker Compose, and Prometheus, and various plugins, including storage plugins, orchestration technologies using Docker Swarm or Kubernetes, and development methodologies using microservices and serverless. Docker offers the following benefits. Docker's consistent and isolated environments result in stable application deployments. Deployments occur in seconds. Because Docker images are small and reusable, they significantly speed up the development process, and Docker automation capabilities help eliminate errors, simplifying the maintenance cycle. Docker supports Agile and CICD DevOps practices.

Docker's easy versioning speeds up testing, rollbacks, and redeployments. Docker helps segment applications for easy refresh, cleanup, and repair, and developers collaborate to resolve issues faster and scale containers when needed. And Docker images are platform independent, so they are highly portable. In this video, you learned that Docker is an open platform for developing, shipping, and running applications as containers. Docker speeds up the deployment process across multiple environments. Docker uses namespaces technology to provide an isolated workspace called the container. Docker creates a set of namespaces for every container, and each aspect runs in a separate namespace with access limited to that namespace.

Docker supports Agile and CICD DevOps practices.

---

### 7. [VIDEO TRANSCRIPT] Building and Running Container Images Video • 2 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/JjETU/building-and-running-container-images
- **Method:** `dom_transcript` | **Length:** 1997 chars

[MUSIC] Welcome to building and running containers. After watching this video, you will be able build a container image using a Dockerfile. Create a running container using an image and describe key Docker commands. This diagram shows the development process of a running container. The steps to create and run containers create a dockerfile use the dockerfile to create a container image and use the container image to create a running container. Use a Dockerfile to create a running container. This sample docker file has the commands from and CMD.

From defines the base image and CMD prints the words hello world on the terminal. You'll notice that this Docker command uses the build command, the tag, the repository, the version, and the current directory. After you run this build, the output messages include sending build context to Docker Daemon, successfully built <image>, which confirms image creation and successfully tagged my-app, which confirms the tag. To verify the creation of the image, run the docker images command. The output displays the repository, my-app, as well as the tag, v1, image ID, creation date, and the image size. Create the container using the run command. With the container image name and tag, the application prints the words hello world.

Execute the Docker PSA command, which displays the details of the container created. Given the appropriate input. The build command is used to create container images with tags from a docker file. The images command will list all the images, their repositories and tags, and their sizes. The run command creates and runs a container from an image. The push command stores images in a configured registry, and the pull command retrieves images from a configured registry. In this video, you learned that the build command is used with a Dockerfile to build a container image.

The run command is used with an image to create a running container and key. Dockerfile commands include build, images, run, pull, and push.

---

### 8. [VIDEO TRANSCRIPT] Docker Objects Video • 4 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/lOkqH/docker-objects
- **Method:** `dom_transcript` | **Length:** 3786 chars

Welcome to introduction to Docker objects. After watching this video, you will be able to identify and describe Docker objects, identify essential Docker file commands, explain container image naming, and describe how Docker uses networks, storage, and plugins. Docker contains objects such as Docker file, images, container, network, storage volumes, and other objects, such as plugins and add-ons. A Docker file is a text file that contains instructions needed to create an image. You can create a Docker file using any editor from the console or terminal. Let's go over several of the essential instructions that Docker provides. A Docker file must always begin with a FROM instruction that defines a base image.

Often the base image is from a public repository, like an operating system or a specific language like Go or Node.js. The RUN instruction executes commands. The CMD instruction defines a default command for execution. A Docker file should have only one CMD instruction. If the Docker file has several CMD instructions, only the last CMD instruction will take effect. Next, let's learn about Docker images. A Docker image is a read only template with instructions for creating a Docker container.

The Docker file provides instructions to build the image, and each Docker instruction creates a new layer in the image. When you change the Docker file and rebuild the image, the Docker engine only rebuilds the changed layers. Images can share these layers, which saves a lot of disk space, as well as network bandwidth when sending and receiving images. When you instantiate this image, you get a running container. At this point, a writable container layer is placed on top of the read only layers, and the writable layer is needed because containers are not immutable as images. Now, let's learn about how images are named. An image name has a unique format that consists of three parts, the host name, the repository, and the tag.

The host name identifies the image registry. A repository is a group of related container images, and the tag provides information about a specific version or variant of an image. Consider the image name docker.io/ubuntu:18.04. The host name docker.io refers to the Docker Hub registry. When using the Docker CLI, you can exclude the docker.io host name. The repository name Ubuntu indicates the Ubuntu image. Finally, the tag, shown here as 18.04, represents the installed Ubuntu version.

Now, let's learn about Docker containers. What is a Docker container? A Docker container is a runnable instance of an image. You can use the Docker API or CLI to create, start, stop, or delete an image. You can connect to multiple networks, attach storage to the container, or create a new image based on its current state. Docker keeps containers well isolated from each other and their host machine. When using Docker, networks help isolate container communications.

By default, data doesn't persist when the container no longer exists. Docker uses volumes and bind mounts to persist data even after a container stops, and plugins such as storage plugins, provide the ability to connect to external storage platforms. In this video you learn that Docker contains objects such as Docker files, images, containers, networks, storage volumes, and other objects, such as plugins and add-ons. Essential Docker instructions include FROM, RUN, and CMD. A Docker container is a runnable instance of an image. An image name format consists of three identifiers, the host name, the repository, and the tag. Docker uses networks to isolate container communications.

Docker uses volumes and binds mounts to persist data even after a container stops running. Plugins, such as storage plugins, provide the ability to connect to external storage platforms.

---

### 9. [VIDEO TRANSCRIPT] Docker Architecture Video • 3 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/5ZK8J/docker-architecture
- **Method:** `dom_transcript` | **Length:** 3280 chars

[MUSIC] Hello and welcome to Docker Architecture. After watching this video, you will be able identify the components of the Docker architecture. Explain the features of the Docker architecture components, and describe the process of containerization using Docker. The Docker client server architecture provides a complete application environment. Docker components include the client, the host, and the registry. Let's take a high level view of how docker works. First, you'll use either the Docker command line interface or REST APIs via the Docker client to send instructions to the Docker host server, commonly called the host.

The Docker host contains the daemon known as dockered. The daemon listens for Docker API requests or commands such as docker run, and processes those commands. The daemon does the heavy lifting to build, run, and distribute docker containers. Then, Docker stores the container images in a registry. The Docker host also includes and manages images, containers, namespace networks, storage plugins, and add-ons. You can use the Docker client to communicate with local and remote docker hosts. You can run the Docker client and daemon on the same system or connect your docker client to a remote Docker daemon, and Docker daemons can also communicate with other daemons to manage docker services.

Docker stores and distributes images in a registry. Registry access is either public, such as Docker hub, which is accessible by everyone, or private. Enterprises usually opt to use a private registry for security reasons. And registry locations are hosted using a third-party provider such as IBM Cloud container registry, or self-hosted in private data centers or on the cloud. Next, let's learn about moving images into the registry. First, developers build and push the images using automation or a build pipeline into a registry where Docker stores these images. Then, local machines, cloud systems, and on premises systems can pull those images.

Let's examine the process in more detail. Here is a visual representation of the Docker architecture, which consists of the client, the Docker host, including the Docker daemon, and the registry with its existing stored images. Let's check out the containerization process. Here's how you use Docker to create a container image. First, use an existing base image or a Docker file. Then issue the build command that creates a container image with a name. Next, issue the push command to store the image to the registry.

The host first checks locally if the image is already available, and then issues the run command with the image name to create the container. If the image is unavailable within the host, the Docker client connects to the registry and pulls the image to the host. The daemon then creates a running container using the image. In this video, you learned that Docker architecture consists of a Docker client, a Docker host, and a registry. The client interacts with the host using commands and REST APIs. The Docker host includes the daemon commonly called dockerd. The docker host also manages images, containers, namespaces, networks, storage, plugins, and add-ons, and containerization is the process used to build, push, and run an image.

To create a running container. [MUSIC]

---

### 10. [READING] Review of Docker Concepts and Understanding a Dockerfile Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/YJjQh/review-of-docker-concepts-and-understanding-a-dockerfile
- **Method:** `dom_reading_cml` | **Length:** 4368 chars

This reading is designed to enhance your understanding of Docker concepts and guide you through the process of comprehending a Dockerfile.

#### Reading Overview:

- Docker Concepts
- Understanding a Dockerfile

#### Docker Concepts

#### Overview

Docker simplifies the process of creating, deploying, and managing applications by using containers. Containers allow you to package an application with its dependencies into a standardized unit for software development. Docker provides tools and a platform to build, ship, and run containers across various environments.

#### Dockerfile

A text file that contains instructions for building a Docker image. It specifies the base image, sets the working directory, installs dependencies, copies application code, exposes ports, and defines commands to run the application.

#### Container

An instance of a Docker image that runs as a process on the host machine. Containers are lightweight, portable, and isolated, making them ideal for deploying and scaling applications.

#### Docker Image Storage

Docker images are stored in registries, which can be public or private. Public registries like Docker Hub host millions of images, while organizations often use private registries for security and control.

#### Where Docker Images Exist

Local Machine: When you build a Docker image, it's initially stored locally on your machine. You can list local Docker images using the docker images command.

Registry: After building, you can push Docker images to a registry, making them accessible from anywhere with access to that registry.

#### Dockerfile

Below is a sample Dockerfile for reference. The subsequent explanation details the commands used, providing a comprehensive understanding of how to write a Dockerfile.

1234567891011121314151617181920212223# Use an official OpenJDK 21 image as the base imageFROM openjdk:21-jdk-slim # Set a working directory inside the containerWORKDIR /app # Label the image with metadataLABEL maintainer="Your Name <your.email@example.com>"LABEL version="1.0"LABEL description="A Java web application running in Docker" # Copy the compiled JAR file to the containerCOPY target/myapp.jar /app/myapp.jar # Expose port 8080 to allow external accessEXPOSE 8080 # Run the application when the container startsCMD ["java", "-jar", "/app/myapp.jar"] # Health check to ensure the application is runningHEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \    CMD curl --fail http://localhost:8080/health || exit 1Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Understanding the Dockerfile

#### 1: Base Image

Uses FROM openjdk:21-jdk-slim, which provides Java 21.

#### 2: Working Directory

Sets /app as the working directory.

#### 3: Labeling the Image

Adds metadata like maintainer name, version, and description.

#### 4: Copying the Application

Copies myapp.jar (your Java web application) into the container.

#### 5: Exposing Port 8080

Allows traffic to reach the application.

#### 6: Running the Application

CMD runs the Java application using java -jar.

#### 7: Health Check

Checks if the app is running at http://localhost:8080/health. If the request fails, Docker marks the container as unhealthy. Runs every 30s with 3 retries if the check fails.

#### Build the Docker Image

1docker build -t my-java-app .Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Run the Container

1docker run -p 8080:8080 my-java-appInformation: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Check Container Health

1docker ps --filter "health=unhealthy"Information: Pressing Tab in the current editor will insert the tab character. Toggle this behavior by pressing Control+M.
#### Summary

In this reading, you learned about Docker concepts and the process of creating a Dockerfile. The provided Dockerfile and the outlined steps demonstrate how to build a Docker image for a Java application. It starts with a JDK 21 base image, defines a working directory, sets up environment variables. The application code is then copied into the container, and a health check is included to ensure the container runs correctly.

Author: Nikesh Kumar

---

### 11. [READING] Summary & Highlights: Understanding the Benefits of Containers Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/WBNfT/summary-highlights-understanding-the-benefits-of-containers
- **Method:** `dom_reading_cml` | **Length:** 1203 chars

Congratulations on completing the first module!

By this point, you should understand the following key concepts:

- A container is a software unit that packages everything needed to build, ship, and run an application.
- Containers help reduce deployment time and costs, improve resource utilization, automate processes, and support next-generation applications such as microservices.
- Popular container technologies and vendors include Docker, Podman, LXC, and Vagrant.
- Docker is an open platform used to develop, ship, and run applications in containers.
- Docker containers may not be the best fit for monolithic applications or workloads with strict high-performance or security requirements.
- Docker architecture consists of three main components: the Docker client, the Docker host, and the container registry.
- The Docker host manages Docker objects such as Dockerfiles, images, containers, networks, storage volumes, plugins, and add-ons.
- Docker networks help isolate communication between containers.
- Docker uses volumes and bind mounts to persist data even after containers stop running.
- Plugins, including storage plugins, enable Docker to connect with external storage platforms.

---

### 12. [READING] Cheat Sheet: Docker CLI Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/wBjIF/cheat-sheet-docker-cli
- **Method:** `dom_reading_cml` | **Length:** 1684 chars

| Command | Description |
| --- | --- |
| curl localhost description | Pings the application. |
| docker build | Builds an image from a Dockerfile. |
| docker build . -t | Builds the image and tags the image id. |
| docker container rm | Removes a container. |
| docker images | Lists the images. |
| docker ps | Lists the containers. |
| docker ps -a description | Lists the containers that ran and exited successfully. |
| docker pull | Pulls the latest image or repository from a registry. |
| docker push | Pushes an image or a repository to a registry. |
| docker run | Runs a command in a new container. |
| docker run -p | Runs the container by publishing the ports. |
| docker stop | Stops one or more running containers. |
| docker stop $(docker ps -q) | Stops all running containers. |
| docker tag | Creates a tag for a target image that refers to a source image. |
| docker --version | Displays the version of the Docker CLI. |
| exit | Closes the terminal session. |
| export MY_NAMESPACE | Exports a namespace as an environment variable. |
| git clone | Clones the git repository that contains the artifacts needed. |
| ibmcloud cr images | Lists images in the IBM Cloud Container Registry. |
| ibmcloud cr login | Logs your local Docker daemon into IBM Cloud Container Registry. |
| ibmcloud cr namespaces | Views the namespaces you have access to. |
| ibmcloud cr region-set | Ensures that you are targeting the region appropriate to your cloud account. |
| ibmcloud target | Provides information about the account you’re targeting. |
| ibmcloud version | Displays the version of the IBM Cloud CLI. |
| ls | Lists the contents of this directory to see the artifacts. |

---

### 13. [READING] Module 1 Glossary: Container Basics Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/tSMyZ/module-1-glossary-container-basics
- **Method:** `dom_reading_cml` | **Length:** 6098 chars

| Term | Definition |
| --- | --- |
| Agile | is an iterative approach to project management and software development that helps teams deliver value to their customers faster and with fewer issues. |
| Client-server architecture | is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. |
| A container | powered by the containerization engine, is a standard unit of software that encapsulates the application code, runtime, system tools, system libraries, and settings necessary for programmers to efficiently build, ship and run applications. |
| Container Registry | Used for the storage and distribution of named container images. While many features can be built on top of a registry, its most basic functions are to store images and retrieve them. |
| CI/CD pipelines | A continuous integration and continuous deployment (CI/CD) pipeline is a series of steps that must be performed in order to deliver a new version of software. CI/CD pipelines are a practice focused on improving software delivery throughout the software development life cycle via automation. |
| Cloud native | A cloud-native application is a program that is designed for a cloud computing architecture. These applications are run and hosted in the cloud and are designed to capitalize on the inherent characteristics of a cloud computing software delivery model. |
| Daemon-less | A container runtime that does not run any specific program (daemon) to create objects, such as images, containers, networks, and volumes. |
| DevOps | is a set of practices, tools, and a cultural philosophy that automate and integrate the processes between software development and IT teams. |
| Docker | An open container platform for developing, shipping and running applications in containers. |
| A Dockerfile | is a text document that contains all the commands you would normally execute manually in order to build a Docker image. Docker can build images automatically by reading the instructions from a Dockerfile. |
| Docker client | is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon. |
| Docker Command Line Interface (CLI) | The Docker client provides a command line interface (CLI) that allows you to issue build, run, and stop application commands to a Docker daemon. |
| Docker daemon (dockerd) | creates and manages Docker objects, such as images, containers, networks, and volumes. |
| Docker Hub | is the world's easiest way to create, manage, and deliver your team's container applications. |
| Docker localhost | Docker provides a host network which lets containers share your host's networking stack. This approach means that a localhost in a container resolves to the physical host, instead of the container itself. |
| Docker remote host | A remote Docker host is a machine, inside or outside our local network which is running a Docker Engine and has ports exposed for querying the Engine API. |
| Docker networks | help isolate container communications. |
| Docker plugins | such as a storage plugin, provides the ability to connect external storage platforms. |
| Docker storage | uses volumes and bind mounts to persist data even after a running container is stopped. |
| LXC | LinuX Containers is a OS-level virtualization technology that allows creation and running of multiple isolated Linux virtual environments (VE) on a single control host. |
| IBM Cloud Container Registry | stores and distributes container images in a fully managed private registry. |
| Image | An immutable file that contains the source code, libraries, and dependencies that are necessary for an application to run. Images are templates or blueprints for a container. |
| Immutability | Images are read-only; if you change an image, you create a new image. |
| Microservices | are a cloud-native architectural approach in which a single application contains many loosely coupled and independently deployable smaller components or services. |
| Namespace | A Linux namespace is a Linux kernel feature that isolates and virtualizes system resources. Processes which are restricted to a namespace can only interact with resources or processes that are part of the same namespace. Namespaces are an important part of Docker's isolation model. Namespaces exist for each type of resource, including networking, storage, processes, hostname control and others. |
| Operating System Virtualization | OS-level virtualization is an operating system paradigm in which the kernel allows the existence of multiple isolated user space instances, called containers, zones, virtual private servers, partitions, virtual environments, virtual kernels, or jails. |
| Private Registry | Restricts access to images so that only authorized users can view and use them. |
| REST API | A REST API (also known as RESTful API) is an application programming interface (API or web API) that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services. |
| Registry | is a hosted service containing repositories of images which responds to the Registry API. |
| Repository | is a set of Docker images. A repository can be shared by pushing it to a registry server. The different images in the repository can be labelled using tags. |
| Server Virtualization | Server virtualization is the process of dividing a physical server into multiple unique and isolated virtual servers by means of a software application. Each virtual server can run its own operating systems independently. |
| Serverless | is a cloud-native development model that allows developers to build and run applications without having to manage servers. |
| Tag | A tag is a label applied to a Docker image in a repository. Tags are how various images in a repository are distinguished from each other. |

---
