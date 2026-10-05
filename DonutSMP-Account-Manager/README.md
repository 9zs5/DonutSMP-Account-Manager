# DonutSMP Account Manager

This project is a starting point for a Fabric-based remote management setup for your own DonutSMP accounts.

Important:
- This is not a password-stealing tool.
- It is intended only for your own machines/accounts.
- It only treats the server as valid when the connection target is donutsmp.net.
- Singleplayer and other servers are treated as offline.

Architecture:
- Fabric client mod on each machine
- Discord bot to send and receive commands
- Local relay / config mapping accounts to machines

This repository currently provides the initial Fabric mod scaffold and the project structure needed to build a jar.
