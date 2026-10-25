class QuizSocket {
  constructor() {
    this.socket = io();
    this.handlers = {};
    this._setup();
  }

  _setup() {
    const events = [
      'auth_success', 'auth_error', 'set_cookie',
      'waiting', 'matched', 'match_timeout', 'match_error',
      'question', 'answer_ack', 'opponent_answered',
      'question_result', 'game_over', 'opponent_disconnected',
    ];
    events.forEach(ev => {
      this.socket.on(ev, data => this._emit(ev, data));
    });
  }

  join(nickname, userId) { this.socket.emit('join', { nickname, userId }); }
  selectCategory(category, mode) { this.socket.emit('select_category', { category, mode: mode || 'pvp' }); }
  cancelMatch() { this.socket.emit('cancel_match'); }
  answer(questionIndex, optionIndex) { this.socket.emit('answer', { questionIndex, optionIndex }); }

  on(event, handler) {
    if (!this.handlers[event]) this.handlers[event] = [];
    this.handlers[event].push(handler);
  }

  _emit(event, data) {
    const list = this.handlers[event];
    if (list) list.forEach(h => h(data));
  }
}

window.quizSocket = new QuizSocket();
