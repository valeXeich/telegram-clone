import { createRouter, createWebHistory } from 'vue-router'
import Chat from '@/views/Chat'
import Login from '@/views/Login'
import ChatDetail from '@/views/ChatDetail'
import SignUp from '@/views/SignUp'
import store from '@/store'

const routes = [
  {
    path: '/',
    component: Chat,
    meta: {
      auth: true
    }
  },
  {
    path: '/login',
    component: Login,
  },
  {
    path: '/room/:id',
    component: ChatDetail,
    meta: {
      auth: true
    }
  },
  {
    path: '/signup',
    component: SignUp
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const requireAuth = to.meta.auth
  const isAuth = store.getters['auth/isAuthenticated'];
  if (requireAuth && isAuth) {
    next();
  } else if (requireAuth && !isAuth) {
    next('/login');
  } else {
    next();
  }
})

export default router
