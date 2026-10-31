import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', name: 'home', component: () => import('@/views/HomeView.vue') },
  { path: '/matching', name: 'matching', component: () => import('@/views/MatchingView.vue') },
  { path: '/game', name: 'game', component: () => import('@/views/GameView.vue') },
  { path: '/result', name: 'result', component: () => import('@/views/ResultView.vue') },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
