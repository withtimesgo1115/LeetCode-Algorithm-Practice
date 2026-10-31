import { AVATAR_COLORS } from '@/utils/constants'

export function useAvatar() {
  function getColor(nickname) {
    let hash = 0
    for (let i = 0; i < nickname.length; i++) {
      hash = nickname.charCodeAt(i) + ((hash << 5) - hash)
    }
    return AVATAR_COLORS[Math.abs(hash) % AVATAR_COLORS.length]
  }

  function getInitial(nickname) {
    return nickname ? nickname.charAt(0).toUpperCase() : '?'
  }

  return { getColor, getInitial }
}
