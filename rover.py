# -*- coding: utf-8 -*-
"""
Module to move a rover in a given field an analyze it.

Classes
-------
    Rover: Move a rover in a given field an analyze it.

"""
import time
from enums import Event, State
from console_input_thread import ConsoleInputThread
from state_machine import StateMachine
from field import Field


class Rover():
    """
    Move a rover in a given field an analyze it.

    Attributes
    ----------
        position : Indicates where the rover is at the momen.
        search_field : The field inside the rover is operating.
        state_machine : state_machine object wich holds all the known and the actual state.
    """

    # public Attributes
    position = ()
    search_field = None
    state_machine = None
    
    # protectet attributes
    _position = ()
    _search_field = None

    def __init__(self, position, search_field):
        """
        Initialize the Rover instance.

        Args
        ----
            position (tuple): Initial position on the given field where the rover should start operate.
            search_field (Field object) : Field inside the rover can move.
        """

        Rover.position = position
        Rover._position = position

        Rover.search_field = search_field
        Rover._search_field = search_field

    def __str__(self):
        """
        Get a readable view of the actual field and the actual position of the rover.
        (Due to readability not via string comprehension solved.)

        Return
        ------
            string : A readable string of the rover in his field.
        """
        _row_string = ""
        _return_string = ""

        for _row in range(0,len(Rover._search_field.field)):
            for _column in range(0,len(Rover._search_field.field[_row])):
                if Rover._position == (_row,_column):
                    _row_string += " R "
                elif Rover._search_field.field[_row][_column] == 1:
                    _row_string += " 1 "
                elif Rover._search_field.field[_row][_column] == 0:
                    _row_string += " 0 "
                elif Rover._search_field.field[_row][_column] == "#":
                    _row_string += " # "

            _return_string += _row_string + "\n"
            _row_string = ""

        return _return_string
            
    def move_to(self,new_position):
        """
        Move the Rover to an new Position inside the given field.
        
        Args
        ----
        new_position (tuple) : The position in the field where you want to move the rover to.
        """
        if type(new_position) != tuple:
            raise TypeError("The new position must be specified as a tuple.")
        elif len(new_position) != 2:
            raise ValueError("The new position tuple must contain exactly 2 elements.")
        else:
            Rover._position = new_position
            Rover.position = new_position








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
    """
    field_data = Field(height=8, width=5)
    rover = Rover((1, 1), field_data)
    print(rover._search_field)
    print(rover._position)
    print(rover.state_machine)
    """
    # 5.2 Methode __str__(self)
    field = [["#", "#", "#", "#", "#"],
              ["#",  0, 0, 0, "#"],
              ["#",  1, 0, 0, "#"],
              ["#",  1, 0, 1, "#"],
              ["#", "#", "#", "#", "#"]]
    field_data = Field(field_list = field)
    rover = Rover((1, 3), field_data)
    print(rover)
    print(repr(str(rover)))

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
