Issue Summary:
On August 10, 2024, at 09:30 AM UTC, a service disruption occurred that lasted for 2 hours and 45 minutes, ending at 12:15 PM UTC. The company’s main e-commerce platform was impacted, leading to significant delays in order processing and checkout failures. During this period, approximately 35% of users experienced slow response times or were unable to complete purchases. The root cause of the incident was identified as a misconfiguration in the Nginx load balancer, which caused traffic to be unevenly distributed across servers, leading to server overload and subsequent failures.
Timeline:
09:30 AM UTC - Issue detected via automated monitoring alerts indicating high error rates and slow response times.
09:35 AM UTC - Initial investigation began focusing on the application server performance.
10:00 AM UTC - Misleading assumption that the database was causing the slowdown led to a 45-minute investigation of database performance.
10:45 AM UTC - Escalated to the infrastructure team after no issues were found in the database.
11:00 AM UTC - Root cause identified as a misconfiguration in the Nginx load balancer, leading to traffic overload on specific servers.
11:30 AM UTC - Configuration corrected and load rebalanced; traffic normalized across servers.
12:15 PM UTC - Full service restored; monitoring confirmed normal operations.
Root Cause and Resolution:
The root cause of the incident was a misconfiguration in the Nginx load balancer that caused uneven traffic distribution. Due to an incorrect setting in the load balancing algorithm, most incoming requests were directed to a single server instead of being evenly distributed across the available servers. This resulted in one server being overloaded and eventually failing, causing a bottleneck that impacted the overall service.
The issue was resolved by correcting the load balancer configuration to use the correct algorithm that evenly distributes traffic across all servers. After the configuration change, the load was rebalanced, and the affected servers recovered, restoring normal service.
Corrective and Preventative Measures:
To prevent similar incidents in the future, the following actions will be taken:
Review and update all Nginx load balancer configurations to ensure correct settings are in place.
Implement additional monitoring to detect uneven traffic distribution across servers.
Conduct a training session for the operations team on load balancer configurations and best practices.
Schedule regular audits of critical infrastructure configurations to identify and correct potential issues.
These measures will help ensure that traffic is consistently balanced across servers, reducing the risk of server overload and service disruptions.

