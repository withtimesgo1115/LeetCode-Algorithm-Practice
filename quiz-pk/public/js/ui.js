const AVATAR_COLORS = [
  '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4',
  '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F',
  '#BB8FCE', '#85C1E9', '#F0B27A', '#82E0AA',
];

function generateAvatar(nickname) {
  const hash = nickname.split('').reduce((acc, ch) => ((acc << 5) - acc) + ch.charCodeAt(0), 0);
  return {
    color: AVATAR_COLORS[Math.abs(hash) % AVATAR_COLORS.length],
    initial: nickname.charAt(0).toUpperCase(),
  };
}

function renderAvatar(el, nickname) {
  if (!el || !nickname) return;
  const { color, initial } = generateAvatar(nickname);
  el.style.backgroundColor = color;
  el.textContent = initial;
}

function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(id);
  if (target) target.classList.add('active');
}

// ── Timer ──────────────────────────────────────────────
let _timerInterval = null;
const CIRCUMFERENCE = 2 * Math.PI * 45; // ~283

function startTimer(seconds, onTick, onEnd) {
  stopTimer();
  const circle = document.getElementById('timer-circle');
  const text = document.getElementById('timer-text');
  if (!circle || !text) return;

  let remaining = seconds;
  circle.classList.remove('danger');
  circle.style.strokeDashoffset = '0';
  text.textContent = remaining;

  _timerInterval = setInterval(() => {
    remaining--;
    if (text) text.textContent = Math.max(0, remaining);
    const offset = CIRCUMFERENCE * (1 - remaining / seconds);
    circle.style.strokeDashoffset = offset;

    if (remaining <= 5) circle.classList.add('danger');
    if (onTick) onTick(remaining);

    if (remaining <= 0) {
      stopTimer();
      if (onEnd) onEnd();
    }
  }, 1000);
}

function stopTimer() {
  if (_timerInterval) {
    clearInterval(_timerInterval);
    _timerInterval = null;
  }
}

// ── Confetti ───────────────────────────────────────────
function showConfetti() {
  const container = document.getElementById('confetti-container');
  if (!container) return;
  container.innerHTML = '';
  const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffd740', '#dda0dd', '#00e676'];
  for (let i = 0; i < 50; i++) {
    const piece = document.createElement('div');
    piece.className = 'confetti-piece';
    piece.style.left = Math.random() * 100 + '%';
    piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    piece.style.animationDelay = Math.random() * 2 + 's';
    piece.style.animationDuration = (2 + Math.random() * 2) + 's';
    piece.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    piece.style.width = (6 + Math.random() * 8) + 'px';
    piece.style.height = (6 + Math.random() * 8) + 'px';
    container.appendChild(piece);
  }
  setTimeout(() => { container.innerHTML = ''; }, 5000);
}

// ── Rank badge ─────────────────────────────────────────
function renderRankBadge(el, rank) {
  if (!el || !rank) return;
  el.textContent = rank.icon + ' ' + rank.name;
}
