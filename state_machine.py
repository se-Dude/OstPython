# -*- coding: utf-8 -*-
"""
Module to store and execute states.

Classes
-------
    StateMachine: Store and execute states.

"""


from enums import State


class StateMachine:
    """
    Store states, set active state and execute the active state.

    Attributes
    ----------
        _states: In the private attribute _states all
                 known states are stored.
        _state: In the private attribute _state the
                name of the active state is stored.
    """

    def __init__(self) -> None:
        """
        Initialize the StateMachine instance.

        """

        self._states = {}
        self._state = None
        self.last_state = None

    def add_state(self, state_name, state):
        """
        Method to add a function to the known states.

        Args
        ----
            state_name (State object): Name of the State to be added.
            state (functin): To the name corresponding function.

        """
        self._states[state_name] = state

    def update(self, event=None):
        """
        Calls the active function with the parameter event.

        Args
        ----
            event (any) : This argument is passed to the called function.

        """

        self._state(event)

    @property
    def state(self):
        """
        Method to get or set the active state.

        Args
        ----
            value (State object): State to be set.

        Returns
        -------
            function : Function where state points to.

        Raises
        ------
            ValueError : If the given state is not known.
        """
        return (list(self._states.keys())[list(self._states.values()).index(self._state)])
        

    @state.setter
    def state(self, value):
        if value in self._states:
            self._state = self._states[value]
        else:
            raise ValueError(f"Unknown state with name {value.name}. "
                             f"The following states are valid: "
                             f"{[item.name for item in self._states]}")


if __name__ == "__main__":
    
    # 4.1 Methode __init__(self)
    # state_machine = StateMachine()
    # print(state_machine._states)
    # print(state_machine._state)
    # print(state_machine.last_state)

    # 4.2 Methode add_state(self, state_name, state)
    # state_machine = StateMachine()

    # def pause(event=None):
    #     print("Taking a pause...")

    # def scan(event=None):
    #     print("Scanning...")

    # state_machine.add_state(State.PAUSE, pause)
    # state_machine.add_state(State.SCAN, scan)
    # print(state_machine._states)
    
    # 4.3 Property state
    state_machine = StateMachine()

    def pause(event=None):
        print("Taking a pause...")

    def scan(event=None):
        print("Scanning...")
    state_machine.add_state(State.PAUSE, pause)
    state_machine.add_state(State.SCAN, scan)
    state_machine.state = State.PAUSE
    print(state_machine.state)
    print(state_machine._state)
    state_machine.state = State.CHECK
    
    
    # 4.4 Methode update(self, event=None)
    # state_machine = StateMachine()

    # def pause(event):
    #     print("Taking a pause...")
    #     print(f"{event = }")
    # state_machine.add_state(State.PAUSE, pause)
    # state_machine.state = State.PAUSE
    # state_machine.update()
    # state_machine.update(State.RESUME)
    