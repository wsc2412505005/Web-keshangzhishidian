import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Library from '../views/Library.vue'
import Keywords from '../views/Keywords.vue'
import About from '../views/About.vue'
import Analysis from '../views/Analysis.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/library',
      name: 'library',
      component: Library,
    },
    {
      path: '/keywords',
      name: 'keywords',
      component: Keywords,
    },
    {
      path: '/about',
      name: 'about',
      component: About,
    },
    {
      path: '/analysis',
      name: 'analysis',
      component: Analysis,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
})

export default router
