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
	def __init__(self, str, x, y, font, fontsize, color, show, origin="", maxX=None, lineSpace=None):
		self.str = str
		self.x = x
		self.y = y
		self.font = font
		self.fontsize = fontsize
		self.color = color
		self.show = show
		self.origin = origin
		self.maxX = maxX
		self.lineSpace = lineSpace

		self.trueFont = pygame.font.SysFont(font, fontsize)

		self.reRender()

		textObjects.append(self)

	#this thing sets the width, height, and render
	def reRender(self):
		if self.maxX != None:
			self.wrappers = self.wrapTextRenders()
			self.renders = [self.trueFont.render(line, True, self.color) for line in self.wrappers]
			if self.renders:
				self.width = max(self.trueFont.size(line)[0] for line in self.wrappers)
				self.height = len(self.wrappers) * self.trueFont.get_linesize()
			else:
				self.width, self.height = 0
		else:
			self.width, self.height = self.trueFont.size(self.str)
			self.renders = [self.trueFont.render(self.str, True, self.color)]
			self.wrappers = [self.str]

	def wrapTextRenders(self):
		stringParts = self.str.split(' ')
		#spaceWidth = self.trueFont.size(' ')[0]
		lines = []
		currentLine = []

		for part in stringParts:
			testLine = ' '.join(currentLine + [part])
			testWidth = self.trueFont.size(testLine)[0]

			if testWidth <= self.maxX:
				currentLine.append(part)
			else:
				if currentLine:
					lines.append(' '.join(currentLine))
					currentLine = [part]
				else:
					lines.append([part])
		if currentLine:
			lines.append(" ".join(currentLine))
		return lines if lines else ['']

	def getRenders(self):
		return self.renders
	
	def getLineSpace(self):
		return self.lineSpace

	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def getShow(self):
		return self.show
	
	def getWidth(self):
		return self.width
	
	def getLineHeight(self):
		return self.trueFont.get_linesize()

	def getHeight(self):
		return self.height
	
	def getOrigin(self):
		return self.origin

	def setShow(self, show):
		self.show = show

	def setStr(self, str):
		self.str = str
		self.reRender()

	def setColor(self, color):
		self.color = color
		self.renders = [self.trueFont.render(line, True, color) for line in self.wrappers]

	def setOrigin(self, origin):
		self.origin = origin

	def setPos(self, x, y):
		self.x = x
		self.y = y
	
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
	
	def setColor(self, color):
		self.color = color
	
	def setShow(self, show):
		self.show = show

textObjects = []

rectObjects = []

flashcards = []

class Flashcard:
	# query: question flashcard asks you
	# answer: answer to the question of flashcard
	# freq: current max countdown of flashcard
	# count: current countdown till do flashcard
	def __init__(self, query, answer):
		self.query = query
		self.answer = answer
		self.freq = 0
		self.count = 0

		flashcards.append(self)

	def getQuery (self):
		return self.query
	
	def getAnswer(self):
		return self.answer
	
	def getFreq(self):
		return self.freq

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
			
			#cnf clickables
			if set == "cnf" and cardGraphic.drawRect().collidepoint(event.pos):
				# the question/answer click check is hard coded. this is Bad
				if screen_height/2 -225 < mouse_y < screen_height/2 -225*8/10:
					selected = "question"
				elif screen_height/2 -225*2/10 < mouse_y < screen_height/2 - 225*0/10:
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
			
			#vfc clickables
			if set == "vfc" and leftButton.drawRect().collidepoint(event.pos):
				if flashcardSelected == 0:
					flashcardSelected  = len(flashcards) - 1
				else:
					flashcardSelected -= 1
			if set == "vfc" and rightButton.drawRect().collidepoint(event.pos):
				if flashcardSelected == len(flashcards) - 1:
					flashcardSelected = 0
				else:
					flashcardSelected += 1

			#drv clickables
			if set == "drv" and cnfSetConfirmButton.drawRect().collidepoint(event.pos):
				if dailyReviewActive == 0:
					#set up the cards
					for card in flashcards:
						if card.getFreq() == 0:
							cardsToReview.append(card)
						else:
							card.addCount(-1)
					dailyReviewActive = 1
				else:
					answerRevealed = 1


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
		cnfText = TextObject("Create new", cnfButtonX, cnfButtonY - 20, "Lexend Medium", 32, (255, 255, 255), True)
		cnfText2 = TextObject("flashcard", cnfButtonX, cnfButtonY + 20, "Lexend Medium", 32, (255, 255, 255), True)

		#reusable assets
		cardGraphic= RectObject(screen_width*5/8, screen_height/2, 700, 450, (255, 255, 255), True)
		cardConfig = TextObject("Question: ", screen_width*5/8 - 340, screen_height/2 - 225*5/5, "Lexend Medium", 28, (120, 120, 120), True, "left", 650)
		cardConfig2 = TextObject("Answer: ", screen_width*5/8 - 340, screen_height/2 - 225*1/5, "Lexend Medium", 28, (120, 120, 120), True, "left", 650)
		leftButton = RectObject(screen_width*5/8 - 300, screen_height*3/4 + 110, 150, 100, (66, 135, 245), True)
		rightButton = RectObject(screen_width*5/8 + 300, screen_height*3/4 + 110, 150, 100, (66, 135, 245), True)
		leftButtonText = TextObject("Prev", screen_width*5/8 - 300, screen_height*3/4 + 110, "Lexend Medium", 50, (255, 255, 255), True)
		rightButtonText = TextObject("Next", screen_width*5/8 + 300, screen_height*3/4 + 110, "Lexend Medium", 50, (255, 255, 255), True)

		#create new flashcard main thing
		cnfSetConfirmButton = RectObject(screen_width*5/8, screen_height*3/4 + 110, 400, 100, (0, 255, 0), True)
		cnfSetConfirmText = TextObject("", screen_width*5/8, screen_height*3/4 + 110, "Lexend Medium", 50, (255, 255, 255), True)

		#daily review button
		drvButtonX = screen_width/5 - 100
		drvButtonY = screen_height*0.47
		drvRect = RectObject(drvButtonX, drvButtonY, 190, 190, (255, 209, 25), True)
		drvText = TextObject("Daily", drvButtonX, drvButtonY - 20, "Lexend Medium", 32, (255, 255, 255), True)
		drvText2 = TextObject("Review", drvButtonX, drvButtonY + 20, "Lexend Medium", 32, (255, 255, 255), True)
		dailyReviewActive = 0
		cardsToReview = []
		currentReviewCard = 0
		answerRevealed = 0

		#view flashcards button
		vfcButtonX = screen_width/5 - 100
		vfcButtonY = screen_height*0.80
		vfcRect = RectObject(vfcButtonX, vfcButtonY, 190, 190, (66, 135, 245), True)
		vfcText = TextObject("View", vfcButtonX, vfcButtonY - 20, "Lexend Medium", 32, (255, 255, 255), True)
		vfcText2 = TextObject("flashcards", vfcButtonX, vfcButtonY + 20, "Lexend Medium", 32, (255, 255, 255), True)
		init = False
		set = ""
		selected = ""
		questionField = ""
		answerField = ""
		confirmation = 0
		flashcardSelected = 0
	#INIT ENDS HERE

	#Wipe frame
	screen.fill("black")

	#set all graphics to false, if anyone needs them they can turn them on
	cardGraphic.setShow(False)
	cardConfig.setShow(False)
	cardConfig2.setShow(False)
	cnfSetConfirmButton.setShow(False)
	cnfSetConfirmText.setShow(False)
	leftButton.setShow(False)
	rightButton.setShow(False)
	leftButtonText.setShow(False)
	rightButtonText.setShow(False)

	# the only reason these are here is for the one time that cardconfig2 is used for the
	# start daily review title. there is probably a better way to do this
	cardConfig2.setOrigin("left")
	cardConfig2.setPos(screen_width*5/8 - 340, screen_height/2 - 225*1/5)
	if set == "cnf":
		cardGraphic.setShow(True)
		cardConfig.setShow(True)
		cardConfig2.setShow(True)
		cnfSetConfirmButton.setShow(True)
		cnfSetConfirmText.setShow(True)

		#flashcard forms stuff
		if selected == "question":
			cardConfig.setStr(f"Question: {questionField}_")
			cardConfig.setColor((30, 30, 30))
		else:
			cardConfig.setStr(f"Question: {questionField}")
			cardConfig.setColor((90, 90, 90))
		if selected == "answer":
			cardConfig2.setStr(f"Answer: {answerField}_")
			cardConfig2.setColor((30, 30, 30))
		else:
			cardConfig2.setStr(f"Answer: {answerField}")
			cardConfig2.setColor((90, 90, 90))
		mouse_pos = pygame.mouse.get_pos()
		if confirmation == 1 and  not cnfSetConfirmButton.drawRect().collidepoint(mouse_pos):
			confirmation = 0
		
		if confirmation == 0:
			cnfSetConfirmText.setStr("SUBMIT")
		elif confirmation == 1:
			cnfSetConfirmText.setStr("CONFIRM?")
	else:
		#reset cnf fields if cnf is not active
		selected = ""
		questionField = ""
		answerField = ""
		cardConfig.setColor((90, 90, 90))
		cardConfig2.setColor((90, 90, 90))

	if set == "vfc":
		cardGraphic.setShow(True)
		cardConfig.setShow(True)
		cardConfig2.setShow(True)

		if len(flashcards) == 0:
			cardConfig.setStr("No flashcards created!")
			cardConfig2.setStr("Create a flashcard with the top button")
		else:
			leftButton.setShow(True)
			rightButton.setShow(True)
			leftButton.setColor((66, 135, 245))
			rightButton.setColor((66, 135, 245))
			leftButtonText.setShow(True)
			rightButtonText.setShow(True)

			cardConfig.setStr(flashcards[flashcardSelected].getQuery())
			cardConfig2.setStr(flashcards[flashcardSelected].getAnswer())

		#reset cnf fields
		selected = ""
		questionField = ""
		answerField = ""
	if set == "drv":
		cardGraphic.setShow(True)
		cardConfig.setColor((30, 30, 30))
		cardConfig2.setColor((30, 30, 30))
		if len(flashcards) == 0:
			cardConfig.setShow(True)
			cardConfig2.setShow(True)
			cardConfig.setStr("No flashcards created!")
			cardConfig2.setStr("Create a flashcard with the top button")
		elif dailyReviewActive == 0:
			cardConfig2.setOrigin("")
			cardConfig2.setPos(screen_width*5/8, screen_height/2)
			cardConfig2.setStr("Start daily review?")
			cnfSetConfirmText.setStr("CONFIRM")
			cardConfig2.setShow(True)
			cnfSetConfirmButton.setShow(True)
			cnfSetConfirmText.setShow(True)
		else:
			cardConfig.setShow(True)
			for card in cardsToReview:
				cardConfig.setStr(card.getQuery())
				if answerRevealed == 0:
					cardConfig2.setShow(False)
					cnfSetConfirmText.setStr("REVEAL")
					cnfSetConfirmButton.setShow(True)
					cnfSetConfirmText.setShow(True)
				else:
					cardConfig2.setStr(card.getAnswer())
					cardConfig2.setShow(True)
					


	# Draw everything (text on top of rect)
	for i in rectObjects:
		if(i.getShow()):
			i.drawRect()
	for i in textObjects:
		if(i.getShow()):
			# Make text not centered, set x and y to top left
			if i.getOrigin() == "left":
				for j in range(len(i.getRenders())):
					screen.blit(i.getRenders()[j], (i.getX(), i.getY() + j*i.getLineHeight()))
			else:
				for j in range(len(i.getRenders())):
					screen.blit(i.getRenders()[j], (i.getX() - i.getWidth()/2, i.getY() - i.getHeight()/2 + j*i.getLineHeight()))

	# flip() the display to put your work on screen
	pygame.display.flip()

	clock.tick(60)  # limits FPS to 60

pygame.quit()


