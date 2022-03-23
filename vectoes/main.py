class vector:
    def __init__(self,*components):
        self.components=components

v1=vector(1,2)
v2=vector(3,5,6)

print(f'v1-->{v1.components}')
print(f'v2-->{v2.components}')