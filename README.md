# Wireshark decoder for Hazelcast Client Protocol
This is a wireshark decoder for the Hazelcast Client Protocol

The Hazelcast Client Protocol is defined in the [hazelcast-client-protocol](https://github.com/hazelcast/hazelcast-client-protocol) repository.

## Prerequisites
- Python 3.10+
- Wireshark 4.4+


## Usage

### (Optional) Generate the wireshark decoders
The generated decoders have been committed to this repository, so these steps are optional.

**Step 1**: (Optional) Clone the hazelcast-client-protocol repository

Find somewhere to clone the hazelcast-client-protocol repository, e.g. your home directory.
This repository contains the protocol definitions for the Hazelcast Client Protocol.

```
git clone https://github.com/hazelcast/hazelcast-client-protocol.git
```


**Step 2**: (Optional) Generate the lua decoders 

```
python generate_wireshark.py -f path-to/hazelcast-client-protocol/protocol-definitions
```


### Add the Hazelcast dissectors to Wireshark

**Step 1**: Copy the decoder to your wireshark plugins location

Check your wireshark plugins location
```
ls ~/.local/lib/wireshark/plugins/
```

Copy the decoder to your wireshark plugins location
```
cp hzc_client.lua ~/.local/lib/wireshark/plugins/
cp hzc_message_types.lua ~/.local/lib/wireshark/plugins/
```

**Step 2**: Restart wireshark and enjoy


# Disclaimer

This is a toy project to learn more about the Hazelcast Client Protocol.   It might give the wrong result
or not work at all.


# Contributing

Feel free to create a Pull Request, or Issue if you see something worth changing or adding.


