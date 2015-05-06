# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## IP-MIB
##    Compiled MIB
##    Do not modify this file directly
##    Run ./noc make-cmib instead
##----------------------------------------------------------------------
## Copyright (C) 2007-2014 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

# MIB Name
NAME = "IP-MIB"
# Metadata
LAST_UPDATED = "2006-02-02"
COMPILED = "2014-11-08"
# MIB Data: name -> oid
MIB = {
    "IP-MIB::ipv6IpForwarding": "1.3.6.1.2.1.4.25",
    "IP-MIB::ipv6IpDefaultHopLimit": "1.3.6.1.2.1.4.26",
    "IP-MIB::ipv4InterfaceTableLastChange": "1.3.6.1.2.1.4.27",
    "IP-MIB::ipv4InterfaceTable": "1.3.6.1.2.1.4.28",
    "IP-MIB::ipv4InterfaceEntry": "1.3.6.1.2.1.4.28.1",
    "IP-MIB::ipv4InterfaceIfIndex": "1.3.6.1.2.1.4.28.1.1",
    "IP-MIB::ipv4InterfaceReasmMaxSize": "1.3.6.1.2.1.4.28.1.2",
    "IP-MIB::ipv4InterfaceEnableStatus": "1.3.6.1.2.1.4.28.1.3",
    "IP-MIB::ipv4InterfaceRetransmitTime": "1.3.6.1.2.1.4.28.1.4",
    "IP-MIB::ipv6InterfaceTableLastChange": "1.3.6.1.2.1.4.29",
    "IP-MIB::ipv6InterfaceTable": "1.3.6.1.2.1.4.30",
    "IP-MIB::ipv6InterfaceEntry": "1.3.6.1.2.1.4.30.1",
    "IP-MIB::ipv6InterfaceIfIndex": "1.3.6.1.2.1.4.30.1.1",
    "IP-MIB::ipv6InterfaceReasmMaxSize": "1.3.6.1.2.1.4.30.1.2",
    "IP-MIB::ipv6InterfaceIdentifier": "1.3.6.1.2.1.4.30.1.3",
    "IP-MIB::ipv6InterfaceEnableStatus": "1.3.6.1.2.1.4.30.1.5",
    "IP-MIB::ipv6InterfaceReachableTime": "1.3.6.1.2.1.4.30.1.6",
    "IP-MIB::ipv6InterfaceRetransmitTime": "1.3.6.1.2.1.4.30.1.7",
    "IP-MIB::ipv6InterfaceForwarding": "1.3.6.1.2.1.4.30.1.8",
    "IP-MIB::ipTrafficStats": "1.3.6.1.2.1.4.31",
    "IP-MIB::ipSystemStatsTable": "1.3.6.1.2.1.4.31.1",
    "IP-MIB::ipSystemStatsEntry": "1.3.6.1.2.1.4.31.1.1",
    "IP-MIB::ipSystemStatsIPVersion": "1.3.6.1.2.1.4.31.1.1.1",
    "IP-MIB::ipSystemStatsInReceives": "1.3.6.1.2.1.4.31.1.1.3",
    "IP-MIB::ipSystemStatsHCInReceives": "1.3.6.1.2.1.4.31.1.1.4",
    "IP-MIB::ipSystemStatsInOctets": "1.3.6.1.2.1.4.31.1.1.5",
    "IP-MIB::ipSystemStatsHCInOctets": "1.3.6.1.2.1.4.31.1.1.6",
    "IP-MIB::ipSystemStatsInHdrErrors": "1.3.6.1.2.1.4.31.1.1.7",
    "IP-MIB::ipSystemStatsInNoRoutes": "1.3.6.1.2.1.4.31.1.1.8",
    "IP-MIB::ipSystemStatsInAddrErrors": "1.3.6.1.2.1.4.31.1.1.9",
    "IP-MIB::ipSystemStatsInUnknownProtos": "1.3.6.1.2.1.4.31.1.1.10",
    "IP-MIB::ipSystemStatsInTruncatedPkts": "1.3.6.1.2.1.4.31.1.1.11",
    "IP-MIB::ipSystemStatsInForwDatagrams": "1.3.6.1.2.1.4.31.1.1.12",
    "IP-MIB::ipSystemStatsHCInForwDatagrams": "1.3.6.1.2.1.4.31.1.1.13",
    "IP-MIB::ipSystemStatsReasmReqds": "1.3.6.1.2.1.4.31.1.1.14",
    "IP-MIB::ipSystemStatsReasmOKs": "1.3.6.1.2.1.4.31.1.1.15",
    "IP-MIB::ipSystemStatsReasmFails": "1.3.6.1.2.1.4.31.1.1.16",
    "IP-MIB::ipSystemStatsInDiscards": "1.3.6.1.2.1.4.31.1.1.17",
    "IP-MIB::ipSystemStatsInDelivers": "1.3.6.1.2.1.4.31.1.1.18",
    "IP-MIB::ipSystemStatsHCInDelivers": "1.3.6.1.2.1.4.31.1.1.19",
    "IP-MIB::ipSystemStatsOutRequests": "1.3.6.1.2.1.4.31.1.1.20",
    "IP-MIB::ipSystemStatsHCOutRequests": "1.3.6.1.2.1.4.31.1.1.21",
    "IP-MIB::ipSystemStatsOutNoRoutes": "1.3.6.1.2.1.4.31.1.1.22",
    "IP-MIB::ipSystemStatsOutForwDatagrams": "1.3.6.1.2.1.4.31.1.1.23",
    "IP-MIB::ipSystemStatsHCOutForwDatagrams": "1.3.6.1.2.1.4.31.1.1.24",
    "IP-MIB::ipSystemStatsOutDiscards": "1.3.6.1.2.1.4.31.1.1.25",
    "IP-MIB::ipSystemStatsOutFragReqds": "1.3.6.1.2.1.4.31.1.1.26",
    "IP-MIB::ipSystemStatsOutFragOKs": "1.3.6.1.2.1.4.31.1.1.27",
    "IP-MIB::ipSystemStatsOutFragFails": "1.3.6.1.2.1.4.31.1.1.28",
    "IP-MIB::ipSystemStatsOutFragCreates": "1.3.6.1.2.1.4.31.1.1.29",
    "IP-MIB::ipSystemStatsOutTransmits": "1.3.6.1.2.1.4.31.1.1.30",
    "IP-MIB::ipSystemStatsHCOutTransmits": "1.3.6.1.2.1.4.31.1.1.31",
    "IP-MIB::ipSystemStatsOutOctets": "1.3.6.1.2.1.4.31.1.1.32",
    "IP-MIB::ipSystemStatsHCOutOctets": "1.3.6.1.2.1.4.31.1.1.33",
    "IP-MIB::ipSystemStatsInMcastPkts": "1.3.6.1.2.1.4.31.1.1.34",
    "IP-MIB::ipSystemStatsHCInMcastPkts": "1.3.6.1.2.1.4.31.1.1.35",
    "IP-MIB::ipSystemStatsInMcastOctets": "1.3.6.1.2.1.4.31.1.1.36",
    "IP-MIB::ipSystemStatsHCInMcastOctets": "1.3.6.1.2.1.4.31.1.1.37",
    "IP-MIB::ipSystemStatsOutMcastPkts": "1.3.6.1.2.1.4.31.1.1.38",
    "IP-MIB::ipSystemStatsHCOutMcastPkts": "1.3.6.1.2.1.4.31.1.1.39",
    "IP-MIB::ipSystemStatsOutMcastOctets": "1.3.6.1.2.1.4.31.1.1.40",
    "IP-MIB::ipSystemStatsHCOutMcastOctets": "1.3.6.1.2.1.4.31.1.1.41",
    "IP-MIB::ipSystemStatsInBcastPkts": "1.3.6.1.2.1.4.31.1.1.42",
    "IP-MIB::ipSystemStatsHCInBcastPkts": "1.3.6.1.2.1.4.31.1.1.43",
    "IP-MIB::ipSystemStatsOutBcastPkts": "1.3.6.1.2.1.4.31.1.1.44",
    "IP-MIB::ipSystemStatsHCOutBcastPkts": "1.3.6.1.2.1.4.31.1.1.45",
    "IP-MIB::ipSystemStatsDiscontinuityTime": "1.3.6.1.2.1.4.31.1.1.46",
    "IP-MIB::ipSystemStatsRefreshRate": "1.3.6.1.2.1.4.31.1.1.47",
    "IP-MIB::ipIfStatsTableLastChange": "1.3.6.1.2.1.4.31.2",
    "IP-MIB::ipIfStatsTable": "1.3.6.1.2.1.4.31.3",
    "IP-MIB::ipIfStatsEntry": "1.3.6.1.2.1.4.31.3.1",
    "IP-MIB::ipIfStatsIPVersion": "1.3.6.1.2.1.4.31.3.1.1",
    "IP-MIB::ipIfStatsIfIndex": "1.3.6.1.2.1.4.31.3.1.2",
    "IP-MIB::ipIfStatsInReceives": "1.3.6.1.2.1.4.31.3.1.3",
    "IP-MIB::ipIfStatsHCInReceives": "1.3.6.1.2.1.4.31.3.1.4",
    "IP-MIB::ipIfStatsInOctets": "1.3.6.1.2.1.4.31.3.1.5",
    "IP-MIB::ipIfStatsHCInOctets": "1.3.6.1.2.1.4.31.3.1.6",
    "IP-MIB::ipIfStatsInHdrErrors": "1.3.6.1.2.1.4.31.3.1.7",
    "IP-MIB::ipIfStatsInNoRoutes": "1.3.6.1.2.1.4.31.3.1.8",
    "IP-MIB::ipIfStatsInAddrErrors": "1.3.6.1.2.1.4.31.3.1.9",
    "IP-MIB::ipIfStatsInUnknownProtos": "1.3.6.1.2.1.4.31.3.1.10",
    "IP-MIB::ipIfStatsInTruncatedPkts": "1.3.6.1.2.1.4.31.3.1.11",
    "IP-MIB::ipIfStatsInForwDatagrams": "1.3.6.1.2.1.4.31.3.1.12",
    "IP-MIB::ipIfStatsHCInForwDatagrams": "1.3.6.1.2.1.4.31.3.1.13",
    "IP-MIB::ipIfStatsReasmReqds": "1.3.6.1.2.1.4.31.3.1.14",
    "IP-MIB::ipIfStatsReasmOKs": "1.3.6.1.2.1.4.31.3.1.15",
    "IP-MIB::ipIfStatsReasmFails": "1.3.6.1.2.1.4.31.3.1.16",
    "IP-MIB::ipIfStatsInDiscards": "1.3.6.1.2.1.4.31.3.1.17",
    "IP-MIB::ipIfStatsInDelivers": "1.3.6.1.2.1.4.31.3.1.18",
    "IP-MIB::ipIfStatsHCInDelivers": "1.3.6.1.2.1.4.31.3.1.19",
    "IP-MIB::ipIfStatsOutRequests": "1.3.6.1.2.1.4.31.3.1.20",
    "IP-MIB::ipIfStatsHCOutRequests": "1.3.6.1.2.1.4.31.3.1.21",
    "IP-MIB::ipIfStatsOutForwDatagrams": "1.3.6.1.2.1.4.31.3.1.23",
    "IP-MIB::ipIfStatsHCOutForwDatagrams": "1.3.6.1.2.1.4.31.3.1.24",
    "IP-MIB::ipIfStatsOutDiscards": "1.3.6.1.2.1.4.31.3.1.25",
    "IP-MIB::ipIfStatsOutFragReqds": "1.3.6.1.2.1.4.31.3.1.26",
    "IP-MIB::ipIfStatsOutFragOKs": "1.3.6.1.2.1.4.31.3.1.27",
    "IP-MIB::ipIfStatsOutFragFails": "1.3.6.1.2.1.4.31.3.1.28",
    "IP-MIB::ipIfStatsOutFragCreates": "1.3.6.1.2.1.4.31.3.1.29",
    "IP-MIB::ipIfStatsOutTransmits": "1.3.6.1.2.1.4.31.3.1.30",
    "IP-MIB::ipIfStatsHCOutTransmits": "1.3.6.1.2.1.4.31.3.1.31",
    "IP-MIB::ipIfStatsOutOctets": "1.3.6.1.2.1.4.31.3.1.32",
    "IP-MIB::ipIfStatsHCOutOctets": "1.3.6.1.2.1.4.31.3.1.33",
    "IP-MIB::ipIfStatsInMcastPkts": "1.3.6.1.2.1.4.31.3.1.34",
    "IP-MIB::ipIfStatsHCInMcastPkts": "1.3.6.1.2.1.4.31.3.1.35",
    "IP-MIB::ipIfStatsInMcastOctets": "1.3.6.1.2.1.4.31.3.1.36",
    "IP-MIB::ipIfStatsHCInMcastOctets": "1.3.6.1.2.1.4.31.3.1.37",
    "IP-MIB::ipIfStatsOutMcastPkts": "1.3.6.1.2.1.4.31.3.1.38",
    "IP-MIB::ipIfStatsHCOutMcastPkts": "1.3.6.1.2.1.4.31.3.1.39",
    "IP-MIB::ipIfStatsOutMcastOctets": "1.3.6.1.2.1.4.31.3.1.40",
    "IP-MIB::ipIfStatsHCOutMcastOctets": "1.3.6.1.2.1.4.31.3.1.41",
    "IP-MIB::ipIfStatsInBcastPkts": "1.3.6.1.2.1.4.31.3.1.42",
    "IP-MIB::ipIfStatsHCInBcastPkts": "1.3.6.1.2.1.4.31.3.1.43",
    "IP-MIB::ipIfStatsOutBcastPkts": "1.3.6.1.2.1.4.31.3.1.44",
    "IP-MIB::ipIfStatsHCOutBcastPkts": "1.3.6.1.2.1.4.31.3.1.45",
    "IP-MIB::ipIfStatsDiscontinuityTime": "1.3.6.1.2.1.4.31.3.1.46",
    "IP-MIB::ipIfStatsRefreshRate": "1.3.6.1.2.1.4.31.3.1.47",
    "IP-MIB::ipAddressPrefixTable": "1.3.6.1.2.1.4.32",
    "IP-MIB::ipAddressPrefixEntry": "1.3.6.1.2.1.4.32.1",
    "IP-MIB::ipAddressPrefixIfIndex": "1.3.6.1.2.1.4.32.1.1",
    "IP-MIB::ipAddressPrefixType": "1.3.6.1.2.1.4.32.1.2",
    "IP-MIB::ipAddressPrefixPrefix": "1.3.6.1.2.1.4.32.1.3",
    "IP-MIB::ipAddressPrefixLength": "1.3.6.1.2.1.4.32.1.4",
    "IP-MIB::ipAddressPrefixOrigin": "1.3.6.1.2.1.4.32.1.5",
    "IP-MIB::ipAddressPrefixOnLinkFlag": "1.3.6.1.2.1.4.32.1.6",
    "IP-MIB::ipAddressPrefixAutonomousFlag": "1.3.6.1.2.1.4.32.1.7",
    "IP-MIB::ipAddressPrefixAdvPreferredLifetime": "1.3.6.1.2.1.4.32.1.8",
    "IP-MIB::ipAddressPrefixAdvValidLifetime": "1.3.6.1.2.1.4.32.1.9",
    "IP-MIB::ipAddressSpinLock": "1.3.6.1.2.1.4.33",
    "IP-MIB::ipAddressTable": "1.3.6.1.2.1.4.34",
    "IP-MIB::ipAddressEntry": "1.3.6.1.2.1.4.34.1",
    "IP-MIB::ipAddressAddrType": "1.3.6.1.2.1.4.34.1.1",
    "IP-MIB::ipAddressAddr": "1.3.6.1.2.1.4.34.1.2",
    "IP-MIB::ipAddressIfIndex": "1.3.6.1.2.1.4.34.1.3",
    "IP-MIB::ipAddressType": "1.3.6.1.2.1.4.34.1.4",
    "IP-MIB::ipAddressPrefix": "1.3.6.1.2.1.4.34.1.5",
    "IP-MIB::ipAddressOrigin": "1.3.6.1.2.1.4.34.1.6",
    "IP-MIB::ipAddressStatus": "1.3.6.1.2.1.4.34.1.7",
    "IP-MIB::ipAddressCreated": "1.3.6.1.2.1.4.34.1.8",
    "IP-MIB::ipAddressLastChanged": "1.3.6.1.2.1.4.34.1.9",
    "IP-MIB::ipAddressRowStatus": "1.3.6.1.2.1.4.34.1.10",
    "IP-MIB::ipAddressStorageType": "1.3.6.1.2.1.4.34.1.11",
    "IP-MIB::ipNetToPhysicalTable": "1.3.6.1.2.1.4.35",
    "IP-MIB::ipNetToPhysicalEntry": "1.3.6.1.2.1.4.35.1",
    "IP-MIB::ipNetToPhysicalIfIndex": "1.3.6.1.2.1.4.35.1.1",
    "IP-MIB::ipNetToPhysicalNetAddressType": "1.3.6.1.2.1.4.35.1.2",
    "IP-MIB::ipNetToPhysicalNetAddress": "1.3.6.1.2.1.4.35.1.3",
    "IP-MIB::ipNetToPhysicalPhysAddress": "1.3.6.1.2.1.4.35.1.4",
    "IP-MIB::ipNetToPhysicalLastUpdated": "1.3.6.1.2.1.4.35.1.5",
    "IP-MIB::ipNetToPhysicalType": "1.3.6.1.2.1.4.35.1.6",
    "IP-MIB::ipNetToPhysicalState": "1.3.6.1.2.1.4.35.1.7",
    "IP-MIB::ipNetToPhysicalRowStatus": "1.3.6.1.2.1.4.35.1.8",
    "IP-MIB::ipv6ScopeZoneIndexTable": "1.3.6.1.2.1.4.36",
    "IP-MIB::ipv6ScopeZoneIndexEntry": "1.3.6.1.2.1.4.36.1",
    "IP-MIB::ipv6ScopeZoneIndexIfIndex": "1.3.6.1.2.1.4.36.1.1",
    "IP-MIB::ipv6ScopeZoneIndexLinkLocal": "1.3.6.1.2.1.4.36.1.2",
    "IP-MIB::ipv6ScopeZoneIndex3": "1.3.6.1.2.1.4.36.1.3",
    "IP-MIB::ipv6ScopeZoneIndexAdminLocal": "1.3.6.1.2.1.4.36.1.4",
    "IP-MIB::ipv6ScopeZoneIndexSiteLocal": "1.3.6.1.2.1.4.36.1.5",
    "IP-MIB::ipv6ScopeZoneIndex6": "1.3.6.1.2.1.4.36.1.6",
    "IP-MIB::ipv6ScopeZoneIndex7": "1.3.6.1.2.1.4.36.1.7",
    "IP-MIB::ipv6ScopeZoneIndexOrganizationLocal": "1.3.6.1.2.1.4.36.1.8",
    "IP-MIB::ipv6ScopeZoneIndex9": "1.3.6.1.2.1.4.36.1.9",
    "IP-MIB::ipv6ScopeZoneIndexA": "1.3.6.1.2.1.4.36.1.10",
    "IP-MIB::ipv6ScopeZoneIndexB": "1.3.6.1.2.1.4.36.1.11",
    "IP-MIB::ipv6ScopeZoneIndexC": "1.3.6.1.2.1.4.36.1.12",
    "IP-MIB::ipv6ScopeZoneIndexD": "1.3.6.1.2.1.4.36.1.13",
    "IP-MIB::ipDefaultRouterTable": "1.3.6.1.2.1.4.37",
    "IP-MIB::ipDefaultRouterEntry": "1.3.6.1.2.1.4.37.1",
    "IP-MIB::ipDefaultRouterAddressType": "1.3.6.1.2.1.4.37.1.1",
    "IP-MIB::ipDefaultRouterAddress": "1.3.6.1.2.1.4.37.1.2",
    "IP-MIB::ipDefaultRouterIfIndex": "1.3.6.1.2.1.4.37.1.3",
    "IP-MIB::ipDefaultRouterLifetime": "1.3.6.1.2.1.4.37.1.4",
    "IP-MIB::ipDefaultRouterPreference": "1.3.6.1.2.1.4.37.1.5",
    "IP-MIB::ipv6RouterAdvertSpinLock": "1.3.6.1.2.1.4.38",
    "IP-MIB::ipv6RouterAdvertTable": "1.3.6.1.2.1.4.39",
    "IP-MIB::ipv6RouterAdvertEntry": "1.3.6.1.2.1.4.39.1",
    "IP-MIB::ipv6RouterAdvertIfIndex": "1.3.6.1.2.1.4.39.1.1",
    "IP-MIB::ipv6RouterAdvertSendAdverts": "1.3.6.1.2.1.4.39.1.2",
    "IP-MIB::ipv6RouterAdvertMaxInterval": "1.3.6.1.2.1.4.39.1.3",
    "IP-MIB::ipv6RouterAdvertMinInterval": "1.3.6.1.2.1.4.39.1.4",
    "IP-MIB::ipv6RouterAdvertManagedFlag": "1.3.6.1.2.1.4.39.1.5",
    "IP-MIB::ipv6RouterAdvertOtherConfigFlag": "1.3.6.1.2.1.4.39.1.6",
    "IP-MIB::ipv6RouterAdvertLinkMTU": "1.3.6.1.2.1.4.39.1.7",
    "IP-MIB::ipv6RouterAdvertReachableTime": "1.3.6.1.2.1.4.39.1.8",
    "IP-MIB::ipv6RouterAdvertRetransmitTime": "1.3.6.1.2.1.4.39.1.9",
    "IP-MIB::ipv6RouterAdvertCurHopLimit": "1.3.6.1.2.1.4.39.1.10",
    "IP-MIB::ipv6RouterAdvertDefaultLifetime": "1.3.6.1.2.1.4.39.1.11",
    "IP-MIB::ipv6RouterAdvertRowStatus": "1.3.6.1.2.1.4.39.1.12",
    "IP-MIB::icmpStatsTable": "1.3.6.1.2.1.5.29",
    "IP-MIB::icmpStatsEntry": "1.3.6.1.2.1.5.29.1",
    "IP-MIB::icmpStatsIPVersion": "1.3.6.1.2.1.5.29.1.1",
    "IP-MIB::icmpStatsInMsgs": "1.3.6.1.2.1.5.29.1.2",
    "IP-MIB::icmpStatsInErrors": "1.3.6.1.2.1.5.29.1.3",
    "IP-MIB::icmpStatsOutMsgs": "1.3.6.1.2.1.5.29.1.4",
    "IP-MIB::icmpStatsOutErrors": "1.3.6.1.2.1.5.29.1.5",
    "IP-MIB::icmpMsgStatsTable": "1.3.6.1.2.1.5.30",
    "IP-MIB::icmpMsgStatsEntry": "1.3.6.1.2.1.5.30.1",
    "IP-MIB::icmpMsgStatsIPVersion": "1.3.6.1.2.1.5.30.1.1",
    "IP-MIB::icmpMsgStatsType": "1.3.6.1.2.1.5.30.1.2",
    "IP-MIB::icmpMsgStatsInPkts": "1.3.6.1.2.1.5.30.1.3",
    "IP-MIB::icmpMsgStatsOutPkts": "1.3.6.1.2.1.5.30.1.4",
    "IP-MIB::ipMIB": "1.3.6.1.2.1.48",
    "IP-MIB::ipMIBConformance": "1.3.6.1.2.1.48.2",
    "IP-MIB::ipMIBCompliances": "1.3.6.1.2.1.48.2.1",
    "IP-MIB::ipMIBGroups": "1.3.6.1.2.1.48.2.2"
}
