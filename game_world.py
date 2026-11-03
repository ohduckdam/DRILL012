# 객체로 구성된 게임 월드

world = [] # 게임 월드에 존재하는 모든 객체를 담는 리스트

# 계층적 구조를 갖는 게임 월드
world = [ [],[],[] ]


#게임 월드에 ㄱㅐㄱ체를 담는 함수
def add_object(o,depth=0):
    world[depth].append(o)

# 게임 월드에서 객체를 제거하는 함수
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

        
# 게임 로직
def update_world():
    for layer in world:
        for o in layer: # 업데이트 중 객체가 제거될 수 있으므로 복사본으로 순회
            o.update()

# 게임 렌더링
def render_world():
    for layer in world:
        for o in layer:
            o.draw()
    