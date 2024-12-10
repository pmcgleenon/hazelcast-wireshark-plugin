# Wireshark disssector for Hazelcast Client Protocol


## Usage

### Generate the wireshark decoders
The generated decoders have been committed to this repository, so these steps are optional.
Do this when updates have been made to the Hazelcast Client Protocol

**Step 1**: Clone the hazelcast-client-protocol repository

Find somewhere to clone the hazelcast-client-protocol repository, e.g. your home directory.
This repository contains the protocol definitions for the Hazelcast Client Protocol.

```
git clone https://github.com/hazelcast/hazelcast-client-protocol.git
```


**Step 2**: Generate the lua decoders 

```
python generate_wireshark.py -f path-to/hazelcast-client-protocol/protocol-definitions
```


**Step 3**: Commit the generated code to this repository


