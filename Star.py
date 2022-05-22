dict_hn={'Arad':42,'Bucharest':0,'Craiova':60,'Drobeta':242,'Eforie':161,
'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':206,'Lugoj':254,
'Mehadia':241,'Neamt':304,'Oradea':180,'Pitesti':100,'Rimnicu':193,
'Sibiu':150,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':314}

dict_gn=dict(
Arad=dict(Zerind=70,Timisoara=112,Sibiu=130),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
Drobeta=dict(Mehadia=70,Craiova=125),
Eforie=dict(Hirsova=66),
Fagaras=dict(Sibiu=99,Bucharest=113),
Giurgiu=dict(Bucharest=90),Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=72,Timisoara=100),
Mehadia=dict(Lugoj=78,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=141),
Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=82,Oradea=141),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=132),
Vaslui=dict(Iasi=92,Urziceni=132),
Zerind=dict(Oradea=71,Arad=75)
)
import queue as Q
#from RMP import dict_gn
#from RMP import dict_hn
start='Arad'
goal='Bucharest'
result=''
def get_fn(citystr):
    cities=citystr.split(" , ")
    hn=gn=0
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def expand(cityq):
    global result
    tot, citystr, thiscity=cityq.get()
    if thiscity==goal:
        result=citystr+" : : "+str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)
main()
