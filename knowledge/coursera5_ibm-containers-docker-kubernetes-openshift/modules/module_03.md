# Module 3: Managing Applications with Kubernetes

### 1. [VIDEO TRANSCRIPT] ReplicaSet Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/KyXOz/replicaset
- **Method:** `dom_transcript` | **Length:** 5271 chars

[MUSIC] Welcome to ReplicaSet. After watching this video, you will be able define a ReplicaSet, explain how a ReplicaSet works, and list the benefits of using a ReplicaSet. If an application is deployed on a single pod, the pod will be unable to perform certain actions. If requests increase, manifold or outages occur. Single pod deployments cannot accommodate growing demands of the application and load balancing across pods. Handle outages by eliminating a single point of failure. Minimize downtime and service interruptions by providing high availability through redundant pods.

Or automatically restart deployments if something goes wrong. We can work around these limitations with a ReplicaSet. A ReplicaSet ensures the right number of pods are always up and running. It always tries to match the actual state of the replicas to the desired state. A ReplicaSet adds or deletes pods for scaling and redundancy, which helps maintain availability. It replaces failing pods or deletes additional pods to maintain the desired state. And it supersedes a ReplicaController and should be used instead.

A ReplicaSet is created for when you create a deployment in your cluster. Deployments manage ReplicaSets, send pods declarative updates, and have many other useful features. That's why a ReplicaSet is best managed by a deployment. Kubernetes is designed to keep object types independent. That is why the ReplicaSet does not own any of the pods. Instead, it uses pod labels to decide which pods to acquire when bringing a deployment to the desired state. Let's look at a deployment template here.

The template metadata defines the labels and spec of potential pod candidates to add or delete. A ReplicaSet is automatically created for you when you create a deployment. To check this, create a deployment and then use a get ReplicaSet command to verify that the ReplicaSet is generated for you. By default, the ReplicaSet only replicates to a single pod. Additionally, if you describe the pod, you will see the pod's details and that it is controlled by the same ReplicaSet. To create a ReplicaSet from scratch, apply a YAML file with the kind attribute set to ReplicaSet as shown. If you define the number of replicas as 1, you get one pod.

This is similar to creating a default without specifying the number of replicas in your YAML file. Lets step through creating a ReplicaSet from scratch. First, use the create ReplicaSet command. The output shows a ReplicaSet was created. Confirm it was created by using the get pods command and observe the status as running and then use the get rs command, rs is short for ReplicaSet. And the output shows the name and other details of the newly created replica set and its pod. But remember, creating a deployment that includes a ReplicaSet is recommended over creating a standalone ReplicaSet.

Before you scale a deployment, you must ensure you have a deployment and a pod. To do this, Create a deployment using the create command. The output will confirm a deployment was created. The deployment creates a pod by default and you can confirm this with the getpods command. The output shows the pod name and other details. You can check the deployment details with the get deploy command. The output shows the deployment is named hello-kubernetes.

Now, once the deployment and pod are in place, use the scale command to scale the deployment and set the desired number of replicas. Here we set the number of replicas to three and the output confirms the deployment is scaled. If you use the getpods command you will see three pods running. The ReplicaSet created two new pods, one ending in 5mflw and the other ending in hbt7v. Lets observe how the ReplicaSet maintains the desired state when the pod is deleted. First, use the get pods command. Our three pods appear in the output as expected.

Now, use the delete pod command to delete the pod ending in 5mflw. The pod ending in 5mflw is deleted. And notice that the desired state does not match the actual state and that the deleted pod is replaced by a new pod automatically. Now use the get pods command again. The output shows the ReplicaSet immediately created a new pod ending in 6lw4r. To get the total number of pods back to three, the ReplicaSet maintains the desired state. Let's now observe how the ReplicaSet maintains desired state when a pod is created.

The getpods command shows our three pods from before. Use the create pod command to create a pod ending in mx9rp. Then use the get pods command again and the output now shows four pods. Desired state does not match actual state. Since the ReplicaSet always strives to match the actual state to the desired state. The new pod ending in mx9rp is marked for deletion and removed automatically. The get pods command now shows the total number of pods restored to three.

And once again the ReplicaSet maintains the desired state. In this video, you learned that a ReplicaSet provides high availability through redundancy. A ReplicaSet enables scaling by creating or deleting pods. You can create a ReplicaSet using the CLI or the YAML descriptor. A ReplicaSet always tries to match the actual state to the desired state. And a best practice is to use a deployment instead of a ReplicaSet directly. [SOUND]

---

### 2. [VIDEO TRANSCRIPT] Autoscaling Video • 7 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/iAa1C/autoscaling
- **Method:** `dom_transcript` | **Length:** 6149 chars

Hello, and welcome to auto-scaling. After watching this video, you will be able to define auto-scaling. Explain the three types of auto scalers, and demonstrate how each auto scaler works. Replica sets provide a good start for scaling, but you don't always want ten instances of your resource running. You should be able to scale as needed. Kubernetes auto-scaling helps optimize resource usage and costs by automatically scaling a cluster in line with demand. Kubernetes enables auto-scaling at two different layers, the cluster or node level and the pod level.

Three types of auto scalars are available in Kubernetes, horizontal pod auto scalar or HPA, vertical pod auto scalar or VPA, and cluster auto scalar or CA. To create auto-scaling, list the current number and state of pods. You have one pod in this scenario. A replica set is automatically created when you create a deployment. In order to auto-scale, you simply use the autoscale command with the requisite attributes. Min is the number of minimum pods. Notice that we have changed the value of min to two.

Max is the number of maximum pods, and CPU percent acts as a trigger that tells the system to create a new pod when the CPU usage reaches 50% across the cluster. In the background, the deployment still uses the replica set to scale up and down. Notice the numbers of replicas in this auto-scaled replica set has changed to two since the minimum number specified in the previous autoscale command was changed to two. Now, in Kubernetes, there are three autoscaling types. The horizontal pod auto scalar or HPA adjusts the number of replicas of an application by increasing or decreasing the number of pods. The vertical pod auto scalar or VPA adjusts the resource requests and limits of a container by increasing or decreasing the resource size or speed of the pods. The cluster auto scaler or CA adjusts the number of nodes in the cluster when pods fail to schedule or demand increases or decreases in relation to the nodes capacity.

In Kubernetes, an HPA automatically updates a workload resource like a deployment by horizontally scaling the workload to match the demand. Horizontal scaling or scaling out automatically increases or decreases the number of running pods as application usage changes. An HPA uses a cluster operator that sets targets for metrics like CPU or memory utilization and the maximum and minimum desired number of replicas. For example, the system load is low early in the morning, so one pod is sufficient. The HPA auto-scales the workload resource to meet usage demands. By 11:00 A.M. Peak load drives a need for three pods.

The HPA auto-scales the workload resource to meet usage demand. Usage drops in the afternoon, so the third pod is marked for deletion and removed, and usage drops even lower by 5:00 P.M. Another pod is marked for deletion and removed. Another way to enable auto-scaling is to manually create the HPA object for a YAML file. Similar to the autoscale command, you can set the minimum and maximum number of pods. The CPU percent flag shows up as, target CPU utilization percentage, and even though you can create an HPA autoscaler from scratch, you should use the autoscale command instead. A best practice is to scale horizontally, but there are some services you may want to run in a cluster, where horizontal scaling is impossible or not ideal.

Vertical scaling or scaling up refers to adding more resources to an existing machine. A VPA lets you scale a service vertically within a cluster. The cluster operator sets targets for metrics like CPU or memory utilization, similar to an HPA. The cluster then reconciles the size of the services pod or pods based on their current usage and the desired target. For example, the system load is low early in the morning, so system resources used by the pod are low. By 11:00 A.M. Peak load drives a need for more capacity.

The VPA auto-scales the pod by adding more system resources, CPU, and memory to meet the demand. Usage drops in the afternoon. The pod is auto-scaled to use fewer system resources, and usage drops even lower by 5:00 P.M. The pod is auto-scaled further to match the 7:00 A.M. Levels. You should not use VPAs with HPAs on resource metrics like CPU or memory. However, you can use them together on custom or external metrics.

A CA auto-scales the cluster itself, increasing or decreasing the number of available nodes that pods can run on. Pods are auto-scaled using HPA or VPA. But when the nodes themselves are overloaded with pods, you can use a CA to auto-scale the nodes so that the pods can rebalance themselves across the cluster. For example, the system load is low early in the morning, so existing nodes can handle the load. When demand increases, new pod requests come in, and the CA auto-scales the cluster by adding a new node and pod to meet the demand. By 11:00 A.M. Peak load brings the new node to full capacity.

When usage drops in the afternoon, unused pods are marked for deletion and removed. When usage drops even lower by 5:00 P.M. All pods in the new node are marked for deletion and removed. Then the node itself is marked and removed. A cluster auto scaler ensures there is always enough computer power to run your tasks, and that you aren't paying extra for unused nodes. For example, nights and weekends may have pure development or continuous integration testing loads, and clusters may have periods where all batch processing jobs are complete, and the new batch doesn't start until later in the day. Each autoscaler type is suitable in specific scenarios.

You should analyze the pros and cons of each to find the best choice. Using a combination of all three types ensures that services run stabely at peak load times, and costs are minimized in times of lower demand. In this video, you'll learn that. Auto-scaling enables scaling as needed at the cluster or node level and the pod level. You can auto-scale a deployment or a replica set. Autoscaler types include horizontal pod or HPA, vertical pod, or VPA, and cluster or CA, and a combination of all three autoscaler types often provides the most optimized solution. A

---

### 3. [READING] Deployment Strategies Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/hRiEX/deployment-strategies
- **Method:** `dom_reading_cml` | **Length:** 7810 chars

### Overview

A Kubernetes deployment strategy defines an application’s lifecycle that achieves and maintains the configured state for objects and applications in an automated manner. Effective deployment strategies minimize risk.

Kubernetes deployment strategies are used to:

- Deploy, update, or rollback ReplicaSets, Pods, Services, and Applications
- Pause/Resume Deployments
- Scale Deployments manually or automatically

### Types of deployment strategies

The following are six types of deployment strategies:

- Recreate
- Rolling
- Blue/green
- Canary
- A/B testing
- Shadow

You can use either a single deployment strategy or a combination of multiple deployment strategies.

### Recreate strategy

In the recreate strategy, Pods running the live version of the application are all shut down simultaneously, and a new version of the application is deployed on newly created Pods.

Recreate is the simplest deployment strategy. There is a short downtime between the shutdown of the existing deployment and the new deployment.

Recreate strategy steps include:

- A new version of the application (v2) is ready for deployment.
- All Pods running the current version (v1) are shut down or deleted.
- New (v2) Pods are created.

The rollback process is completed in the reverse order, replacing version 2 (v2) with version 1 (v1).

| Pros | Cons |
| --- | --- |
| Simple setup | Short downtime occurs between shutdown and new deployment |
| Application version completely replaced |  |

### Rolling (ramped) strategy

In a rolling strategy, each Pod is updated one at a time. A single v1 Pod is replaced with a new v2 Pod. Each v1 Pod is updated in this way until all Pods are v2. During a rolling strategy update, there is hardly any downtime since users are directed to either version.

Rolling strategy steps include:

- A new version of the application (v2) is ready for deployment.
- One of the Pods running the current version (v1) is shut down or deleted.
- A new (v2) Pod is created to replace the (v1) Pod that was removed.
- Steps 2 and 3 are repeated until all (v1) Pods are removed and replaced with (v2) Pods.

The rollback process is reversed, where v2 Pods are replaced by v1 Pods.

| Pros | Cons |
| --- | --- |
| Simple setup | Rollout/rollback takes time |
| Suitable for stateful applications that need to handle rebalancing of the data | You cannot control traffic distribution |

### Blue/green strategy

In a blue/green strategy, the blue environment is the live version of the application. The green environment is an exact copy that contains the deployment of the new version of the application. The green environment is thoroughly tested. Once all changes, bugs, and issues are addressed, user traffic is switched from the blue environment to the green environment.

Blue/green strategy steps include:

- Create a new environment identical to the current production environment.
- Design the new version and test it thoroughly until it is ready for production.
- Route all user traffic to the new version.

To perform a rollback, switch the environments back.

| Pros | Cons |
| --- | --- |
| Instant rollout/rollback (no downtime) | Expensive (requires double resources) |
| New version is available immediately to all users | Rigorous testing required before releasing to production |
|  | Handling stateful applications is difficult |

### Canary strategy

In a canary strategy, the new version of the application is tested using a small set of random users alongside the current live version of the application. Once the new version of the application is successfully tested, it is then rolled out to all users.

Canary strategy steps include:

- Design a new version of the application.
- Route a small sample of user requests to the new version.
- Test for efficiency, performance, bugs, and issues, and rollback as needed.
- Repeat steps 1 to 3. Once all issues are resolved, route all traffic to the new version.

Rollback has no downtime since few users are exposed to the new version.

| Pros | Cons |
| --- | --- |
| Convenient for reliability, error, and performance monitoring | Slow rollout, gradual user access |
| Fast rollback |  |

### A/B testing strategy

The A/B testing strategy, also known as split testing, evaluates two versions of an application (version A and version B). With A/B testing, each version has features that cater to different sets of users. You can select which version is best for global deployment based on user interaction and feedback.

A/B testing strategy steps include:

- Design a new version of the application by adding mostly UI features.
- Identify a small set of users based on conditions like weight, cookie value, query parameters, geolocalization, browser version, screen size, operating system, and language.
- Route requests from the user set to the new version.
- Check for bugs, efficiency, performance, and issues.
- Once all issues are resolved, route all traffic to the new version.

Rollbacks can be implemented, but downtime can impact the user.

| Pros | Cons |
| --- | --- |
| Multiple versions can run in parallel | Requires intelligent load balancer |
| Full control over traffic distribution | Difficult to troubleshoot errors for a given session, distributed tracing becomes mandatory |

### Shadow strategy

In a shadow strategy, a “shadow version” of the application is deployed alongside the live version. User requests are sent to both versions, and both handle all requests, but the shadow version does not forward responses back to the users. This lets developers see how the shadow version performs using real-world data without interrupting user experience.

To perform a rollback, switch the environments back.

| Pros | Cons |
| --- | --- |
| Performance testing with production traffic | Expensive (double resources) |
| No user impact | Not a true user test, can lead to misinterpreted results |
| No downtime | Complex setup |
|  | Requires monitoring for two environments |

### Deployment strategies summary

| Strategy | Zero Downtime | Real Traffic Testing | Targeted Users | Cloud Cost | Rollback Duration | NegativeUser Impact | Complexity of Setup |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recreate Version 1 is removed then version 2 is rolled out | X | X | X | •-- | ••• | ••• | - - - |
| Ramped Version 1 is replaced by a slow rollout of version 2 | ✓ | X | X | •-- | ••• | •-- | •-- |
| Blue/Green Version 2 is released together with version 1, then the traffic is switched to version 2 | ✓ | X | X | ••• | - - - | ••- | ••- |
| Canary Version 2 is first released to a subset of users, then fully rolled out when production ready | ✓ | ✓ | X | •-- | •-- | •-- | ••- |
| A/B Testing Version 2 is only released to a subset of users with specific traits | ✓ | ✓ | ✓ | •-- | •-- | •-- | ••• |
| Shadow Version 2 receives real-world traffic together with version A but doesn’t respond to users | ✓ | ✓ | X | ••• | - - - | - - - | ••• |

To create a good strategy:

- Consider the product type and the target audience
- Shadow and canary strategies use live user requests, as opposed to using a sample of users.
- The A/B testing strategy is useful if the version of the application requires minor tweaks or UI feature changes.
- The blue/green strategy is useful if your version of the application is complex or critical and needs proper monitoring with no downtime during deployment.
- The canary strategy is a good choice if you want zero downtime and are comfortable exposing your version of the application to the public.
- A rolling strategy gradually deploys the new version of the application. There is no downtime, and it is easy to roll back.
- The recreate strategy is a good choice if the application is not critical and users aren’t impacted by a short downtime.

---

### 4. [VIDEO TRANSCRIPT] Rolling Updates Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/UE6Rc/rolling-updates
- **Method:** `dom_transcript` | **Length:** 5527 chars

Welcome to Rolling Updates. After watching this video, you will be able to Explain what a rolling update is and how it works List the pre-steps before a rolling update can be applied and Demonstrate how to roll back a rolling update Rolling updates are automated updates that occur on a scheduled basis. They roll out automated and controlled app changes across pods, work with pod templates like deployments, and allow for rollback as needed. To prepare your application to enable rolling updates, add liveness probes and readiness probes to deployments. That way, deployments are appropriately marked as ready. Next, add a rolling update strategy to the YAML file. In this example, you are creating a deployment with 10 pods.

Your strategy is to have at least 50% of the pods always available. The max surge of 2 says that there can only be 2 pods added to the 10 you defined earlier. For a zero-downtime system, set the max unavailable to 0. Setting the max surge to 100% would double the number of pods and create a complete replica before taking the original set down after the rollout is complete. And sometimes, it is also useful to use the miniReadySeconds attribute to wait a few seconds before moving to the next pod in the rollout stage. Let's look at a working example of rolling out an application update. You have a deployment with 3 pods in your replica set.

Your application displays the message, Hello World! Your client has submitted a new request. And you have a new image for your application with a different message. Instead of the original text, you need to show Hello World v2 to your users. But you cannot have any downtime in your application. First, you need to build, tag, and upload this new image to Docker Hub. Your new software has been dockerized and then updated to Docker Hub with the name and tag hello-kubernetes-upcar-hello-kubernetes-colon-2.0.

These are simple Docker commands, not related to Kubernetes at all. Now, apply this new image to your deployment. You have the 3 pods from the first command. The second command sets the image flag to the updated tag image on Docker Hub. The output says the image has been updated. But let's verify if that actually happened. You can see the status of the rollout by using the rollout status command.

The API shows deployment hello-kubernetes successfully rolled out. That's great. Now, if you go back to the URL, you will see the new message Hello World v2. Sometimes, there are errors in a deployment, or the client can change their minds. Rollbacks are easy to implement in Kubernetes. Use an undo command on the rollout. Use the get pods command to confirm the rollout pods are terminated.

You will also see 3 new pods that are created as part of this rollback. If you visit the site again, you will see the original message. And that's how you roll back challenges to your application. Now, let's take a look at how rolling updates work, both all at once and one at a time. In an all-at-once rollout, all v1 objects must be removed before v2 objects can become active. Here, you see version 1 of an app with 3 pods running that users can access. When version 2 is deployed, new pods are created.

The version 1 pods are marked for deletion and remove. User access is blocked. Once the version 1 pods are removed, the version 2 pods become active and user access is restored. Notice the time lag between deployment and pod updates. In an all-at-once rollback, all v2 objects must be removed before v1 objects can become active. Let's see what an all-at-once rollback looks like. Here, you see version 2 of an app with 3 pods running that users can access.

When version 1 of the app is deployed, new pods are created. The version 2 pods are marked for deletion and removed. And user access is blocked. Once the version 2 pods are removed, the version 1 pods become active and user access is restored. In a one-at-a-time rollout, the update is staggered so user access is not interrupted. Here, you see version 1 of an app with 3 running pods that users can access. When version 2 is deployed, a new pod is created.

The first version 1 pod is marked for deletion and removed. And the v2 pod becomes active. Then, a second v2 pod is created. And the second version 1 pod is marked for deletion and removed. The second v2 pod becomes active. A third v2 pod is created. And the third version 1 pod is marked for deletion and removed.

And now, the third v2 pod becomes active. With a staggered update, user access is not interrupted. In a one-at-a-time rollback, the update rollback is staggered so user access is not interrupted. Let's see what a one-at-a-time rollback looks like. Here, you see version 2 of an app with 3 running pods that users can access. When version 1 of the app is deployed, a new pod is created. The first version 2 pod is marked for deletion and removed.

And the v1 pod becomes active. Now, a second v1 pod is created. The second version 2 pod is marked for deletion and removed. And the second v1 pod becomes active. Then, a third v1 pod is created. And the third version 2 pod is marked for deletion and removed. And the third v1 pod becomes active.

In this video, you learned that Rolling updates roll out app changes in a controlled and automated way. Rolling updates publish changes to applications without noticeable interruption. Rolling updates can rollback changes when an application needs to revert. And, rolling updates and rollbacks can be performed using all-at-once and one-at-a-time strategies.

---

### 5. [VIDEO TRANSCRIPT] ConfigMaps and Secrets Video • 6 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/ZxJVt/configmaps-and-secrets
- **Method:** `dom_transcript` | **Length:** 5558 chars

Welcome to Config Maps and Secrets. After watching this video, you will be able to Identify important config map characteristics Describe config map capabilities Describe three ways to create a config map and Describe three ways to create a secret As software developers, a good practice to adopt is to avoid hard-coding configuration variables in application code by keeping the configuration variables separate so that any changes in configuration settings do not require code changes. A config map is an API object that stores non-confidential data in key-value pairs and is meant for non-sensitive information as they do not provide secrecy or encryption. In addition, a config map provides configuration data to pods and deployments so that the configuration data is not hard-coded inside the application code. Data stored in a config map cannot exceed one megabyte. For larger amounts of data, consider mounting a volume or use a separate database or file service. A config map has optional data and binary data fields and in this case, there is no spec field in the template and the config name must be a valid DNS subdomain name.

A config map is reusable for multiple deployments, thus decoupling the environment from the deployments themselves. You can create a config map by using string literals, by using an existing properties or key equals value file or by providing a config map YAML descriptor file. You can use the first and second ways to help create such a YAML file. The deployment or pods consume a config map by using environment variables with the config map key ref attribute or by mounting a file using the volumes plugin. Kubernetes applies the config map to the pod or the deployment just before running the pod or deployment. You'll use the environment variable directly in the YAML file. The message variable is used in the JavaScript file as process.env.message.

Apply this development descriptor to our deployment and the application displays the string hello from the config file. The result is excellent, but the message is hard-coded in the descriptor file. Let's change this situation by using a config map. The simplest way to provide a config map is to provide a key value pair in the center of the config map command. After this first step, the second step is to tell our deployment about the new message variable and specify its location for pickup. You do that by adding the environment section in the deployment descriptor as shown and using the value from attribute to point to the config map created in the first step. In this case, the deployment will look for a key named message in the config map named myconfig.

Another way to add the message variable in the config map is to use a file that contains all environment variables in the key equals value format. Such a file is useful for adding many variables instead of listing those variables one by one on the command line. Here is a file with just one message key and a value hello from the my.properties file. You can now create the config map by using the from file flag. Notice that the key is my.properties in the deployment descriptor section. To use the config map in the server.js file, refer to it as process.env.message. Use the describe command to get the YAML output.

Then view the environment section. If you specify a directory to the from file flag, the entire directory is loaded into the config map. You can also load a specific file with a key by using the from file equals key equals file name format. Finally, you can use a YAML file with the config map descriptor and apply that file. In our case, we have saved the output from kubectl to get config map. To get config map as a YAML file called my-config.yaml. The first command indicates that there is no config map to begin with.

Here, you are creating the config map.yaml file. You'll now apply the YAML file to your cluster, which creates the config map. Note the message in the config map file description. Using the YAML file will get you the same results as the other methods. Now, working with a secret is like working with a config map. First, create a secret using a string literal. Next, the get command verifies that the secret was created.

Finally, to prove that our secret is indeed a secret, use the describe command and check that you don't see any secret written using display text. You can print out the secret in YAML format, and you'll see that the value is fully encoded. To use the secret, add another environment to the deployment descriptor as shown, and then use the application key by referring to the application as process.env.API_CREDS. The screenshot displays the secret along with other environmental variables from the node.js file. Another way to use the secret key in your application is to use volume mounts. Create the same secret as done previously. In the descriptor YAML file, use a volume for the secret with a corresponding volume mount.

Each container in the descriptor file has its own volume mount, but shares the volume. The api-creds secret is mounted as a file at etc/API, and the application will read and process the file to extract the secret. In this video, you learned that you can use a config map to provide variables for your application. You can create a config map by using a string literal, by using a properties file, or by using YAML. You can use a secret to provide sensitive information to your application. And you can create a secret by using a string literal, by using environment variables, or by using volume mounts.

---

### 6. [VIDEO TRANSCRIPT] Service Binding Video • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/lecture/UVWRU/service-binding
- **Method:** `dom_transcript` | **Length:** 4556 chars

Welcome to Service Binding. After watching this video, you will be able to explain the roles and goals of service binding. Describe how to bind a Kubernetes cluster to an external service. Identify commands to retrieve the secrets in your Kubernetes cluster, and describe how to use service binding in apps. What is service binding? Service binding is the process needed to consume external services or backing services, including REST APIs, databases, and event buses in our applications. Service binding manages configuration and credentials for back end services while protecting sensitive data.

In addition, service binding makes service credentials available to you automatically as a secret. Service binding consumes the external service by binding the application to a deployment. Then the application code uses the credentials from the binding and calls the corresponding service. Here, you can see an architectural diagram that illustrates the binding of a Kubernetes cluster to an external service. Next, let's learn the steps required to bind the service to your application. Let's use an IBM Cloud Service example. Service binding quickly create service credentials for an IBM Cloud service.

You create the service credentials using IBM's Public Cloud service endpoint, and then store or bind your service credentials in a Kubernetes secret in your cluster. Here's how to bind an IBM Cloud service to your cluster. First, you provision an instance of the service. Then you bind the service to your cluster to create service credentials for your service that use the public cloud service endpoint. Next, store the credentials in a Kubernetes secret. Finally, you configure your app to access the service credentials in the Kubernetes secret. The IBM Cloud catalog provides various services that range from visual recognition to natural language processing and creating chat bots.

We are using the tone analyzer service to explain binding. This service uses linguistic analysis to detect tone in a given text. The service provides an SDK in Java script. You bind the service to the deployment so that the credentials are automatically available. The code then uses the credentials from the binding and calls the tone analyzer service. Now that you know the steps, let's examine some code. In the first step, provision an instance of the service by creating the service instance using the command line interface.

You can also provision an instance of the service by using the catalog on the IBM Cloud website. In the second step, you bind this newly created service instance to your cluster by using the service bind command. IBM Cloud Service Binding automatically creates a Kubernetes secret with the service credentials. The credentials of a service instance are base 64 encoded and stored inside your secret in the JSON format. Now that the service is bound to your cluster, here in Step 3, you can verify your secret object. The Get Secrets command shows all the secrets in your Kubernetes cluster. Or you can retrieve the same secrets in the Kubernetes dashboard user interface, as well as on the IBM Cloud Kubernetes service.

To access the data in your secret, choose one of the following options. Mount the secret as a volume to your Pod, based on the specifications provided in Step 1. This action creates a JSON formatted file named binding that is stored in the Volume Mounts directory. The binding file includes all information and credentials required to access the IBM Cloud Service. Or you can reference the secret in environment variables. The environment variables binding, API key, binding.username, and binding.password, correspond to the API Key username and password of the Watson Tone analyzer service instance created in the previous step. The displayed code snippet shows a sample node.js application using the binding.API Key, the binding.username, and the binding.password environment variable inside an express.JS application that will be deployed to the IBM Cloud Kubernetes Service.

In this video, you'll learn that binding an external service to your deployment automatically provides the credentials to use the service inside the code. Credentials are stored as a secret that can be consumed using volume mounts and volumes. Binding manages configuration and credentials for back end services while protecting sensitive data, and you can configure your app to use the credentials stored in the secret, either by mounting the secret as a volume to your pod or by referencing the secret in environment variables.

---

### 7. [READING] Transforming Retail - The Impact of Kubernetes and Containerization Reading • 10 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/oYN53/transforming-retail-the-impact-of-kubernetes-and-containerization
- **Method:** `dom_reading_cml` | **Length:** 6289 chars

### Objectives

After completing this reading, you will be able to:

- Identify key challenges in the retail sector and strategies to address them
- Recognize the role of Kubernetes and containerization as a transformative solution
- Describe the impact of Kubernetes and containerization on retail

### Critical Hurdles in the Retail Sector

In the fast-paced and fiercely competitive field of retail, digital infrastructure plays a pivotal role in facilitating seamless operations across both in-store and online channels. With the growing demand for seamless shopping experiences and the need to handle large traffic spikes during peak seasons, retailers face significant IT challenges. These include scalability issues, slow deployment processes, inefficient resource utilization, and inadequate disaster recovery mechanisms.

### Let's delve into each of these challenges individually:

- Scalability issues Retail platforms often struggle to manage sudden surges in traffic during sales events or holiday seasons. Traditional systems are not designed to scale efficiently, leading to performance issues and downtime.
- Deployment bottlenecks Introducing new features and updates can be slow and cumbersome. Retail websites must frequently introduce new offers or sales to keep customers engaged. However, making these changes can be a slow and challenging process. Retailers need to ensure minimal disruption to services while deploying changes.
- Resource utilization Striking the right balance between over-provisioning and underutilization of resources poses a significant challenge. Poor resource management not only drives up operational costs but also wastes computing power, compounding the problem further.
- Disaster recovery Though every organization has a Disaster Recovery Plan and a Business Continuity Plan in place, many retailers lack robust strategies, leaving them vulnerable to significant losses during system failures. Ensuring business continuity during outages is critical.

#### Now, let's explore some strategic goals to address these challenges:

- Enhance scalability performance Develop a flexible infrastructure that can dynamically scale to accommodate fluctuating loads while maintaining optimal performance.
- Accelerate deployment cycles Establish an efficient deployment process to smoothly introduce new features and updates with minimal downtime and service interruptions.
- Optimize resource utilization Enhance resource management practices to drive cost savings and operational efficiency.
- Strengthen disaster recovery Create a reliable disaster recovery plan to reduce downtime and maintain uninterrupted operations.

#### Transformative solutions: Leveraging Kubernetes and containerization

Transition to microservices architecture

- Breaking down large applications into smaller, independent microservices allows for flexible and scalable application development. It is possible to develop, implement, and scale each microservice independently.
- Using Docker to containerize these microservices ensures consistency across development, testing, and production environments.

Kubernetes for orchestration

- Orchestration: Kubernetes manages the deployment, scaling, and operation of containerized applications, providing an efficient and automated way to handle the infrastructure.
- Load balancing and auto-scaling: Kubernetes enables applications to adapt dynamically to varying traffic loads, ensuring consistent performance during peak hours. Furthermore, it scales down during off-peak hours to reduce computational costs.

Implementing CI/CD pipelines:

- Continuous Integration/Continuous Deployment (CI/CD): Automating the build, test, and deployment process with tools like Jenkins, GitLab CI/CD, or CircleCI accelerates development cycles and improves reliability.
- Blue-green deployments: Kubernetes supports blue-green deployment strategies, allowing for seamless updates and quick rollbacks if needed.

Resource management and cost optimization:

- Dynamic resource allocation: Kubernetes optimizes resource allocation based on real-time demand, improving utilization and reducing waste.
- Monitoring: Implementing monitoring (Prometheus / Grafana) solutions provides insights into system performance and resource usage.

Enhancing disaster recovery and high availability

- Multi-region deployments: Deploying Kubernetes clusters across multiple regions enhances high availability and disaster recovery capabilities.
- Automated backups: Using tools like Velero for regular backups of Kubernetes cluster states and persistent volumes ensures data integrity and quick recovery in case of failure.

### Aftermath: Kubernetes-containerization impact on retail

- Improved scalability and performance: Retailers can seamlessly manage traffic surges during sales events without downtime or performance issues. Retail platforms can smoothly handle large traffic during major holiday sales, thanks to Kubernetes’ auto-scaling capabilities.
- Faster deployment cycles: With CI/CD pipelines, retailers can deploy new features and updates multiple times a day, reducing time-to-market and enhancing customer satisfaction. It reduced feature deployment time from weeks to minutes.
- Optimized resource utilization: Dynamic resource management leads to a drastic reduction in operational costs. Retailers can benefit from scaling down resources during off-peak hours, resulting in significant cost savings.
- Enhanced disaster recovery: Multi-region Kubernetes clusters and automated backup solutions ensure near-zero downtime during outages. Retail platforms can maintain uninterrupted service during data center failures, minimizing potential revenue losses.

### Summary

In this reading, you learned that:

- With the growing demand for seamless shopping experiences and the need to handle large traffic spikes during peak seasons, retailers face significant IT challenges.
- The adoption of Kubernetes and containerization is revolutionizing the IT infrastructure of the retail industry.
- Through embracing microservices and harnessing Kubernetes’ orchestration capabilities, retailers have seen significant strides in scalability, deployment speed, resource optimization, and disaster recovery.

#### Author

Lavanya Rajalingam

---

### 8. [READING] Summary & Highlights: Managing Applications with Kubernetes Reading • 2 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/KItzh/summary-highlights-managing-applications-with-kubernetes
- **Method:** `dom_reading_cml` | **Length:** 922 chars

Congratulations! You have completed this module. At this point, you know:

- A ReplicaSet enables scaling by creating or deleting pods.
- A ReplicaSet always tries to match the actual state to the desired state.
- Autoscaling enables scaling as needed at the cluster or node level, and the pod level.
- Autoscaler types include horizontal pod (HPA), vertical pod (VPA), and cluster (CA).
- Rolling updates roll out app changes in a controlled and automated way.
- Rolling updates and rollback can be performed using all-at-once and one-at-a-time strategies.
- ConfigMaps are used to provide variables for your application.
- Secrets are used to provide sensitive information to your application.
- Binding an external Service to your deployment automatically provides the credentials to use the Service inside the code.
- Binding manages configuration and credentials for back-end Services while protecting sensitive data.

---

### 9. [READING] Module 3 Cheat Sheet: The kubectl CLI Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/Cvqqp/module-3-cheat-sheet-the-kubectl-cli
- **Method:** `dom_reading_cml` | **Length:** 613 chars

| Command | Description |
| --- | --- |
| kubectl autoscale deployment | Autoscales a Kubernetes Deployment. |
| kubectl create configmap | Creates a ConfigMap resource. |
| kubectl get deployments -o wide | Lists deployments with details. |
| kubectl get hpa | Lists Horizontal Pod Autoscalers (hpa) |
| kubectl scale deployment | Scales a deployment. |
| kubectl set image deployment | Updates the current deployment. |
| kubectl rollout | Manages the rollout of a resource. |
| kubectl rollout restart | Restarts the resource so that the containers restart. |
| kubectl rollout undo | Rollbacks the resource. |

---

### 10. [READING] Module 3 Glossary: Managing Applications with Kubernetes Reading • 5 min
- **URL:** https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift/supplement/jhQGa/module-3-glossary-managing-applications-with-kubernetes
- **Method:** `dom_reading_cml` | **Length:** 2200 chars

| Term | Definition |
| --- | --- |
| Cluster Autoscaler | Also known as CA. An API resource that autoscales the cluster itself, increasing and decreasing the number of available nodes that pods can run on. |
| Config Map | An API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume. |
| Horizontal Pod Autoscaler | Also known as:HPA An API resource that automatically scales the number of Pod replicas based on targeted CPU utilization or custom metric targets. |
| Linguistic Analysis | Detects the tone in a given text. |
| IBM Cloud catalog | provides various Services that range from visual recognition to natural language processing and creating chatbots. |
| Persistent Volume | An API object that represents a piece of storage in the cluster. Available as a general, pluggable resource that persists beyond the lifecycle of any individual Pod. |
| Persistent Volume Claim | Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container. |
| Rolling Updates | Provide a way to roll out application changes in an automated and controlled fashion throughout your pods. Rolling updates work with pod templates such as deployments. Rolling updates allow for rollback if something goes wrong. |
| Secrets | Stores sensitive information, such as passwords, OAuth tokens, and ssh keys. |
| Service binding | is the process needed to consume external Services or backing Services, including REST APIs, databases, and event buses in your applications. |
| Tone Analyzer Service | is used for explaining service binding. This IBM Cloud Service uses linguistic analysis to detect tone in a given text. |
| Vertical Pod Autoscaler also known as VPA | An API resource that adds resources to an existing machine. A VPA lets you scale a service vertically within a cluster. |
| Volume | A directory containing data, accessible to multiple containers in a Pod. |
| Volume Mount | entails mounting of the declared volume into a container in the same Pod. |
| Volume Plugin | A Volume Plugin enables integration of storage within a Pod. |

---
