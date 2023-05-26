import { DefaultAPIInstance } from "@/axios"

export default {
    namespaced: true,
    state() {
        return {
            rooms: []
        }
    },
    getters: {
        rooms(state) {
            return state.rooms;
        }
    },
    mutations: {
        setRooms(state, rooms) {
            state.rooms = rooms;
        }
    },
    actions: {
        async getRooms({ commit }) {
            const { data } = await DefaultAPIInstance.get('chat/rooms');
            commit('setRooms', data);
        },
        async getRoom(_, id) {
            const { data } = await DefaultAPIInstance.get(`chat/room/${id}`);
            return data;
        }
    }
}