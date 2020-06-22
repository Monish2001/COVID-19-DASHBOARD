import covid
import mongodb


def state_list_func():
    state_list = []
    states = mongodb.state()
    statelist = list(states)

    for i in statelist:
        for k, v in i.items():
            state_list.append(v)
    return(state_list)
