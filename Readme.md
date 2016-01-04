DO NOT USE THIS FOR CRYPTO/SECURITY! This was a school project and is in no way a secure or usuable (or complete for that matter) implementation of Shamir Secret Sharing. It was for a Crypto course paper. Again, DO NOT USE THIS FOR ANY CRYPTOGRAPHIC OR SECURITY PURPOSE!!! It is not secure!

Shamir's Secret Sharing
By: Tian Chen and Christopher Funk

ShamirScheme.py is the main Shamir's Secret Sharing Class. It uses ShamirMath.py, which exists for prime number generation and Lagrange Interpolation.

Dealer.py and Client.py are the distributed portion of the Secret Sharing.

To run the distributed Dealer/Client, you may run them either all on localhost or distributed.
Localhost:
    To Startup the Dealer:
        python Dealer.py
        or
            make
        in the Shamir folder, note that this runs Dealer for localhost config only

    To Startup the Clients:
        python Client.py

Distributed:
    To Startup the Dealer:
        python Dealer.py [server name/hostname] [port num]
            i.e.
            python Dealer.py server.address.com 5252
            if your Dealer.py is being executed on machine server.address.com and set to listen to port 5252

    To Startup the Clients:
        python Client.py [dealer server name/hostname] [port num]
            i.e.
            python Client.py server.address.com 5252
            if the Dealer is on server.address.com listening on port 5252


The Dealer will ask you for a Secret, the number of clients you are expecting, and the desired threshold.
The number of clients(shareholders) and Threshold must both be 2 or greater. Secret Sharing falls apart when
they are under 2.
Note: The secret character set is ASCII only.

Use Ctrl+C to kill clients and see how the secret recovery works. Once you step under the threshold, you get gibberish back.
Note: With only one client remaining, it can crash.


Tests
In /Tests/, to run secret sharing tests:
    python SecretSharingTest.py
