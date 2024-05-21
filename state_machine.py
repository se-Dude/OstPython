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

    # public attributes
    last_state = None

    # protectet attributes
    _states = {}
    _state = None

    def __init__(self) -> None:
        """
        Initiliaze the StateMachine instance.

        """

        StateMachine._states = {}
        StateMachine._state = None
        StateMachine.last_state = None

    def add_state(self, state_name, state):
        """
        Method to add a function to the known states.

        Args
        ----
            state_name (State): Name of the State to be added.
            state (num): Value of the state to be added.

        """
        StateMachine._states[state_name] = state

    def update(self, event=None):
        """
        Initiliaze the Field instance.

        Args
        ----
            state_name (State): Name of the State to be added.
            state (num): Value of the state to be added.

        """

        StateMachine._states[StateMachine._state](event)

    @property
    def state(self):
        """
        Method to get or set the active state.

        Args
        ----
            value (State): State to be set.

        Returns
        -------
            function : Function where state points to.

        Raises
        ------
            ValueError : If the given state is not known.
        """
        return StateMachine._states[StateMachine._state]

    @state.setter
    def state(self, value):
        if value in StateMachine._states:
            StateMachine._state = value
        else:
            raise ValueError(f"Unknown state with name {value.name}. "
                             f"The following states are valid: "
                             f"{[item.name for item in StateMachine._states]}")


if __name__ == "__main__":
    # 4.1 Methode __init__(self)
    state_machine = StateMachine()
    print(state_machine._states)
    print(state_machine._state)
    print(state_machine.last_state)

    # 4.2 Methode add_state(self, state_name, state)
    state_machine = StateMachine()

    def pause(event=None):
        print("Taking a pause...")

    def scan(event=None):
        print("Scanning...")

    state_machine.add_state(State.PAUSE, pause)
    state_machine.add_state(State.SCAN, scan)
    print(state_machine._states)

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
    state_machine = StateMachine()

    def pause(event=None):
        print("Taking a pause...")
        print(f"{event = }")
    state_machine.add_state(State.PAUSE, pause)
    state_machine.state = State.PAUSE
    state_machine.update()
    state_machine.update("test")
