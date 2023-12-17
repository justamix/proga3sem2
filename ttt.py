import pygame
import sys

pygame.init()
size_block = 100
margin = 15
width = heigth = size_block * 3 + margin * 4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tac_toe")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
query = 0
game_over = False
def check_win(mas, sign):
    space = 0
    for row in mas:
        space += row.count(0)
        if row.count(sign) == 3:
            return sign
    for column in range(3):
        if mas[0][column] == sign and mas[1][column] == sign and mas[2][column] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if space == 0:
        return "TIE"
    return False
    
while True:
    #цикл обработки событий
    for event in pygame.event.get():
        #выход
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #заполнение ячеек
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][column] == 0:
                if query % 2 == 0:
                    mas[row][column] = 'x'
                    query += 1
                else:
                    mas[row][column] = 'o'
                    query += 1
        #перезапуск партии
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query = 0
            
    #отрисовка игрового поля
    if not game_over:
        for row in range(3):
            for column in range(3):
                if mas[row][column] == 'x':
                    color = red
                elif mas[row][column] == 'o':
                    color = green
                else:
                    color = white
                x = column * size_block + (column + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x - 5 + size_block, y + 5), (x + 5, y + size_block - 5), 3)
                if color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
    
    #проверка на победу игроков
    if (query - 1) % 2 == 0:
        gameover = check_win(mas, 'x')
    else:
        gameover = check_win(mas, 'o')      

    #вывод текста после конца партии
    if gameover:
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(gameover, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2       
        screen.blit(text1, [text_x, text_y])
        game_over = True
    pygame.display.update()