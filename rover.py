# -*- coding: utf-8 -*-

import time
from enums import Event, State
from console_input_thread import ConsoleInputThread
from state_machine import StateMachine
from field import Field


class Rover():
    """ToDo"""

    # public Attributes
    position = ()
    search_field = Field()
    state_machine = StateMachine()
    # ToDo delete this: Everithing else privet______________________________________________________
    # protectet attributes
    _position = ()
    _search_field = Field()

    def __init__(self, position, search_field):

        Rover.position = position
        Rover._position = position

        



    def _toggle_pause_resume(self):
        """Toggle the state of the rover between PAUSE and RESUME."""
        if self.state_machine.state == State.PAUSE:
            print('Resuming...')
            self.state_machine.state = State.RESUME
            self.state_machine.update(event=Event.USER_INPUT)
        else:
            print('Pausing...')
            self.state_machine.last_state = self.state_machine.state
            self.state_machine.state = State.PAUSE


if __name__ == "__main__":
    def main(rover):
        input_thread = ConsoleInputThread(rover.state_machine.update)
        input_thread.start()
        while True:
            if rover.state_machine.state not in {State.PAUSE, State.RESUME}:
                print(rover)
            rover.state_machine.update(event=Event.PERIODIC_TIMER)
            time.sleep(0.5)

    # 5.1 Methode __init__(self, position, search_field)
    field_data = Field(height=8, width=5)
    rover = Rover((1, 1), field_data)
    print(rover._search_field)
    print(rover._position)
    print(rover.state_machine)

    # 5.2 Methode __str__(self)
    # field = [["#", "#", "#", "#", "#"],
    #           ["#",  0, 0, 0, "#"],
    #           ["#",  1, 0, 0, "#"],
    #           ["#",  1, 0, 1, "#"],
    #           ["#", "#", "#", "#", "#"]]
    # field_data = Field(field_list = field)
    # rover = Rover((1, 3), field_data)
    # print(rover)
    # print(repr(str(rover)))

    # 5.3 Methode move_to(self, new_position)
    # field_data = Field(height=4, width=5)
    # rover = Rover((1, 1), field_data)
    # print(rover)
    # rover.move_to((2, 2))
    # print(rover)
    # rover.move_to([2, 2])
    # rover.move_to((2, 2, 2))
    # rover.move_to((2,))

    # 5.4 Property load
    # field_data = Field(height=4, width=4)
    # rover = Rover((1, 1), field_data)
    # print(rover.load)

    # 5.5 Methode take_sample(self)
    # field = [["#", "#", "#", "#", "#"],
    #          ["#",  0, 0, 0, "#"],
    #          ["#",  1, 0, 0, "#"],
    #          ["#",  1, 0, 1, "#"],
    #          ["#", "#", "#", "#", "#"]]
    # field_data = Field(field_list=field)
    # rover = Rover((2, 1), field_data)
    # print(rover._load)
    # rover.take_sample()
    # print(rover._load)
    # rover.move_to((3, 1))
    # rover.take_sample()
    # print(rover._load)

    # 5.6 Methode _pause(self, event)
    # field_data = Field(height=4, width=4)
    # rover = Rover((1, 1), field_data)
    # print(rover.state_machine._states)
    # rover.state_machine.state = State.PAUSE
    # print(rover.state_machine.state)
    # rover.state_machine.update(event=Event.USER_INPUT)

    # 5.7 Methode _resume(self, event)
    # field_data = Field(height=4, width=4)
    # rover = Rover((1, 1), field_data)
    # rover.state_machine.last_state = State.PAUSE
    # rover.state_machine.state = State.RESUME
    # print(rover.state_machine.state)
    # rover.state_machine.update(event = Event.USER_INPUT)
    # print(rover.state_machine.state)

    # 5.8 Methode _scan(self, event)
    # field = [["#", "#", "#", "#", "#"],
    #          ["#",  1, 1, 0, "#"],
    #          ["#",  1, 0, 0, "#"],
    #          ["#", "#", "#", "#", "#"]]
    # field_data = Field(field_list=field)
    # rover = Rover((1, 1), field_data)
    # rover.state_machine.state = State.SCAN
    # print(rover.state_machine.state)
    # rover.state_machine.update(event=Event.USER_INPUT)
    # print(rover.state_machine.state)
    # rover.state_machine.state = State.SCAN
    # print(rover)
    # rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover)
    # rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover)
    # rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover)
    # rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover)

    # 5.9 Methode _check(self, event)
    # field = [["#", "#", "#", "#"],
    #          ["#",  1, 0, "#"],
    #          ["#",  1, 0, "#"],
    #          ["#", "#", "#", "#"]]
    # field_data = Field(field_list=field)
    # rover = Rover((1, 1), field_data)
    # rover.state_machine.state = State.CHECK
    # rover.state_machine.update(event=Event.USER_INPUT)
    # print(rover.state_machine.state)
    # rover.state_machine.state = State.CHECK
    # print(rover.load)
    # rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover.load)
    # rover.move_to((2, 1))
    # rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover.load)
    # rover.move_to((2, 2))
    # print(rover)

    # 5.10 Methode _move(self, event)
    # field = [["#", "#", "#", "#", "#"],
    #           ["#",  0, 0, 0, "#"],
    #           ["#",  1, 0, 1, "#"],
    #           ["#", "#", "#", "#", "#"]]
    # field_data = Field(field_list=field)
    # rover = Rover((1, 1), field_data)
    # rover.state_machine.state = State.SCAN
    # print(rover)
    # for i in range(4):
    #     rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # print(rover)
    # rover.state_machine.state = State.MOVE
    # for i in range(6):
    #     rover.state_machine.update(event=Event.PERIODIC_TIMER)
    #     print(rover)
    #     time.sleep(0.5)

    # field = [["#", "#", "#", "#", "#", "#"],
    #          ["#",  0, 1, 1, 0, "#"],
    #          ["#",  0, 1, 0, 1, "#"],
    #          ["#", "#", "#", "#", "#", "#"],]
    # field_data = Field(field_list=field)
    # rover = Rover((1, 1), field_data)
    # rover.state_machine.state = State.SCAN
    # # print(rover)
    # for i in range(5):
    #     rover.state_machine.update(event=Event.PERIODIC_TIMER)
    # # print(rover)
    # rover.state_machine.state = State.MOVE
    # for i in range(8):
    #     rover.state_machine.update(event=Event.PERIODIC_TIMER)
    #     print(rover)
    #     time.sleep(0.5)

    # 6. Gesamtsystem
    # field = [["#", "#", "#", "#", "#"],
    #          ["#",  0, 0, 1, "#"],
    #          ["#",  1, 1, 0, "#"],
    #          ["#", "#", "#", "#", "#"]]
    # field_data = Field(field_list=field)

    # rover = Rover((1, 1), field_data)
    # main(rover)
