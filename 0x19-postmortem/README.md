Issue Summary
•	Duration: May 16, 2024, 09:00 AM - 11:30 AM (UTC-4)
•	Impact: The user authentication service experienced intermittent downtime during the specified duration. Users attempting to log in or register encountered delays and failed login attempts. Approximately 20% of users were affected.
•	Root Cause: A database connection pool overflow led to a bottleneck in the user authentication process.
Timeline
•	09:00 AM: The issue was detected when an engineer noticed an unusual increase in failed login attempts.
•	09:10 AM: Monitoring alerts indicated a rise in response time for the authentication service.
•	09:20 AM: Investigation began, focusing on backend servers and network latency.
•	09:45 AM: Initial assumption: Network congestion might be causing the delays.
•	10:00 AM: Further investigation revealed a spike in database connections.
•	10:15 AM: Assumption: Database performance degradation might be causing the delays.
•	10:30 AM: Debugging paths taken: Tweaking database configurations to handle more connections.
•	10:45 AM: No significant improvement observed, and investigation shifted towards database query optimization.
•	11:00 AM: Incident escalated to the database administration team.
•	11:15 AM: Database administrators identified the connection pool overflow as the root cause.
•	11:30 AM: The incident was resolved by increasing the connection pool size and optimizing query execution.
Root Cause and Resolution
•	Root Cause: The connection pool for the database had a predefined limit that was exceeded due to sudden high user activity. As a result, new connection requests were being delayed, impacting the authentication process.
•	Resolution: The connection pool size was increased to accommodate higher traffic and prevent overflow. Additionally, database queries were optimized to reduce the load on the database server.
Corrective and Preventative Measures Improvements/Fixes:
