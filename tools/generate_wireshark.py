import os
import yaml
import argparse
from os import listdir
from os.path import isfile, join

from yaml import MarkedYAMLError

# Define the input directory for protocol definitions and output file for message types
def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate Lua message type map from protocol definitions.')
    parser.add_argument('-f', '--folder', type=str, required=True,
                        help='Directory containing protocol definition YAML files')
    parser.add_argument('-o', '--output', type=str, default='hz_message_types.lua',
                        help='Output Lua file name (default: hz_message_types.lua)')
    return parser.parse_args()

# Function to parse a YAML file and extract message types
def parse_protocol_definition(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to generate Lua message type map
def generate_message_type(services):
    message_type_map = {}
    id_fmt = "0x%02x%02x%02x"
    
    for service in services:  
        if "methods" in service:
            methods = service["methods"]
            if methods is None:
                raise NotImplementedError("Methods not found for service " + service)

        service_name = service["name"]
        print(f"Processing: {service_name}")
        for method in service["methods"]:
            request_id = f"{id_fmt % (service['id'], method['id'], 0)}"
            response_id = f"{id_fmt % (service['id'], method['id'], 1)}"

            message_type_map[request_id] = f"{service_name}.{method['name']} Request"
            message_type_map[response_id] = f"{service_name}.{method['name']} Response"

            events = method.get("events", None)
            if events is not None:
                for i in range(len(events)):
                    event_id = f"{id_fmt % (service['id'], method['id'], i + 2)}"
                    message_type_map[event_id] = f"{events[i]['name']} Event"

    return message_type_map  # Return only the message type map

# Function to generate decoders for requests, responses, and events
def generate_decoders(services, output_file_path):
    decoders = {}  # New dictionary to hold decoders
    id_fmt = "0x%02x%02x%02x"
    
    with open(output_file_path, 'w') as lua_file:
        lua_file.write("-- This file is auto-generated. Do not manually edit.\n\n")
        
        for service in services:  
            if "methods" in service:
                methods = service["methods"]
                if methods is None:
                    raise NotImplementedError("Methods not found for service " + service)

            service_name = service["name"]
            for method in service["methods"]:
                request_id = f"{id_fmt % (service['id'], method['id'], 0)}"
                response_id = f"{id_fmt % (service['id'], method['id'], 1)}"

                request_decoder = f"decode_{service_name}_{method['name']}_request"
                response_decoder = f"decode_{service_name}_{method['name']}_response"
                
                decoders[request_id] = request_decoder  # Add decoder for request
                decoders[response_id] = response_decoder  # Add decoder for response

                # Write request decoder function to Lua file
                lua_file.write(f"function {request_decoder}()\n")
                lua_file.write(f"    print('{request_decoder} called')  -- Debug print\n")
                lua_file.write(f"    -- Request ID: {request_id}\n")  # Comment with request_id on a separate line
                lua_file.write("    -- TODO\n")  # TODO comment
                lua_file.write("end\n\n")

                # Write response decoder function to Lua file before processing events
                lua_file.write(f"function {response_decoder}()\n")
                lua_file.write(f"    print('{response_decoder} called')  -- Debug print\n")
                lua_file.write(f"    -- Response ID: {response_id}\n")  # Comment with response_id on a separate line
                lua_file.write("    -- TODO\n")  # TODO comment
                lua_file.write("end\n\n")

                # Process events after writing the response decoder
                events = method.get("events", None)
                if events is not None:
                    for i in range(len(events)):
                        event_id = f"{id_fmt % (service['id'], method['id'], i + 2)}"
                        event_decoder = f"decode_{events[i]['name']}"  # Add decoder for event
                        decoders[event_id] = event_decoder  # Add decoder for event

                        # Write event decoder function to Lua file
                        lua_file.write(f"function {event_decoder}()\n")
                        lua_file.write(f"    print('{event_decoder} called')  -- Debug print\n")
                        lua_file.write(f"    -- Event ID: {event_id}\n")  # Comment with event_id on a separate line
                        lua_file.write("    -- TODO\n")  # TODO comment
                        lua_file.write("end\n\n")

        # Write local decoders to a file
        lua_file.write("local decoders = {\n")
        for message_id, decoder in decoders.items():
            lua_file.write(f'    ["{message_id}"] = "{decoder}",\n')
        lua_file.write("}\n\n")

        # Add the callDecoder function
        lua_file.write("function callDecoder(message_id)\n")
        lua_file.write("    local decoder_name = decoders[message_id]\n")
        lua_file.write("    if decoder_name then\n")
        lua_file.write("        _G[decoder_name]()  -- Call the function by name\n")
        lua_file.write("    else\n")
        lua_file.write("        print(\"Unknown message ID: \" .. message_id)\n")
        lua_file.write("    end\n")
        lua_file.write("end\n")

    return decoders  # Return only the decoders

# Function to write the Lua file
def write_message_type_file(message_type_map, output_file_path):
    with open(output_file_path, 'w') as lua_file:
        lua_file.write("-- This file is auto-generated. Do not manually edit.\n")
        lua_file.write("local message_type_map = {\n")
        for message_id, message_name in message_type_map.items():
            lua_file.write(f'    ["{message_id}"] = "{message_name}",\n')
        lua_file.write("}\n\n")
        lua_file.write("local function getMessageTypeString(type)\n")
        lua_file.write("    return message_type_map[type] or \"Unknown Message Type\"\n")
        lua_file.write("end\n\n")
        lua_file.write("return {\n")
        lua_file.write("    getMessageTypeString = getMessageTypeString\n")
        lua_file.write("}\n")

def load_services(protocol_def_dir):
    service_list = listdir(protocol_def_dir)
    services = []
    for service_file in service_list:
        file_path = join(protocol_def_dir, service_file)
        if isfile(file_path):
            with open(file_path, "r") as file:
                try:
                    data = yaml.load(file, Loader=yaml.Loader)
                except MarkedYAMLError as err:
                    print(err)
                    exit(-1)
                services.append(data)
    return services

# Main execution
if __name__ == "__main__":
    args = parse_arguments()
    protocol_dir = args.folder
    output_file_path = args.output
    services = load_services(protocol_dir)
    message_type_map = generate_message_type(services)  # Get message type map
    write_message_type_file(message_type_map, output_file_path)
    
    decoders = generate_decoders(services, 'hz_decoders.lua')  # Get decoders and write to Lua file

    
