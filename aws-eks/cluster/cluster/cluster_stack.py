
##
## From https://aws.amazon.com/tutorials/deploy-webapp-eks/module-one/
##

from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_eks as eks,
    aws_ec2 as ec2   
)

from aws_cdk.lambda_layer_kubectl_v28 import KubectlV28Layer
from constructs import Construct
import yaml

class ClusterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a master role 
        iam_role = iam.Role(self, id=f"{construct_id}-iam",
                    role_name=f"{construct_id}-iam", assumed_by=iam.AccountRootPrincipal())
         
         # Create and EKS Cluster 
        eks_cluster = eks.Cluster(
            self, id=f"{construct_id}-cluster",
            cluster_name=f"{construct_id}-cluster", 
            masters_role=iam_role,
            default_capacity_instance=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            version=eks.KubernetesVersion.V1_28,
            kubectl_layer=KubectlV28Layer(self, "KubectlLayer")
        )

        # Read the deployment config
        with open("../cdk8s/dist/cdk8s-deployment.k8s.yaml", 'r') as stream:
             deployment_yaml = yaml.load(stream, Loader=yaml.FullLoader)

        # Read the service config
        with open("../cdk8s/dist/cdk8s-service.k8s.yaml", 'r') as stream:
             service_yaml = yaml.load(stream, Loader=yaml.FullLoader)

        eks_cluster.add_manifest(f"{construct_id}-app-deployment", deployment_yaml)
        
        eks_cluster.add_manifest(f"{construct_id}-app-service", service_yaml)
