import axios from "axios";
import store from '@/store'

const loginConfig = {
    baseURL: 'http://127.0.0.1:8000/',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
}

export const LoginAPIInstance = axios.create(loginConfig)

const defaultConfig = {
    baseURL: 'http://127.0.0.1:8000/',
    headers: {
        'Content-Type': 'application/json'
    }
}

const token = localStorage.getItem('authToken')
if (token) defaultConfig.headers['Authorization'] = `Bearer ${token}`

export const DefaultAPIInstance = axios.create(defaultConfig)

DefaultAPIInstance.interceptors.response.use(undefined, async (error) => {
    const { response, config } = error
    if (response.status === 401) {
      console.log('Logout failed', response.status)
      await store.dispatch('auth/refresh')
      return DefaultAPIInstance(config)
    }
    return Promise.reject(error)
})