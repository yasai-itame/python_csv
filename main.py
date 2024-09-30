import sys

sys.path.append("roboter")
import roboter.controller.conversation

def main():
    roboter.controller.conversation.talk_about_book()

if __name__ == '__main__':
    main()