from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import BFDConfigSerializer, BGPPeerGroupSerializer, BGPPeerSerializer, BGPSessionConfigSerializer, VNISerializer, VXLANSerializer

class BFDConfigViewSet(NetBoxModelViewSet):
    queryset = models.BFDConfig.objects.prefetch_related('tags')
    serializer_class = BFDConfigSerializer

class BGPSessionConfigViewSet(NetBoxModelViewSet):
    queryset = models.BGPSessionConfig.objects.prefetch_related('tags', 'bfd_config') #prefetch_related prevents n+1 querie problem by bulk querying these relations
    serializer_class = BGPSessionConfigSerializer

class BGPPeerViewSet(NetBoxModelViewSet):
    queryset = models.BGPPeer.objects.prefetch_related('tags', 'device', 'session_config')
    serializer_class = BGPPeerSerializer

class BGPPeerGroupViewSet(NetBoxModelViewSet):
    queryset = models.BGPPeerGroup.objects.prefetch_related('tags', 'device', 'session_config', 'peers')
    serializer_class = BGPPeerGroupSerializer

class VNIViewSet(NetBoxModelViewSet):
    queryset = models.VNI.objects.prefetch_related('tags', 'vlan')
    serializer_class = VNISerializer

class VXLANViewSet(NetBoxModelViewSet):
    queryset = models.VXLAN.objects.prefetch_related('tags', 'vni')
    serializer_class = VXLANSerializer