from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Organization, ISDAS, SCIONLinkAssignment


class NestedOrganizationSerializer(WritableNestedSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'display')


class OrganizationSerializer(NetBoxModelSerializer):
    isd_ases_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Organization
        fields = (
            'id', 'display', 'short_name', 'full_name', 'description', 'comments',
            'isd_ases_count', 'created', 'last_updated'
        )


class NestedISDASSerializer(WritableNestedSerializer):
    class Meta:
        model = ISDAS
        fields = ('id', 'display')


class ISDASSerializer(NetBoxModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )
    organization_display = serializers.CharField(source='organization.display', read_only=True)
    link_assignments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = ISDAS
        fields = (
            'id', 'display', 'isd_as', 'description', 'organization', 'organization_display',
            'appliances', 'comments', 'link_assignments_count', 'created', 'last_updated'
        )


class NestedSCIONLinkAssignmentSerializer(WritableNestedSerializer):
    class Meta:
        model = SCIONLinkAssignment
        fields = ('id', 'display')


class SCIONLinkAssignmentSerializer(NetBoxModelSerializer):
    isd_as = serializers.PrimaryKeyRelatedField(
        queryset=ISDAS.objects.all()
    )
    isd_as_display = serializers.CharField(source='isd_as.display', read_only=True)
    # Placeholder for future external ticket URL if implemented
    ticket_url = serializers.CharField(source='get_ticket_url', read_only=True)

    class Meta:
        model = SCIONLinkAssignment
        fields = (
            'id', 'display', 'isd_as', 'isd_as_display', 'core', 'interface_id',
            'relationship', 'status', 'peer_name', 'peer', 'local_underlay', 'peer_underlay', 'ticket', 'ticket_url',
            'comments', 'created', 'last_updated'
        )
