from collections import defaultdict
from dataclasses import dataclass

@dataclass
class DataClass:
    a: str
    b: str
    count: int
    e: str

def aggregate_field(data, field):
    temp_dict = defaultdict(lambda: defaultdict(int))
    print(temp_dict)
    for d in data:
        key = (d.a, d.b, d.e)
        print(key)
        temp_dict[key][field] += getattr(d, field)
        print( temp_dict[key][field])
        temp_dict[key]['data'] = d
        print(temp_dict)
    return [DataClass(a=k[0], b=k[1], count=v[field], e=k[2]) for k, v in temp_dict.items()]

data = [DataClass(a="A",b="B",count=10,e="aaa"),DataClass(a="A",b="B",count=20,e="aaa"),DataClass(a="Z",b="Z",count=10,e="DDD"),DataClass(a="Z",b="Z",count=100,e="DDD"),DataClass(a="Q",b="Q",count=1,e="DDD")]

result = aggregate_field(data, 'count')
for r in result:
    print(r)