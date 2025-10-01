from typing import Optional
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from dcim.models import Device
from utilities.choices import ChoiceSet

from .constants import APP_LABEL

class AddressFamilyChoices(ChoiceSet):
    CHOICES = [
        ('ipv4_unicast', 'IPv4 Unicast', 'blue'),
        ('ipv6_unicast', 'IPv6 Unicast', 'purple'),
        ('ipv4_labeled_unicast', 'IPv4 Labeled Unicast', 'blue'),
        ('ipv6_labeled_unicast', 'IPv6 Labeled Unicast', 'purple'),
        ('vpnv4_unicast', 'VPNv4 Unicast', 'blue'),
        ('vpnv6_unicast', 'VPNv6 Unicast', 'purple'),
        ('ipv4_multicast', 'IPv4 Multicast', 'blue'),
        ('ipv6_multicast', 'IPv6 Multicast', 'purple'),
        ('vpnv4_multicast', 'VPNv4 Multicast', 'blue'),
        ('vpnv6_multicast', 'VPNv6 Multicast', 'purple'),
        ('ipv4_flowspec', 'IPv4 Flowspec', 'red'),
        ('vpnv4_flowspec', 'VPNv4 Flowspec', 'red'),
        ('vpls', 'VPLS', 'orange'),
        ('evpn', 'EVPN', 'green'),
    ]

class BFDConfig(NetBoxModel):
    """
    Configuration model for BFD (Bidirectional Forwarding Detection) profiles.
    """
    hello_interval = models.PositiveIntegerField(
        verbose_name='Hello Interval',
        help_text='The minimum interval for sending BFD control packets.'
    )

    multiplier = models.PositiveIntegerField(
        verbose_name='Dead Multiplier',
        help_text='Number of hello packets missed before the session is declared down.'
    )

    description = models.CharField(
        max_length=256,
        blank=True
    )

    class Meta:
        ordering = ('hello_interval', 'multiplier', 'description')
        ## Ensures that each combination of interval and multiplier is unique
        # unique_together = ('hello_interval', 'multiplier')

    def __str__(self):
        """
        Returns a human-readable string representation of the BFD configuration.
        """
        return f'Hello: {self.hello_interval}, Multiplier: {self.multiplier}, Desc: {self.description}'
    
    def get_absolute_url(self):
        '''Get the absolute URL to this object'''
        return reverse(f'plugins:{APP_LABEL}:bfdconfig', args=[self.pk])
    



class BGPSessionConfig(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    address_families = ArrayField(
        base_field=models.CharField(max_length=30, choices=AddressFamilyChoices),
        blank=True,
        null=True
    )

    peer_asn = models.BigIntegerField(
        blank=True,
        null=True
    )

    import_policy = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    export_policy = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    next_hop_self = models.BooleanField(
        default=False
    )

    hardcoded_description = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    hello_interval = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    keepalive_interval = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    ebgp_multihop = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    unencrypted_password = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    encrypted_password = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    source_interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    source_ip = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    local_asn = models.BigIntegerField(
        blank=True,
        null=True
    )
    
    bfd_config = models.ForeignKey(
        to=BFDConfig,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:bgpsessionconfig', args=[self.pk])
    

class BGPPeer(NetBoxModel):
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='bgp_peers',
        blank=False,
        null=False
    )

    peer_ip = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='bgp_peer'
    )

    session_config = models.ForeignKey(
        to=BGPSessionConfig,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=100,
        blank=True
    )

    @property
    def remote_device(self) -> Optional[Device]:
        if self.peer_ip.assigned_object and hasattr(self.peer_ip.assigned_object, 'device'):
            return self.peer_ip.assigned_object.device
        return None

    class Meta:
        ordering = ('name', 'peer_ip',)
        verbose_name = 'BGP Peer'
        verbose_name_plural = 'BGP Peers'

    def __str__(self):
        return f'{self.device} -> {self.remote_device} ({self.peer_ip})'

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:bgppeer', args=[self.pk])
    



class BGPPeerGroup(NetBoxModel):
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='bgp_peer_groups'
    )
    name = models.CharField(
        max_length=100
    )

    description = models.CharField(
        max_length=100,
        blank=True
    )

    session_config = models.ForeignKey(
        to=BGPSessionConfig,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    peers = models.ManyToManyField(
        to=BGPPeer,
        blank=True,
        related_name='peer_groups'
    )

    class Meta:
        ordering = ('name',)
        unique_together = ('device', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:bgppeergroup', args=[self.pk])




class VNI(NetBoxModel):
    vlan = models.ForeignKey(
        to='ipam.VLAN',
        on_delete=models.PROTECT,
        related_name='vnis'
    )

    vnid = models.PositiveIntegerField(
        verbose_name='VNI',
        unique=True,
    )

    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='vnis',
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:
        ordering = ('vnid',)
        unique_together = ('vnid', 'tenant')

    def __str__(self):
        return f'{self.vnid}'

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:vni', args=[self.pk])


class VXLAN(NetBoxModel):
    vni = models.ForeignKey(
        to=VNI,
        on_delete=models.PROTECT,
        related_name='vxlan'
    )

    ipv4_gateway = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    ipv6_gateway = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    l3mtu = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    ingress_replication = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ('vni',)

    def __str__(self):
        return f'VXLAN for {self.vni}'

    def get_absolute_url(self):
        return reverse(f'plugins:{APP_LABEL}:vxlan', args=[self.pk])