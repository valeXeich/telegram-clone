import { createStore } from 'vuex'
import auth from './modules/auth.module'
import chat from './modules/chat.module'
import user from './modules/user.module'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    chat,
    user
  }
})
