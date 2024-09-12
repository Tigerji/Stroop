def random_net(num_neuron = 100, local_conn = 10, ext_conn = 20):
    net_structure = [[]]
    for i in num_neuron:
        net_structure[i].append(list(range(num_neuron)))
    return net_structure
