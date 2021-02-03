import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue';
import Spaces from '../views/Spaces.vue';
import Boards from '../views/Boards.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/spaces',
    name: 'Spaces',
    component: Spaces
  },
  {
    path: '/boards',
    name: 'Boards',
    component: Boards
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
