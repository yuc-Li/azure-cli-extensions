# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

class testUtil:
    # Set your auth info.
    def authorization_info():
        msiClientId = '00000000-0000-0000-0000-000000000000'  # Managed Service Identity ClientId
        msiObjectId = '00000000-0000-0000-0000-000000000000'  # Managed Service Identity ObjectId
        authorizationUserId = '00000000-0000-0000-0000-000000000000'
        identityProfileMsiResourceId = '/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/Group/providers/Microsoft.ManagedIdentity/userAssignedIdentities/msi'

        return '--assigned-identity-object-id {} --assigned-identity-client-id {} --authorization-user-id {} --assigned-identity-id {}' \
            .format(msiObjectId, msiClientId, authorizationUserId, identityProfileMsiResourceId)

    # Config flink cluster cpu and memory.

    def flink_config_str():
        return ' --job-manager-cpu 1 --job-manager-memory 2000 --task-manager-cpu 6 --task-manager-memory 49016 '

    # Config cluster autoscale config.

    def autoScale_config_str():
        return "--enable-autoscale --autoscale-profile-type ScheduleBased --decommission-time -1 --schedule-default-count 5 --schedule-time-zone 'UTC' --schedule-schedules \"[{count:10,days:[Monday,Sunday],end-time:'9:00',start-time:'8:00'}]\""
