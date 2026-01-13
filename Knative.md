It was set
```Shell
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```
A configuration that somehow worked:
```shell
minikube config set driver docker
minikube delete --all --purge
minikube start
minikube ssh
# in the minikube container terminal:
sudo apt-get -y install qemu-user-static
minikube stop
minikube start
kn quickstart minikube
```
Other Minikube commands:
```shell
minikube dashboard

minikube config set memory 8192
minikube config set cpus 4
minikube config set kubernetes-version 1.16.2
minikube config set vm-driver kvm2
minikube config set container-runtime crio
minikube config view

minikube addons enable ingress

minikube delete
```

As informed by the output of the `quickstart` plugin, one has to open in a separate terminal a tunnel to the cluster:
```Shell
minikube tunnel --profile knative
```
Some testing with example service
```Shell
kn service create hello --image ghcr.io/knative/helloworld-go:latest --port 8080 --env TARGET=World
kn service list
curl "$(kn service describe hello -o url)"
kn service update hello --env TARGET=Knative
kn revisions list
kn service update hello --traffic hello-00001=50 --traffic @latest=50
```
Enabling building functions in the cluster
```Shell
kubectl apply -f https://storage.googleapis.com/tekton-releases/pipeline/previous/v0.49.0/release.yaml
kubectl create clusterrolebinding default:knative-serving-namespaced-admin --clusterrole=knative-serving-namespaced-admin  --serviceaccount=default:default
```
Creating a function
```bash
func create -l quarkus helloquarkus
```
Deploying the function
```Shell
func deploy -b=s2i --remote --registry docker.io/szymonharabasz -p helloquarkus
```
Calling the function
```Shell
curl http://helloquarkus.default.127.0.0.1.sslip.io
```
## Generals
From the Kubernetes perspective Knative Serving runs one `controller` process. It has a group if controllers in the sense of controlling theory, that run as goroutines and implement Go `Reconciller` interface.  They are:
- `configuration`, `revision`, `route`, `service`
- `labeler`, `serverlessservice`, `gc`

The Autoscaler assigns routes for which no instances are available to Activator. The Activator "pokes" the Autoscaler when a request arrives. When instances are becoming available, the Activator remains in the data path as a throttling, buffering proxy for the traffic. Once the Autoscaler believes that enough instances are available, it removes the Activator from the path by updating the Ingress configuration.
#### A simple Serving YAML
```yaml
apiversion: serving.knative.dev/v1
kind: Configuration
metadata:
	name: helloworld-example
spec:
	template:
		metadata:
			name: this-too-is-a-name # name for the revision
		spec:
			containers:
			- name: first-and-only-container
			  image: gcr.io/knative-samples/helloworld-go
			  env:
			  - name: TARGET
			    value: "It has a name!"
			  imagePullSecrets:
			    # name of a Kubernetes Secret
			  - name: registry-credentials-for-example-com 
```
Use if with:
```shell
kubectl apply -f helloworld.yaml
```
Environment variables injected by Knative:
`PORT`, `K_REVISION`, `K_CONFIGURAION`, `K_SERVICE`

Example Kubernetes ConfigMap and Secret
```yml
apiversion: v1
kind: ConfigMap
metadata:
	name: example-configmap
data:
	foo: "bar"

apiversion: v1
kind: Secret
metadata:
	name: example-secret
type: Opaque
data:
	password: "password123"
```
Apply and use it with `kn`:
```shell
kubectl applt -f example-configmap.yaml example-secret.yaml
kn service update hello-example --env-from configmap:example-configmap \
	--env-fron secret:example-secret
```
Using them in the YAML file:
```yml
...
spec:
	template:
		spec:
			containers:
			- image: ...
			  envFrom:
			  - configMapRef:
				  name: example-configmap
			  - secretRef:
				  name: example-secret
```
Other way, allowing to select which keys in a ConfigMap/Secret are mapped an to which environment variables:
```YAML
...
containers:
- image: ...
  env: 
  - name: FOO
    valueFrom:
		configMapKeyRef:
			name: example-configmap
			key: foo
  - name: PASSWORD
    valueFrom:
		secretKeyRef:
			name: example-secret
			key: password
```

Mounting configuration as a `tmpfs` filesystem:
```shell
kn service update hello-example --mount /sikrits=secret:example-secret
```
In YAML:
```yaml
spec:
	volumes:
	- name: sikkrits-9034cf59
	  secret:
		secretName: example-secret
	containers:
	  name: ...
	  voumeMounts:
	  - mountPath: /sikkrits
	    name: exsec-9034cf59
	    readonly: true
```

Probes:
```yaml
containers:
- name: ...
  image: ...
  livenessProbe:
	httpGet:
	  path: /deadoralive
  readinessProbe:
    tcpSocket:
```
With Knative, there is no `port`, instead `$PORT` is used by default.

Consumption limits:
```shell
kn service update hello-example \
	--requests-cpu 500m --requests-memory 256Mi
	--limits-cpu 800m --limits-memoty 512Mi
```
In YAML:
```yaml
containers:
- name: ...
  image: ...
  resources:
    requests:
      cpu: 500m
      memory: 256Mi
    limits:
	  cpu: 800m
	  memory: 512Mi
```

Timeout in seconds and container concurrency:
```yaml
spec:
	template:
		spec:
			timeoutSeconds: 600 # highest possible without reconfiguring the 
								# installation
			containerConcurrency: 20 # requests that can be handled 
									 # concurrently by my container 
```

Defining routes
```YAML
apiversion: serving.knative.dev/v1
kind: Route
metadata:
	name: route-example
spec:
	traffic:
	- configurationName: hello-example
	  revisionName: ...
	  latestRevision: true
	  percent: 100
```
One has to take into account logical constraints between having `revisionName` present and `latestRevision` set to `true` or `false`. 

Revisions can be tagged and untagged, which influences how routes work:
```shell
kn service update service-name --tag revision1=tag1 --tag revision2=tag2 \
	--tag revision3=tag3
kn service update service-name --untag tag3
```
One can then call specific revisions by separate URLs:
```shell
curl http://tag2-service-name.default.example.com
```
And tags can be used in traffic splitting:
```shell
kn service update service-name --traffic tag1=23 --traffic tag2=56 \
	--traffic @latest=22
```
## Eventing
Creating a Broker:
```sh
kn broker create default
```
Creating a useful CloudEvents Player service:
```sh
kn service create cloudevents-player \
	--image ruromero/cloudevents-player:latest 
	--env BROKER_URL=http://default
```
Creating a triggrr:
```sh
kn trigger create cloudevents-player --sink cloudevents-player
```
where the service created before is also a Sink. It was already a source by just being able to send events and knowing the address of the Broker. Deleting a trigger:
```sh
kn trigger delete cloudevents-player
```
More specifically, any Kubernetes record with the fields `Sink` and `CloudEventOverrides` is treaded as a Source by Knative through duck typing.
Listing defined Source types:
```sh
kn source list-types
```
Using a built-in `ping` Source:
```sh
kn source ping create ping-player \
	--sink http://cloudevents-player.default.example.com
kn source ping update ping-player \
	--data '{"foo":"and likewise bar"}'
```
Setting any Kubernetes record (instead of a URL) as a Sink:
```sh
kn source ping update ping-player --sink ksvc:cloudevents-player
```
Or more explicitly for a Knative Service:
```sh
kn source ping update ping-player --sink service:cloudevents-player
```
CloudEvents can be created by making a POST request with headers corresponding to CloudEvent attributes. The name of a header is the name of the attribute prefixed with `ce-`.
Required attributes:
`specversion` - the only value is `1.0` 
`source` - like `cdn.example.com`
`type` - like `com.example.cdn/flush`
`id` - best to use UUID v4
Optional attributes:
`datacontenttype` - like `application/json`
`dataschema`, `subject`, `type`
Extension attributes:
`dataref`,`traceparent`,`tracestate`,`partitionkey`,`rate`,`sequencetype`,`sequence`.
#### Theory behind autoscaling
Average concurrent requests in a sample of instances:
$$
\langle N_\mathrm{req}\rangle=
\frac{\sum_\mathrm{intance}N_\mathrm{req}(\mathrm{instance})}{N_\mathrm{intance}}.
$$
Average concurrent requests in a time window:
$$
\bar{N}_\mathrm{req}=
\frac{\sum_\mathrm{intance}N_\mathrm{req}(\mathrm{instance})}
{N_\mathrm{buckets}}
$$
Target concurrent requests per instance:
$$
\odot N_\mathrm{req}=\max(N_\mathrm{req})\cdot\odot U,
$$
where $U$ - utilisation. Then **desired instances**:
$$
\odot N_\mathrm{instance}=\frac{\bar{N}_\mathrm{req}}{\odot N_\mathrm{req}}.
$$
Absolute instance error:
$$
\sigma(N_\mathrm{instance})=\odot N_\mathrm{instance}-N_\mathrm{instance}.
$$
Relative error:
$$
\delta(N_\mathrm{instance})=\frac{\sigma(N_\mathrm{instance})}{N_\mathrm{instance}}.
$$
