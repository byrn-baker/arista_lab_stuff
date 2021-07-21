import yaml
from jinja2 import Template

config = """
DC1:
    Spine1:
        interfaces:
            Loopback0: 192.168.101.101/32
            Ethernet2: 192.168.103.1/31
            Ethernet3: 192.168.103.7/31
            Ethernet4: 192.168.103.13/31
            Ethernet5: 192.168.103.19/31
            Ethernet6: 192.168.103.25/31
            Ethernet7: 192.168.103.31/31
        bgp:
          asn: 65100
    Spine2:
        interfaces:
            Loopback0: 192.168.101.102/32
            Ethernet2: 192.168.103.3/31
            Ethernet3: 192.168.103.9/31
            Ethernet4: 192.168.103.15/31
            Ethernet5: 192.168.103.21/31
            Ethernet6: 192.168.103.27/31
            Ethernet7: 192.168.103.33/31
        bgp:
          asn: 65100
    Spine3:
        interfaces:
            Loopback0: 192.168.101.103/32
            Ethernet2: 192.168.103.5/31
            Ethernet3: 192.168.103.11/31
            Ethernet4: 192.168.103.17/31
            Ethernet5: 192.168.103.23/31
            Ethernet6: 192.168.103.29/31
            Ethernet7: 192.168.103.35/31
        bgp:
          asn: 65100
    Leaf1:
        interfaces:
            Loopback0: 192.168.101.11/32
            Loopback1: 192.168.102.11/32
            Ethernet3: 192.168.103.0/31
            Ethernet4: 192.168.103.2/31
            Ethernet5: 192.168.103.4/31
        bgp:
          asn:65101
          spine-peers:
            - 192.168.103.1
            - 192.168.103.3
            - 192.168.103.5
    Leaf2:
        interfaces:
            Loopback0: 192.168.101.12/32
            Loopback1: 192.168.102.11/32
            Ethernet3: 192.168.103.6/31
            Ethernet4: 192.168.103.8/31
            Ethernet5: 192.168.103.10/31
        bgp:
          asn: 65101
          spine-peers:
            - 192.168.103.7
            - 192.168.103.9
            - 192.168.103.11
    Leaf3:
        interfaces:
            Loopback0: 192.168.101.13/32
            Loopback1: 192.168.102.13/32
            Ethernet3: 192.168.103.12/31
            Ethernet4: 192.168.103.14/31
            Ethernet5: 192.168.103.16/31
        bgp:
          asn: 65102
          spine-peers:
            - 192.168.103.13
            - 192.168.103.15
            - 192.168.103.17
    Leaf4:
        interfaces:
            Loopback0: 192.168.101.14/32
            Loopback1: 192.168.102.13/32
            Ethernet3: 192.168.103.18/31
            Ethernet4: 192.168.103.20/31
            Ethernet5: 192.168.103.22/31
        bgp:
          asn: 65102
          spine-peers:
            - 192.168.103.19
            - 192.168.103.21
            - 192.168.103.23
    Borderleaf1:
        interfaces:
            Loopback: 192.168.101.21/32
            Loopback1: 192.168.102.21/32
            Ethernet3: 192.168.103.24/31
            Ethernet4: 192.168.103.26/31
            Ethernet5: 192.168.103.28/31
            Ethernet12: 192.168.254.0/31
        bgp:
          asn: 65103
          spine-peers:
            - 192.168.103.25
            - 192.168.103.27
            - 192.168.103.29
    Borderleaf2:
        interfaces:
            Loopback: 192.168.102.22/32
            Loopback1: 192.168.102.21/32
            Ethernet3: 192.168.103.30/31
            Ethernet4: 192.168.103.32/31
            Ethernet5: 192.168.103.34/31
            Ethernet12: 192.168.254.2/31
        bgp:
          asn: 65103
          spine-peers:
            - 192.168.103.31
            - 192.168.103.33
            - 192.168.103.35
DC2:
    Spine1:
        interfaces:
            Loopback0: 192.168.201.101/32
            Ethernet2: 192.168.203.1/31
            Ethernet3: 192.168.203.7/31
            Ethernet4: 192.168.203.13/31
            Ethernet5: 192.168.203.19/31
            Ethernet6: 192.168.203.25/31
            Ethernet7: 192.168.203.31/31
        bgp:
          asn: 65200
    Spine2:
        interfaces:
            Loopback0: 192.168.201.102/32
            Ethernet2: 192.168.203.3/31
            Ethernet3: 192.168.203.9/31
            Ethernet4: 192.168.203.15/31
            Ethernet5: 192.168.203.21/31
            Ethernet6: 192.168.203.27/31
            Ethernet7: 192.168.203.33/31
        bgp:
          asn: 65200
    Spine3:
        interfaces:
            Loopback0: 192.168.201.103/32
            Ethernet2: 192.168.203.5/31
            Ethernet3: 192.168.203.11/31
            Ethernet4: 192.168.203.17/31
            Ethernet5: 192.168.203.23/31
            Ethernet6: 192.168.203.29/31
            Ethernet7: 192.168.203.35/31
        bgp:
          asn: 65200
    Leaf1:
        interfaces:
            Loopback0: 192.168.201.11/32
            Loopback1: 192.168.202.11/32
            Ethernet3: 192.168.203.0/31
            Ethernet4: 192.168.203.2/31
            Ethernet5: 192.168.203.4/31
        bgp:
          asn: 65201
          spine-peers:
            - 192.168.203.1
            - 192.168.203.3
            - 192.168.203.5
    Leaf2:
        interfaces:
            Loopback0: 192.168.201.12/32
            Loopback1: 192.168.202.11/32
            Ethernet3: 192.168.203.6/31
            Ethernet4: 192.168.203.8/31
            Ethernet5: 192.168.203.10/31
        bgp:
          asn: 65201
          spine-peers:
            - 192.168.203.7
            - 192.168.203.9
            - 192.168.203.11
          iBGP-peer: 192.168.255.1
    Leaf3:
        interfaces:
            Loopback0: 192.168.201.13/32
            Loopback1: 192.168.202.13/32
            Ethernet3: 192.168.203.12/31
            Ethernet4: 192.168.203.14/31
            Ethernet5: 192.168.203.16/31
        bgp:
          asn: 65202
          spine-peers:
            - 192.168.203.13
            - 192.168.203.15
            - 192.168.203.17
    Leaf4:
        interfaces:
            Loopback0: 192.168.201.14/32
            Loopback1: 192.168.202.13/32
            Ethernet3: 192.168.203.18/31
            Ethernet4: 192.168.203.20/31
            Ethernet5: 192.168.203.22/31
        bgp:
          asn: 65202
          spine-peers:
            - 192.168.203.19
            - 192.168.203.21
            - 192.168.203.23
    Borderleaf1:
        interfaces:
            Loopback0: 192.168.201.21/32
            Loopback1: 192.168.202.21/32
            Ethernet3: 192.168.203.24/31
            Ethernet4: 192.168.203.26/31
            Ethernet5: 192.168.203.2/31
            Ethernet12: 192.168.254.0/31
        bgp:
          asn: 65203
          spine-peers:
            - 192.168.203.2
            - 192.168.203.2
            - 192.168.203.2
    Borderleaf2:
        interfaces:
            Loopback0: 192.168.202.2/32
            Loopback1: 192.168.202.2/32
            Ethernet3: 192.168.203.3/31
            Ethernet4: 192.168.203.3/31
            Ethernet5: 192.168.203.3/31
            Ethernet12: 192.168.254.2/31
        bgp:
          asn: 65203
          spine-peers:
            - 192.168.203.3
            - 192.168.203.3
            - 192.168.203.35
"""
tm = Template
("service routing protocols model multi-agent
    {% for dc in config }
        {% for switch in dc %}
            {% for intf in switch %}
                {% if 'Loopback' in intf %}
      ip prefix-list LOOPBACK permit {{ intf }}
                {% endif }
            {% endfor %}
        {% endfor %}
    {% endffor %}")
msg = tm.render(intf=intf)
print(msg)
