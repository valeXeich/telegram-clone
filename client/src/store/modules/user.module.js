import { DefaultAPIInstance } from "@/axios"

export default {
    namespaced: true,
    state() {
        return {
            user: localStorage.getItem('user')
        }
    },
    actions: {
        async getUser({commit}) {
            const {data} = await DefaultAPIInstance.get('users/');
            commit('setUser', data)
        }
    },
    mutations: {
        setUser(state, user) {
            localStorage.setItem('user', JSON.stringify(user))
            state.user = JSON.stringify(user)
        }
    },
    getters: {
        user(state) {
            return JSON.parse(state.user)
        }
    }
}