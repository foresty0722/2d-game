from pico2d import *
import game_framework
import boys_state

def enter():
	global bgImage
	bgImage = load_image('../resource/title.png')

def exit():
	global bgImage
	del bgImage

def draw():
	clear_canvas()
	bgImage.draw(400, 300)
	update_canvas()

def update():
	delay(0.03)

def handle_events():
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT:
			game_framework.quit()
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				game_framework.quit()
			elif e.key == SDLK_SPACE: # 스페이스바를 누르면 상태변환
				game_framework.push_state(boys_state)

def pause():
	pass

def resume():
	pass

if __name__ == '__main__': #메인자체를 실행할때(임포트된게아니고) 만 실행
	import sys
	current_module = sys.modules[__name__]	
	open_canvas()
	game_framework.run(current_module)
	close_canvas()
