import sys
sys.path.append("roboter")

from models import robot

def talk_about_book():
    book_robot = robot.Robot()
    book_robot.question()
