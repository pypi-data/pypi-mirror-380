from kubernetes import client, config
from kubernetes.client.rest import ApiException

def create_job(api_instance,ipfs_cid, app_name):
    container = client.V1Container(
        name="buildkit",
	    image="andreasoikonomakis/oasees-builder:latest",
        #image="oasees-builder",
        #image_pull_policy="Never",
        security_context=client.V1SecurityContext(privileged=True),
        command=["/entrypoint.sh"],
        args=["/bin/bash", "-c", f"python3 /download_ipfs.py http://ipfs-kubo-service.default.svc.cluster.local:5002 {ipfs_cid} . && "
              f"nerdctl -a /run/k3s/containerd/containerd.sock --namespace k8s.io build -t {app_name}:oasees ."],
        env=[
            client.V1EnvVar(name="IPFS_CID", value=ipfs_cid),
            client.V1EnvVar(name="app_name", value=app_name)
        ],
        volume_mounts=[client.V1VolumeMount(mount_path="/run/k3s/containerd/containerd.sock", name="containerd-socket")]
    )
    
    volume = client.V1Volume(
        name="containerd-socket",
        host_path=client.V1HostPathVolumeSource(path="/run/k3s/containerd/containerd.sock", type="Socket")
    )

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "buildkit"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container], volumes=[volume], node_selector={"node-role.kubernetes.io/master" : "true"})
    )

    spec = client.V1JobSpec(template=template, ttl_seconds_after_finished=1)

    job_name="image-build-job-{}".format(app_name)

    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name),
        spec=spec
    )

    resp=""
    try:
        api_response = api_instance.create_namespaced_job(body=job,namespace="default")
        resp="Job {} created".format(job_name)
    except ApiException as e:
        resp="Error for Job {}".format(job_name)


    return resp


def create_load_job(ipfs_api_url,api_instance,ipfs_cid, app_name, worker_node_name,worker_node_user):
    container = client.V1Container(
        name="buildkit",
	    image="andreasoikonomakis/oasees-loader:latest",
        #image="oasees-builder",
        #image_pull_policy="Never",
        security_context=client.V1SecurityContext(privileged=True),
        command=["/entrypoint.sh"],
        args=["/bin/bash", "-c",
                f"python3 /download_ipfs.py {ipfs_api_url} {ipfs_cid} {app_name} . && \
                nerdctl -a /run/k3s/containerd/containerd.sock --namespace k8s.io load --all-platforms -i {app_name} && \
                envsubst < /manifests/template.yaml | kubectl apply -f -"
            ],
        env=[
            # client.V1EnvVar(name="IPFS_CID", value=ipfs_cid),
            client.V1EnvVar(name="IMAGE_NAME", value=app_name.split(".")[0]),
            client.V1EnvVar(name="NODE_NAME", value=worker_node_name)
        ],
        volume_mounts=[client.V1VolumeMount(mount_path="/run/k3s/containerd/containerd.sock", name="containerd-socket"),
                       client.V1VolumeMount(mount_path="/manifests/template.yaml", name="template-app-deployment")]
    )
    
    volume = client.V1Volume(
        name="containerd-socket",
        host_path=client.V1HostPathVolumeSource(path="/run/k3s/containerd/containerd.sock", type="Socket")
        )
    volume_b = client.V1Volume(
        name="template-app-deployment",
        host_path=client.V1HostPathVolumeSource(path="/home/"+worker_node_user+"/.oasees_sdk/template.yaml", type="File")
        )
    

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "buildkit"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container], volumes=[volume,volume_b],node_selector={"node-role.kubernetes.io/master" : "true"},service_account_name="loader")
    )

    spec = client.V1JobSpec(template=template, ttl_seconds_after_finished=1)

    job_name="image-loading-job-{}".format(app_name)

    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name),
        spec=spec
    )

    resp=""
    try:
        api_response = api_instance.create_namespaced_job(body=job,namespace="default")
        resp="Job {} created".format(job_name)
    except ApiException as e:
        resp="Error for Job {}".format(job_name)
        print(e)


    return resp
