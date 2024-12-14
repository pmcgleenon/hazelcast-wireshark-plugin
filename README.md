# Wireshark decoder for Hazelcast Client Protocol
This is a wireshark decoder for the Hazelcast Client Protocol

The Hazelcast Client Protocol is defined in the [hazelcast-client-protocol](https://github.com/hazelcast/hazelcast-client-protocol) repository.

## Prerequisites
- Python 3.10+
- Wireshark 4.4+


## Usage

### Add the Hazelcast dissectors to Wireshark

**Step 1**: Copy the decoder to your wireshark plugins location

Check your wireshark plugins location
```
ls ~/.local/lib/wireshark/plugins/
```

Copy all of the lua files to your wireshark plugins location
```
cp hz_client.lua ~/.local/lib/wireshark/plugins/
cp hz_message_types.lua ~/.local/lib/wireshark/plugins/
cp hz_decoders.lua ~/.local/lib/wireshark/plugins/
```

**Step 2**: Restart wireshark and enjoy


# Disclaimer

This is a toy project to learn more about the Hazelcast Client Protocol.   It might give the wrong result
or not work at all.   It needs more work to fully implement the message decoders.


# Contributing

Feel free to create a Pull Request, or Issue if you see something worth changing or adding.


