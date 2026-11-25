# Module 2: Kubernetes Basics

### 1. [VIDEO TRANSCRIPT] Container Orchestration Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/PIyHG/container-orchestration
- **Method:** `dom_transcript` | **Length:** 5959 chars

Welcome to container orchestration. After watching this video, you will be able to define the challenges of container management, determine when container orchestration is needed, and demonstrate container orchestration benefits. Everyone's container journey starts with one container. However, things don't stay this way for long. Over time, new applications are written and projects are deployed globally to increase availability. That one initial container inevitably becomes several containers. Initially, that growth is easy to handle, but soon it's overwhelming.

Consider connecting, managing, and scaling hundreds or thousands of containers into a large application like a database or web app. This can easily get out of control. To create scale and manage large numbers of containers, container orchestration is needed. Container orchestration is a process that automates the container life cycle of a container based or containerized application. This includes deployment, management, scaling, networking, and availability. Container orchestration is necessary in large dynamic environments, since it streamlines complexity, enables hands-off deployment and scaling, increases speed, agility, and efficiency. Seamlessly integrates into CI/CD workflows, and DevOp practices, and allows development teams to use resources more efficiently.

Container orchestration can be implemented on premises and on public, private, or multi cloud environments. It is often a critical part of an organization security, orchestration, automation, and response requirements, also known as SOAR requirements. Container orchestration tools have a wide variety of features. These features include defining which container images make up the application, and where they are located, in what registry, improving provisioning and deployment of containers for a more automated, unified, and smooth process, securing network connections between containers, ensuring availability and performance by relocating the containers to another host if an outage or shortage of system resources occurs. Scaling containers to meet demand and load balance requests, handling resource allocation and scheduling of containers to the underlying infrastructure, performing rolling updates and rollbacks, and conducting health checks to ensure applications are running or performing the necessary actions when checks fail. Container orchestration uses configuration files written in YAML or JSON. These files configure each container so it can find resources, establish a network, and store logs.

Container orchestration also automatically schedules the deployment of a new container to a cluster, and finds the right host based on predefined settings or restrictions. Additionally, container orchestration manages the container's life cycle based on specifications in the configuration file. This includes system parameters, like CPU and memory, and file parameters, like proximity and file metadata, and container orchestration supports scaling and enhances productivity through automation. Here are some well known container orchestration tools. Marathon is a framework for Apache Mesos, an open source cluster manager that was developed by the University of California at Berkeley. It allows you to scale container infrastructure by automating the bulk of management and monitoring tasks. HachiCorps Nomad is a free and open source cluster management and scheduling tool that supports docker and other stand alone, virtualized or containerized applications on all major operating systems across all infrastructure, whether on premises or in the Cloud.

This flexibility lets teams work with any type and level of workload. Docker Swarm automates the deployment of containerized applications, but was designed specifically to work with docker engine and other docker tools, making it a popular choice for teams already working in docker environments. Developed by Google and maintained by the Cloud Native Computing Foundation, CNCF, the open source platform Kubernetes is the defactor standard for container orchestration. Kubernetes automates a host of container management tasks, including deployment, storage provisioning, load balancing, and scaling, service discovery, and self-healing, the ability to restart, replace, or remove a failed container. With broad functionality and an expanding ecosystem of open source supporting tools, Kubernetes is widely supported by leading Cloud providers, many of whom now offer fully managed Kubernetes services. Container orchestration helps to meet business goals and increase profitability by using automation. The benefits of container orchestration for developers and administrators include increased productivity, removing the burden of individually installing and managing each container, which in turn reduces errors and frees development teams to focus on application improvement.

Faster deployments, iteratively releasing new features and capabilities faster and deploying containers and containerized applications rapidly. Reduced costs, being cost effective, service containers have lower overhead and use fewer resources than virtual machines or traditional servers. Stronger security, sharing resources and isolating application processes, improving the container's overall security, easier scalability, scaling applications using a single command and faster error recovery, maintaining high availability by detecting and resolving issues like infrastructure failures automatically. In this video, you learn that managing large numbers of containers is difficult. Container orchestration automates the container life cycle, resulting in faster deployments, reduced errors, higher availability, and stronger security. Popular container orchestration tools include Marathon, Nomad, Docker Swarm, and Kubernetes. Finally, container orchestration improves productivity, deployment, costs, security, scalability, and error recovery.

---

### 2. [VIDEO TRANSCRIPT] Introduction to Kubernetes Video • 7 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/eHlCb/introduction-to-kubernetes
- **Method:** `dom_transcript` | **Length:** 6094 chars

[MUSIC] Welcome to introduction to Kubernetes. After watching this video you will be able define Kubernetes, explain what Kubernetes is not, relate Kubernetes concepts, describe Kubernetes capabilities and describe the Kubernetes ecosystem. The official Kubernetes documentation describes Kubernetes as an open-source system for automating, deployment, scaling and management of containerized applications. Kubernetes is widely available and has positioned itself as the de facto choice for container orchestration. Kubernetes is an open-source containerization orchestration platform developed as a project by Google and is currently maintained by the Cloud Native Computing Foundation. It is easily portable across clouds and on premises. With its growing ecosystem of projects and products by both member and non-member partners, Kubernetes is recognized as the go to container orchestration solution.

Kubernetes as a service grew as an extension of containers as a service. Kubernetes facilitates declarative management in which it automatically performs the necessary operations towards achieving the called for state. Here's what Kubernetes is not, it is not a traditional all inclusive platform as a service. It is not rigid or opinionated, but more of a flexible model that supports an extremely diverse variety of workloads, including stateless, stateful and data processing workloads. It can work with all applications that can be containerized, it does not provide continuous integration continuous delivery pipelines to build applications or deploy source code, it does not prescribe logging, monitoring and alerting solutions. Organizations are free to select and integrate third party and open-source tools, and it does not provide built in middleware databases or other services. Let's check out some Kubernetes concepts.

Concepts of Kubernetes include the following, pods represent the smallest deployable compute object and the higher level abstractions to run workloads, services expose applications running on sets of pods. Each pod is assigned a unique IP address and sets of pods have a single DNS name. Kubernetes supports both persistent and temporary storage for pods. Configuration, which refers to the provisioning of resources for configuring pods. Security measures for cloud-native workloads, which enforce security for pod and API access. Policies for groups of resources, ensuring that pods match to nodes so that the kubelet can find them and run the pods. Scheduling and eviction that runs and proactively terminates one or more pods on resource starved Nodes.

Preemption, which is all about prioritization. Preemption terminates lower priority Pods so that pods with higher priority can schedule and run on Nodes. And finally, cluster administration provides the details necessary to create or administer a cluster. Kubernetes capabilities include, automated rollouts of changes to application or configuration. Health monitoring and rolling back changes, storage orchestration that mounts a chosen storage system including local storage, network storage or public cloud, and horizontal scaling of workloads based on metrics or via commands. Additional capabilities include the following, automated bin packing that increases utilization and cost saving using a mix of critical and best-effort workloads. Automated bin packing performs container auto placement based on resource requirements and conditions without sacrificing high availability.

Kubernetes includes secret and configuration management of sensitive information including passwords, OAuth tokens, and SSH keys, and handles deployments and updates to secrets and configuration without rebuilding images and Kubernetes assigns both IPv4 and IPv6 addresses to Pods and services. Kubernetes manages batch and continuous integration workloads and automatically replaces failed containers, it self heals failing or unresponsive containers. It discovers pods using IP addresses or a DNS name and load balances traffic for better performance and high availability, and Kubernetes adds features to your cluster without modifying source code. The Kubernetes ecosystem is a large, rapidly growing ecosystem where its services, support, and tools that are widely available. Running containerized applications require separate tools. In addition to the Kubernetes orchestration tool, the ecosystem includes services like building container images, storing images in a container registry, application logging and monitoring, and CI/CD capabilities. The Kubernetes ecosystem is a huge collection of products, services, and providers.

Leading public cloud providers include Prisma, IBM, Google, and AWS. Open source framework providers include Red Hat, VMware, SUS, Mesosphere, Docker, and Cloud Foundry. Management providers include Digital Ocean, loodse, SUPERGIANT, CloudSoft, turbonomic, Techtonic, and Weaverworks. Tool providers include JFrog, Univa, Aspen Mesh, Bitnami, and Cloud 66. Monitoring and logging providers include sumologic, DATADOG, New Relic, iguazio, Grafana SignalFX, sysdig, and Dynatrace. Security providers include GUARDCORE, BLACKDUCK, yubico, cilium, aqua, TwistLock, and Alcide and load balancing providers include AVI networks, VMware, and NGiNX. In this video you learned that Kubernetes is a highly portable, horizontally scalable open-source container orchestration system with automated deployment and simplified management capabilities.

Its concepts include Pods and workloads services, storage configuration, security policies, scheduling and eviction, preemption, and administration. You also learned that Kubernetes capabilities include automated rollouts and rollbacks, storage orchestration, horizontal scaling, automated bin packing, secret and configuration management. IPv4/IPv6 dual stack support, batch execution, self-healing, service discovery and load balancing and finally, designed for extensibility. And the Kubernetes ecosystem includes public cloud providers, frameworks, management, tools, monitoring and logging, security, and load balancing. [MUSIC]

---

### 3. [VIDEO TRANSCRIPT] Kubernetes Architecture Video • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/Y9KXn/kubernetes-architecture
- **Method:** `dom_transcript` | **Length:** 4956 chars

Welcome to Kubernetes Architecture. After watching this video, you will be able to Identify the components of a Kubernetes architecture Identify the components of a control plane and Identify the components of a worker plane This architecture diagram highlights the main components in a Kubernetes system. A deployment of Kubernetes is called a Kubernetes cluster. A Kubernetes cluster is a cluster of nodes that runs containerized applications. Each cluster has one master node, the Kubernetes control plane, and one or more worker nodes. The control plane maintains the intended cluster state by making decisions about the cluster and detecting and responding to events in the cluster. As an analogy, it is similar to a thermostat.

You specify the desired temperature, and the thermostat regulates heating and cooling systems continuously to achieve the specified state. An example of a decision made by the control plane is the scheduling of workloads. And an example of responding to an event is creating new resources when an application is deployed. Nodes are the worker machines in a Kubernetes cluster. In other words, user applications are run on nodes. Nodes are not created by Kubernetes itself, but rather by the cloud provider. This allows Kubernetes to run on a variety of infrastructures.

The nodes are then managed by the control plane. In the Kubernetes control plane, the Kubernetes API server exposes the Kubernetes API. The API server serves as the front end for the control plane. All communication in the cluster utilizes this API. For example, the Kubernetes API server accepts commands to view or change the state of the cluster. The main implementation of a Kubernetes API server is kube-api-server, which is designed to scale horizontally by kube-instances. You can run several instances of kube-api-server and balance traffic between those instances. etcd is a highly available, distributed key-value store that contains all the cluster data.

When you tell Kubernetes to deploy your application, that deployment configuration is stored in etcd. etcd defines the state in a Kubernetes cluster, and the system works to bring the actual state to match the desired state. The Kubernetes scheduler assigns newly created pods to nodes. This basically means that the kube-scheduler determines where your workloads should run within the cluster. The scheduler selects the most optimal node according to Kubernetes scheduling principles, configuration options, and available resources. The Kubernetes controller manager runs all the controller processes that monitor the cluster state, and ensure the actual state of a cluster matches the desired state. Finally, the cloud controller manager runs controllers that interact with the underlying cloud providers. These controllers effectively link clusters into a cloud provider's API.

Since Kubernetes is open source and would ideally be adopted by a variety of cloud providers and organizations, Kubernetes strive to be as cloud-agnostic as possible. The cloud controller manager allows both Kubernetes and the cloud providers to evolve freely without introducing dependencies on the other. Nodes are the worker machines in a Kubernetes cluster. In other words, user applications are run on nodes. Nodes can be virtual or physical machines. Each node is managed by the control plane and contain the services necessary to run applications. Nodes include pods, which are the smallest deployment entity in Kubernetes.

Pods include one or more containers. Containers share all the resources of the node and can communicate among themselves. The kubelet is the most important component of a worker node. This controller communicates with the kube API server to receive new and modified pod specifications and ensure that the pods and their associated containers are running as desired. The kubelet also reports to the control plane on the pod's health and status. And in order to start a pod, the kubelet uses the container's runtime. The container runtime is responsible for downloading images and running containers.

Rather than providing a single container runtime, Kubernetes implements a container runtime interface that permits pluggability of the container runtime. While Docker is likely the best known runtime, Podman and Creo are two other commonly used container runtimes. Lastly, the Kubernetes proxy is a network proxy that runs on each node in a cluster. This proxy maintains network rules that allow communication to pods running on nodes. In other words, communication to workloads running on your cluster. In this video, you learned that A control plane makes global decisions about the Kubernetes cluster. A control plane is made up of controllers, an API server, a scheduler, and an ETCD.

A worker plane is made up of nodes, kubelet, container runtime, and kube proxy. Worker nodes run important Kubernetes components as well as user workloads deployed on the cluster.

---

### 4. [VIDEO TRANSCRIPT] Kubernetes Objects - Part 1 Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/SSUpV/kubernetes-objects-part-1
- **Method:** `dom_transcript` | **Length:** 5734 chars

Welcome to Kubernetes Objects Part 1. After watching this video, you will be able to Define a Kubernetes object and its properties Describe basic Kubernetes objects and their features And Demonstrate how Kubernetes objects relate to each other In the real world, an object is something that has an identity, a state, and a behavior. A window or a shopping cart are examples of objects. A software object is a bundle of data that has an identity, a state, and a behavior. Examples include variables, data structures, and specific functions. Another term is entity, which also has an identity and associated data. For example, in banking, a customer account is an entity.

Finally, the term persistent means something will last even if there is a server failure or network attack. An example is persistent storage. Kubernetes objects are persistent entities. Examples include pods, namespaces, replica sets, deployments, and more. Kubernetes objects consist of two main fields, object spec and status. The object spec is provided by the user, which dictates an object's desired state. Status is provided by Kubernetes.

This describes the current state of the object. Kubernetes works towards matching the current state to the desired state. To work with these objects, use the Kubernetes API directly with the client libraries and the kubectl command-line interface or both. Labels are key-value pairs attached to objects. They are intended for identification of objects. However, a label does not uniquely identify a single object. Many objects can have the same labels, and this helps to organize and group objects.

Label selectors are the core grouping method in Kubernetes. They allow you to identify a set of objects. Namespaces provide a mechanism for isolating groups of resources within a single cluster. This is useful when teams share a cluster for cost-saving purposes or for maintaining multiple projects in isolation. Namespaces are ideal when the number of cluster users is large. Examples of namespaces are KubeSystem, intended for system users and the default namespace used to hold users' applications. There are different patterns of working with namespaces.

There may be only one namespace for a user who works with one team, which only has one project that is deployed into a cluster. Alternatively, there may be many teams or projects, or a lot of users with different needs, where additional namespaces may be created. Namespaces provide a scope for the names of objects. Each object must have a unique name for that resource type within that namespace. A pod is the simplest unit in Kubernetes. A pod represents a process or a single instance of an application running in the cluster. A pod usually wraps one or more containers, and creating replicas of a pod serves to scale an application horizontally.

YAML files are often used to define the object that you want to create. The YAML file shown defines a simple pod. The kind field specifies the kind of object to be created. In this case, we create a pod. The spec field provides the appropriate fields for the object to be created, such as the containers that will run in this pod. A pod spec must contain at least one container. In this example, the container is named nginx.

The image field dictates which image will run in the pod, and the ports array lists the ports that the container exposes. A replica set is a set of identical running replicas of a pod that are horizontally scaled. The configuration files for a replica set and a pod are different from each other. The replicas field specifies the number of replicas that should be running at any given time. Whenever this field is updated, the replica set creates or deletes pods to meet the desired number of replicas. A pod template is included in the replica set spec, which defines the pods that should be created by the replica set. Under the Selector field, the labels supplied in the Match Labels field specify the pods that can be acquired by the replica set.

Notice that the label identified in the Match Labels field is the same as the Labels field in the pod template. Both are the app nginx. Creating replica sets directly is not recommended. Instead, create a deployment, which is a higher-level concept that manages replica sets and offers more features and better control. A deployment is a higher-level object that provides updates for both pods and replica sets. Deployments run multiple replicas of an application using replica sets and offer additional management capabilities on top of these replica sets. Deployments are suitable for stateless applications.

For stateful applications, stateful sets are used. Examples of deployments include the deployment of a replicated application, pod updates managed by a deployment, or the scaling up of an application. This deployment specification example shows the kind is deployment, which defines the number of replicas, a selector to identify which pods can be acquired, and a pod template. One key feature provided by deployments but not replica sets is rolling updates. A rolling update scales up a new version to the appropriate number of replicas and scales down the old version to zero replicas. The replica set ensures that the appropriate number of pods exist, while the deployment orchestrates the rollout of a new version. In this video, you learned that Kubernetes objects are persistent entities.

Their main fields are object spec and status. Namespaces help in isolating groups of resources within a single cluster. Pods represent a process or an instance of an app running in the cluster. Replica sets create and manage horizontally scaled running pods, and deployments provide updates for pods and replica sets.

---

### 5. [VIDEO TRANSCRIPT] Kubernetes Objects - Part 2 Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/e6oIT/kubernetes-objects-part-2
- **Method:** `dom_transcript` | **Length:** 5924 chars

[MUSIC] Welcome to Kubernetes Objects, Part 2. After watching this video, you will be able to, describe the purposes, properties, and uses of a service, describe the roles and uses for the ClusterIP, NodePort, LoadBalancer, and External Name Services, and describe the roles and uses for Ingress, Daemonset, StatefulSet, and a Job. A service is a REST object, like Pods. Services are a logical abstraction for a set of Pods in a cluster. They provide policies for accessing the Pods in cluster and act as a load balancer across the Pods. Each service is assigned a unique IP address for accessing applications deployed on Pods, and a service eliminates the need for a separate service discovery process. A service supports multiple protocols such as TCP, which is the default protocol, UDP, and others, and supports multiple port definitions.

The port number with the same name can vary in each backend Pod. In addition, a service can have an optional selector and can optionally map incoming ports to a target port. Next, let's learn why a service is needed. A service is needed because Pods in a cluster can be destroyed and new Pods can be created at any time. This volatility leads to discoverability issues because of changing IP addresses. A service keeps track of Pod changes and exposes a single IP address or a DNS name, and utilizes selectors to target a set of Pods. For native Kubernetes applications, API endpoints are updated whenever changes are detected to the Pods in the service.

For non-native applications, Kubernetes uses a virtual- IP-based bridge or load balancer in between the applications and the backend Pods. There are 4 types of Cluster IP, NodePort, LoadBalancer, and External Name. Let's learn about each service type. Cluster IP is the default and most common service type. Kubernetes assigns a cluster internal IP address to the cluster IP service that makes the service only reachable within the cluster. A cluster IP service cannot make requests to service from outside the cluster. You can set the cluster IP address in the service definition file, and the cluster IP service provides inter service communication within the cluster, for example, communication between the front end and backend components of your app.

An extension of Cluster IP Service, a NodePort Service creates and routes the incoming requests automatically to the cluster IP service. A NodePort exposes the service on each node's IP address at a static port. Note that for security purposes, production use is not recommended. Kubernetes exposes a single service with no load balancing requirements for multiple services. An extension of the NodePort service, an external load balancer, or ELB, creates NodePort and Cluster IP services automatically. An ELB integrates and automatically directs traffic to the NodePort service. To expose a service to the Internet, you need a new ELB with an IP address.

You can use a cloud provider's ELB to host your cluster. The external name service type maps to a DNS name and not to any selector and requires a spec.externalName parameter. The external name service maps the service to the contents of the external name field that returns a CNAME record and its value. You can use an external name to create a service that represents external storage and enables Pods from different namespaces to talk to each other. Next, Ingress is an API object that, when combined with a controller, provides routing rules to manage external users access to multiple services in a Kubernetes cluster. In production, Ingress exposes applications to the Internet via port 80 for HTTP or port 443 for HTTPs. While the cluster monitors Ingress, an external load balancer is expensive and is managed outside the cluster.

A DaemonSet is an object that makes sure that nodes run a copy of a Pod. As nodes are added to a cluster, Pods are added to the nodes. Pods are garbage collected when removed from a cluster. If you delete a DaemonSet, all Pods are removed. DaemonSets are ideally used for storage, logs, and monitoring nodes. A StatefulSet is an object that manages stateful applications, manages deployment and scaling of Pods, and provides guarantees about the ordering and uniqueness of Pods. A StatefulSet maintains a sticky identity for each Pod request, and provides persistent storage volumes for your workloads.

And lastly, a Job creates Pods and tracks the Pod completion process. Jobs are retried until completed. Deleting a Job will remove the created Pods. Suspending a Job will delete its active Pods until the Job resumes. A Job can run several Pods in parallel and CronJobs are regularly used to create Jobs on an iterative schedule. In this video, you learn that, a service in Kubernetes is a REST object that provides policies for accessing the Pods and cluster. Cluster IP is the default and most common service type and provides inter service communication within the cluster.

An extension of Cluster IP Service, a NodePort Service creates and routes the incoming requests automatically to the Cluster IP Service. An extension of the NodePort Service, an External Load Balancer creates NodePort and Cluster IP Services automatically. An Ingress is an API object that, when combined with a controller, provides routing rules to manage external users' access to multiple services in a Kubernetes cluster. You also learned that using a DaemonSet ensures that there is at least one instance of the Pod on all your nodes. You can use External Name to create a Service that represents external storage and enables Pods from different namespaces to talk to each other. A StatefulSet manages stateful applications, manages Pod deployment and scaling, maintains a sticky identity for each Pod request, and provides persistent storage volumes for your workloads. And finally, a Job creates Pods and tracks the Pod completion process.

Jobs are retried until completed. [MUSIC]

---

### 6. [VIDEO TRANSCRIPT] Using Kubectl Video • 7 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/tcNh4/using-kubectl
- **Method:** `dom_transcript` | **Length:** 6176 chars

[MUSIC] Welcome to using Kubectl. After watching this video you will be able define Kubectl and the command structure. List the three command types, their features and advantages, and list commonly used commands with specific examples. Kubectl is the Kubernetes command line interface or CLI. Kubectl stands for kube command tool line. Kubectl is one of the key tools for working with Kubernetes, and it helps users deploy applications, inspect and manage cluster resources, view logs, and more. It provides many features for users who work with Kubernetes clusters and manage running cluster workloads. And three Kubectl command types are imperative commands, imperative object configuration and declarative object configuration Kubectl commands use the following structure. Keeping each component in order is critical. Command means any operation to be performed like create, get, apply, or delete. Type means resource type, like pod deployment or replica set, name means resource name, if applicable, and flags means special options or modifiers that override default values.

Imperative commands allow you to create, update, and delete live objects directly. Operations should be specified to the command as arguments or flags. Imperative commands are easy to learn and run. For example, to create a pod with a specific container, simply run the command as shown, specifying only a pod name and the container image. But imperative commands don't provide an audit trailer, which is important for tracking changes. They aren't flexible since options are limited, they don't use templates, and they cannot integrate with change review processes, but they are ideal for development and test environments. Imperative commands do also have disadvantages. Suppose a developer runs a command to deploy an application. Another developer wants to deploy that same application, but they cannot because there is no configuration file. The second developer must check with the first developer for the exact command to deploy and then run it. It would be best if both developers used a template for the deployment, since it overcomes the limitations of working with imperative commands.

In imperative object configuration, the kubectal command specifies required operations, optional flags, and at least one file name. The specified configuration file must contain a full definition of the objects in YAML or JSON format. To create the objects defined in the file, run the command kubectl create - f nginx.yaml using the same configuration templates in multiple environments will produce identical results. A configuration file may be stored in a source control system like Git. It can integrate with change processes, and it provides audit trails and templates for creating new objects. But using it requires understanding of the object schema and requires writing a YAML or JSON file now imperative object configuration also has limitations. You need to specify all necessary command operations. For example, if a developer performs an update operation that isn't merged into the configuration file, then another developer cannot use the updated configuration in future deployments. The second developer instead uses the original or previous configuration. It is better to define the desired state in a shared configuration file than when you deploy. Kubernetes automatically determines the necessary operations. This is known as declarative object configuration. Declarative object configuration stores configuration data in files. Operations are identified by Kubectl instead of being specified by the user. This works on directories or individual files. For example, the cubectal apply command mentions a directory as shown, then applies configuration data to all files in that directory. The user is not required to perform any operations since they are performed by the system automatically. Configuration files define a desired state, and Kubernetes actualizes that state, and this approach is the ideal method for production systems. Here is an example of declarative configuration. A developer performs updates to a running application. Since configuration data is stored in the shared template, there is still one source of truth for the configuration of this project.

Now, even if another developer misses several of these updates, all they need to do is apply the current configuration template to ensure the deployed object is as expected. Kubernetes automatically determines and performs the necessary operations to match the current state to the desired state. Here are a few of the commonly used Kubectl commands and descriptions. The get command accesses a file container or any other resource. The delete command deletes a file or container. The autoscale command applies the auto scaling process to the selected file or container, and so on. You can find all Kubectl commands at Kubernetes IO. Kubectl get commands allow you to listen services in a current namespace, pods in all namespaces, a particular deployment and pods in the current namespace.

Kubectl apply commands create resources using YAML or JSON files. They use extensions like .yaml,.yml, or .json. You can use apply commands to create resources from multiple files or from a URL. Kubectl scale commands scale the number of replicas you can use scale commands to scale, a replica set named foo to 3, or a resourceinfo .yaml to 3. Let's create a deployment with three replicas of the nginx image. Create the deployment using the apply command. The output confirms the deployment creation. The get deployment command provides the specific my-dep deployment details.

The output confirms the creation of three replicas ready up to date and available. In this video you learn that Kubectl is the Kubernetes command line interface. The Kubectl command structure is Kubectl command type name flags. Imperative commands are the easiest to learn, have no audit trail, and are not flexible. Imperative object configuration uses templates to ensure proper deployment, replication. And finally declarative object configuration is automated, requires no user input, and is ideal for production systems. [MUSIC]

---

### 7. [READING] Ingress Objects vs. Ingress Controller Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/apb8W/ingress-objects-vs-ingress-controller
- **Method:** `dom_reading_cml` | **Length:** 2741 chars

In Kubernetes, external access to cluster services is overseen by Ingress, consisting of two core components: the Ingress API object and the Ingress controller. Let's understand these elements and their collaborative functionality.

### Ingress objects

The Ingress acts as a supervisor for external access, exposing routes from outside the cluster to internal services, mainly focusing on HTTP and HTTPS traffic. It adheres to rules defined on the Ingress resource to regulate traffic routing.

It doesn't manage arbitrary ports or protocols. Instead, it can provide services with externally accessible URLs, balance traffic, handle SSL/TLS termination, and enable name-based virtual hosting. For non-HTTP and non-HTTPS services, specific service types such as Service.Type=NodePort or Service.Type=LoadBalancer are typically used.

### Ingress controllers

On the operational side, the Ingress controller is the deployed cluster resource responsible for implementing rules specified by the Ingress API object. Unlike certain controllers that automatically run as part of the kube-controller-manager binary, the Ingress controller requires explicit activation for the Ingress resource to function. Its primary role is to execute the directives outlined in the Ingress, commonly utilizing a load balancer or setting up additional frontends to handle incoming traffic.

### Ingress objects vs Ingress controllers

| Feature | Ingress Objects | Ingress Controllers |
| --- | --- | --- |
| Definition | API object managing external access to services | Cluster resource implementing rules specified by Ingress |
| Primary Function | Regulates external access routing | Implements rules, fulfilling the Ingress |
| Configuration Source | Rules defined on the Ingress resource | Reads and processes information from the Ingress object |
| Traffic Handling | Manages HTTP and HTTPS routes | Utilizes load balancer, configures frontends for traffic |
| Activation | Active upon configuration with Ingress resource | Must be explicitly running for Ingress to function |
| Handling Protocols | Focused on HTTP and HTTPS | Implements rules for various protocols and ports |
| Automatic Startup | Activated with configuration | Requires explicit activation in the cluster |
| Analogy | Traffic rule set for the cluster | Executor, similar to Nginx instance handling rules |

### Conclusion

In Kubernetes, overseeing external access includes Ingress, which consists of Ingress objects and Ingress controllers. Ingress manages the routing of HTTP and HTTPS traffic, and Ingress controllers implement these rules in the cluster. Understanding this interplay is essential for effective external access management in Kubernetes.

### Author(s)

Namrah Arif

---

### 8. [READING] Kubernetes Antipatterns Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/H44eh/kubernetes-antipatterns
- **Method:** `dom_reading_cml` | **Length:** 6150 chars

In Kubernetes, identifying and avoiding anti-patterns is crucial for maintaining a robust container orchestration environment. These misleading practices may initially appear effective but can lead to complications. This reading explores ten prevalent Kubernetes anti-patterns and recommends alternative practices for a smoother and more sustainable deployment.

#### 1. Avoid baking configuration in container images

Containers offer the advantage of using a consistent image throughout the production process. To achieve adaptability across different environments, building images without embedding configuration directly into containers is essential.

Issue: Problems arise when images contain environment-specific artifacts that deviate from the tested version, necessitating image rebuilds and risking inadequately tested versions in production. Identification of environment-dependent container images involves spotting features like hardcoded IP addresses, passwords, and environment-specific prefixes.

Best practice: Create generic images independent of specific runtime settings. Containers enable the consistent use of a single image throughout the software lifecycle, promoting simplicity and efficiency.

#### 2. Separate application and infrastructure deployment

Infrastructure as Code (IaC) allows defining and deploying infrastructure like writing code. While deploying infrastructure through a pipeline is advantageous, separating infrastructure and application deployment is crucial.

Issue: Using a single pipeline for both infrastructure and application deployment leads to resource and time wastage, especially when changes in application code outpace infrastructure changes.

Best practice: Split infrastructure and application deployment into separate pipelines to optimize efficiency and resource utilization.

#### 3. Eliminate specific order in deployment

Maintaining application stability despite delays in dependencies is crucial in container orchestration. Unlike traditional fixed startup orders, Kubernetes and containers initiate components simultaneously.

Issue: Challenges arise when poor network latency disrupts communication, potentially causing pod crashes or temporary service unavailability.

Best practice: Proactively anticipate failures, establish frameworks to minimize downtime, and adopt strategies for simultaneous component initiation to enhance application resilience.

#### 4. Set memory and CPU limits for pods problem

The default Kubernetes setting without specified resource limits allows an application to potentially monopolize the entire cluster, causing disruptions.

Best practice: Establish resource limits for all applications, conduct a thorough examination of each application's behavior under various conditions, and strike the right balance to optimize cluster performance.

#### 5. Avoid pulling the latest tag in production problem

The utilization of the "latest" tag in production settings often results in unforeseen pod crashes, triggered by sporadic image pulls lacking specificity. This absence of clear versioning makes troubleshooting challenging, particularly during downtime resolution where swift identification of issues is paramount.

Best practice: Use specific and meaningful image tags, incorporating possibly the date and time of the build. Furthermore, it is crucial to uphold the immutability of container images and store data externally in persistent storage. Avoiding post-deployment modifications to containers ensures safer and more repeatable deployment processes.

#### 6. Segregate production and non-production workloads problem

Relying on a single cluster for all operational needs poses challenges. Security concerns arise from default permissions and complications with non-namespaced Kubernetes resources.

Best practice: Establish a second cluster exclusively for production purposes, avoiding complexities associated with multi-tenancy. Maintain at least two clusters—one for production and one for non-production.

#### 7. Refrain from ad-hoc deployments with kubectl edit/patch problem

Configuration drift occurs when multiple environments deviate due to unplanned deployments or changes, leading to failed deployments.

Best practice: Conduct all deployments through Git commits for comprehensive history, precise knowledge of cluster contents, and easy recreation or rollback of environments.

#### 8. Implement health checks with liveness and readiness probes problem

Neglecting health checks can lead to various issues. Overly complex health checks with unpredictable timings can cause internal denial-of-service attacks within the cluster.

Best practice: Configure health probes for each container, use liveness and readiness probes, and prioritize robust health checks for reliable application responsiveness.

#### 9. Prioritize secret handling and use vault problem

Embedding secrets directly into containers is poor practice. Using multiple secret handling methods or complex injection mechanisms can complicate local development and testing.

Best practice: Use a consistent secret handling strategy, consider HashiCorp Vault, handle secrets uniformly across environments, and pass them to containers during runtime for enhanced resilience and security.

#### 10. Use controllers and avoid running multiple processes per container problem

Directly using pods in production poses limitations. Pods lack durability, automatic rescheduling, and data retention guarantees. Running multiple processes in a single container without controllers can lead to issues.

Best practice: Utilize Deployment with a replication factor, define one process per container, use multiple containers per pod if necessary, and leverage workload resources like Deployment, Job, or StatefulSet for reliability and scalability.

### Conclusion

Understanding and avoiding these Kubernetes anti-patterns contribute to a more resilient and efficient container orchestration environment. Embracing best practices ensures smoother deployments, reduces technical debt, and enhances the overall stability of Kubernetes-based applications.

Author: Namrah Arif

---

### 9. [READING] Summary & Highlights: Kubernetes Basics Reading • 3 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/S6kTb/summary-highlights-kubernetes-basics
- **Method:** `dom_reading_cml` | **Length:** 2396 chars

Congratulations! You have completed this module. At this point, you know:

- Container orchestration automates the container lifecycle resulting in faster deployments, reduced errors, higher availability, and more robust security.
- Kubernetes Is a highly portable, horizontally scalable, open-source container orchestration system with automated deployment and simplified management capabilities.
- Kubernetes architecture consists of a control plane and one or more worker planes.
- A control plane includes controllers, an API server, a scheduler, and an etcd.
- A worker plane includes nodes, a kubelet, container runtime, and kube-proxy.
- Kubernetes objects include Namespaces, Pods, ReplicaSets, Deployments, and Services.
- Namespaces help in isolating groups of resources within a single cluster.
- Pods represent a process or an instance of an app running in the cluster.
- ReplicaSets create and manage horizontally scaled running Pods.
- Deployments provide updates for Pods and ReplicaSets.
- A service in Kubernetes is a REST object that provides policies for accessing the pods and cluster.
- Kubernetes capabilities include automated rollouts and rollbacks, storage orchestration, horizontal scaling, automated bin packing, secret and configuration management, Ipv4/Ipv6 dual-stack support, batch execution, self-healing, service discovery, load balancing, and extensible design.
- Services in Kubernetes are REST objects that provide policies for accessing the pods and cluster. ClusterIP provides Inter-service communication within the cluster; a NodePort Service creates and routes the incoming requests automatically to the ClusterIP Service; the External Load Balancer, or ELB, creates NodePort and ClusterIP Services automatically and External Name service represents external storage as well as enables Pods from different namespaces to talk to each other.
- Ingress is an API object that provides routing rules to manage external users' access to multiple services in a Kubernetes cluster; whereas using a DaemonSet ensures that there is at least one copy of the pod on all nodes; a StatefulSet manages stateful applications, manages Pod deployment and scaling, maintains a sticky identity for each Pod request and provides persistent storage volumes for your workloads and lastly a Job creates pods and tracks the Pod completion process; Jobs are retried until completed.

---

### 10. [READING] Module 2 Cheat Sheet: Understanding Kubernetes Architecture Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/fSSHO/module-2-cheat-sheet-understanding-kubernetes-architecture
- **Method:** `dom_reading_cml` | **Length:** 1030 chars

| Command | Description |
| --- | --- |
| for …do | Runs a for command multiple times as specified. |
| kubectl apply | Applies a configuration to a resource. |
| kubectl config get-clusters | Displays clusters defined in the kubeconfig. |
| kubectl config get-contexts | Displays the current context. |
| kubectl create | Creates a resource. |
| kubectl delete | Deletes resources. |
| kubectl describe | Shows details of a resource or group of resources. |
| kubectl expose | Exposes a resource to the internet as a Kubernetes service. |
| kubectl get | Displays resources. |
| kubectl get pods | Lists all the Pods. |
| kubectl get pods -o wide | Lists all the Pods with details. |
| kubectl get deployments | Lists the deployments created. |
| kubectl get services | Lists the services created. |
| kubectl proxy | Creates a proxy server between a localhost and the Kubernetes API server. |
| kubectl run | Creates and runs a particular image in a pod. |
| kubectl version | Prints the client and server version information. |

---

### 11. [READING] Module 2 Glossary: Kubernetes Basics Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/j1k9X/module-2-glossary-kubernetes-basics
- **Method:** `dom_reading_cml` | **Length:** 8907 chars

| Term | Definition |
| --- | --- |
| Automated bin packing | Increases resource utilization and cost savings using a mix of critical and best-effort workloads. |
| Batch execution | Manages batch and continuous integration workloads and automatically replaces failed containers, if configured. |
| Cloud Controller Manager | A Kubernetes control plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API, and separates out the components that interact with that cloud platform from components that only interact with your cluster. |
| Cluster | A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node. |
| Container Orchestration | Container orchestration is a process that automates the container lifecycle of containerized applications. |
| Container Runtime | The container runtime is the software that is responsible for running containers. |
| Control Loop | A non-terminating loop that regulates the state of a system. A thermostat is an example of a control loop. |
| Control plane | The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers. |
| Controller | In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state. |
| Data (Worker) Plane | The layer that provides capacity such as CPU, memory, network, and storage so that the containers can run and connect to a network. |
| DaemonSet | Ensures a copy of a Pod is running across a set of nodes in a cluster. |
| Declarative Management | A desired state that can be expressed (for example, the number of replicas of a specific application),and Kubernetes will actively work to ensure that the observed state matches the desired state. |
| Deployment | An object that provides updates for both Pods and ReplicaSets. Deployments run multiple replicas of an application by creating ReplicaSets and offering additional management capabilities on top of those ReplicaSets. In addition, deployments are suitable for stateless applications. |
| Designed for extensibility | Adds features to your cluster without adding or modifying source code. |
| Docker Swarm | Automates the deployment of containerized applications but was designed specifically to work with Docker Engine and other Docker tools making it a popular choice for teams already working in Docker environments. |
| Ecosystem | A composition of services, support and tools that are widely available. The Kubernetes ecosystem is a large, rapidly growing ecosystem where its services, support, and tools are widely available. |
| etcd | A highly available key value store that contains all the cluster data. For any deployment, the deployment configuration is stored in etcd. It is the source of truth for the state in a Kubernetes cluster, and the system works to bring the cluster state into line with what is stored in etcd. |
| Eviction | Process of terminating one or more Pods on Nodes. |
| Imperative commands | Create, update, and delete live objects directly. |
| Imperative Management | Defining steps and actions to get to a desired state. |
| Ingress | An API object that manages external access to the services in a cluster, typically HTTP. |
| IPv4/IPv6 dual stack | Assigns both IPv4 and IPv6 addresses to Pods and Services. |
| Job | A finite or batch task that runs to completion. |
| Kubectl | Also known as kubectl Command line tool for communicating with a Kubernetes cluster's control plane, using the Kubernetes API. |
| Kubelet | The kubelet is the primary "node agent" that runs on each node. The kubelet takes a set of PodSpecs (a YAML or JSON object that describes a pod) provided primarily through the apiserver and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by Kubernetes. |
| Kubernetes | Is the de facto open-source platform standard for container orchestration. It was developed by Google and is maintained by the Cloud Native Computing Foundation (CNCF). Kubernetes automates container management tasks, like deployment, storage provisioning, load balancing and scaling, service discovery, and fixing failed containers. Its open-source toolset and wide array of functionalities are very attractive to leading cloud providers, who both support it, and in some cases, also offer fully managed Kubernetes services. |
| Kubernetes API | The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster. |
| Kubernetes API Server | The Kubernetes API server validates and configures data for the api objects which include pods, services, replication controllers, and others. The API Server services REST operations and provides the frontend to the cluster's shared state through which all other components interact. |
| Kubernetes Controller Manager | Runs all the controller processes that monitor the cluster state and ensures that the actual state of a cluster matches the desired state. Examples of controllers that ship with Kubernetes are the replication controller, endpoints controller, namespace controller, and service accounts controller. |
| Kubernetes Cloud Controller Manager | A Kubernetes control plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API, and separates out the components that interact with that cloud platform from components that only interact with your cluster. |
| Kubernetes Proxy | A network proxy that runs on each node in a cluster. This proxy maintains network rules that allow communication to Pods running on nodes—in other words, communication to workloads running on the cluster. The user must create a service with the apiserver API to configure the proxy. |
| kube-scheduler | Control plane component that watches for newly created Pods with no assigned node, and selects a node for them to run on. |
| Label Selector | Allows users to filter a list of resources based on labels. |
| Labels | Tags objects with identifying attributes that are meaningful and relevant to users. |
| Load balancing | Balances traffic across Pods for better performance and high availability. |
| Marathon | Is an Apache Mesos framework. Apache Mesos is an open-source cluster manager developed by UC Berkeley. It lets users scale container infrastructure through the automaton of most management and monitoring tasks. |
| Namespace | An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster. |
| Node | The worker machine in a Kubernetes cluster. User applications are run on nodes. Nodes can be virtual or physical machines. Each node is managed by the control plane and is able to run Pods. |
| Nomad | (Hashicorp) is a free and open-source cluster management and scheduling tool that supports Docker and other applications on all major operating systems across all infrastructure, whether on-premises or in the cloud. This flexibility lets teams work with any type and level of workload. |
| Object | An entity in the Kubernetes system. The Kubernetes API uses these entities to represent the state of your cluster. |
| Persistence | Ensures that an object exists in the system, until the object is modified or removed. |
| Preemption | Logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node. |
| Self-healing | Restarts, replaces, reschedules, and kills failing or unresponsive containers. |
| Service | An abstract way to expose an application running on a set of Pods as a network service. |
| Service Discovery | Discovers Pods using their IP addresses or a single DNS name. |
| StatefulSet | Manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods. |
| Storage | A data store that supports persistent and temporary storage for Pods. |
| Storage Orchestration | Automatically mounts your chosen storage system whether from local storage, network storage, or public cloud. |
| Pod | The smallest and simplest Kubernetes object. Represents a process running in a cluster; it also represents a single instance of an application running in a cluster. Usually, a Pod wraps a single container but, in some cases encapsulates multiple tightly coupled containers that share resources. |
| Proxy | In computing, a proxy is a server that acts as an intermediary for a remote service. |
| ReplicaSet | A ReplicaSet (aims to) maintain a set of replica Pods running at any given time. |
| Workload | A workload is an application running on Kubernetes. |

---
