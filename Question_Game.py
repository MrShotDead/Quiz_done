import pgzrun
game_over = False
#import crash_trigger
WIDTH=1000
HEIGHT=600
question = []
timer123 = 10
q_box = Rect(100,50,800,100)
ans_1 = Rect (61,175,325,175)
ans_2 = Rect (600,175,325,175)
ans_3 = Rect (61,400,325,175)
ans_4 = Rect (600,400,325,175)
timer = Rect (405,175,175,175)
ans = [ans_1,ans_2,ans_3,ans_4]
not_a_skip_box = Rect (405,400,175,175)
def quedtions():
    file = open("txt_a.txt","r")
    global question
    for i in file:
        question.append(i)
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(q_box,"yellow")
    screen.draw.filled_rect(ans_1,"yellow")
    screen.draw.filled_rect(ans_2,"yellow")
    screen.draw.filled_rect(ans_3,"yellow")
    screen.draw.filled_rect(ans_4,"yellow")
    screen.draw.filled_rect(timer,"purple")
    screen.draw.filled_rect(not_a_skip_box,"purple")
    screen.draw.textbox(me_no_english[0],q_box,color = "blue")
    screen.draw.textbox(me_no_english[1],ans_1,color = "blue")
    screen.draw.textbox(me_no_english[2],ans_2,color = "blue")
    screen.draw.textbox(me_no_english[3],ans_3,color = "blue")
    screen.draw.textbox(me_no_english[4],ans_4,color = "blue")
    screen.draw.textbox("skip",not_a_skip_box, color = "green")
    screen.draw.textbox(str (timer123),timer, color = "green")
def sheeka():
    global timer123
    if timer123:
        timer123 = timer123-1
    if timer123 < 0:
#delete all files
        m_f()
def write():
    global question
    return question.pop(0).split(",")
def reddit():
    global me_no_english
    if question:
        me_no_english = write()
        print (question)
    else: 
        me_no_english = ["tryhard get a life nerd touch grass lil bro","why","are","you","so","NERDY"]
def on_mouse_down(pos):
    number = 1
    for i in ans:
        if i.collidepoint(pos):
            if number==int(me_no_english[5]):
                reddit()
            else:
                m_f()
        number = number+1
    if not_a_skip_box.collidepoint(pos) and question and timer123:
        skip()
def skip():
    global me_no_english
    if question and timer123: 
        me_no_english = write()
        print (question)
quedtions()
def m_f():
    global me_no_english
    global game_over
    global timer123
    me_no_english = ["GGs","GGs","GGs","GGs","GGs","Skill_Issue"]
    game_over = True
    timer123 = 0
print (question)    
me_no_english = write()
clock.schedule_interval(sheeka,3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132)
pgzrun.go()