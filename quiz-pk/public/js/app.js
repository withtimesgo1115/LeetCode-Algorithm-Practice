const GameState = { HOME: 'home', MATCHING: 'matching', PLAYING: 'playing', RESULT: 'result' };

const CATEGORY_ICONS = { '文学艺术': '📚', '法律': '⚖️', '历史地理': '🌍', '物理化学生物': '🔬', '科技创新': '💡', '成语辨析': '✍️', '时事政治': '📰' };
const CATEGORY_GRADIENTS = [
  'linear-gradient(135deg, #667eea, #764ba2)',
  'linear-gradient(135deg, #f093fb, #f5576c)',
  'linear-gradient(135deg, #4facfe, #00f2fe)',
  'linear-gradient(135deg, #43e97b, #38f9d7)',
  'linear-gradient(135deg, #fa709a, #fee140)',
  'linear-gradient(135deg, #a18cd1, #fbc2eb)',
];

class App {
  constructor() {
    this.state = GameState.HOME;
    this.userId = localStorage.getItem('quiz_uid');
    this.nickname = localStorage.getItem('quiz_nickname') || '';
    this.category = null;
    this.opponent = null;
    this.myScore = 0;
    this.oppScore = 0;
    this.qIndex = 0;
    this.totalQ = 5;
    this.answered = false;
    this.categories = [];
    this.myRank = null;
    this.oppRank = null;
    this.singleMode = false;

    this._init();
  }

  async _init() {
    if (this.nickname) {
      document.getElementById('nickname-input').value = this.nickname;
    }
    await this._loadCategories();
    this._bindSocket();
    this._bindUI();

    if (this.userId && this.nickname) {
      quizSocket.join(this.nickname, this.userId);
    }
  }

  async _loadCategories() {
    try {
      const res = await fetch('/api/categories');
      this.categories = await res.json();
    } catch { this.categories = []; }
    this._renderCategories();
  }

  _renderCategories() {
    const grid = document.getElementById('category-grid');
    let html = this.categories.map((cat, i) => {
      const icon = CATEGORY_ICONS[cat.category] || '📖';
      const grad = CATEGORY_GRADIENTS[i % CATEGORY_GRADIENTS.length];
      return '<div class="category-card disabled" data-category="' + this._esc(cat.category) + '" style="background:' + grad + '20;border-color:' + grad + '40">'
        + '<div class="category-icon">' + icon + '</div>'
        + '<div class="category-name">' + this._esc(cat.category) + '</div>'
        + '</div>';
    }).join('');

    html += '<div class="category-card random-mode disabled" data-category="随机模式">'
      + '<div class="category-icon">🎲</div>'
      + '<div class="category-name">随机模式</div>'
      + '<div style="font-size:12px;color:var(--text-secondary);margin-top:4px">全分类混合出题</div>'
      + '</div>';

    grid.innerHTML = html;
  }

  _bindUI() {
    document.getElementById('btn-enter').addEventListener('click', () => this._enterNickname());
    document.getElementById('nickname-input').addEventListener('keydown', e => {
      if (e.key === 'Enter') this._enterNickname();
    });

    document.getElementById('category-grid').addEventListener('click', e => {
      const card = e.target.closest('.category-card');
      if (card && !card.classList.contains('disabled') && this.nickname) {
        this.category = card.dataset.category;
        this._go(GameState.MATCHING);
        quizSocket.selectCategory(this.category, this.singleMode ? 'single' : 'pvp');
      }
    });

    document.getElementById('btn-single-player').addEventListener('click', () => {
      this.singleMode = !this.singleMode;
      const btn = document.getElementById('btn-single-player');
      btn.textContent = this.singleMode ? '单人模式 ✓' : '单人练习';
      btn.style.opacity = this.singleMode ? '1' : '';
    });

    document.getElementById('btn-cancel-match').addEventListener('click', () => {
      quizSocket.cancelMatch();
      this._go(GameState.HOME);
    });

    document.getElementById('btn-play-again').addEventListener('click', () => {
      this.myScore = 0; this.oppScore = 0; this.qIndex = 0;
      this._go(GameState.MATCHING);
      quizSocket.selectCategory(this.category, this.singleMode ? 'single' : 'pvp');
    });

    document.getElementById('btn-back-home').addEventListener('click', () => {
      this._go(GameState.HOME);
    });

    document.getElementById('btn-leaderboard').addEventListener('click', () => this._showLeaderboard());
    document.getElementById('btn-close-leaderboard').addEventListener('click', () => {
      document.getElementById('modal-leaderboard').classList.add('hidden');
    });
  }

  _enterNickname() {
    const input = document.getElementById('nickname-input');
    const name = input.value.trim();
    if (name.length < 1 || name.length > 8) return;
    this.nickname = name;
    localStorage.setItem('quiz_nickname', name);
    quizSocket.join(name, this.userId);

    document.querySelectorAll('.category-card').forEach(c => c.classList.remove('disabled'));
  }

  _bindSocket() {
    quizSocket.on('set_cookie', data => {
      this.userId = data.userId;
      localStorage.setItem('quiz_uid', data.userId);
    });

    quizSocket.on('auth_success', data => {
      this.userId = data.userId;
      localStorage.setItem('quiz_uid', data.userId);
      this.myRank = data.rank;
      document.querySelectorAll('.category-card').forEach(c => c.classList.remove('disabled'));
      this._updateHomeRank();
    });

    quizSocket.on('auth_error', data => {
      alert(data.message || '登录失败');
    });

    quizSocket.on('waiting', () => {
      const el = document.getElementById('matching-category');
      const label = this.category === '随机模式' ? '随机模式' : '「' + this.category + '」';
      if (el) el.textContent = '正在等待对手选择' + label + '...';
    });

    quizSocket.on('matched', data => {
      this.opponent = data.opponent;
      this.oppRank = data.opponentRank;
      this.totalQ = data.totalQuestions;
      const nameEl = document.getElementById('matching-name-opponent');
      const avatarEl = document.getElementById('matching-avatar-opponent');
      if (nameEl) nameEl.textContent = data.opponent;
      if (avatarEl) {
        avatarEl.classList.remove('matching-opponent');
        renderAvatar(avatarEl, data.opponent);
      }
      renderRankBadge(document.getElementById('matching-rank-opponent'), data.opponentRank);
      setTimeout(() => this._go(GameState.PLAYING), 1200);
    });

    quizSocket.on('match_timeout', () => {
      alert('匹配超时，请重新选择');
      this._go(GameState.HOME);
    });

    quizSocket.on('match_error', data => {
      alert(data.message || '匹配失败');
      this._go(GameState.HOME);
    });

    quizSocket.on('question', data => {
      this.qIndex = data.index;
      this.answered = false;
      this._renderQuestion(data);
      startTimer(data.totalTime, null, () => {});
    });

    quizSocket.on('answer_ack', data => {
      this.answered = true;
      this.myScore = data.totalScore;
      this._updateScores();
      this._showAnswerResult(data.correct, data.score, data.isLast);
      const bar = document.getElementById('progress-me');
      bar.className = 'progress-bar ' + (data.correct ? 'correct' : 'wrong');
    });

    quizSocket.on('opponent_answered', () => {
      document.getElementById('progress-opponent').className = 'progress-bar answered';
    });

    quizSocket.on('question_result', data => {
      stopTimer();
      this.myScore = data.playerScore;
      this.oppScore = data.opponentScore;
      this._updateScores();
      this._highlightCorrect(data.correctAnswer);

      setTimeout(() => {
        document.getElementById('progress-me').className = 'progress-bar';
        document.getElementById('progress-opponent').className = 'progress-bar';
      }, 1500);
    });

    quizSocket.on('game_over', data => {
      this.myRank = data.playerRank;
      this.oppRank = data.opponentRank;
      this._showResult(data);
      this._go(GameState.RESULT);
    });

    quizSocket.on('opponent_disconnected', () => {
      alert('对手已断开连接');
      this._go(GameState.HOME);
    });
  }

  _go(state) {
    this.state = state;
    const map = {
      [GameState.HOME]: 'screen-home',
      [GameState.MATCHING]: 'screen-matching',
      [GameState.PLAYING]: 'screen-game',
      [GameState.RESULT]: 'screen-result',
    };
    showScreen(map[state]);

    if (state === GameState.MATCHING) {
      const label = this.category === '随机模式' ? '随机模式' : '「' + this.category + '」';
      document.getElementById('matching-category').textContent = '正在寻找' + label + '的对手...';
      renderAvatar(document.getElementById('matching-avatar-me'), this.nickname);
      document.getElementById('matching-name-me').textContent = this.nickname;
      renderRankBadge(document.getElementById('matching-rank-me'), this.myRank);
      const oppAvatar = document.getElementById('matching-avatar-opponent');
      oppAvatar.className = 'avatar matching-opponent';
      oppAvatar.textContent = '?';
      oppAvatar.style.backgroundColor = '';
      document.getElementById('matching-name-opponent').textContent = '等待中...';
      document.getElementById('matching-rank-opponent').textContent = '';
    }

    if (state === GameState.HOME) {
      this._loadCategories();
      this._updateHomeRank();
    }
  }

  _updateHomeRank() {
    const display = document.getElementById('user-rank-display');
    if (this.myRank && display) {
      display.classList.remove('hidden');
      document.getElementById('home-rank-icon').textContent = this.myRank.icon;
      document.getElementById('home-rank-name').textContent = this.myRank.name;
    }
  }

  _renderQuestion(data) {
    document.getElementById('question-counter').textContent = (data.index + 1) + '/' + this.totalQ;
    document.getElementById('question-text').textContent = data.text;

    // Category tag
    const catTag = document.getElementById('question-category-tag');
    if (catTag && data.category) {
      catTag.textContent = data.category;
      catTag.style.display = '';
    }

    // Double score badge
    const doubleBadge = document.getElementById('double-score-badge');
    if (doubleBadge) {
      if (data.isLast) {
        doubleBadge.classList.remove('hidden');
      } else {
        doubleBadge.classList.add('hidden');
      }
    }

    const container = document.getElementById('options-container');
    container.innerHTML = '';
    const labels = ['A', 'B', 'C', 'D'];
    const fragment = document.createDocumentFragment();
    data.options.forEach((opt, i) => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.index = i;
      btn.innerHTML = '<span class="option-label">' + labels[i] + '</span>'
        + '<span class="option-text">' + this._esc(opt) + '</span>';
      btn.addEventListener('click', () => {
        if (this.answered) return;
        quizSocket.answer(data.index, i);
        container.querySelectorAll('.option-btn').forEach(b => b.classList.add('disabled'));
        btn.classList.add('selected');
      });
      fragment.appendChild(btn);
    });
    container.appendChild(fragment);

    const circle = document.getElementById('timer-circle');
    circle.classList.remove('danger');
    circle.style.stroke = '';
    document.getElementById('timer-text').textContent = data.totalTime;

    document.getElementById('progress-me').className = 'progress-bar';
    document.getElementById('progress-opponent').className = 'progress-bar';
    this._updateScores();
  }

  _updateScores() {
    document.getElementById('game-score-me').textContent = this.myScore;
    document.getElementById('game-score-opponent').textContent = this.oppScore;
  }

  _showAnswerResult(correct, score, isLast) {
    const overlay = document.getElementById('answer-result-overlay');
    document.getElementById('result-icon').textContent = correct ? '✓' : '✗';
    document.getElementById('result-icon').style.color = correct ? 'var(--correct-color)' : 'var(--wrong-color)';
    document.getElementById('result-score').textContent = correct ? '+' + score : '+0';
    const doubleEl = document.getElementById('result-double');
    if (doubleEl) {
      doubleEl.textContent = isLast ? '双倍!' : '';
    }
    overlay.classList.remove('hidden');
    setTimeout(() => overlay.classList.add('hidden'), 1200);
  }

  _highlightCorrect(correctIndex) {
    document.querySelectorAll('.option-btn').forEach((btn, i) => {
      btn.classList.remove('disabled');
      if (i === correctIndex) btn.classList.add('correct');
      else if (btn.classList.contains('selected')) btn.classList.add('wrong');
    });
  }

  _showResult(data) {
    const badge = document.getElementById('result-badge');
    const title = document.getElementById('result-title');

    if (data.result === 'win') {
      badge.textContent = '🏆';
      title.textContent = '你赢了！';
      title.style.color = 'var(--correct-color)';
      showConfetti();
    } else if (data.result === 'lose') {
      badge.textContent = '😢';
      title.textContent = '你输了';
      title.style.color = 'var(--wrong-color)';
    } else {
      badge.textContent = '🤝';
      title.textContent = '平局！';
      title.style.color = 'var(--timer-color)';
    }

    renderAvatar(document.getElementById('result-avatar-me'), this.nickname);
    renderAvatar(document.getElementById('result-avatar-opponent'), data.opponentNickname);
    document.getElementById('result-name-me').textContent = this.nickname;
    document.getElementById('result-name-opponent').textContent = data.opponentNickname;
    document.getElementById('result-score-me').textContent = data.playerScore;
    document.getElementById('result-score-opponent').textContent = data.opponentScore;

    renderRankBadge(document.getElementById('result-rank-me'), data.playerRank);
    renderRankBadge(document.getElementById('result-rank-opponent'), data.opponentRank);
  }

  async _showLeaderboard() {
    try {
      const res = await fetch('/api/leaderboard');
      const data = await res.json();
      const list = document.getElementById('leaderboard-list');
      if (data.length === 0) {
        list.innerHTML = '<p style="text-align:center;color:var(--text-secondary);padding:20px">暂无数据</p>';
      } else {
        list.innerHTML = data.map((item, i) => {
          const rankClass = i === 0 ? 'gold' : i === 1 ? 'silver' : i === 2 ? 'bronze' : '';
          const rankBadge = item.rank ? item.rank.icon + ' ' + item.rank.name : '';
          return '<div class="leaderboard-item">'
            + '<div class="leaderboard-rank ' + rankClass + '">' + (i + 1) + '</div>'
            + '<div class="leaderboard-info">'
            + '<div class="leaderboard-name">' + this._esc(item.nickname) + ' <span style="font-size:11px;color:var(--text-secondary)">' + rankBadge + '</span></div>'
            + '<div class="leaderboard-stats">' + item.games_won + '胜 / ' + item.games_played + '场 (' + item.win_rate + '%)</div>'
            + '</div></div>';
        }).join('');
      }
      document.getElementById('modal-leaderboard').classList.remove('hidden');
    } catch { alert('加载排行榜失败'); }
  }

  _esc(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }
}

document.addEventListener('DOMContentLoaded', () => { window.app = new App(); });
