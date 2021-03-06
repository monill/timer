import multiprocessing

from gui.bomb_timer import TimerGui
from listener.gamestate import ListenerWrapper


def main():
    # Message queue used for comms between processes
    queue = multiprocessing.Queue()
    gui = TimerGui(queue)
    listener = ListenerWrapper(queue)

    gui.start()
    listener.start()

    gui.join()
    listener.shutdown()
    listener.join()


if __name__ == "__main__":
    main()
