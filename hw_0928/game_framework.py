class GameState:
    def __init__(self,state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.draw = state.draw


class TestGameState:

    def __init__(self,name):
        self.name = name

    def enter(self):
        print('state [%s] entered' % self.name)

    def exit(self):
        print('state [%s] exited' %self.name)

    def pause(self):
        print('state [%s] paused' %self.name)

    def resume(self):
        print('state [%s] resume' %self.name)

    def handle_events(self):
        print('state [%s] handle_events' %self.name)

    def update(self):
        print('state [%s] update' %self.name)

    def draw(self):
        print('state [%s] draw' %self.name)


running = None
stack = None

def change_state(state):
    global stack
    if(len(stack)>0):
        stack.pop().exit()
    stack.append(state)
    state.enter()

def push_state(state):
    global stack
    if(len(stack) >0):
        stack[-1].pause() #stack에 넣기
    stack.append(state)

def pop_state():
    global stack
    size = len(stack)
    if size == 1:
        quit()
    elif size > 1 :
        # 현재 상태의 탈출 함수를 실행한다.
        stack[-1].exit()
        #재시작 함수 이전의 상태로 돌아간다
        stack[-1].resume()#[-1]로 뒤에서부터 꺼낸다

def quit():
    global running
    runnig = False

def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()
    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        #반복해서 맨위의 스택을 삭제해서 함수를 실행되도록한다.
    while (len(stack) > 0 ):
        stack[-1].exit()
        stack.pop()
