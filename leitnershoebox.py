# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

screen_width = 1280

screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

class TextObject:
	def __init__(self, str, x, y, font, fontsize, color, show, origin):
		self.str = str
		self.x = x
		self.y = y
		self.font = font
		self.fontsize = fontsize
		self.color = color
		self.show = show
		self.origin = origin

		self.trueFont = pygame.font.SysFont(font, fontsize)

		self.width, self.height = self.trueFont.size(str)

		self.render = self.trueFont.render(str, True, color)

		textObjects.append(self)

	def getRender(self):
		return self.render
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def getShow(self):
		return self.show
	
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
	
	def getOrigin(self):
		return self.origin

	def setShow(self, show):
		self.show = show

	def setStr(self, str):
		self.str = str
		self.width, self.height = self.trueFont.size(str)
		self.render = self.trueFont.render(str, True, self.color)

	def setColor(self, color):
		self.color = color
		self.render = self.trueFont.render(self.str, True, color)
	
class RectObject:
	def __init__(self, x, y, width, length, color, show):
		self.x = x
		self.y = y
		self.width = width
		self.length = length
		self.color = color
		self.show = show

		rectObjects.append(self)
	
	def drawRect(self):
		return pygame.draw.rect(screen, self.color, pygame.Rect(self.x - self.width/2, self.y - self.length/2, self.width, self.length))
	
	def getShow(self):
		return self.show
	
	def setShow(self, show):
		self.show = show

textObjects = []

rectObjects = []

flashcards = []

class Flashcard:
	# query: question flashcard asks you
	# answer: answer to the question of flashcard
	# freq: current day frequency of flashcard
	# count: current count of days till do flashcard
	def __init__(self, query, answer):
		self.query = query
		self.answer = answer
		self.freq = 1
		self.count = 1

		flashcards.append(self)

	def setFreq(self, freq):
		self.freq = freq

	def setCount(self, count):
		self.count = count

	def addCount(self, count):
		self.count += count

	global init

	init = True

def appendKey(str, rawkey, shift):
	modString = str
	if rawkey == "space":
		modString = f"{modString} "
	elif rawkey == "backspace":
		modString = modString[:len(modString)-1]
	elif shift:
		if len(rawkey) == 1:
			if rawkey == "1":
				modString = f"{str}!"
			elif rawkey == "/":
				modString = f"{modString}?"
			elif rawkey == "2":
				modString = f"{modString}@"
			elif rawkey == "3":
				modString = f"{modString}#"
			elif rawkey == "4":
				modString = f"{modString}$"
			elif rawkey == "5":
				modString = f"{modString}%"
			elif rawkey == "6":
				modString = f"{modString}^"
			elif rawkey == "7":
				modString = f"{modString}&"
			elif rawkey == "8":
				modString = f"{modString}*"
			elif rawkey == "9":
				modString = f"{modString}("
			elif rawkey == "0":
				modString = f"{modString})"
			elif rawkey == ";":
				modString = f"{modString}:"
			elif rawkey == "\'":
				modString = f"{modString}\""
			else:
				modString = f"{modString}{rawkey.upper()}"
	else:
		if len(rawkey) == 1:
			modString = f"{modString}{rawkey}"
	return modString
	
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONUP:
			mouse_x, mouse_y = event.pos

			#print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")
			#print(f"Button pressed: {cncRect.drawRect().collidepoint(event.pos)}")

			#set the scene...
			if cnfRect.drawRect().collidepoint(event.pos):
				if set == "cnf":
					set = ""
				else:
					set = "cnf" # create new flashcard
			if drvRect.drawRect().collidepoint(event.pos):
				if set == "drv":
					set = ""
				else:
					set = "drv" # daily review
			if vfcRect.drawRect().collidepoint(event.pos):
				if set == "vfc":
					set = ""
				else:
					set = "vfc" # view flashcards

			if set == "cnf" and cardGraphic.drawRect().collidepoint(event.pos):
				if screen_height/2 -225*9/10 < mouse_y < screen_height/2 -225*7/10:
					selected = "question"
				elif screen_height/2 -225*7/10 < mouse_y < screen_height/2 -225*5/10:
					selected = "answer"
				else:
					selected = ""
			else:
				selected = ""
			if set == "cnf" and cnfSetConfirmButton.drawRect().collidepoint(event.pos):
				if confirmation == 0:
					confirmation = 1
				elif confirmation == 1:

					# the flashcard code here
					Flashcard(questionField, answerField)

					set = ""
		if event.type == pygame.KEYDOWN:
			if selected == "question":
				questionField = appendKey(questionField, pygame.key.name(event.key), event.mod & pygame.KMOD_SHIFT)
			if selected == "answer":
				answerField = appendKey(answerField, pygame.key.name(event.key), event.mod & pygame.KMOD_SHIFT)
				
	
	if init:
		#initialize all objects. sorry i couldnt do this outside the while loop
		title = TextObject("Shoebox", screen_width*5/8, screen_height/10, "Lexend Medium", 72, (255, 255, 255), True, "")
		underline = RectObject(screen_width*5/8, screen_height/10 + 45, 400, 5, (255, 255, 255), True)

		divider = RectObject(screen_width/4, screen_height/2, 10, screen_height, (255, 255, 255), True)

		#create new flashcard button
		cnfButtonX = screen_width/5 - 100
		cnfButtonY = screen_height*0.15
		cnfRect = RectObject(cnfButtonX, cnfButtonY, 190, 140, (0, 255, 0), True)
		cnfText = TextObject("Create new", cnfButtonX, cnfButtonY - 20, "Lexend Medium", 32, (255, 255, 255), True, "")
		cnfText2 = TextObject("flashcard", cnfButtonX, cnfButtonY + 20, "Lexend Medium", 32, (255, 255, 255), True, "")

		#reusable assets
		cardGraphic= RectObject(screen_width*5/8, screen_height/2, 700, 450, (255, 255, 255), True)
		cnfSetConfig = TextObject("Question: ", screen_width*5/8 - 340, screen_height/2 - 225*4/5, "Lexend Medium", 28, (120, 120, 120), True, "left")
		cnfSetConfig2 = TextObject("Answer: ", screen_width*5/8 - 340, screen_height/2 - 225*3/5, "Lexend Medium", 28, (120, 120, 120), True, "left")
		#create new flashcard main thing
		
		cnfSetConfirmButton = RectObject(screen_width*5/8, screen_height*3/4 + 110, 400, 100, (0, 255, 0), True)
		cnfSetConfirmText = TextObject("", screen_width*5/8, screen_height*3/4 + 110, "Lexend Medium", 50, (255, 255, 255), True, "" )

		#daily review button
		drvButtonX = screen_width/5 - 100
		drvButtonY = screen_height*0.47
		drvRect = RectObject(drvButtonX, drvButtonY, 190, 190, (255, 209, 25), True)
		drvText = TextObject("Daily", drvButtonX, drvButtonY - 20, "Lexend Medium", 32, (255, 255, 255), True, "")
		drvText2 = TextObject("Review", drvButtonX, drvButtonY + 20, "Lexend Medium", 32, (255, 255, 255), True, "")

		#view flashcards button
		vfcButtonX = screen_width/5 - 100
		vfcButtonY = screen_height*0.80
		vfcRect = RectObject(vfcButtonX, vfcButtonY, 190, 190, (66, 135, 245), True)
		vfcText = TextObject("View", vfcButtonX, vfcButtonY - 20, "Lexend Medium", 32, (255, 255, 255), True, "")
		vfcText2 = TextObject("flashcards", vfcButtonX, vfcButtonY + 20, "Lexend Medium", 32, (255, 255, 255), True, "")
		init = False
		set = ""
		selected = ""
		questionField = ""
		answerField = ""
		confirmation = 0
	#INIT ENDS HERE

	#Wipe frame
	screen.fill("black")

	if set == "cnf":
		cardGraphic.setShow(True)
		cnfSetConfig.setShow(True)
		cnfSetConfig2.setShow(True)
		cnfSetConfirmButton.setShow(True)
		cnfSetConfirmText.setShow(True)

		#flashcard forms stuff
		if selected == "question":
			cnfSetConfig.setStr(f"Question: {questionField}_")
			cnfSetConfig.setColor((30, 30, 30))
		else:
			cnfSetConfig.setStr(f"Question: {questionField}")
			cnfSetConfig.setColor((90, 90, 90))
		if selected == "answer":
			cnfSetConfig2.setStr(f"Answer: {answerField}_")
			cnfSetConfig2.setColor((30, 30, 30))
		else:
			cnfSetConfig2.setStr(f"Answer: {answerField}")
			cnfSetConfig2.setColor((90, 90, 90))
		mouse_pos = pygame.mouse.get_pos()
		if confirmation == 1 and  not cnfSetConfirmButton.drawRect().collidepoint(mouse_pos):
			confirmation = 0
		
		if confirmation == 0:
			cnfSetConfirmText.setStr("SUBMIT")
		elif confirmation == 1:
			cnfSetConfirmText.setStr("CONFIRM?")
	elif set == "vfc":
		cardGraphic.setShow(True)
	else:
		cardGraphic.setShow(False)
		cnfSetConfig.setShow(False)
		cnfSetConfig2.setShow(False)
		cnfSetConfirmButton.setShow(False)
		cnfSetConfirmText.setShow(False)
		selected = ""
		questionField = ""
		answerField = ""

	# Draw everything (text on top of rect)
	for i in rectObjects:
		if(i.getShow()):
			i.drawRect()
	for i in textObjects:
		if(i.getShow()):
			if i.getOrigin() == "left":
				screen.blit(i.getRender(), (i.getX(), i.getY() - i.getHeight()/2))
			else:
				screen.blit(i.getRender(), (i.getX() - i.getWidth()/2, i.getY() - i.getHeight()/2))

	# flip() the display to put your work on screen
	pygame.display.flip()

	clock.tick(60)  # limits FPS to 60

pygame.quit()


