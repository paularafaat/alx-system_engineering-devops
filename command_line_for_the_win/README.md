How To Use SFTP to Securely Transfer Files with a Remote Server
Introduction
FTP, the File Transfer Protocol, was a popular, unencrypted method of transferring files between two remote systems. As of 2022, it has been deprecated by most modern software due to a lack of security, and can mostly only be used in legacy applications.

SFTP, which stands for Secure File Transfer Protocol, is a separate protocol packaged built into SSH that can implement FTP commands over a secure connection. Typically, it can act as a drop-in replacement in any contexts where an FTP server is still needed.

In almost all cases, SFTP is preferable to FTP because of its underlying security features and ability to piggy-back on an SSH connection. FTP is an insecure protocol that should only be used in limited cases or on networks you trust.

Although SFTP is integrated into many graphical tools, this guide will demonstrate how to use it through its interactive command line interface.
