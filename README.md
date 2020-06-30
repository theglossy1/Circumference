# Circumference

### Hassle-free link between RADIUS and Sonar

This software runs on a FreeRADIUS server and initiates a connection to the Sonar cloud service using an API username/password. With only outbound https sessions from the RADIUS server to Sonar (utilizing Socket.IO), instant bidirectional communication allows for:

   - Always-secure connectivity between Sonar and Circumference's MySQL server without the need for inbound firewall rules, specific NATs, or MySQL-over-TLS certificate hassles.
   - RADIUS Change of Authorization without the need for inbound firewall rules or specific NATs or dealing with CoA proxy hassles.

Previously, inbound access was required from a Sonar cloud instance to FreeRADIUS Genie (the predecessor to Circumference) for MySQL (typically tcp/3306) and for CoA (typically udp/3799 or 1700).

How does this work? Once a Socket.IO connection is established, two-way communication can happen over only one TCP session, initiated via standard https from inside your local network. If a change of authorization is required, it is initiated by Sonar, travels over the https tunnel, and is executed by Circucumference using standard CoA.

Check out a [video of this in action](https://jemnetworks.com/Circumference.mp4).

For Sonar employees, [see more details here](https://docs.google.com/document/d/15uS14CEOntbdFZM_Vk_Vc9a0t9tKRj31gcwP6Zs0th8/edit?usp=sharing).