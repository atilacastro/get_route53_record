import boto3
import sys
import re
client = boto3.client('route53')
paginate_hosted_zones = client.get_paginator('list_hosted_zones')
paginator_list_record_sets = client.get_paginator('list_resource_record_sets')
# dns = []
for Record in paginator_list_record_sets.paginate(HostedZoneId='Z2I2T4XUUD7WRU',):
    for ResourceRecordSets in Record['ResourceRecordSets']:
        if 'ResourceRecords' in ResourceRecordSets:
            dns = []
            for record in ResourceRecordSets['ResourceRecords']:
                dns.append(record['Value'])
        elif 'AliasTarget' in ResourceRecordSets:
            dns = ResourceRecordSets['AliasTarget'] ['DNSName']
        else:
            raise Exception('Tipo de registro desconhecido: {}'.format(ResourceRecordSets))
        print("{}|{}|{}".format(ResourceRecordSets['Type'], ResourceRecordSets['Name'], dns))
