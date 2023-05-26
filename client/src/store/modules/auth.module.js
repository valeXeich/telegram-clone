import axios from "axios"
import { LoginAPIInstance, DefaultAPIInstance } from "@/axios"

const TOKEN_KEY = 'authToken'

export default {
    namespaced: true,
    state() {
        return {
            token: localStorage.getItem(TOKEN_KEY) || null,
            refreshToken: localStorage.getItem('refreshToken') || null,
        }
    },
    getters: {
        token(state) {
            return state.token
        },
        isAuthenticated(state) {
            return !!state.token;
        },
        refreshToken(state) {
            return state.refreshToken
        }
    },
    mutations: {
        setToken(state, accessToken) {
            state.token = accessToken;
            localStorage.setItem(TOKEN_KEY, accessToken);
        },
        setRefreshToken(state, refreshToken) {
            state.refreshToken = refreshToken
            localStorage.setItem('refreshToken', refreshToken)
        },
        logout(state) {
            state.token = null;
            localStorage.removeItem(TOKEN_KEY);
            localStorage.removeItem('user')
            localStorage.removeItem('refreshToken')
            DefaultAPIInstance.defaults.headers.common["Authorization"] = null;
        }
    },
    actions: {
        async login({ commit, dispatch }, payload) {
            try {
                const { data } = await LoginAPIInstance.post('auth/signin', payload);
                commit('setToken', data.access_token);
                commit('setRefreshToken', data.refresh_token)
                DefaultAPIInstance.interceptors.request.use(config => {
                    config.headers['Authorization'] = `Bearer ${data.access_token}`
                    return config
                })
                await dispatch('user/getUser', {}, {root: true})
            } catch (e) {
                if (e.response.status === 404) {
                    throw Error(e.response.data.detail)
                } else if (e.response.status === 422) {
                    throw Error('Empty fields')
                }
                console.log('bad login', e);
            }
        },
        async signUp(payload) {
            try {
                const response = await LoginAPIInstance.post('auth/signup', payload)
            } catch (e) {
                console.log('bad signup', e)
            }
        },
        async refresh({ commit, getters }) {
            try {
                const refreshToken = getters['refreshToken']
                const { data } = await axios.post('auth/refresh-token', {refresh_token: refreshToken})
                DefaultAPIInstance.interceptors.request.use(config => {
                    config.headers['Authorization'] = `Bearer ${data.access_token}`
                    return config
                })
                commit('setToken', data.access_token)
            } catch (e) {
                console.log('bad refresh', e)
            }
        }
    }
}