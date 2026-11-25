# Module 2: Cloud Computing Models

### 1. [VIDEO TRANSCRIPT] Overview of Cloud Service Models Video • 4 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/03i9N/overview-of-cloud-service-models
- **Method:** `dom_transcript` | **Length:** 3624 chars

(Music) In our introductory cloud video we briefly talked about the three service models available on the cloud: Infrastructure as a Service, Platform as a Service, and Software as a Service. Before we dive into the details of each of these service models in the subsequent videos, let's get started with a quick overview of these models. >> Hi, I'm Tessa Rhodes, and I'm a designer on IBM Cloud. So let's start with the foundation here with IaaS. IaaS is a set of compute networking and storage resources that have been virtualized by a vendor so that a user can access and configure them any way they want. In design we have a concept of talking about users called personas, and the persona for IaaS is a system admin. Or an IT admin.

Let's jump up to the top with Software as a Service, that's the easy one. Software as a Service is just software that you don't have to install on your machine and you don't have to manually update. And so, the user for Software as a Service could be anyone. In fact, if you're watching this on YouTube right now, then you're a user of Software as a Service. It's usually charged on a subscription model. rather than a one-time license fee. And that brings us to Platform as a Service. PaaS takes advantage of all the virtualized resources from Iaas and then just abstracts them away, so the user doesn't have to worry about managing any of those virtualized resources.

The user for PaaS is not a system admin, usually. It's usually a dev. In IBM we call this dev "Jane." That's the name of our persona. And so this whole metaphor, the pyramid metaphor, is meant to indicate that as you move down, you're increasing complexity in terms of your knowledge and management of infrastructure resources and you're increasing the ease of use. Another metaphor I use when I'm talking to the designers on my team about PaaS, is having to do with a car. So in this metaphor IaaS is like leasing a car.

So if you've ever leased a car, you probably did a lot of research, and you care about the specs of the car and the performance. You care about the color of the car, what kind of car it is. You're the one driving and you're paying for it. You're also paying for the gas and any tolls or maintenance. With Platform as a Service in this metaphor, that's more like renting a car. So say you're on vacation and you just got off the airport and you're going to pick up your rental car. You don't really care what color it is. You don't really even care about the specs of it, but you're still driving and you're paying for the gas and any tolls you go through.

Software as a Service is again the easiest one. That one's more like getting a taxi or an Uber. So with the taxi or an Uber, you don't care at all about what kind of car it is, what color it is and in fact, you're not even the one driving, or paying for gas, or any tolls because that's baked into the price. >>So let's see what it means in terms of cloud computing and its three service models. With IaaS, the cloud provider manages the physical resources, data centers, cooling, power, network and security, as well as computing resources that include servers and storage. With PaaS the provider, in addition to the computing resources, also manages the platform infrastructure which includes the operating systems, development tools, databases, and business analytics. In the SaaS model, in addition to the infrastructure and the platform resources, the provider also hosts and manages the applications and data.

In the next video, we'll take a closer look at Infrastructure-as-a-Service its features, benefits, and some use cases.

---

### 2. [VIDEO TRANSCRIPT] IaaS - Infrastructure as a Service Video • 4 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/Ip8ad/iaas-infrastructure-as-a-service
- **Method:** `dom_transcript` | **Length:** 3691 chars

In this video, we will discuss the Infrastructure-as-a-Service model in more detail. Infrastructure-as-a-Service, commonly referred to as “IaaS,” – or simply “eye-es” - is a form of cloud computing that delivers fundamental compute, network, and storage resources to consumers on-demand, over the internet, on a pay-as-you-go basis. The cloud provider hosts the infrastructure components traditionally present in an on-premises data center as well as the virtualization or hypervisor layer. In an IaaS Cloud environment, customers can create or provision virtual machines (or VMs) in their choice of Region and Zone available from the Cloud Provider. These VMs typically come pre-installed the customer’s choice of operating system. The customers can then deploy middleware, install applications, and run workloads on these VMs. They can also and create storage for their workloads and backups.

Cloud providers often provide customers the ability to track and monitor the performance and usage of their cloud services and manage disaster recovery. Let’s look at the key components of cloud infrastructure: Physical data centers: IaaS providers manage large data centers that contain the physical machines required to power the various layers of abstraction on top of them. In most IaaS models, end users do not interact directly with the physical infrastructure but experience it as a service provided to them. Compute: IaaS providers manage the hypervisors and end-users programmatically provision virtual instances with desired amounts of compute, memory, and storage resources. Cloud compute typically comes with supporting services like auto scaling and load balancing that provide scalability and high performance. Network: Users get access to networking resources on the cloud through virtualization or programmatically, through APIs. Storage: There are three types of cloud data storage: object, file, and block storage.

Object storage is the most common mode of storage in the cloud, given that it is highly distributed and resilient. IaaS supports a wide array of use cases. We’ll look at some typical use cases here. Organizations today are using cloud infrastructure services to enable their teams to set up test and development environments faster, helping create new applications more quickly. By abstracting the low-level components, cloud infrastructure is helping developers focus more on business logic than infrastructure management. Business continuity and disaster recovery require a significant amount of technology and staff investments. IaaS is helping organizations reduce this cost and make applications and data accessible as usual during a disaster or outage.

Organizations are using cloud infrastructure to deploy their web applications faster and also scale infrastructure up and down as demand fluctuates. Organizations are leveraging the high-performance computing capabilities of cloud infrastructure to solve complex problems involving millions of variables and calculations such as climate and weather predictions and financial modeling. Mining massive data sets to locate valuable patterns, trends, and associations requires a huge amount of processing power. Cloud infrastructure not only provides the required high-performance computing but also makes it economically viable. While there are some concerns regarding the lack of transparency in the cloud infrastructure’s configuration and management and dependency on a third-party for workload availability and performance, Infrastructure-as-a-Service is the fastest growing cloud model today. In the next video, we will look at Platform-as-a-Service model, its features, benefits, and some use cases

---

### 3. [VIDEO TRANSCRIPT] PaaS - Platform as a Service Video • 6 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/uzX6E/paas-platform-as-a-service
- **Method:** `dom_transcript` | **Length:** 5438 chars

[MUSIC] Platform as a service, commonly referred to as P-a-a-S or simply, PaaS, is a cloud computing model that provides customers a complete platform to develop, deploy, manage and run applications created by them or acquired from a third party. The PaaS provider hosts everything: servers, networks, storage, operating system, application runtimes, APIs, middleware, databases and other tools at their data center. The provider also takes responsibility for the installation, configuration, and operation of the application infrastructure, leaving the user responsible for only the application code and its maintenance. Customers pay for this service on a usage basis and purchase resources on demand. With IaaS, the cloud provider offers access to raw computing resources such as servers, storage, and networking, while the user is responsible for the platform and application software. With P-a-a-S or PaaS, the cloud service provider delivers and manages the entire platform infrastructure, abstracting users from the lower level details of the environment. Let's look at some essential characteristics of platform as a service or PaaS.

PaaS clouds are distinguished by the high level of abstraction they provide to the users, eliminating the complexity of deploying applications, configuring infrastructure, and provisioning and configuring supporting technologies like load balancers and databases. PaaS clouds provide services and APIs that help simplify the job of developers in delivering elastically scalable and highly available cloud applications. These services typically include a variety of capabilities such as APIs for distributing, caching, queuing and messaging, file and data storage, workload management, user identity, and analytics, thus eliminating the need to integrate disparate components. The PaaS runtime environment executes end user code according to policies set by the application owner and cloud provider. Many of the PaaS offerings provide developers with rapid deployment mechanisms or push and run mechanism for deploying and running applications. PaaS offerings support a range of application infrastructure or middleware capabilities such as application servers, database management systems, business analytics servers, mobile backend services, integration services, business process management systems, rules engines, and complex event processing systems. Such an application infrastructure assists developers by reducing the amount of code that must be written while expanding the application's functional capabilities.

The most important use case for PaaS is strategic, build, test, deploy, enhance and scale applications rapidly and cost effectively. Let's look at some more use cases for PaaS. API development and management. Organizations are using PaaS to develop, run, manage and secure APIs and microservices, which are loosely coupled, independently deployable components and services. Internet of Things, or IoT: PaaS clouds support a broad range of application environments, programming languages, and tools used for IoT deployments. Business analytics, or intelligence: PaaS tools allow organizations to analyze their data to find business insights that enable more informed business decisions and predictions. Business Process management, or BPM.

Organizations are using the PaaS cloud to access BPM platform delivered as a service. Master data management, or MDM: Organizations are leveraging the PaaS cloud to provide a single point of reference for critical business data, such as information about customer transactions and analytical data to support decision-making. Let's look at some advantages of using PaaS. Scalability, made possible because of the rapid allocation and deallocation of resources with a pay-as-you-use model offered by PaaS. The APIs support services and middleware capabilities that PaaS clouds provide assist developers in focusing their efforts on application development and testing, resulting in faster time-to-market for their products and services. Middleware capabilities also reduce the amount of code that need to be written while expanding the application's functional capabilities. Greater agility and innovation: because using PaaS platforms means that you can experiment with multiple operating systems, languages and tools without having to invest in these resources.

You can evaluate and prototype ideas with very low risk exposure, resulting in faster, easier, less risky adoption of a wider range of resources. Some of the key PaaS offerings available in the market today include AWS Elastic Beanstalk, Cloud Foundry, IBM Cloud Paks, Windows Azure, Red Hat OpenShift, Magento Commerce Cloud, force.com, and Apache Stratos. PaaS clouds do come with some risks, risks that all cloud offerings have in general, such as information security threats and dependency on the service provider's infrastructure. Services can get impacted when a service provider's infrastructure experiences downtime. Customers also don't have any direct control over the changes that may take place when a provider makes changes in its strategy, service offerings or tools. But the benefits can far outweigh these risks. PaaS continues to experience strong growth and is predicted to become the prevailing platform delivery model moving forward.

In the next video, we will look at software as a service model, its features, benefits, and some use cases. [MUSIC]

---

### 4. [VIDEO TRANSCRIPT] SaaS - Software as a Service Video • 4 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/V7y5Y/saas-software-as-a-service
- **Method:** `dom_transcript` | **Length:** 3745 chars

Software-as-a-Service, or “SaaS,” is a cloud offering that provides users with access to a service provider’s cloud-based software. SaaS providers maintain the servers, databases, and code that constitute an application. They also manage access to the application, including security, availability, and performance. Applications reside on a remote cloud network, and users use these applications without having to maintain and update the infrastructure. Core business processes supported by SaaS today include email and collaboration via offerings such as Microsoft's Office 365 and Google's Gmail, Customer Relationship Management via services such as NetSuite CRM and Salesforce, Human Resource Management via services from Workday and SAP SuccessFactors, financial management, billing and collaboration, and many more. According to Forrester Research, SaaS has overtaken on-premises solutions in categories such as human capital management (HCM), customer relationship management (CRM), and collaboration. Solutions once available with several different deployment options are now SaaS-only: Let’s look at key characteristics of Software-as-a-Service: SaaS clouds have a multitenant architecture. Infrastructure and code are maintained centrally and accessed by all users. SaaS makes it easy for users to manage privileges, monitor data use, and ensure everyone sees the same information at the same time.

Security, compliance, and maintenance are all part of the offering. In SaaS, customizations are often limited, however some SaaS applications may allow certain types of customizations like branding; they can modify data fields and enable or disable features within the business process. These customizations are preserved through upgrades. Users pay for the use of the services via a subscription model. The use of resources can be scaled easily, depending on service needs. Key benefits of adopting SaaS: Businesses can directly procure solutions without upfront capital and assistance from IT, greatly reducing the time from decision to value from months to days. SaaS greatly increases workforce productivity and efficiency.

Users can access core business apps from wherever; they can also buy and deploy apps in minutes reducing the typical obstacles enterprises have to test the products they might use. Using SaaS applications, individuals and small enterprises can spread out their software costs over time. Let’s look at some use cases for SaaS: Organizations are moving to SaaS for their core business needs as part of their strategic transformation to reduce on-premises IT infrastructure and reduce capital expenditure. Organizations are leveraging SaaS to avoid the need for ongoing upgrades, maintenance, and patching, done traditionally by internal IT resources; applications run reliably with minimal input, for example, email servers and office collaboration and productivity tools. Organizations are increasingly opting for SaaS eCommerce Platforms to manage their websites, marketing, sales, and operations. With SaaS, organizations are able to take advantage of the resilience and business continuity of the cloud provider. Enterprises are now developing SaaS integration platforms (or SIPs) for building additional SaaS applications, moving SaaS beyond standalone software functionality to a platform for mission-critical applications. SaaS does evoke some concerns, as well.

Primary among them being data ownership and data safety. Security is an important consideration when you’re allowing a third-party to maintain business-critical data. And application access relies on a good network connection. But the benefits far outweigh the concerns, with SaaS making up the largest segment of the cloud market today.

---

### 5. [READING] Lesson 1 Summary: Service Models Reading • 1 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/supplement/Yocqq/lesson-1-summary-service-models
- **Method:** `dom_reading_cml` | **Length:** 1388 chars

In this lesson, you have learned the following:

- With IaaS, the cloud provider manages physical resources.
- With PaaS, the provider manages the platform infrastructure.
- In the SaaS model, the provider hosts and manages the applications and data.
- Infrastructure-as-a-Service is a form of cloud computing that delivers fundamental computer, network, and storage resources to consumers on-demand, over the network, on a pay-as-you-go basis.
- The key components of cloud infrastructure are: - Physical data centers - Compute - Network - Storage
- Platform-as-a-Service is a cloud computing model that provides customers with a complete platform—hardware, software, and infrastructure.
- The high level of abstraction, support services, runtime environments, rapid deployment mechanisms, and middleware capabilities distinguishes PaaS clouds.
- PaaS advantages are: - Scalability - Faster time to market products and services. - Greater agility and innovation
- Software-as-a-Service is a cloud offering that provides users with access to a service provider’s cloud-based software.
- SaaS characteristics are: - Multitenant architecture - Security, compliance, and maintenance - Customization of applications - Subscription model - Scaling
- SaaS advantages are: - Direct procurement of solutions - Improved workforce productivity and efficiency - Enable distribution of software costs

---

### 6. [VIDEO TRANSCRIPT] Public Cloud Video • 5 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/9js5f/public-cloud
- **Method:** `dom_transcript` | **Length:** 4882 chars

In our introductory cloud video we briefly mentioned the four deployment models for cloud. In this video, we will discuss the Public Cloud deployment model in more detail. Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. The four cloud deployment models include—Public Cloud, Private Cloud, Community Cloud and Hybrid Cloud. In a public cloud model, users get access to servers, storage, network, security, and applications as services delivered by cloud service providers over the internet. Using web consoles and APIs, users can provision the resources and services they need. The cloud provider owns, manages, provisions, and maintains the infrastructure, renting it out to customers either for a subscription charge or usage-based fee.

Users don’t own the servers their applications run on or storage their data consumes, or manage the operations of the servers, or even determine how the platforms are maintained. In very much the same way that we consume and pay for utilities such as water, electricity, or gas in our everyday lives, we don’t own any of these cloud resources—we make an agreement with the service provider, use the resources, and pay for what we use within a certain period. Public clouds offer significant cost savings in terms of Total Cost for Ownership (TCO) as the provider bears all the capital, operational, and maintenance expenses for the infrastructure and the facilities they are hosted in. It makes scalability as easy as requesting more capacity. However, with a public cloud, the user does not have any control over the computing environment and is subject to the performance and security of the cloud provider’s infrastructure. There are several public cloud providers in the market today, such as Amazon Web Services, Microsoft Azure, IBM Cloud, Google Cloud Platform, and Alibaba Cloud. While all providers include a common set of core services, such as servers, storage, network, security, and databases, they also offer a wide spectrum of niche services with varied payment options.

Let’s talk about some of the characteristics of a public cloud: A public cloud is a virtualized multi-tenant architecture enabling tenants or users to share computing resources, residing outside their firewalls The cloud provider's pool of resources, including infrastructure, platforms, and software, are NOT dedicated for use by a single tenant or organization Resources are distributed on an as-needed basis offered through a variety of subscription and pay-as-you-go models. Public clouds have significant benefits; we’ll go over some of these benefits here: Vast on-demand resources are available, allowing applications to respond seamlessly to fluctuations in demand. Considering the large number of users that share the centralized cloud resources on-demand, the public cloud offers the most significant economies of scale. The sheer number of server and network resources available on the public cloud means that a public cloud is highly available —if one physical component fails, the service still runs unaffected on the remaining available components. It’s also important to note some concerns users have regarding public clouds—key among them being security and data sovereignty compliance. Security issues such as data breaches, data loss, account hijacking, insufficient due diligence, and system and application vulnerability seem to be some of the fears users continue to have concerning security in the public cloud. With data being stored in different locations and accessed across national borders, it has also become increasingly critical for companies to be compliant with data sovereignty regulations governing the storage, transfer, and security of data.

A service provider’s ability to not just keep up with the regulations, but also the interpretation of these regulations, is a concern shared by many businesses Let’s look at some common use cases for public cloud: Organizations are increasingly opting to access cloud-based applications and platforms so their teams can focus on building and testing applications, and reducing time-to-market for their products and services. Businesses with fluctuating capacity and resourcing needs are opting for the public cloud. Organizations are using public cloud computing resources to build secondary infrastructures for disaster recovery, data protection, and business continuity. More and more organizations are using cloud storage and data management services for greater accessibility, easy distribution, and backing up their data. IT departments are outsourcing the management of less critical and standardized business platforms and applications to pubic cloud providers. In the next video, we will look at the private cloud model, its features, benefits, and some use cases.

---

### 7. [VIDEO TRANSCRIPT] Private Cloud Video • 4 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/Cn1ph/private-cloud
- **Method:** `dom_transcript` | **Length:** 4289 chars

The National Institute of Standards and Technology defines private cloud as cloud infrastructure provisioned for exclusive use by a single organization comprising multiple consumers, such as the business units within the organization. It may be owned, managed, and operated by the organization, a third party or some combination of them, and it may exist on or off premises. Private cloud platforms can be implemented internally or externally. When the platform is provisioned over an organization's internal infrastructure, it runs on-premises and is owned, managed, and operated by the organization. When it is provisioned over a cloud providers infrastructure, it is owned, managed, and operated by the service provider. This external private cloud offering that resides on a cloud service providers infrastructure is called a Virtual Private Cloud or VPC. A VPC is a public cloud offering that lets an organization establish its own private and secure cloud-like computing environment in a logically isolated part of a shared public cloud.

Using a VPC, organizations can leverage the dynamic scalability, high availability, and lower cost of ownership of a public cloud, while having the infrastructure and security tailored to the organization's unique needs. Virtual Private Cloud are offered by most public cloud providers, such as IBM and Amazon. A private cloud is a virtualized environment modeled to bring in the benefits of a public cloud platform without the perceived disadvantages of an open-end shared public platform. Users of a private cloud, such as developers and business units in an organization still get to leverage benefits such as economies of scale, granular scale, operational efficiencies, and users self-service while exercising full control over access, security and compliances specific to their organization and business. Private cloud provide you with; one, the ability to leverage the value of cloud computing using systems that are directly managed or under perceived control of the organization's internal IT. Two, the ability to better utilize internal computing resources, such as the organization's existing investments in hardware and software, thereby reducing costs. Three, better scalability through virtualization and cloud bursting.

That is, leveraging public cloud instances for a period of time, but returning to the private cloud when the surge is meet. Four, controlled access and greater security measures customized to specific organizational needs. Five, the ability to expand and provision things in a relatively short amount of time, providing greater agility. Organizations may choose to opt for private cloud because of various reasons, because their applications provide a unique competitive advantage. There are security and regulatory concerns, or because their data is highly sensitive and subject to strict industry or governmental regulations. Let's look at some common use cases for a private cloud. One, a private cloud is an opportunity for organizations to modernize and unify their in-house and legacy applications.

Moving these applications from their dedicated hardware to the cloud also allows them to leverage the power of the compute resources and multiple services available on the cloud. Two, using the private cloud, organizations are integrating data and application services from their existing applications with public cloud services. This allows them to leverage their private cloud's compute capability for the larger jobs while pulling data into an application on a private cloud to leverage public cloud services. Essentially, opening their data centers to work with cloud services. Three, application portability is a key feature of cloud platforms. Using the private cloud gives organizations the ability to build applications anywhere and move them anywhere without having to compromise security and compliance in the process. Four, some of the key reasons that may prevent an organization for moving to a public cloud include security and regulatory concerns and data sensitivity.

A private cloud offers these organizations the benefits of on-demand enterprise resources while exercising full control over critical security and compliance issues from within the environment of their dedicated cloud

---

### 8. [VIDEO TRANSCRIPT] Hybrid Cloud Video • 9 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/42DD1/hybrid-cloud
- **Method:** `dom_transcript` | **Length:** 8885 chars

Hybrid Cloud is a computing environment that connects an organization's on-premise private Cloud and third-party public Cloud, into a single flexible infrastructure for running the organizations applications and workloads. The mix of public and private Cloud resources gives organizations the flexibility to choose the optimal Cloud for each application or workload. Workloads move freely between the two Clouds as needs change, organizations can choose to run the sensitive, highly regulated, and mission-critical applications or workloads with reasonably constant performance and capacity requirements on private Cloud infrastructure, while deploying the less sensitive and more dynamic workloads on the public Cloud. With proper integration and orchestration between the public and private Clouds, you can leverage both Clouds for the same workload. For example, you can leverage public Cloud instances for a period of time, but returned to the private Cloud when the search is met, also known as Cloud bursting. The key tenants of a hybrid Cloud are interoperability, scalability, and portability. Hybrid Cloud is interoperable, which means that the public and private Cloud services can understand each other's APIs, configuration, data formats, and forms of authentication and authorization.

When there's a spike in demand, a workload running on the private Cloud can leverage the additional public Cloud capacity making it scalable. A hybrid Cloud is also portable. Since you're no longer locked in with a specific vendor, you can move applications and data not just between on-premise and Cloud systems, but also between Cloud service providers. Hybrid is about taking the best of both worlds. There are two common types of hybrid Clouds, hybrid mono Cloud and hybrid multi-Cloud. Hybrid mono Cloud is a hybrid Cloud with one Cloud provider while a hybrid multi-Cloud is an open standards-based stack that can be deployed on any public Cloud infrastructure. The difference lies in the flexibility that the hybrid multi-Cloud offers organizations to move workloads and environments from one vendor to another.

There's also a variant of hybrid multi-Cloud called the composite multi-Cloud, which makes this flexibility even more granular as it distributes single applications across multiple providers, allowing you to move application components across Cloud services and vendors as needed. Hybrid Cloud offers significant benefits in areas of security and compliance, scalability and resilience, resource optimization and cost-saving. A hybrid Cloud lets organizations deploy highly regulated or sensitive workloads in a private Cloud while running the less sensitive workloads on a public Cloud. Using a hybrid Cloud, you can scale up quickly, inexpensively, and even automatically using the public Cloud infrastructure, all without impacting the other workloads running on your private Cloud. Because you're not locked in with a specific vendor and also don't have to make either/or decisions between the different Cloud models, you can make the most cost efficient use of your infrastructure budget. You can maintain workloads where they are most efficient, spin up environments using Pay-As-You-Go in the public Cloud, and rapidly adopt new tools as you need them. However, hybrid Clouds are complex and challenging to deploy and maintain since they involve synchronization, redirection, latency, security, portability, interoperability, and compatibility of policies, applications and data and so on.

A typical organization will have a range of applications and workloads spread across private, public, and traditional IT environments. This represents a range of opportunities for optimization via a hybrid Cloud approach. Let's look at some increasingly common Hybrid Cloud use cases. Software-as-a-service integration. Through Hybrid Integration, Organizations are connecting software-as- -a-service applications available in the public Cloud to their existing public Cloud, private Cloud and traditional IT applications to deliver new solutions. Data and AI integration. Organizations today are creating richer and more personal experiences by combining new data sources on the public Cloud, such as weather, social, the Internet of Things, CRM, and ERP, with existing data and analytics, machine learning and AI capabilities.

Enhancing legacy apps. An increasing number of organizations are using public Cloud services to upgrade the user experience of their on-premises applications and deploy them globally to new devices while incrementally modernizing their core business systems. VMware migration. More and more organizations are lifting and shifting their on-premises virtualized workloads to a public Cloud without conversion or modification to reduce their on-premises datacenter footprint, and position themselves to scale without added capital expense. Leveraging public Cloud services. Using the private Cloud, organizations are integrating data and application services from their existing applications with public Cloud services. This allows them to leverage their private Cloud compute capability for the larger jobs while pulling data into an application on a private Cloud to leverage public Cloud services, essentially, opening their datacenters to work with Cloud services.

Hi everyone. My name is Sai Vennam and I'm a developer advocate with IBM. Today, I'm excited to introduce a three-part video series on hybrid Cloud architectures. Hybrid Cloud is a concept that's been around for quite some time, but we're finding that it's becoming increasingly used to architect and modernize existing or legacy applications. According to research, we found that 75% of non-Cloud applications will be moving to the Cloud in the next three years. This goes to say that if you're not already thinking about your hybrid Cloud strategy, you may be falling behind. If you want to learn more about the basics of hybrid Cloud, check out my hybrid Cloud explained video where I covered the basic concepts of all hybrid Cloud architectures.

In this three-part series, I want to dive deeper and hit on key concepts that make up a hybrid Cloud architecture. To do that, we're going to start with Part 1 of this video series which is going to be connect. Connectivity and interoperability are core concepts of hybrid Cloud architectures. You can imagine that you have existing applications that may be running on-prem working with maybe a private Cloud, and you can also imagine you'd be taken advantage of public Cloud as well. You have services that are running across all of these environment, we need a way to securely connect them to one another. Taking advantage of open-source solutions that we have, things like Linux-based containers, Kubernetes, Istio, as well as multi cluster management tools, message queues, brokers, the list is endless but there's a lot of solutions out there when used properly, help you hit that connectivity that you need with hybrid Cloud architectures. In Part 2, we want to talk about modernization.

We'll be switching gears a little bit here. You can imagine that with existing applications that you may have, you may have a monolithic application that you want to break apart and move to a public Cloud, and that might allow you to take better advantage of scaling the public environments offer. That's a very simple use case and one of many when it comes to modernizing your applications. In Part 2, I'm going to hit on strategies to modernize those legacy applications which is a core part of hybrid Cloud architectures. In Part 3, we want to talk about security. We're finding that every year you're hearing about a different data breach and we're hearing about privacy regulations that are becoming increasingly more strict being imposed on companies. The fact is moving to hybrid Cloud might scare some folks, but we have to write solutions to ensure that you can take advantage of your existing On-prem assets, the security, and the ease of use that you have there while securely moving some of your assets to a public or even a private Cloud.

This allows you to have the comfort taken advantage of all the resources you have on public Cloud while still maintaining the security that's required of your architectures. I believe that this three-part series is going to help tackle the three major issues that you may have when architecting your hybrid Cloud applications. As always, we're always checking for your comments and your feedback, and if you have any other topics that you'd like us to cover and light boarding videos, please let us know below. Be sure to subscribe and stay tuned for future videos in this series and if you want to get started on your hybrid Cloud architecture journey right now, go ahead and check out some of the links that we have below and the videos that we have lined up. Thank you.

---

### 9. [VIDEO TRANSCRIPT] Expert Viewpoints: Cloud Computing Service and Deployment Models Video • 5 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/lecture/RzNdv/expert-viewpoints-cloud-computing-service-and-deployment-models
- **Method:** `dom_transcript` | **Length:** 4321 chars

[Music] Welcome to Cloud Computing Service Models - Expert Viewpoints. In this video we will listen to several cloud experts discuss the choice and adoption of different cloud models. Can you talk about use case scenarios or considerations for choosing the right cloud model for your organization? Model as in IaaS, SaaS or PasS; or public, private, or hybrid. When choosing a cloud model for your organization, you want to consider where is your organization at in the cloud journey? So if they have a lease that's about to expire at the data center, then they might not have time to rewrite the application to be cloud native. They might just have time to take the application exactly as it is on the virtual machines in the data center, and move them onto virtual machines in the cloud.

That's called Infrastructure-as-a-Service. If you have more time, you could consider re-platforming, and that means putting it on a Platform-as-a-Service, such as Containers, or a service that operates the operating system for you, patches the operating system for you and all you have to do is install extra dependencies yourself. Or if you want to move really fast and you have a brand new product that you're just starting to write, why not start with the latest approach, which is Functions-as-a-Service? Use serverless functions, and you can move really fast because you don't have to manage any underlying infrastructure. The security of the operating system is handled for you by the cloud provider. Generally, my answer is to stay as high on the stack as you can to meet your business requirements. So SaaS applications provide the business value with little or no technology resource investment beyond the subscriptions.

So if that works, that's great. Platform-as-a-Service, as I mentioned, allows developers to focus on building and deploying new applications without having to grapple with the details of cloud infrastructure. And if [COUGH] in a lot of cases that will save money and investment and allow you to focus on building your products more quickly in time to market. Infrastructure-as-a-Service though, is the right answer when you need specific control of all the compute and network resources to achieve your business goals. So in many cases that'll make sense too. While choosing the right cloud model, organizations should consider what are their business needs, the level of control that they would like to have, and the cost. If your business needs an out of the box software like email, CRM, event management tool, etc, then choose Software-as-a-Service.

It will offer access from anywhere and any device, automatic software updates, low cost and easy adoptions. You will need a vendor to manage the software. If you require a platform for building products, then choose Platform-as-a-Service. It is a perfect choice for software development companies, as it provides developers with reduced development time, different programming language support, easy collaboration with teams, and reduces the cost. If your business simply needs a virtual machine, then opt for Infrastructure-as-a-Service. Scenarios for using Infrastructure-as-a-Service can be hosting a website, virtual data centers or performing data analysis. Infrastructure-as-a-Service is more expensive than SaaS or PaaS and all issues related to virtual machine management is businesses responsibility.

However, it is more reliable and secure as data is kept at designated data centers. As you move down the layers of abstraction from Software-as-a-Service all the way to Infrastructure-as-a-Service, the tradeoff is that you take on more management responsibilities yourself with the advantage of having more control over how your resources are configured. I'll typically only take that tradeoff when I have to. So let's say I'm building a website. I'll typically default to a Software-as-a-Service option, let's say WordPress. But then maybe it turns out the website I'm building is somewhat complicated and I want it to be a react app. I might host that app on a Platform-as-a-Service, but then let's suppose I have a requirement that my app needs to run in an operating system that is not supported by the Platform-as-a-Service.

At that point I'll have to just provision some VMs myself and figure out how to run it myself. [MUSIC]

---

### 10. [READING] Community Cloud Reading • 6 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/supplement/wgELI/community-cloud
- **Method:** `dom_reading_cml` | **Length:** 6004 chars

In this reading, you will learn about community cloud and how it is implemented with reference to Google Cloud as an example.

### What is a community cloud?

A community cloud is defined by NIST SP 800-145 as:

“Cloud infrastructure [that] is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.”

### Why community cloud?

Community cloud approach is used by organizations for the following reasons:

- The community cloud members work under the same set of security controls.
- The approach provides the members the same attributes like citizenship and authorization controls while giving limited physical and/or logical access to resources.
- It also supports data localization and some data sovereignty requirements based on the location of the community cloud’s data centers.
- The approach defines a perimeter security model encompassing the community cloud.

### Implementation of software-defined community cloud

To establish a security perimeter, most legacy community clouds depend on physical separation from other clouds. However, this implementation could not meet the advanced security, manageability, or compliance requirements of the industry.

In the modern architecture, a software-defined community cloud is designed to deliver the required benefits. Google Cloud is a software-defined approach that provides security and compliance assurances without the strict physical infrastructure constraints of legacy approaches. The Google community clouds use a combination of technologies referred to as “assured clouds” that can:

- Define communities around common projects, security and compliance requirements, and policy.
- Separate shared community projects from other projects.
- Modify capabilities of a community’s boundary based on policy-controlled and audited configuration changes.

### Comparison between traditional and software-defined community cloud

The software-defined community cloud provides many benefits to the users in comparison to the traditional community cloud implementation. The following table depicts the comparison between the two implementations based on the characteristics as stated in the definition given by NIST.

| Characteristic | NIST Definition SP 800-145 | Traditional Cloud Community Implementation | Software-Defined Community Cloud |
| --- | --- | --- | --- |
| Infrastructure Exclusivity | The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns | Separate data centers with separate infrastructure | Each project is effectively a private cloud with isolated infrastructure primitives |
| All users subject to common security controls | (implied) | Same security controls apply across exclusive infrastructure shared by the community | Assured Workloads controls are scoped to the community and enforced through terms of service |
| Personhood and citizenship of support staff | It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, | Personnel must be physically located at dedicated facilities | Access management service restricts support to personnel with required attributes (personhood, citizenship, work location, and more) |
| Data localization | and it may exist on or off premises | Community dedicated storage devices | Enforced by software |
| Defined security parameter | (implied) | The community is the enclave | Each project is its own enclave |

### Software defined community cloud as a new type of “Government Cloud”

In Google Cloud Platform (GCP), a project is a unique, logical grouping of “infrastructure primitives.” In this context, an infrastructure primitive is any atomic unit of capacity in GCP – a virtual machine (VM), a persistent disk (PD), a storage bucket, and others. Projects are “global resources” that can be assigned infrastructure primitives from any region or zone.

Every project is an individual project separate from other customers’ projects. Low-level resources like hypervisors, blocks in our distributed blockstore that underlies Google Cloud Storage (GCS), and other components are isolated with resource abstractions that enforce the isolation both logically and cryptographically.

A Private Cloud deployment model is defined in NIST SP 800-145 as:

Cloud infrastructure [that] is provisioned for exclusive use by a single organization comprising multiple consumers (such as business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist on or off premises.

When a project is created within GCP, the infrastructure primitives that are assigned to that project are scoped to only that project. This scoping of infrastructure primitives effectively creates an “enclave” per Project.

When overlaid with Assured Workloads constraints for data residency, support personnel attributes, and security controls common to that community, these per-project private cloud enclaves become software-defined community clouds.

### Benefits of a software-defined community cloud

The approach Google Cloud has taken brings multiple benefits such as meeting security and compliance requirements. New hardware, new services, and improvements to existing services are accessed faster than in traditional community clouds. The process by which new cloud technology can be onboarded and made available is also faster. Overall efficiency is improved in this model due to the scale of infrastructure available to the community; this can translate to improved availability and performance. Security enhancements can be scaled and implemented more quickly.

---

### 11. [READING] Lesson 2 Summary: Deployment Models Reading • 2 min
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/supplement/MuNCm/lesson-2-summary-deployment-models
- **Method:** `dom_reading_cml` | **Length:** 1458 chars

In this lesson, you have learned:

- Deployment models indicate where the infrastructure resides, who owns and manages it, and how cloud resources and services are made available to users. There are four main deployment models available on the cloud—public, private, hybrid, and community.
- In the public cloud model, the service provider owns, manages, provisions, and maintains the physical infrastructure such as data centers, servers, networking equipment, and storage, with users accessing virtualized computing, networking and storage resources as services.
- In the private cloud model, the provider provisions the cloud infrastructure for exclusive use by a single organization. The private cloud infrastructure can be internal to the organization and run on-premises. Or it can be on a public cloud, as in the case of Virtual Private Clouds (VPC), and be owned, managed, and operated by the cloud provider.
- In the hybrid cloud model, an organization’s on-premise private cloud and a third-party, public cloud are connected as a single, flexible infrastructure that leverages the features and benefits of both Public and Private clouds.
- In the community cloud model, the provider provisions the cloud infrastructure for use by a community of organizations with shared concerns. One or more of the organizations in the community, a third-party provider, or both are responsible for the ownership, management, and operation of this infrastructure.

---

### 12. [READING] Module 2 Glossary: Cloud Computing Models
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/supplement/TpUje/module-2-glossary-cloud-computing-models
- **Method:** `dom_reading_cml` | **Length:** 1985 chars

| Term | Definition |
| --- | --- |
| BPM | Business Process Management |
| Composite multicloud | A variant of hybrid multicloud, distributes single applications across multiple providers, allowing you to move application components across cloud services and vendors as needed |
| CRM | Customer Relationship Management |
| HCM | Human Capital Management |
| Hybrid cloud | A computing environment that connects an organization’s on-premises private cloud and third-party public cloud into a single, flexible infrastructure for running the organization’s applications and workloads |
| Hybrid monocloud | A hybrid cloud with one cloud provider |
| Hybrid multicloud | An open standards-based stack that can be deployed on any public cloud infrastructure |
| IaaS | Infrastructure as a service is a form of cloud computing that delivers fundamental compute, network, and storage resources to consumers on-demand, over the network, on a pay-as-you-go basis |
| IoT | Internet of things |
| MDM | Master Data Management |
| PaaS | Platform as a service is a cloud computing model that provides customers a complete platform—hardware, software, and infrastructure—to develop, deploy, manage, and run applications created by them or acquired from a third-party |
| Pay-as-you-go | Users can order cloud resources from a larger pool of available resources and pay for them on a per-use basis |
| Private Cloud | Cloud infrastructure provisioned for exclusive use by a single organization comprising multiple consumers, such as the business units within the organization |
| Public cloud | Users get access to servers, storage, network, security, and applications as services delivered by cloud service providers over the internet |
| SaaS | Software as a service is a cloud offering that provides users with access to a service provider’s cloud-based software |
| SIP | SaaS integration platforms |
| TCO | Total cost for ownership |
| VM | Virtual machine |
| VPC | Virtual Private Cloud |

---

### 13. [READING] Reading: IBM Cloud Account
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/supplement/8PL2M/reading-ibm-cloud-account
- **Method:** `dom_reading_cml` | **Length:** 966 chars

This is an optional lesson and is not required to complete the course. In this lesson, you will first:

- Obtain a feature code to enable you to create an IBM Cloud trial account without a credit card. Once you have received your feature code, it's essential to follow the detailed instructions to activate and set up your IBM Cloud account properly.
- Create the IBM Cloud account - Please go through the step-by-step instructions provided in the link to ensure you complete the setup correctly. Take your time reviewing the instructions before moving forward. This will help avoid any issues later in the lab exercises.

The IBM Cloud account is required for an optional hands-on lab only in a subsequent module. In case you have any issues with creating the account, you can simply skip this lesson and proceed to the next module.

If you get an error when you obtain the feature code, see "Ways To Troubleshoot" in [Optional] Hands-on Lab: Create an IBM account.

---

### 14. [READING] [Optional] Hands-on Lab: Create an IBM account
- **URL:** https://www.coursera.org/learn/introduction-to-cloud/supplement/52eqk/optional-hands-on-lab-create-an-ibm-account
- **Method:** `dom_reading_cml` | **Length:** 4977 chars

### Lab overview:

To access the resources and services that the IBM Cloud provides, you need an IBM Cloud Account. This lab will take you through step-by-step instructions to create one.

### Objective(s):

After completing this lab, you will be able to:

- Create an IBM Cloud Trial Account using a Feature Code

### Prerequisite:

Please ensure you click on the "Launch App" button from the previous section of this lab to get a feature code and activate the trial account before moving forward with the lab instructions. These instructions will help you create an IBM Cloud account.

Note: These instructions only apply to creating a NEW IBM Cloud account using an email address that you have not used previously to create another IBM Cloud account. If you have already used your IBM Cloud feature code in another course/lab to create an IBM Cloud account, please skip this lab, as the code can only be used once.

## Activate Trial Account

- The previous section of the lab is the first step for activating your IBM Cloud trial account using Feature Code.
- On clicking on the Launch App button, you will get a unique code.
- Next, click on Activate Your Trial. It will redirect you to the IBM Cloud registration page, to create an account on IBM Cloud.

## Create an IBM Cloud Account

- Once you are on the account creation page, follow the below instructions to create an IBM cloud trial account.
- Enter your Email address [preferably use Gmail ID or Yahoo ID] and a strong Password, as per criteria, and then click the Next button.

NOTE: Please ensure that you provide an email address that you have not used previously to create any other IBM Cloud account, and you can readily access your email to retrieve the verification code required in the next step.

- An email is sent to the address you signed up with to confirm your email address. Check your email and copy and paste Verification code. Then click Next.

- Once your email is successfully verified, enter your First name and Last name, and select your country (for example, United States) under Country or region then click Next.

Note: Kindly use your full last name instead of just using single letters/initials. For example:First Name: AdaLast Name: Lovelace

- Go through the Account Notice. If you wish, you can opt for email updates. Then accept the Terms and Conditions and click Continue.

- Before creating your account, review the account privacy notice and acknowledge that you have read and understood by checking the checkbox and clicking Continue.

It takes a few seconds to create and set up your account.

- On the next screen, you will be asked to verify your identity where you will see the feature code has been applied for you already. Then click on Create account.

Note: It might take a couple of minutes to create your account.

Note: Please ensure you do not use the Credit Card option to verify your account for coursework as that can result in unnecessary charges and delays in activating your account.

- Once you have successfully created your IBM Cloud account, you should see the dashboard.

- Now you may explore the IBM Catalog for exploring the services and resources offered by IBM Cloud.

## Ways To Troubleshoot

If you encounter any of the below errors while activating your IBM Cloud trial account, please follow the steps as instructed below.

- Ooops snap! The promotional codes for IBM Cloud are very popular and have temporarily run out. Please check back soon. Reason - It takes 24 to 48 hours to populate new feature codes. Solution - Please try again later
- Something went wrong error. Reason - This could be because you have already applied a code to this email earlier or your domain/country/IP is restricted. Solution - Try from another email id
- Feature code expired. Reason - You may have applied the feature code already once. Solution - Create a new IBM cloud account and write to the support team as per the instructions below.
- If your trial ends. Reason - Trial accounts are valid only for 6 months, and the same feature code cannot be applied again. Solution - Create a new IBM cloud account and write to the support team as per the instructions below.

### Other Possible Solutions:

- Try clearing your browser's cache and cookies
- Try from a different browser on an incognito mode.

If you still face any issues, please write an email to support@cognitiveclass.ai with the following details

Subject Line: Feature Code Issue

Email Content:

- Name of the course you are undertaking.
- The course link where you obtained the feature code.
- The feature code you are trying to apply.
- The error message that it is shown.
- The email ID used to create the IBM Cloud account.
- Your username.

Once you obtain a new feature code, you can create a new account using a different Email ID.

Congratulations! You have successfully created your IBM Cloud Account!

### Author(s)

#### Lavanya

#### Other Contributor(s)

Rav Ahuja, Antonio Cangiano

---
