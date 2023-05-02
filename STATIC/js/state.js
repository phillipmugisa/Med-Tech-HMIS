class State {
  constructor (state = null) {
    this.state = state;

    return state
  }
  setState(newState) {
    this.state = newState
  }

  get name() {
    return this.state;
  }
}