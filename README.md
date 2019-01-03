# XDAG Python Example

Currently there are three ways to integrate XDAG wallet.
1. Use exchange wallet address and user's wallet address as combination to distingush different users.
1. Maintain multi wallets by yourself program.
1. Use decimal numbers to distingush different users.

This example just demonstrate the first way.

The main repo for XDAG: https://github.com/xdagger/xdag  
API Doc: https://explorer.xdag.io/api-docs  
Explorer: https://explorer.xdag.io  
Getting Started: https://github.com/XDagger/xdag/wiki/Getting-started  

How to setup testnet: 
1. Build your binary version following https://github.com/XDagger/xdag/wiki/Getting-started
1. If you run nodes on the same machine, just copy those files to different folders.
1. Currently, to run a testnet just need two nodes.
1. Modify the `netdb-white-testnet.txt` and `netdb-testnet.txt` according to your configuration.
1. The launch command is `./xdag -t -z RAM -v 7 -p 127.0.0.1:<port for node> -P 127.0.0.1:<port for miners>:64:64:64:1:5:5:0.5 -rpc-enable -disable-refresh`
   
For example:

If wanna launch two nodes.
1. Copy those files to two folders, let's assume folder `xdag1` and `xdag2`.
1. Modify the `netdb-white-testnet.txt` and `netdb-testnet.txt` in both folders.
>127.0.0.1:3366  
>127.0.0.1:3367  

1. In the folder for the first node run this command `./xdag -t -z RAM -v 7 -p 127.0.0.1:3366 -P 127.0.0.1:8888:64:64:64:1:5:5:0.5 -disable-refresh` to launch one node.
1. In the folder for the second node run this command `./xdag -t -z RAM -v 7 -p 127.0.0.1:3367 -P 127.0.0.1:8889:64:64:64:1:5:5:0.5 -disable-refresh` to launch another node.
1. Make a new folder for wallet, and copy those files to the new folder.
1. Launch your wallet by command `./xdag -t 127.0.0.1:8888` to connect to node `xdag1`. 
1. For sure you can make many wallets as you want by make different folders and connect to `xdag1` node by using `127.0.0.1:8888` or `xdag2` node by using `127.0.0.1:8889`.
   
   
Hint:
1. Currently `explorer.xdag.io` is only for main net. For your local testnet, you have to check the instructions on how to setup explorer.
2. If have any problem, please join XDAG Community discord channel `https://discord.gg/YxXUVQJ`. Or contact me through XDAG Developers Chinese QQ Group `676955224`.
