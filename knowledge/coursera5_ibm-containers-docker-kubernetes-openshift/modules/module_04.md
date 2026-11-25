# Module 4: The Kubernetes Ecosystem: OpenShift, Istio, etc.

### 1. [VIDEO TRANSCRIPT] Introduction to Red Hat OpenShift Video • 7 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/vJTaB/introduction-to-red-hat-openshift
- **Method:** `dom_transcript` | **Length:** 6816 chars

Welcome to introduction to Red Hat OpenShift. After watching this video, you will be able to explain what OpenShift is and list its features, describe OpenShift CLI, architecture, and components, and compare OpenShift with Kubernetes. OpenShift, developed and supported by Red Hat, is an enterprise-ready Kubernetes container platform built for the hybrid Cloud strategy. It provides a consistent application platform to manage hybrid, multi-Cloud, and edge deployments. It is built on the technological foundation of Linux, containers, and automation. It provides full stack automated operations and self-service provisioning for developers to efficiently move ideas from development to production. Besides container orchestration, it provides additional tooling around the complete life cycle of applications.

From build, to CI/CD, to monitoring, and logs. Both Kubernetes and OpenShift are container orchestration platforms. Kubernetes is a critical component of OpenShift. OpenShift is used as an extension of Kubernetes to provide a more robust and comprehensive platform for containerized applications. Let's review the features of OpenShift. Apps can scale to thousands of instances across hundreds of nodes in seconds. Flexible hybrid infrastructure options simplify deployment and management.

Open source standards use Kubernetes and Open Container Initiative, OCI containers, which means development is familiar and containers are portable across multiple environments. It includes a comprehensive set of developer tools, multi-language support, command line, IDE integrations, and more. It supports over air platform upgrades, and services from the operator hub can be fully configured and deployed with one click upgrades. Container and app builds, deployments, scaling, and health management are streamlined and automated. OpenShift also enhances support for smaller footprint topologies in edge scenarios for better mapping, connectivity, and availability. It easily manages and enforces policies across multiple clusters at scale. It offers access controls, networking and enterprise registry, built in scanner, enhanced threat detection, life cycle vulnerability management, and risk profiling.

OpenShift supports enterprise persistent storage solutions for running stateful and stateless apps. The OpenShift partner ecosystem provides additional storage and network services, as well as IDE, CI, integrations, and more. Let's compare the main aspects between OpenShift and Kubernetes. OpenShift is a product, while Kubernetes is an open source project. Installation on OpenShift has limited options after the installation starts, while Kubernetes is installable on every Linux environment. OpenShift is less flexible, while Kubernetes is more flexible. OpenShift is available online with Azure and dedicated, while Kubernetes is available on EKS, on AWS, GKE, on GCP, and AKS on Azure.

OpenShift image streams provide better management, while Kubernetes container image management is not that easy. OpenShift has a very strict security policy, while Kubernetes security maintenance is easy. OpenShift router objects permit external access, while Kubernetes ingress objects permit external access to Kubernetes clusters. OpenShift uses the less flexible deployment config command, while Kubernetes uses more flexible deployment objects. OpenShift provides a good user experience, while Kubernetes requires extra tools for a better user experience. OpenShift provides good networking solutions out of the box, while Kubernetes provides third party plugins when network solutions are unavailable. OpenShift provides a good service catalog, while Kubernetes offers less provision for better services in clusters.

OpenShift has a user friendly web console layout that is easy to learn for beginners, while Kubernetes console layout is difficult to learn for beginners. The OpenShift CI and CD integrate with Jenkins, while the Kubernetes CI and CD can be integrated, but not with Jenkins. OpenShift runs on top of a Kubernetes cluster, with object data stored in the etcd key-value store. It has a microservices-based architecture. Its services are REST APIs, which expose the core objects, and controllers, which read the REST APIs, apply changes to the other objects, and report status or write back to the object. They also maintain the cluster desired state. Docker provides abstraction for packaging and creating Linux-based lightweight container images.

Kubernetes provides cluster management and orchestrates containers on multiple hosts. OpenShift features add management of source code, builds, and deployments for developers, managing and promoting images at scale as they flow through your system, application management at scale, team and user tracking management of a large developer organization, and networking infrastructure that supports the cluster. In an OpenShift environment, the Kubernetes master runs on Red Hat Enterprise Linux CoreOS, while worker nodes support Red Hat Enterprise Linux. That is the Red Hat base layer. Next is the Kubernetes architecture and a set of services. Cluster services include integrated monitoring, a private registry within the cluster, networking solutions, and many others. Platform services help users manage their workloads.

Application services help users build Cloud native apps. Developer services increase developer productivity. OpenShift offers a set of command line interface or CLI tools that lets users perform various admin and development operations from the terminal. OpenShift CLI or OC is the most commonly used CLI tool to perform end-to-end operations. It runs on Windows, Linux, or Mac. OC lets you work directly with project source code using command script, script OpenShift operations, and manage projects during restricted bandwidth or availability of the web console. Since OpenShift runs on top of a Kubernetes cluster, a copy of kubectl is also included with OC.

The OC and kubectl binary offer the same capabilities, but OC is further extended to natively support OpenShift features, such as deployment configs, build configs, routes, image streams, and image stream tags. These are not available in standard Kubernetes. OC also offers an inbuilt login command for authentication. Additional commands like new app are also supported by OC, which makes it easier to get new applications started using existing source code or pre-built images. In this video, you learn that Kubernetes and OpenShift are container orchestration platforms, OpenShift is an enterprise-ready Kubernetes container platform built for open hybrid Cloud, OpenShift runs on a Kubernetes cluster, with object data stored in the etcd key-value store, and OpenShift is easier to use, integrates with Jenkins, and has more services and features.

---

### 2. [VIDEO TRANSCRIPT] Builds Video • 7 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/n1fgh/builds
- **Method:** `dom_transcript` | **Length:** 6036 chars

Welcome to Builds. After watching this video, you will be able describe what a build is, build input sources and build strategy. Describe what image streams do and identify their features. Explain how to automate builds using build triggers. List the steps used for the build config process and explain source to image docker and custom build strategies. A build is the process of transforming inputs into a resultant object, for example, transforming source code to a container image. A build requires a build configuration file or build config, which defines the build strategy and input sources.

Commonly used build strategies are source-to-image, or S2I, Docker, and custom. A build input source provides content for builds. You can use the following build inputs listed in order of precedence, inline Dockerfile definitions, content extracted from existing images, Git repositories, binary or local inputs, input secrets, and external artifacts. Note that multiple inputs can be combined into a single build, and an inline Dockerfile takes precedence and overwrites any external Dockerfile. An image stream is an abstraction for referencing container images within OpenShift. An image stream continuously creates and updates container images, but does not contain actual image data. Instead, it points to images stored in internal and external registries or to other image streams.

A single image stream can consist of many different tags, such as latest dev and test, and each tag points to a certain image in a registry. To deploy an application, you'll refer to the image stream tag rather than hardcode the registry URL and tag. If the source image location changes, you'll update the image stream definition rather than individually updating all the deployments. An image stream also provides a trigger capability that automatically invokes builds and deployments when a new version of an image is available. Rather than running builds manually automate the process using triggers. Webhook triggers send a request to an API endpoint, and they also support generic webhooks and the more often used GitHub webhooks, which send the trigger request to the API endpoint on any new commit or a pull request or other circumstances. Next is the image change trigger, which triggers builds when a new version of an image is available.

For instance, if you build your application using a node JS base image, that image is updated when security fixes are released and other updates occur. Finally, a configuration change trigger causes a new build to run when you create a new build config resource. Let's look at a sample configuration file for BuildConfig. The specification creates a new build config named Ruby Sample build. The run policy field controls how builds created from a build configuration need to run values include the default, serial, or sequentially and simultaneously. You can also specify a list of triggers that creates a new build. The source section defines the build's source, and the source type determines the primary input, like a git repository, an inline Dockerfile, or binary payloads.

The strategy section shows which strategy was used to execute the build, such as source, docker, or custom strategy. This example uses the ruby-20-centos7 container image and source-to-image, or S2I, strategy for the application build. So after you build the container image, it is pushed into the repository described in the output section, and the postCommit section defines an optional build hook. Another build strategy offered by OpenShift is called source-to-image, or S2I. The S2I tool builds reproducible container images and injects a container image with the app source to produce a ready to run image. The new image is built by incorporating a builder image plus the source that avoids using a Dockerfile, which enables going from source-to-image in a single step. Openshift comes with a variety of available builder images, saving you time and development effort.

Using a Docker build strategy requires a repository that contains a Dockerfile and the necessary artifacts. When you kick off a build, Openshift takes the input, invokes the Docker build command, and creates an image, which is then pushed to the internal OpenShift registry. Here are four ways to implement the Docker build strategy. Replace Dockerfile from image, use Dockerfile path, use Docker environment variables, or add Docker build arguments. In a custom build strategy, you must define and create your own builder image required for the build process. Custom builder images are regular docker images that contain the logic needed to transform the inputs into the expected outputs. Both Docker and S2I strategies result in runnable images, but the custom build strategy creates additional objects like JAR files and CI/CD deployment that performs unit or integration tests.

Custom builds are only available to cluster administrators because they run with high privileges. Cloud-native development requires greater automation throughout the container lifecycle. Automation is available using the continuous integration and continuous delivery pipeline, or CI/CD. For example, the OpenShift CI/CD process automatically merges new code requests to the repository, then builds, tests, approves, and deploys a new version to different environments. In this video, you learned that a build is a process that transforms inputs into an object. Build inputs in order of precedence include inline Dockerfile definitions, content extracted from existing images, git repositories, binary or local inputs, input secrets, and external artifacts. An image stream is an abstraction for referencing container images within Openshift.

You can automate builds using a webhook, image change, or configuration change trigger. Commonly used build strategies include source-to-image, or S2I, Docker, and custom build strategies. And finally, builds require a build configuration file or build config, which defines the build strategy and input sources.

---

### 3. [VIDEO TRANSCRIPT] Operators Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/KCgf3/operators
- **Method:** `dom_transcript` | **Length:** 5439 chars

Welcome to Operators. After watching this video, you will be able to Define an operator and explain its purpose Show the relation between custom controllers, the operator pattern, and custom resource definitions, or CRDs and explain the purpose of the operator hub, framework, and maturity model. Operators automate cluster tasks and act as a custom controller to extend the Kubernetes API. Operators run in a pod and interact with the API server, package, deploy, and manage Kubernetes applications, and automate app creation, configuration, and management via continuous real-time decisions. Operators package, deploy, and manage native apps in Kubernetes, automate other tasks, and ensure all relevant components are included. There are human operators and software operators. Human operators understand the system they control.

They know how to deploy services and how to recognize and fix problems. Software operators try to capture the knowledge of human operators and automate the same processes. Operators provide ease of repeatable installation and upgrade processes, regular full system health checks of each component in the system, over-the-air or OTA updates for components and software vendors' content, a way to collect and spread knowledge from field engineers to all users, and integration with APIs and CLI tools such as kubectl and OC commands. Let's see how service brokers compare with operators. Service brokers provide a short-running process that cannot perform the consecutive day's operations, such as upgrades, failover, or scaling, customizations and parameterization only at the time of installation, and off-cluster services. Operators provide a long-running process that can perform operations like upgrades, failover, or scaling every day, customizations and parameterizations as operators constantly watch the current state of your cluster, and off-cluster services. Custom Resource Definitions, or CRDs, store and retrieve objects in the Kubernetes API.

CRDs extend Kubernetes functionality beyond built-in resources like deployments and pods. They make the Kubernetes API more modular and flexible. Users can install CRDs in clusters, but each CRD is available only in the cluster it is installed. And once installed, CRD objects are accessible using kubectl, similar to pods and other resources. To change the state of a cluster, custom controllers are used. Controllers reconcile a cluster's actual state with its configured state. Custom controllers do the same reconciling for custom resources.

Combining CRDs and custom controllers creates a declarative API. This combination is known as the operator pattern. Custom controllers interpret CRD data as the desired state and reconcile a cluster's actual state to match the CRD data. The Operate Framework is an open-source toolset that covers coding, testing, delivery, and operator updates. The Operator SDK, which includes Helm, Go, and Ansible, helps authors build, test, and package their operators without requiring knowledge of Kubernetes API complexities. The Operator Lifecycle Manager, or OLM, controls the install, upgrade, and role-based access control, or RBAC, of operators in a cluster. The Operator Registry stores CRDs, Cluster Service Versions, or CSVs, and operator metadata for packages and channels.

It runs in Kubernetes or OpenShift clusters to provide the operator catalog data to OLM. The Operator Hub web console lets cluster administrators find operators to install on their cluster. The sophistication of operator management logic varies depending on the type of service represented by the operator. This operator maturity model defines the phases of maturity for general day-to-operation activities and ranges from basic install to autopilot. It also shows which activities are supported by the Helm, Go, and Ansible capabilities of the Operator SDK. Some operator examples include deploying an application to the OpenShift cluster. This can go beyond deployments to include secrets, config maps, and storage resources, scaling the application with the help of multiple replicas based on the application type, automation of rote tasks in a cluster, like taking and restoring backups of an application state, and integration.

Let's consider more about the first example. To deploy a whole application, create a custom resource for that app, and then a custom controller for that CRD. The operator logic determines how to reconcile the actual and configured states. A CRD requires the creation of deployments, services, storage, and other objects. The Operator Hub view of the OpenShift web console enables operator installation with one click. Operator Hub has many different types of operators available, including Red Hat operators, certified operators from independent service vendors partnered with Red Hat, community operators from the open source community but not officially supported by Red Hat, and custom operators defined by users. You can install many tools from the Kubernetes ecosystem via the Operator Hub.

An example is the Istio Service Mesh. In this video, you learn that CRDs extend the Kubernetes API. CRDs paired with custom controllers create new declarative APIs in Kubernetes. Operators use CRDs and custom controllers to automate cluster tasks. The Operator Framework covers coding, testing, delivery, and updates. And the Operator Maturity Model defines the phases of maturity for activities.

---

### 4. [VIDEO TRANSCRIPT] Istio Video • 7 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/7fFum/istio
- **Method:** `dom_transcript` | **Length:** 6706 chars

Welcome to Istio. After watching this video, you will be able to Describe a service mesh Identify the four concepts that Istio supports Describe the benefits and challenges of using Istio with microservices and Identify the four basic communication service monitoring metrics A service mesh is a dedicated layer for making service-to-service communication secure and reliable. Among other things, service meshes provide traffic management to control the flow of traffic between services, security to encrypt traffic between services, and observability of service behavior to troubleshoot and optimize applications. The service mesh term describes a software that creates a security or network domain with a pattern for achieving the above capabilities. Istio is a platform-independent service mesh often used on Kubernetes. In keeping with the definition of a service mesh, Istio exhibits these four concepts. First, there's Connection.

Connection enables Istio to intelligently control the traffic between services in Canary deployments, A-B tests, and other deployment models. Next is Security. Istio secures services through authentication, authorization, and encryption. Istio also provides enforceability and provides control by enforcing policies across an entire fleet. And finally, Istio supports observability. Using Istio, you can observe the traffic flow in your mesh, trace call flows and dependencies, and view metrics such as latency and errors. Istio features transport-layer security-encrypted communications between services in a cluster, combined with the appropriate authentication and authorization.

Istio load balances traffic for different protocols, including HTTP, TCP, gRPC, and WebSocket traffic. Istio supports granular configuration of traffic flow, known as routing rules, and supports control with continuous retries, fault injection methods, and automatic failovers. Along with policies and API support for access controls, rate limits, and quotas, Istio also provides automatic monitoring, logging, and tracking of both inbound and outbound traffic. Istio is extensible and can handle a diverse range of deployment needs. Istio runs on Kubernetes, where you can add applications of a cluster to the mesh, extend the mesh to additional clusters, or connect to virtual machines or other endpoints running outside of Kubernetes. Next, let's check out how Istio works with microservices. There are two main components in Istio, the control plane and the data plane.

Communication between services is handled by the data plane. If a service mesh is absent, the network cannot identify the type of traffic that flows, the source, or the destination, and cannot make necessary decisions. All network traffic is subject to, or intercepted by, a proxy called Envoy, which is used by the service mesh and allows many features depending on the configuration. The control plane takes the desired configuration and its view of the services and dynamically programs and updates the proxy servers as the environment changes. A cornerstone of cloud-native development is microservices architecture. Microservices are a cloud-native architectural approach in which a single application contains many loosely coupled and independently deployable smaller components or services. Microservices have well-defined APIs for communicating with each other.

The benefits of microservices are multiple. Code updates are easy, as only the relevant service needs to be updated instead of the entire application. They allow teams to use different technology stacks for each component. In addition, components can be scaled independently instead of the entire application. Challenges of microservices include encryption of traffic to ensure secure communication. Development teams might want to roll out new features to a subset of users or compare two versions of features in their application to see which engages users the most. In these cases, teams need canary deployments and A-B testing.

But communication between microservices also leads to cascading failures if one service is unreachable or particularly slow. Developers need retries and circuit-breaking to prevent errors in one microservice from cascading to others. Consider the application architecture shown on the screen, in which the UI talks to an ordering microservice. The ordering microservice interacts with the inventory microservice, which then talks to a database. Service-to-service communication enables any microservice architecture, but as that communication gets more complex, a service mesh can help improve it. Let's check out some more of Istio's capabilities. Istio performs traffic shifting by gradually migrating the traffic from one version of a microservice to other versions.

So, say a team working on the ordering microservice has a new update to that microservice. The team begins by sending 5% of traffic to that second version. And over time, the team can increase this to 50% and eventually to 100%. Similarly, Istio request routing allows you to perform A-B testing and direct a particular version of a microservice to a subset of users while sending the original version to the remaining users. The process ensures that a new version increases user engagement or performance. Istio also provides a variety of security measures for your microservices, including encryption. Istio defends from man-in-the-middle attacks by encrypting traffic between microservices.

In addition, Istio makes it easier to implement policies for service access control so that services can only talk to the other required services. In this example, the UI service would be unable to directly communicate with the inventory service, even if it tried. Among other metrics, Istio provides service communication metrics. These metrics cover the four basic service monitoring needs – latency, traffic, errors, and saturation. For example, Istio provides metrics on request counts so that you can see how much traffic your requests are receiving and request duration, shown here in seconds, so that you can find bottlenecks and ensure that there are prompt responses. In this video, you learn that a service mesh provides traffic management to control the flow of traffic between services, security to encrypt traffic between services, and observability of service behavior to troubleshoot and optimize applications. Istio supports the four concepts of connection, security, enforcement, and observability.

One of the examples where Istio is commonly used is with microservices applications. And, Istio provides service communication metrics for basic service monitoring needs, including latency, traffic, errors, and saturation.

---

### 5. [READING] Automating Builds with Build Triggers in OpenShift Reading • 15 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/kHuX0/automating-builds-with-build-triggers-in-openshift
- **Method:** `dom_reading_cml` | **Length:** 6458 chars

### Objectives

After completing this reading, you will be able to:

- Understand the concept and importance of build triggers in OpenShift.
- Identify and describe the different types of build triggers available in OpenShift.
- Explain how webhook triggers work and their key features.
- Describe the process and benefits of image change triggers.
- Understand the functionality and advantages of configuration change triggers.

#### Introduction to Build Triggers

In OpenShift, build triggers are essential for automating the build process, ensuring that applications are continuously updated and built efficiently. This reading will explore the different types of build triggers available in OpenShift, explaining each trigger in detail and how they contribute to a streamlined build process.

#### Understanding Build Triggers

Build triggers in OpenShift are mechanisms that automatically initiate a build process based on specific events or conditions. By using these triggers, developers can automate and simplify the process of updating and deploying applications, leading to faster development cycles and reduced manual intervention.

#### Types of Build Triggers

OpenShift offers several types of build triggers, each designed to respond to different events or changes in your environment. The main types of build triggers are:

- Webhook Triggers
- Image Change Triggers
- Configuration Change Triggers

### Let's delve into each type in detail:

#### 1. Webhook Triggers

Webhook triggers are a powerful feature that allows builds to be initiated via HTTP requests. These triggers are commonly used to integrate with external systems, such as GitHub, to automate builds based on specific repository events.

#### How Webhook Triggers Work

When a webhook trigger is configured, it sets up an endpoint in OpenShift that listens for HTTP POST requests. For instance, GitHub can be configured to send a request to this endpoint whenever a new commit is pushed to a repository, a pull request is merged, or other specified events occur. This request triggers the build process in OpenShift, ensuring that the latest code changes are automatically built and deployed.

#### Key Features

- Integration with Git Repositories: Supports triggers from popular repositories like GitHub, GitLab, and Bitbucket.
- Event-Driven: Initiates builds based on various events such as commits, merges, or tag creations.
- Flexibility: Supports both generic and GitHub-specific webhooks, making it versatile for different use cases.

#### Example Workflow

Below is a basic workflow diagram illustrating how a GitHub webhook trigger operates:

Workflow Explanation:

- A developer pushes new code to the GitHub repository.
- GitHub sends a POST request to the OpenShift webhook endpoint.
- The webhook triggers a new build in OpenShift.
- OpenShift builds the application and updates the deployment.

#### 2. Image Change Triggers

Image change triggers automatically initiate builds when a new version of a container image becomes available. This type of trigger is particularly useful for maintaining up-to-date applications with the latest dependencies or security patches.

#### How Image Change Triggers Work

When an image change trigger is set up, it monitors a specified container image for updates. For example, if your application relies on a Node.js base image, an image change trigger can be configured to detect updates to this base image. When a new version of the image is available, the trigger initiates a build process to incorporate the updated image into your application.

#### Key Features

- Automated Dependency Management: Ensures that applications are automatically rebuilt with the latest base images or libraries.
- Security and Maintenance: Helps in quickly responding to security vulnerabilities by initiating builds with updated base images.
- Continuous Updates: Keeps applications up-to-date with the latest changes in dependent images.

#### Example Workflow

Here is a simple workflow diagram illustrating how an image change trigger functions:

Workflow Explanation:

- A new version of the base image (e.g., Node.js) is pushed to the image registry.
- The image change trigger detects the update.
- OpenShift initiates a new build process using the updated base image.
- The application is rebuilt and redeployed with the latest image.

#### 3. Configuration Change Triggers

Configuration change triggers initiate builds when a new BuildConfig resource is created or an existing one is modified. These triggers allows builds to automatically reflect changes in the build configuration, such as updates to source code repositories or changes in build strategies.

#### How Configuration Change Triggers Work

Configuration change triggers monitor the BuildConfig resources in OpenShift. Whenever a new BuildConfig is created or an existing one is updated, the trigger automatically starts a new build. The triggers ensure that any changes in the build configuration are immediately applied to the application, keeping it in sync with the latest configuration settings.

#### Key Features

- Automatic Build Updates: Ensures builds reflect the latest configuration changes without manual intervention.
- Simplified Configuration Management: Helps in managing and applying build configurations efficiently.
- Flexibility: Allows for a wide range of configuration changes to trigger builds, such as updates to source repositories, build strategies, or output settings.

#### Example Workflow

Below is a basic workflow diagram showing how a configuration change trigger operates:

Workflow Explanation:

- A new BuildConfig resource is created or an existing one is updated.
- The configuration change trigger detects the change.
- OpenShift initiates a new build process based on the updated BuildConfig.
- The application is rebuilt and redeployed with the new configuration.

#### Conclusion

Build triggers in OpenShift provide a robust mechanism for automating the build and deployment process. By using webhook, image change, and configuration change triggers, you can ensure that your applications are continuously built and updated based on the latest changes and events. This automation leads to more efficient development cycles, quicker response times to updates or issues, and reduced manual overhead. Thus, ultimately contributing to a more streamlined and reliable development workflow.

#### Author:

Rajashree Patil

---

### 6. [READING] Summary & Highlights: The Kubernetes Ecosystem: OpenShift, Istio, etc. Reading • 3 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/9qohh/summary-highlights-the-kubernetes-ecosystem-openshift-istio-etc
- **Method:** `dom_reading_cml` | **Length:** 1131 chars

Congratulations! You have completed this module. At this point, you know:

- OpenShift® is an enterprise-ready Kubernetes container platform built for open hybrid cloud.
- OpenShift is easier to use, integrates with Jenkins, and has more services and features.
- Custom resource definitions (CRDs) extend the Kubernetes API.
- CRDs paired with custom controllers create new, declarative APIs in Kubernetes.
- Operators use CRDs and custom controllers to automate cluster tasks.
- A build is a process that transforms inputs into an object.
- An ImageStream is an abstraction for referencing container images in OpenShift.
- A service mesh provides traffic management to control the flow of traffic between services, security to encrypt traffic between services, and observability of service behavior to troubleshoot and optimize applications.
- Istio is a service mesh that supports four concepts of connection, security, enforcement, and observability. It is commonly used with Microservices applications.
- Istio provides service communication metrics for basic service monitoring needs: latency, traffic, errors, and saturation.

---

### 7. [READING] Module 4 Cheat Sheet: OpenShift CLI Reading • 1 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/Fsg6H/module-4-cheat-sheet-openshift-cli
- **Method:** `dom_reading_cml` | **Length:** 169 chars

| Command | Description |
| --- | --- |
| oc get | Displays a resource. |
| oc project | Switches to a different project. |
| oc version | Displays version information |

---

### 8. [READING] Module 4 Glossary: OpenShift Basics Reading • 15 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/n35f8/module-4-glossary-openshift-basics
- **Method:** `dom_reading_cml` | **Length:** 7999 chars

| Term | Definition |
| --- | --- |
| A/B testing | Strategy is mostly used for testing new features in front-end applications. It is used to evaluate two versions of the application namely A and B, to assess which one performs better in a controlled environment. The two versions of the applications differ in terms of features and cater to different sets of users. Based on the interaction and responses received from the users such as feedback, you can choose one of the versions of the application that can be deployed globally into production. |
| Build | The process of transforming inputs into a resultant object. |
| BuildConfig | An OpenShift-specific object that defines the process for a build to follow. The build process makes use of the input sources and the build strategy. The BuildConfig is the blueprint, and the build is an instance of that blueprint. |
| Canary Deployments | Aims to deploy the new version of the application by gradually increasing the number of users. The canary deployment strategy uses the real users to test the new version of the application. As a result, bugs and issues can be detected and fixed before the new version of the application is deployed globally for all the users. |
| Circuit breaking | A method to prevent errors in one microservice from cascading to other microservices. |
| Configuration Change | A trigger that causes a new build to run when a new BuildConfig resource is created. |
| Control Plane | The control plane takes the desired configuration and its view of the services and dynamically programs and updates the proxy servers as the environment changes. |
| Custom build strategy | Requires you to define and create your own builder image. |
| Custom builder images | Are regular Docker images that contain the logic needed to transform the inputs into the expected output. |
| CRDs | Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server. |
| Custom controllers | Reconcile the custom resources (CRDs) actual state with its desired state. |
| Data plane | Communication between services is handled by the data plane. If a service mesh is absent, the network cannot identify the type of traffic that flows, the source, and the destination and make any necessary decisions. |
| Enforceability (Control) | Istio provides control by enforcing policies across an entire fleet and ensures resources are fairly distributed among consumers. |
| Envoy proxy | All network traffic is subject to or intercepted by a proxy, called Envoy, used by the service mesh and allows many features depending on the configuration. |
| Human operators | Understand the systems they control. They know how to deploy services and how to recognize and fix problems. |
| Image Change | A trigger to rebuild a containerized application when a new or updated version of an image is available. For example, if an application is built using a Node.js base image, that image will be updated as security fixes are released and other updates occur. |
| ImageStream | An abstraction for referencing container images within OpenShift. Each image contains an ID, or digest, that identifies it. ImageStreams do not contain image data but rather are pointers to image digests. |
| ImageStream Tag | An identity to the pointer in an ImageStream that points to a certain image in a registry. |
| Istio | A platform-independent and popular service mesh platform, often used with Kubernetes. It intelligently controls the flow of traffic and API calls between services, conducts a range of tests and reduces the complexity of managing network services. Istio secures services through authentication, authorization, and encryption. Istio provides control by defining policies that can be enforced across an entire fleet. With Istio, you can observe traffic flow in your mesh so you can trace call flows, dependencies, and you can view service communication metrics such as latency, traffic, errors and saturation. |
| Man-in-the-middle attacks | A man-in-the-middle (MiTM) attack is a type of cyber-attack where the attacker secretly intercepts and relays messages between two parties who believe they are communicating directly with each other. The attack is a type of eavesdropping in which the attacker intercepts and then controls the entire conversation. |
| Observability | Helps to observe the traffic flow in your mesh, trace call flows and dependencies, and view metrics such as latency and errors. |
| OpenShift | A hybrid cloud, enterprise Kubernetes application. |
| OpenShift CI/CD process | Automatically merges new code changes to the repository, builds, tests, approves, and deploys a new version to different environments. |
| Operators | Automate cluster tasks and act as a custom controller to extend the Kubernetes API. |
| Operator Framework | Is a family of tools and capabilities to deliver an efficient customer experience. It is not just about writing code; what is also critical is testing, delivery, and updating Operators. |
| OperatorHub | Web console lets cluster administrators find Operators to install on their cluster. It provides many different types of Operators available, including Red Hat Operators, Certified Operators from independent service vendors partnered with Red Hat, Community Operators from the open-source community but not officially supported by Red Hat, and custom Operators defined by users. |
| Operator Lifecycle Manager | (or OLM) Controls the install, upgrade, and role-based access control (or RBAC) of Operators in a cluster. |
| Operator maturity model | Defines the phases of maturity for general day two Operations activities and ranges from Basic Install to Auto Pilot. |
| Operator Pattern | A system design that links a Controller to one or more custom resources. |
| Operator Registry | Stores CRDs, cluster service versions (CSVs), and Operator metadata for packages and channels. It runs in Kubernetes or OpenShift clusters to provide the Operator catalog data to OLM. |
| Operator SDK | (which includes Helm, Go, and Ansible) Helps authors build, test, and package their Operators without requiring knowledge of Kubernetes API complexities. |
| postCommit | Section defines an optional build hook. |
| Retries | A mechanism used in microservices to automatically reattempt a failed request to another service. |
| runPolicy | Field controls how builds created from a build configuration need to run. Values include the default Serial (sequentially) and simultaneously. |
| Service Broker | Provides a short-running process that cannot perform the consecutive day’s operations such as upgrades, failover, or scaling. |
| Service Mesh | A dedicated layer for making service-to-service communication secure and reliable. It provides traffic management to control the flow of traffic between services, security to encrypt traffic between services, and observability of service behavior; so, you can troubleshoot and optimize applications. |
| Software operators | Try to capture the knowledge of human operators and automate the same processes. |
| Source-to-Image | A tool for building reproducible container images. Also abbreviated S2i, it injects application source code into a container image to produce a ready-to-run image. |
| Source strategy | Section shows the strategy used to execute the build, such as a Source, Docker, or Custom strategy. |
| Source type | Determines the primary input like a Git repository, an inline Dockerfile, or binary payloads. |
| Webhook | A trigger that sends a request to an OpenShift Container Platform API endpoint. Often this will be a GitHub webhook, though it can also be a generic webhook. If a GitHub webhook is utilized, GitHub can send the request to OpenShift when there is a new commit on a certain branch, or a pull request is merged, or under many more circumstances. Webhooks are a great way to automate development flows so that builds can occur automatically as new code is developed. |

---
