from opcua import Client, ua


def read_motor1_status(node_id):
    client_node = client.get_node(node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    print("Motor 1 Status : "  + str(client_node_value))

def read_motor2_status(node_id):
    client_node = client.get_node(node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    print("Motor 2 Status : "  + str(client_node_value))

def read_counts(node_id):
    client_node = client.get_node(node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    print("Counts : "  + str(client_node_value))

def read_message(node_id):
    client_node = client.get_node(node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    print("Message : "  + str(client_node_value))    

###############################################################################

def write_motor1(node_id, value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
    print("Motor 1 Status  : " + str(client_node_value))

def write_motor2(node_id, value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
    print("Motor 2 Status  : " + str(client_node_value))

def write_counts(node_id, value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)
    print("Counts : "  + str(client_node_value))

def write_message(node_id, value):
    client_node = client.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.String))
    client_node.set_value(client_node_dv)
    print("Message : "  + str(client_node_value))



if __name__ == "__main__":


    client = Client("opc.tcp://192.168.0.1:4840")
    try:
        client.connect()

        read_motor1_status('ns=3;s="Python"."Motor 1"') #("nodeid")
        read_motor2_status('ns=3;s="Python"."Motor 2"') #("nodeid")
        read_counts('ns=3;s="Python"."Counts"') #("nodeid")
        read_message('ns=3;s="Python"."Message"') #("nodeid")

        write_motor1('ns=3;s="Python"."Motor 1"',True) #("nodeid")
        write_motor2('ns=3;s="Python"."Motor 2"',True) #("nodeid")
        write_counts('ns=3;s="Python"."Counts"', 75) #("nodeid")
        write_message('ns=3;s="Python"."Message"','Hello from python') #("nodeid")

    finally:
        client.disconnect()
